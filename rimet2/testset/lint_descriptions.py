"""Lint generation descriptions so every statement is checkable by ear (PS: write only what can be confirmed).

Flags: hedges, emotion->acoustics inferences ("calm, so low-pitched"), unmeasurable claims, missing times for
events in long clips, > 300 words, and estimates which F3 axes are covered.
"""
from __future__ import annotations

import re

HEDGES = re.compile(r"\b(maybe|perhaps|possibly|probably|might|could be|seems?|appears? to|either|or so|kind of|"
                    r"sort of|somewhat)\b", re.I)
INFERENCE = re.compile(r"\b(calm|angry|sad|happy|anxious|nervous)\b[^.]{0,40}\b(so|therefore|hence|which means)\b",
                       re.I)
UNCHECKABLE = re.compile(r"\b(thinks|believes|wants|feels that|secretly|in her mind|in his mind)\b", re.I)
EVENT_WORDS = re.compile(r"\b(laugh|cough|sigh|breath|click|door|whistle|horn|bell|bark|clap|knock|ring)\w*", re.I)
TIME = re.compile(r"\d+(\.\d+)?\s*(s|sec|seconds|ms)\b|\d+(\.\d+)?\s*[–-]\s*\d+(\.\d+)?\s*s\b", re.I)

AXIS_HINTS = {
    "voice": re.compile(r"\b(woman|man|voice|pitch|hz|semitone|creak|breathy|falsetto|whisper|pace|syllable|pause)",
                        re.I),
    "recording": re.compile(r"\b(phone|microphone|mic|room|reverb|echo|noise|background|channel|band|codec|fan|"
                            r"traffic|hall|outdoor)", re.I),
    "intent": re.compile(r"\b(to (her|his|a|the) |addressing|talking to|speaking to|reading|teasing|scolding|"
                         r"reassuring|sarcas|mock|subtext)", re.I),
}


def axes_covered(desc: str) -> list[str]:
    return [a for a, r in AXIS_HINTS.items() if r.search(desc)]


def lint(desc: str) -> list[str]:
    w = []
    n = len(desc.split())
    if n > 300:
        w.append(f"{n} words (> 300 will be cut)")
    for m in HEDGES.finditer(desc):
        w.append(f"hedge '{m.group(0)}' - commit or drop the statement")
    if INFERENCE.search(desc):
        w.append("infers acoustics from emotion - state the acoustics directly")
    for m in UNCHECKABLE.finditer(desc):
        w.append(f"uncheckable inner state '{m.group(0)}'")
    if EVENT_WORDS.search(desc) and not TIME.search(desc) and n > 60:
        w.append("events mentioned without times - add 'at 3.2–3.9 s' style spans")
    missing = {"voice", "recording", "intent"} - set(axes_covered(desc))
    if missing:
        w.append(f"axes not covered: {', '.join(sorted(missing))}")
    return w
