"""Proxy for generation 'instruction relevance' (PS: 3 listeners check each statement of the description).

1. Decompose the description into atomic, checkable statements (LLM, FActScore-style) with item type,
   optional span and optional measurable key/value.
2. Route each statement to a verifier:
   - measurable (pitch, rate, pauses, channel, snr, reverb, events with times)  -> evidence toolkit
   - perceptual (gender, phonation, emotion, intent)                           -> captioner-as-judge:
       the captioner describes the audio, an LLM decides entails / contradicts / unknown
3. Share of statements met = proxy for 5 x relevance. Validate against a small human check (report agreement).
Verifiers here are NEVER the training reward models used for the same round (avoid reward hacking).
"""
from __future__ import annotations

from dataclasses import dataclass

from rimet2.common.llm import LLMFn, extract_json
from rimet2.eval.rubric import overlaps

DECOMPOSE = """Split this voice-generation instruction into atomic statements that a listener could check in
the audio, one fact per statement. Keep times in seconds when given. For each statement give:
item_type (one of Speaker, Source, Morphology, Pitch, Timing, Event, Channel, Space, Other sounds, Coupling,
Addressee, Subtext, Change), and when measurable a key among [gender, f0_median_hz, f0_range_st,
rate_syl_s, pause_ms, channel, snr_db, rt60_s, event] with a value.
INSTRUCTION:
<<<{desc}>>>
Return ONLY JSON: [{{"text": "...", "item_type": "...", "t0": null, "t1": null, "key": null, "value": null}}]"""

ENTAIL = """Audio description written by a careful listener (it may omit things):
<<<{caption}>>>
Measured facts: {facts}
Statement to check: "{stmt}"
Answer with one word: yes (clearly true of the audio), no (clearly false), or unknown."""

TOL = {"f0_median_hz": 0.12, "f0_range_st": 3.0, "rate_syl_s": 0.25, "pause_ms": 0.35, "snr_db": 6.0, "rt60_s": 0.35}
REL = {"f0_median_hz", "rate_syl_s", "pause_ms"}  # relative tolerance keys


@dataclass
class Statement:
    text: str
    item_type: str
    t0: float | None = None
    t1: float | None = None
    key: str | None = None
    value: object = None


def decompose(llm: LLMFn, description: str) -> list[Statement]:
    out = extract_json(llm(DECOMPOSE.format(desc=description)))
    sts = []
    for d in out:
        try:
            sts.append(Statement(d["text"], d.get("item_type", "Speaker"), d.get("t0"), d.get("t1"), d.get("key"),
                                 d.get("value")))
        except KeyError:
            continue
    return sts


def check_measurable(st: Statement, scene_claims) -> bool | None:
    """Compare against evidence claims (machine values). None = cannot decide by measurement."""
    if not st.key:
        return None
    for c in scene_claims:
        if st.key not in c.value:
            continue
        if st.t0 is not None and c.timed and not overlaps(c.t0, c.t1, st.t0, st.t1 or st.t0):
            continue
        cv, sv = c.value[st.key], st.value
        if isinstance(cv, (int, float)) and isinstance(sv, (int, float)):
            tol = TOL.get(st.key, 0.15)
            return abs(cv - sv) <= (tol * abs(sv) if st.key in REL else tol)
        return str(sv).lower() in str(cv).lower() or str(cv).lower() in str(sv).lower()
    if st.key == "event":
        return False  # an event was requested but nothing was detected
    return None


def relevance(llm: LLMFn, description: str, scene_claims, caption: str) -> tuple[float, list[dict]]:
    sts = decompose(llm, description)
    facts = "; ".join(c.text for c in scene_claims[:25])
    rows = []
    for st in sts:
        ok = check_measurable(st, scene_claims)
        how = "measurement"
        if ok is None:
            ans = llm(ENTAIL.format(caption=caption, facts=facts, stmt=st.text)).strip().lower()
            ok = ans.startswith("yes")
            how = "judge"
        rows.append({"text": st.text, "item_type": st.item_type, "met": bool(ok), "how": how})
    share = sum(r["met"] for r in rows) / len(rows) if rows else 0.0
    return share, rows
