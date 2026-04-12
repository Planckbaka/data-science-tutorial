"""统一 LLM 调用封装 — 支持 OpenAI / Anthropic / 通义千问，一套接口切换多家模型。"""

import os
from dotenv import load_dotenv

load_dotenv()


def call_llm(
    prompt: str,
    provider: str = "openai",
    model: str | None = None,
    system: str = "你是一个有帮助的AI助手。",
    temperature: float = 0.7,
    max_tokens: int = 1024,
) -> str:
    """调用 LLM 并返回文本响应。

    Args:
        prompt: 用户输入的 prompt
        provider: 模型提供方 ("openai" | "anthropic" | "dashscope")
        model: 模型名称，None 则使用各提供方的默认模型
        system: 系统提示词
        temperature: 生成温度 (0-1)
        max_tokens: 最大输出 token 数

    Returns:
        模型生成的文本
    """
    if provider == "openai":
        return _call_openai(prompt, model or "gpt-4o-mini", system, temperature, max_tokens)
    elif provider == "anthropic":
        return _call_anthropic(prompt, model or "claude-sonnet-4-20250514", system, temperature, max_tokens)
    elif provider == "dashscope":
        return _call_dashscope(prompt, model or "qwen-turbo", system, temperature, max_tokens)
    else:
        raise ValueError(f"不支持的 provider: {provider}，可选: openai, anthropic, dashscope")


def _call_openai(prompt: str, model: str, system: str, temperature: float, max_tokens: int) -> str:
    from openai import OpenAI

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content


def _call_anthropic(prompt: str, model: str, system: str, temperature: float, max_tokens: int) -> str:
    import anthropic

    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )
    return response.content[0].text


def _call_dashscope(prompt: str, model: str, system: str, temperature: float, max_tokens: int) -> str:
    from openai import OpenAI

    client = OpenAI(
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content


async def call_llm_async(
    prompt: str,
    provider: str = "openai",
    model: str | None = None,
    system: str = "你是一个有帮助的AI助手。",
    temperature: float = 0.7,
    max_tokens: int = 1024,
) -> str:
    """异步版本的 LLM 调用 — 用于 01-python-advanced 中的 async 练习以及 Agent 并发场景。"""
    if provider == "openai":
        from openai import AsyncOpenAI

        client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = await client.chat.completions.create(
            model=model or "gpt-4o-mini",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": prompt},
            ],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content
    elif provider == "anthropic":
        import anthropic

        client = anthropic.AsyncAnthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        response = await client.messages.create(
            model=model or "claude-sonnet-4-20250514",
            max_tokens=max_tokens,
            system=system,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
        )
        return response.content[0].text
    else:
        raise ValueError(f"异步调用暂不支持 provider: {provider}")
