"""Qwen3-Omni-30B-A3B-Captioner wrappers (round 0 + raw caption source for the fused captioner).

The Captioner takes AUDIO ONLY (no text prompt), single turn, clips <= 30 s.
Backends:
  - vLLM (recommended for bulk): tensor_parallel_size=4 BF16, or FP8 TP=2 x 2 replicas on L4s.
  - transformers (simple, slow): device_map="auto".
Card sampling: temperature 0.6, top_p 0.95, top_k 20. Round 0 uses exactly these (seeded) settings.
"""
from __future__ import annotations

import os
from typing import Iterable

DEFAULT_MODEL = os.environ.get("RIMET2_OMNI", "models/Qwen3-Omni-30B-A3B-Captioner")


def _conversation(path: str) -> list[dict]:
    return [{"role": "user", "content": [{"type": "audio", "audio": path}]}]


class OmniCaptionerVLLM:
    def __init__(self, model_path: str = DEFAULT_MODEL, tp: int = 4, max_model_len: int = 32768,
                 gpu_memory_utilization: float = 0.92, max_num_seqs: int = 16, quantization: str | None = None):
        from transformers import Qwen3OmniMoeProcessor
        from vllm import LLM

        self.processor = Qwen3OmniMoeProcessor.from_pretrained(model_path)
        self.llm = LLM(model=model_path, trust_remote_code=True, tensor_parallel_size=tp,
                       gpu_memory_utilization=gpu_memory_utilization, max_model_len=max_model_len,
                       max_num_seqs=max_num_seqs, limit_mm_per_prompt={"audio": 1}, quantization=quantization,
                       seed=1234)

    def caption(self, paths: Iterable[str], n: int = 1, temperature: float = 0.6, top_p: float = 0.95,
                top_k: int = 20, max_tokens: int = 2048, seed: int = 1234) -> list[list[str]]:
        from qwen_omni_utils import process_mm_info
        from vllm import SamplingParams

        reqs = []
        for p in paths:
            conv = _conversation(p)
            text = self.processor.apply_chat_template(conv, add_generation_prompt=True, tokenize=False)
            audios, _, _ = process_mm_info(conv, use_audio_in_video=False)
            reqs.append({"prompt": text, "multi_modal_data": {"audio": audios}})
        sp = SamplingParams(n=n, temperature=temperature, top_p=top_p, top_k=top_k, max_tokens=max_tokens, seed=seed)
        outs = self.llm.generate(reqs, sp)
        return [[c.text.strip() for c in o.outputs] for o in outs]


class OmniCaptionerHF:
    def __init__(self, model_path: str = DEFAULT_MODEL):
        import torch
        from transformers import Qwen3OmniMoeForConditionalGeneration, Qwen3OmniMoeProcessor

        self.model = Qwen3OmniMoeForConditionalGeneration.from_pretrained(
            model_path, dtype=torch.bfloat16, device_map="auto", attn_implementation="sdpa")
        self.processor = Qwen3OmniMoeProcessor.from_pretrained(model_path)

    def caption(self, paths: Iterable[str], n: int = 1, temperature: float = 0.6, top_p: float = 0.95,
                top_k: int = 20, max_tokens: int = 2048, seed: int = 1234) -> list[list[str]]:
        import torch
        from qwen_omni_utils import process_mm_info

        res = []
        for p in paths:
            conv = _conversation(p)
            text = self.processor.apply_chat_template(conv, add_generation_prompt=True, tokenize=False)
            audios, _, _ = process_mm_info(conv, use_audio_in_video=False)
            inputs = self.processor(text=text, audio=audios, return_tensors="pt", padding=True,
                                    use_audio_in_video=False).to(self.model.device).to(self.model.dtype)
            outs = []
            for k in range(n):
                torch.manual_seed(seed + k)
                ids = self.model.generate(**inputs, max_new_tokens=max_tokens, do_sample=True, temperature=temperature,
                                          top_p=top_p, top_k=top_k, thinker_return_dict_in_generate=True,
                                          return_audio=False)
                seq = ids.sequences if hasattr(ids, "sequences") else ids[0].sequences
                outs.append(self.processor.batch_decode(seq[:, inputs["input_ids"].shape[1]:],
                                                        skip_special_tokens=True)[0].strip())
            res.append(outs)
        return res


def get_captioner(backend: str = "vllm", **kw):
    return OmniCaptionerVLLM(**kw) if backend == "vllm" else OmniCaptionerHF(**kw)
