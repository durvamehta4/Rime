r"""Claims -> prose, with calibrated commitment and a 300-word budget.

Decision rule (see docs): state claim c iff  p_c > tau_c,  tau_c = q*w' / (h*w + q*w'), tuned on DevReal.
Budget: maximise sum_c p_c * w_c  s.t.  sum_c len_c <= budget  (greedy by p_c*w_c/len_c; exact for our sizes
in practice because claim lengths are similar). Output order is fixed and listener-friendly:
  header -> recording (Channel, Space, Other sounds) -> voice globals (Speaker, Source, Pitch, Timing)
  -> timeline (timed claims sorted by t0) -> intent.
"""
from __future__ import annotations

from .schema import DEFAULT_TYPE_WEIGHT, Claim, SceneScore

LANG_NAME = {"hi": "Hindi", "ta": "Tamil"}
ORDER = ["Channel", "Space", "Other sounds", "Coupling", "Speaker", "Source", "Pitch", "Timing", "Morphology",
         "Event", "Addressee", "Subtext", "Change"]


def fmt_t(t: float) -> str:
    return f"{t:.1f}"


def claim_sentence(c: Claim) -> str:
    s = c.text.strip()
    if not s.endswith((".", "!", "?")):
        s += "."
    if c.timed and not s.lower().startswith(("at ", "from ", "between ")) and fmt_t(c.t0) not in s:
        s = f"{fmt_t(c.t0)}–{fmt_t(c.t1)} s: {s}"
    return s


def select_claims(claims: list[Claim], tau: float | dict = 0.5, budget_words: int = 285,
                  weights: dict | None = None, header_words: int = 4) -> list[Claim]:
    """Calibrated commitment + knapsack. `tau` may be a float or a per-item-type dict."""
    w = weights or DEFAULT_TYPE_WEIGHT
    keep = [c for c in claims if c.p > (tau.get(c.item_type, 0.5) if isinstance(tau, dict) else tau)]
    # de-duplicate identical sentences
    seen, uniq = set(), []
    for c in keep:
        k = claim_sentence(c).lower()
        if k not in seen:
            seen.add(k)
            uniq.append(c)
    uniq.sort(key=lambda c: c.p * w[c.item_type] / max(1, len(claim_sentence(c).split())), reverse=True)
    out, used = [], header_words
    for c in uniq:
        n = len(claim_sentence(c).split())
        if used + n <= budget_words:
            out.append(c)
            used += n
    return out


def verbalize(scene: SceneScore, tau: float | dict = 0.5, budget_words: int = 285,
              weights: dict | None = None) -> str:
    chosen = select_claims(scene.claims, tau, budget_words, weights)
    header = f"{LANG_NAME.get(scene.lang, scene.lang)}, {scene.duration_s:.1f} s."
    untimed = sorted([c for c in chosen if not c.timed], key=lambda c: ORDER.index(c.item_type))
    timed = sorted([c for c in chosen if c.timed], key=lambda c: (c.t0, c.t1))
    rec = [c for c in untimed if c.axis == "recording"]
    voice = [c for c in untimed if c.axis == "voice"]
    intent = [c for c in untimed if c.axis == "intent"]
    paras = [header]
    if rec:
        paras.append(" ".join(claim_sentence(c) for c in rec))
    if voice:
        paras.append(" ".join(claim_sentence(c) for c in voice))
    if timed:
        paras.append(" ".join(claim_sentence(c) for c in timed))
    if intent:
        paras.append(" ".join(claim_sentence(c) for c in intent))
    text = "\n\n".join(paras)
    assert len(text.split()) <= 300, "description exceeds 300 words"
    return text
