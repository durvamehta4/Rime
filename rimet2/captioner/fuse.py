"""Fuse measurement claims (evidence toolkit) with model claims (Omni captioner) into one calibrated SceneScore.

Rules (the 'Verified Loop' captioner side):
  1. Measurement claims are kept with their own priors.
  2. A model claim that CONFLICTS with a measurement on the same key (gender, f0, channel, snr, event time) is dropped.
  3. A model claim that AGREES with a measurement raises that claim's p (agree += 1) and is merged into it.
  4. Model-only claims keep p = self-consistency frequency x item-type prior (intent claims heavily discounted).
  5. Optional calibrator maps raw p -> calibrated probability per item type (isotonic, fitted on DevReal).
"""
from __future__ import annotations

from rimet2.eval.rubric import overlaps
from rimet2.scene.schema import Claim, SceneScore

MODEL_PRIOR = {  # how often an Omni claim of this type is right, before calibration (conservative defaults)
    "Speaker": 0.8, "Source": 0.55, "Morphology": 0.5, "Pitch": 0.5, "Timing": 0.45, "Event": 0.6,
    "Channel": 0.6, "Space": 0.6, "Other sounds": 0.65, "Coupling": 0.35,
    "Addressee": 0.35, "Subtext": 0.3, "Change": 0.35,
}
NUM_TOL = {"f0_median_hz": 0.15, "snr_db": 8.0, "rate_syl_s": 0.3}


def _conflict(m: Claim, c: Claim) -> bool | None:
    """True=conflict, False=agree, None=unrelated."""
    shared = set(m.value) & set(c.value)
    if not shared:
        return None
    k = next(iter(shared))
    mv, cv = m.value[k], c.value[k]
    if k == "event":
        if not (m.timed and c.timed):
            return None
        same = str(mv).split()[0] in str(cv) or str(cv).split()[0] in str(mv)
        return None if not same else (not overlaps(m.t0, m.t1, c.t0, c.t1))
    if isinstance(mv, (int, float)) and isinstance(cv, (int, float)):
        tol = NUM_TOL.get(k, 0.2)
        rel = k in ("f0_median_hz", "rate_syl_s")
        return abs(mv - cv) > (tol * abs(mv) if rel else tol)
    return str(mv).lower() != str(cv).lower()


def fuse(measured: list[Claim], model_claims: list[Claim], lang: str, duration_s: float,
         calibrator=None, transcript: str = "") -> SceneScore:
    out = [Claim(**{**m.__dict__}) for m in measured]
    authorities = list(out)  # evidence-toolkit claims are the reference for conflict checks
    for c in model_claims:
        verdicts = [(m, _conflict(m, c)) for m in authorities]
        if any(v is True for _, v in verdicts):
            continue  # rule 2
        agreeing = [m for m, v in verdicts if v is False]
        if agreeing:  # rule 3
            for m in agreeing:
                m.agree += 1
                m.p = 1 - (1 - m.p) * (1 - MODEL_PRIOR[c.item_type] * c.p)
            continue
        c2 = Claim(**{**c.__dict__})
        c2.p = MODEL_PRIOR[c.item_type] * c.p if c.source in ("omni", "llm", "model") else c.p
        out.append(c2)  # rule 4
    if calibrator is not None:
        for c in out:
            c.p = calibrator(c)
    out = [c for c in out if not (c.timed and c.t1 > duration_s + 0.5)]  # spans past the end are hallucinated
    return SceneScore(lang=lang, duration_s=duration_s, claims=out, transcript=transcript,
                      meta={"fusion": "v1", "n_measured": len(measured), "n_model": len(model_claims)})
