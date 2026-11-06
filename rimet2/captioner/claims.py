"""Raw caption(s) -> atomic Claims (FActScore-style decomposition) + K-sample self-consistency."""
from __future__ import annotations

import re

from rimet2.common.llm import LLMFn, extract_json
from rimet2.scene.schema import AXES, Claim

SPLIT = """Split this audio description into short atomic factual claims, one fact each, keeping the wording
close to the original. Drop vague filler and pure speculation words ("perhaps", "suggests") by marking hedged=true.
For each claim give item_type from: Speaker, Source, Morphology, Pitch, Timing, Event, Channel, Space,
Other sounds, Coupling, Addressee, Subtext, Change.
If the claim refers to a time span give t0/t1 in seconds, else null. If it states one of these attributes
give key/value: gender (male/female), age_lo/age_hi (years), f0_median_hz, rate_syl_s, channel
(narrowband/wideband), snr_db, event (short lowercase label), phonation (modal/breathy/creaky/falsetto/whisper),
emotion (one word), language (hindi/tamil/english/...).
DESCRIPTION:
<<<{caption}>>>
Return ONLY JSON: [{{"text": "...", "item_type": "...", "t0": null, "t1": null, "hedged": false,
"key": null, "value": null}}]"""

_NORM = re.compile(r"[^a-z0-9 ]+")


def split_caption(llm: LLMFn, caption: str, source: str = "omni") -> list[Claim]:
    out = extract_json(llm(SPLIT.format(caption=caption)))
    claims = []
    for d in out:
        it = d.get("item_type")
        if it not in AXES or d.get("hedged"):
            continue
        t0, t1 = d.get("t0"), d.get("t1")
        if (t0 is None) != (t1 is None):
            t0 = t1 = None
        try:
            t0 = float(t0) if t0 is not None else None
            t1 = float(t1) if t1 is not None else None
            if t0 is not None and t1 < t0:
                t0, t1 = t1, t0
        except (TypeError, ValueError):
            t0 = t1 = None
        val = {d["key"]: d["value"]} if d.get("key") and d.get("value") is not None else {}
        claims.append(Claim(str(d["text"]).strip(), it, p=0.5, t0=t0, t1=t1, source=source, value=val))
    return claims


def _sig(c: Claim) -> str:
    if c.value:
        k, v = next(iter(c.value.items()))
        if isinstance(v, (int, float)):
            v = round(float(v), -1) if k == "f0_median_hz" else round(float(v))
        return f"{c.item_type}|{k}={str(v).lower()}"
    words = sorted(set(_NORM.sub(" ", c.text.lower()).split()) - {"the", "a", "an", "is", "of", "and", "with", "in"})
    return f"{c.item_type}|" + " ".join(words[:6])


def self_consistency(samples: list[list[Claim]]) -> list[Claim]:
    """Merge claims from K captions of the SAME clip; p = fraction of samples that contain the claim signature."""
    K = len(samples)
    buckets: dict[str, list[Claim]] = {}
    for claims in samples:
        seen = set()
        for c in claims:
            s = _sig(c)
            if s in seen:
                continue
            seen.add(s)
            buckets.setdefault(s, []).append(c)
    merged = []
    for s, cs in buckets.items():
        c = cs[0]
        timed = [x for x in cs if x.timed]
        if timed:  # median span across samples
            t0 = sorted(x.t0 for x in timed)[len(timed) // 2]
            t1 = sorted(x.t1 for x in timed)[len(timed) // 2]
            c = Claim(c.text, c.item_type, p=c.p, t0=t0, t1=max(t0, t1), source=c.source, value=c.value)
        c.p = len(cs) / K
        merged.append(c)
    return merged
