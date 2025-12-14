sys_prompt_1 = '''
你是一个出色的图片分类助手，对于用户输入的一张图片，可以识别图片中的主体，并且输出正确的类别。
'''
sys_prompt_2 = """
你是一个出色的颜色识别助手，对于用户输入的一张纯色图，正确输出正确的颜色类别。
"""
sys_prompt_3 = '''
你是一个出色的情绪识别助手，对于用户输入的一张图片，识别图片中任务的情绪。
'''
user_prompt = '''
识别图片中的内容，再回答正确分类之前先输出理由。输出格式为。
1.reasoning
{{在这里插入你的推理内容}}
2.answer
{{在这里输出最终的类别名，例如：狸花猫}}
'''
D:\CommonFiles\GitHub\LLM-abitily-test\代码\qxk

def parse(completions):
    import re

    def _to_text(x):
        if x is None:
            return ""
        if isinstance(x, str):
            return x
        if isinstance(x, dict):
            if "content" in x and isinstance(x["content"], str):
                return x["content"]
            try:
                return x["choices"][0]["message"]["content"]
            except Exception:
                return str(x)
        try:
            if hasattr(x, "choices") and x.choices:
                msg = x.choices[0].message
                if hasattr(msg, "content"):
                    return msg.content or ""
        except Exception:
            pass
        return str(x)

    text = _to_text(completions).strip()
    if not text:
        return "", ""

    # Normalize line breaks
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Primary pattern: 1.reasoning ... 2.answer ...
    primary = re.compile(
        r"(?is)"  # ignorecase + dot matches newline
        r"(?:^|\n)\s*(?:1\s*[\.|、\)]\s*)?(?:reasoning|分析|理由)\s*[:：]?\s*\n?"
        r"(?P<reasoning>.*?)"
        r"(?:\n\s*(?:2\s*[\.|、\)]\s*)?(?:answer|答案|结论)\s*[:：]?\s*\n?)"
        r"(?P<answer>.*)$"
    )
    m = primary.search(text)
    if m:
        reasoning = (m.group("reasoning") or "").strip()
        answer = (m.group("answer") or "").strip()
        answer = answer.splitlines()[0].strip() if answer else answer
        return reasoning, answer

    # Fallback 1: locate an answer marker and split
    ans_marker = re.search(r"(?is)(?:^|\n)\s*(?:2\s*[\.|、\)]\s*)?(?:answer|答案|结论)\s*[:：]?\s*\n?", text)
    if ans_marker:
        reasoning = text[: ans_marker.start()].strip()
        answer = text[ans_marker.end() :].strip()
        answer = answer.splitlines()[0].strip() if answer else answer
        return reasoning, answer

    # Fallback 2: treat last non-empty line as answer
    lines = [ln.strip() for ln in text.split("\n") if ln.strip()]
    if not lines:
        return "", ""
    if len(lines) == 1:
        return "", lines[0]
    return "\n".join(lines[:-1]).strip(), lines[-1]