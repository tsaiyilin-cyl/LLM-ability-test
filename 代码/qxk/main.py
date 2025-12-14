import base64
import os
from dotenv import load_dotenv

from fastapi import FastAPI, File, Form, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from openai import AsyncOpenAI

_here = os.path.dirname(os.path.abspath(__file__))
_repo_root_env = os.path.abspath(os.path.join(_here, "..", ".env"))
load_dotenv(_repo_root_env)

app = FastAPI()


@app.get("/")
async def index():
    here = os.path.dirname(os.path.abspath(__file__))
    return FileResponse(os.path.join(here, "index.html"))


@app.post("/api/chat")
async def chat(
    base_url=Form("https://api.whatai.cc"),
    model=Form("hunyuan-vision"),
    system_prompt=Form(""),
    user_prompt=Form(""),
    image=File(None),
):
    base_url = (base_url or "").strip().rstrip("/")
    if not base_url:
        base_url = "https://api.whatai.cc"
    if not base_url.endswith("/v1"):
        base_url = f"{base_url}/v1"

    if "hunyuan.cloud.tencent.com" in base_url:
        api_key = os.getenv("HUNYUAN_API_KEY") or os.getenv("TENCENT_API_KEY")
        if not api_key:
            raise HTTPException(
                status_code=400,
                detail="Missing HUNYUAN_API_KEY (or TENCENT_API_KEY) env var for Tencent Hunyuan base_url",
            )
    else:
        api_key = os.getenv("WHATAI_API_KEY") or os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise HTTPException(status_code=400, detail="Missing WHATAI_API_KEY (or OPENAI_API_KEY) env var")

    client = AsyncOpenAI(api_key=api_key, base_url=base_url)

    user_content = None
    if image is None:
        user_content = [{"type": "text", "text": user_prompt}]
    else:
        raw = await image.read()
        if not raw:
            raise HTTPException(status_code=400, detail="Empty image file")
        mime = getattr(image, "content_type", None) or "application/octet-stream"
        b64 = base64.b64encode(raw).decode("utf-8")
        user_content = [
            {"type": "text", "text": user_prompt},
            {"type": "image_url", "image_url": {"url": f"data:{mime};base64,{b64}"}},
        ]

    try:
        resp = await client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content},
            ],
            timeout=60,
        )
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Upstream request failed: {e}")

    try:
        content = resp.choices[0].message.content or ""
    except Exception:
        content = ""

    raw = resp.model_dump()
    usage = raw.get("usage") or {}
    completion_tokens = usage.get("completion_tokens")
    prompt_tokens = usage.get("prompt_tokens")
    total_tokens = usage.get("total_tokens")

    return JSONResponse(
        {
            "content": content,
            "completion_tokens": completion_tokens,
            "prompt_tokens": prompt_tokens,
            "total_tokens": total_tokens,
            "raw": raw,
        }
    )


here = os.path.dirname(os.path.abspath(__file__))
app.mount("/static", StaticFiles(directory=here, html=False), name="static")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)