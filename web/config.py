# -*- coding: utf-8 -*-
"""
配置文件
"""

# OpenAI API 配置
OPENAI_API_BASE = "https://api.whatai.cc"
OPENAI_API_KEY = "sk-LxHyQAmGfoMXPLS2qxQs9lUWTjlkYJU48IHnFCk3VFtZ442I"

# 可用模型列表
AVAILABLE_MODELS = {
    "国内模型": [
        {"id": "ernie-5.0-thinking-preview", "name": "文心 5.0"},
        {"id": "doubao-pro-32k", "name": "豆包"},
        {"id": "moonshot-v1-8k", "name": "Kimi"},
        {"id": "qwen-turbo", "name": "通义千问"},
    ],
    "国外模型": [
        {"id": "o3", "name": "OpenAI o3"},
        {"id": "gpt-5.2-thinking", "name": "GPT-5.2 Thinking"},
        {"id": "claude-3-5-sonnet-20241022", "name": "Claude 3.5 Sonnet"},
        {"id": "gemini-3-pro-preview-thinking-*", "name": "Gemini 3 Pro Thinking"},
        {"id": "gemini-2.5-pro-preview-thinking", "name": "Gemini 2.5 Pro Thinking"},
        {"id": "grok-beta", "name": "Grok"},
        {"id": "llama-3.1-70b-instruct", "name": "Llama 3.1"},
    ],
}
