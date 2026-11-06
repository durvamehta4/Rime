"""Minimal LLM client for an OpenAI-compatible server (vLLM `vllm serve models/Qwen3-8B`), stdlib only.

Also provides robust JSON extraction from model output and a deterministic mock for CPU tests.
"""
from __future__ import annotations

import json
import os
import re
import urllib.request
from typing import Callable

LLMFn = Callable[[str], str]


def openai_chat(base_url: str | None = None, model: str | None = None, temperature: float = 0.0,
                max_tokens: int = 2048, system: str | None = None, timeout: float = 600,
                disable_thinking: bool = True) -> LLMFn:
    base_url = base_url or os.environ.get("RIMET2_LLM_URL", "http://localhost:8000/v1")
    model = model or os.environ.get("RIMET2_LLM_MODEL", "Qwen3-8B")

    def call(prompt: str) -> str:
        msgs = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": prompt}]
        body = {"model": model, "messages": msgs, "temperature": temperature, "max_tokens": max_tokens}
        if disable_thinking:  # Qwen3 chat template switch, honoured by vLLM
            body["chat_template_kwargs"] = {"enable_thinking": False}
        req = urllib.request.Request(base_url.rstrip("/") + "/chat/completions", data=json.dumps(body).encode(),
                                     headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            out = json.loads(r.read())
        return out["choices"][0]["message"]["content"]

    return call


_THINK_RE = re.compile(r"<think>.*?</think>", re.S)


def extract_json(text: str):
    """Return the first JSON object/array found in `text` (tolerates code fences, think blocks, trailing text)."""
    text = _THINK_RE.sub("", text)
    text = re.sub(r"```(?:json)?", "", text)
    pairs = [("{", "}"), ("[", "]")]
    pairs.sort(key=lambda p: (text.find(p[0]) if text.find(p[0]) != -1 else 1 << 30))
    for opener, closer in pairs:
        start = text.find(opener)
        while start != -1:
            depth, in_str, esc = 0, False, False
            for i in range(start, len(text)):
                ch = text[i]
                if in_str:
                    if esc:
                        esc = False
                    elif ch == "\\":
                        esc = True
                    elif ch == '"':
                        in_str = False
                elif ch == '"':
                    in_str = True
                elif ch == opener:
                    depth += 1
                elif ch == closer:
                    depth -= 1
                    if depth == 0:
                        cand = text[start:i + 1]
                        try:
                            return json.loads(cand)
                        except json.JSONDecodeError:
                            cand2 = re.sub(r",\s*([}\]])", r"\1", cand)  # trailing commas
                            try:
                                return json.loads(cand2)
                            except json.JSONDecodeError:
                                break
            start = text.find(opener, start + 1)
    raise ValueError("no JSON found in LLM output")


def mock_llm(responses: dict[str, str] | Callable[[str], str]) -> LLMFn:
    """Deterministic mock: dict keyed by a substring of the prompt, or a function."""
    if callable(responses):
        return responses

    def call(prompt: str) -> str:
        for k, v in responses.items():
            if k in prompt:
                return v
        raise KeyError("mock_llm: no response for prompt")

    return call
