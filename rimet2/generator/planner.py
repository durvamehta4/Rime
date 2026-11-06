"""Planner: free-text description + text to say -> RenderPlan (timed segments, voice style, ecology, coupling).

Factorisation: the voice model gets only VOICE-side instructions per segment; the ecology renderer gets the
RECORDING axis; coupling becomes both a voice instruction (louder/brighter) and a level change.
Round 1 uses a prompted Qwen3-8B; round 2 a LoRA trained on (verbaliser prose -> plan) pairs (train/lora_llm.py).
"""
from __future__ import annotations

import json
import re

from rimet2.common.llm import LLMFn, extract_json
from rimet2.scene.schema import Ecology, RenderPlan, Segment

PROMPT = """You turn a voice-generation instruction into a JSON render plan for a {lang_name} TTS system.
Text to say (native script, must be spoken exactly, split across segments in order, nothing added or dropped):
<<<{text}>>>
Instruction:
<<<{desc}>>>

Rules:
- speaker: gender ("female"/"male"/null), age_band (e.g. "20-30" or null), region (or null), f0_hz (number or
  null), timbre (short English words or "").
- global_style: one short English instruction for the voice (pace, phonation, emotion) that holds for the
  whole clip. Never mention room, microphone, phone line or background sounds here.
- segments: split the text where the instruction changes delivery or timing. Each: text (exact substring),
  t0/t1 (seconds if the instruction gives times, else null), style (voice-only instruction for this part),
  pause_after_ms (integer), events_inline (subset of ["[laugh]","[breath]","[sigh]","[cough]"] placed AFTER
  the words if the speaker makes that sound there).
- ecology: channel one of [clean, phone_narrowband, landline, voip, voip_poor, laptop]; codec "" unless named;
  clipping 0..1; space one of [dry, small_room, medium_room, bathroom, large_hall]; rt60_s or null;
  background (short noun phrase or ""); snr_db (number, lower = louder noise) or null; events: list of
  non-speech sounds with label, t0, t1, level_db_rel_speech (-20 quiet .. +3 loud), query.
- coupling: list of {{"t0": s, "effect": "louder_brighter", "gain_db": number}} only if the voice reacts to noise.
- target_duration_s: number if given, else null.
Return ONLY the JSON object with keys lang, speaker, global_style, segments, ecology, coupling, target_duration_s."""

LANG_NAME = {"hi": "Hindi", "ta": "Tamil"}


def plan_llm(llm: LLMFn, text: str, desc: str, lang: str) -> RenderPlan:
    d = extract_json(llm(PROMPT.format(text=text, desc=desc, lang_name=LANG_NAME.get(lang, lang))))
    d["lang"] = lang
    plan = RenderPlan.from_dict(d)
    return repair(plan, text, lang)


def repair(plan: RenderPlan, text: str, lang: str) -> RenderPlan:
    """Guarantee the words: if segments don't reproduce the text exactly, fall back to one segment."""
    joined = " ".join(s.text.strip() for s in plan.segments if s.text.strip())
    norm = lambda s: re.sub(r"\s+", " ", s).strip()
    if norm(joined) != norm(text):
        style = plan.global_style or (plan.segments[0].style if plan.segments else "")
        plan.segments = [Segment(text=text, style=style)]
    for s in plan.segments:
        s.events_inline = [e for e in s.events_inline if e in ("[laugh]", "[breath]", "[sigh]", "[cough]")]
    return plan


# ---------- rule-based fallback (no LLM; also used in tests) ----------
_CH = [("phone", "phone_narrowband"), ("telephone", "landline"), ("call", "phone_narrowband"),
       ("laptop", "laptop"), ("video call", "voip")]
_SP = [("bathroom", "bathroom"), ("tiled", "bathroom"), ("hall", "large_hall"), ("echo", "large_hall"),
       ("small room", "small_room"), ("room", "small_room"), ("studio", "dry"), ("close mic", "dry")]


def plan_rules(text: str, desc: str, lang: str) -> RenderPlan:
    d = desc.lower()
    g = "female" if re.search(r"\b(woman|female|girl|lady)\b", d) else ("male" if re.search(r"\b(man|male|boy)\b", d)
                                                                       else None)
    m = re.search(r"(\d{2,3})\s*hz", d)
    eco = Ecology(channel=next((v for k, v in _CH if k in d), "clean"),
                  space=next((v for k, v in _SP if k in d), "dry"))
    m2 = re.search(r"(fan|traffic|rain|tv|television|crowd|kitchen|hum)", d)
    if m2:
        eco.background, eco.snr_db = m2.group(1), 15.0
    style = ", ".join(w for w in ["slow" if "slow" in d else "", "fast" if "fast" in d else "",
                                  "whisper" if "whisper" in d else "", "excited" if "excit" in d else "",
                                  "calm" if "calm" in d else ""] if w)
    return RenderPlan(lang=lang, speaker={"gender": g, "f0_hz": float(m.group(1)) if m else None},
                      global_style=style, segments=[Segment(text=text, style=style)], ecology=eco)


def plan(text: str, desc: str, lang: str, llm: LLMFn | None = None) -> RenderPlan:
    if llm is None:
        return plan_rules(text, desc, lang)
    try:
        return plan_llm(llm, text, desc, lang)
    except Exception:
        return plan_rules(text, desc, lang)


def voice_instruct(p: RenderPlan, seg: Segment) -> str:
    """Voice-side instruction for one segment (speaker attributes + style, never ecology)."""
    sp = p.speaker or {}
    who = " ".join(x for x in [sp.get("age_band") and f"{sp['age_band']} year old", sp.get("gender"),
                               sp.get("region") and f"speaker of {sp['region']}"] if x)
    bits = [f"A {who} voice." if who else "", f"Pitch around {sp['f0_hz']:.0f} Hz." if sp.get("f0_hz") else "",
            sp.get("timbre", ""), p.global_style, seg.style]
    return " ".join(b.strip() for b in bits if b and b.strip())


def dumps(p: RenderPlan) -> str:
    return json.dumps(json.loads(p.to_json()), ensure_ascii=False)
