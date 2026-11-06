"""Round 0 generator (official baseline): Qwen3-TTS-12Hz-1.7B-CustomVoice, description passed as `instruct`.

Fixed, documented recipe (reproducible):
  speaker   = gender-matched preset chosen by sample index (female/male keyword rule; default cycles all 9)
  instruct  = the description, truncated to 300 words
  language  = "Auto" (Hindi/Tamil are not in the official list)
  seed      = base_seed + sample index
"""
from __future__ import annotations

import re

from .voices import CUSTOMVOICE_SPEAKERS, Qwen3TTS

FEMALE = re.compile(r"\b(woman|female|girl|lady|her|she|mother|grandmother)\b", re.I)
MALE = re.compile(r"\b(man|male|boy|gentleman|his|he|father|grandfather)\b", re.I)


def gender_rule(desc: str) -> str | None:
    f, m = len(FEMALE.findall(desc)), len(MALE.findall(desc))
    if f > m:
        return "female"
    if m > f:
        return "male"
    return None


def presets_for(desc: str) -> list[str]:
    g = gender_rule(desc)
    return CUSTOMVOICE_SPEAKERS[g] if g else CUSTOMVOICE_SPEAKERS["female"] + CUSTOMVOICE_SPEAKERS["male"]


def generate(tts: Qwen3TTS, text: str, desc: str, n: int = 10, base_seed: int = 1234):
    pres = presets_for(desc)
    instruct = " ".join(desc.split()[:300])
    outs = []
    for i in range(n):
        wav, sr = tts.custom(text, speaker=pres[i % len(pres)], instruct=instruct, seed=base_seed + i)
        outs.append((wav, sr, {"speaker": pres[i % len(pres)], "seed": base_seed + i}))
    return outs
