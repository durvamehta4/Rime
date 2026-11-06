"""Audio -> evidence dict -> verifiable Claims (SceneScore). Claims carry calibrated-ish priors `p`;
captioner/calibrate.py refits these on DevReal annotations (isotonic per item type).

CLI:  python -m rimet2.evidence.run clip.wav --lang hi [--neural] > evidence.json
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict

import numpy as np

from rimet2.common.audio import load
from rimet2.scene.schema import Claim, SceneScore

from . import dsp, pitch, timing, voicequality

ANALYSIS_SR = 16000


def collect(x: np.ndarray, sr: int, neural: bool = False, device: str = "cuda", pitch_backend: str = "yin") -> dict:
    ev: dict = {"duration_s": round(len(x) / sr, 3), "sr": sr}
    segs = None
    if neural:
        from . import models
        segs = models.silero_segments(x, sr)
    segs = segs if segs else dsp.energy_vad(x, sr)
    ev["speech_segments"] = segs
    band = dsp.bandwidth(x, sr)
    ev["band"] = asdict(band)
    ev["clipping_ratio"] = dsp.clipping_ratio(x)
    ev["snr_dsp_db"] = dsp.snr_active(x, sr, segs)
    ev["loudness_std_db"] = dsp.loudness_flatness(x, sr, segs)
    t, f0, ap = pitch.track(x, sr, backend=pitch_backend, device=device)
    st = pitch.stats(f0)
    ev["pitch"] = asdict(st) if st else None
    ev["creak_spans"] = voicequality.creak_spans(t, f0, ap, x, sr, segs) if st else []
    tm = timing.timing(x, sr, segs)
    ev["timing"] = {"pauses": tm.pauses, "speech_time_s": tm.speech_time_s, "syllables": tm.syllables,
                    "rate_syl_s": tm.rate_syl_s, "onset_s": tm.onset_s, "offset_s": tm.offset_s,
                    "isochrony_cv": timing.isochrony(tm.nuclei_t)}
    # per-segment pitch movement (for Morphology/Pitch contour claims)
    ev["segment_pitch_move_st"] = [pitch.segment_slope_st(t, f0, a, b) for a, b in segs]
    if neural:
        from . import models
        ev["brouhaha"] = models.brouhaha(x, sr, device)
        ev["sed"] = models.sed_events(x, sr, device=device)
        ev["age_gender"] = models.age_gender(x, sr, device)
    return ev


def _gender(ev: dict) -> tuple[str | None, float]:
    ag = ev.get("age_gender")
    if ag:
        pf, pm = ag["p_female"], ag["p_male"]
        if max(pf, pm) > 0.5:
            return ("female", pf) if pf > pm else ("male", pm)
    st = ev.get("pitch")
    if st:  # weak F0 prior; only used when the classifier is absent
        f = st["median_hz"]
        if f > 185:
            return "female", 0.75
        if f < 135:
            return "male", 0.75
    return None, 0.0


def claims_from_evidence(ev: dict) -> list[Claim]:
    C: list[Claim] = []
    dur = ev["duration_s"]
    # ---- Channel ----
    b = ev["band"]
    if b["narrowband"]:
        C.append(Claim(f"A narrowband, telephone-like channel: the voice is band-limited to roughly "
                       f"{int(round(b['low_hz'], -1))}–{int(round(b['high_hz'], -2))} Hz", "Channel", p=0.85,
                       source="measurement", value={"channel": "narrowband", "band_high_hz": b["high_hz"]}))
    elif b["high_hz"] >= 6500:
        C.append(Claim(f"A wideband recording with energy up to about {b['high_hz'] / 1000:.0f} kHz, not a phone line",
                       "Channel", p=0.75, source="measurement", value={"channel": "wideband",
                                                                       "band_high_hz": b["high_hz"]}))
    if ev["clipping_ratio"] > 2e-4:
        C.append(Claim("The loudest syllables are clipped, adding a harsh distortion", "Channel", p=0.7,
                       source="measurement", value={"clipping": True}))
    # ---- Space / noise ----
    br = ev.get("brouhaha") or {}
    snr = br.get("snr_db") if br.get("snr_db") is not None else ev["snr_dsp_db"]
    src = "measurement"
    if snr is not None:
        if snr >= 30:
            C.append(Claim("The background is quiet; the noise floor sits far below the voice", "Other sounds",
                           p=0.7, source=src, value={"snr_db": snr}))
        elif snr <= 12:
            C.append(Claim(f"A steady background noise is clearly audible, only about {snr:.0f} dB below the voice",
                           "Other sounds", p=0.65, source=src, value={"snr_db": snr}))
    c50 = br.get("c50_db")
    if c50 is not None:
        if c50 >= 25:
            C.append(Claim("Close microphone in a dry space; almost no room reverberation", "Space", p=0.65,
                           source="measurement", value={"c50_db": c50}))
        elif c50 <= 8:
            C.append(Claim("Noticeable room reverberation: the voice rings in a reflective room", "Space", p=0.6,
                           source="measurement", value={"c50_db": c50}))
    # ---- Speaker ----
    g, pg = _gender(ev)
    if g:
        C.append(Claim(f"A {'woman' if g == 'female' else 'man'} speaks", "Speaker", p=pg,
                       source="measurement", value={"gender": g}))
    ag = ev.get("age_gender")
    if ag and ag.get("age_years"):
        a = ag["age_years"]
        lo = int(max(18, 10 * np.floor((a - 8) / 10)))
        C.append(Claim(f"Adult, roughly {lo} to {lo + 20} years old", "Speaker", p=0.45, source="model",
                       value={"age_lo": lo, "age_hi": lo + 20}))
    # ---- Pitch ----
    st = ev.get("pitch")
    if st and st["n_voiced"] >= 30:
        conf = 0.9 if st["voiced_frac"] > 0.25 else 0.7
        C.append(Claim(f"Median pitch about {st['median_hz']:.0f} Hz", "Pitch", p=conf, source="measurement",
                       value={"f0_median_hz": st["median_hz"]}))
        rng = st["range_st"]
        desc = "a narrow, fairly flat" if rng < 4 else ("a moderate" if rng < 8 else "a wide, animated")
        C.append(Claim(f"Pitch moves within {desc} range of about {rng:.0f} semitones", "Pitch", p=conf - 0.1,
                       source="measurement", value={"f0_range_st": rng}))
    # ---- Timing ----
    tm = ev["timing"]
    if tm["speech_time_s"] > 1.0 and tm["syllables"] >= 4:
        r = tm["rate_syl_s"]
        pace = "slow" if r < 3.5 else ("brisk" if r > 6 else "moderate")
        C.append(Claim(f"A {pace} pace of about {r:.1f} syllables per second", "Timing", p=0.65,
                       source="measurement", value={"rate_syl_s": r}))
    if tm["onset_s"] > 0.4:
        C.append(Claim(f"Speech starts after about {tm['onset_s']:.1f} s of lead-in", "Timing", p=0.75,
                       source="measurement", value={"onset_s": tm["onset_s"]}))
    for a, bb in tm["pauses"]:
        if bb - a >= 0.3:
            C.append(Claim(f"A pause of about {int(round((bb - a) * 1000, -1))} ms", "Timing", p=0.75,
                           t0=round(a, 2), t1=round(bb, 2), source="measurement", value={"pause_ms": (bb - a) * 1000}))
    if ev["loudness_std_db"] and ev["loudness_std_db"] < 3.0 and tm["speech_time_s"] > 2:
        C.append(Claim("Loudness stays even throughout", "Morphology", p=0.55, source="measurement",
                       value={"loudness_std_db": ev["loudness_std_db"]}))
    # ---- Source (phonation) ----
    for a, bb in ev.get("creak_spans", [])[:3]:
        C.append(Claim("Creaky voice (vocal fry) with low, irregular pulses", "Source", p=0.5, t0=a, t1=bb,
                       source="measurement", value={"phonation": "creaky"}))
    # ---- Events ----
    for e in (ev.get("sed") or []):
        it = "Event" if e["vocal"] else "Other sounds"
        if e["t1"] - e["t0"] >= 0.9 * dur:
            C.append(Claim(f"Throughout the clip: {e['label'].lower()} in the background", it, p=min(0.9, e["p"]),
                           source="model", value={"event": e["label"].lower()}))
        else:
            C.append(Claim(f"{e['label']}", it, p=min(0.9, e["p"]), t0=e["t0"], t1=e["t1"], source="model",
                           value={"event": e["label"].lower()}))
    return C


def scene_from_audio(path_or_x, lang: str, sr: int | None = None, neural: bool = False, device: str = "cuda",
                     pitch_backend: str = "yin") -> tuple[SceneScore, dict]:
    if isinstance(path_or_x, str):
        x, sr = load(path_or_x, sr=ANALYSIS_SR)
    else:
        x = path_or_x
    ev = collect(x, sr, neural=neural, device=device, pitch_backend=pitch_backend)
    return SceneScore(lang=lang, duration_s=ev["duration_s"], claims=claims_from_evidence(ev),
                      meta={"evidence_version": "v1"}), ev


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("audio")
    ap.add_argument("--lang", default="hi")
    ap.add_argument("--neural", action="store_true")
    ap.add_argument("--device", default="cuda")
    ap.add_argument("--pitch-backend", default="yin")
    a = ap.parse_args(argv)
    scene, ev = scene_from_audio(a.audio, a.lang, neural=a.neural, device=a.device, pitch_backend=a.pitch_backend)
    json.dump({"evidence": ev, "scene": json.loads(scene.to_json())}, sys.stdout, ensure_ascii=False, indent=1,
              default=float)


if __name__ == "__main__":
    main()
