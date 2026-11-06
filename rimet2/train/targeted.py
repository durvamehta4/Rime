r"""Weak-area targeting + known-by-construction captioner training data.

Budget per item type k (from the per-type rubric breakdown on held-out REAL dev audio):
    n_k = N * wbar_k (1 - F_k) / sum_j wbar_j (1 - F_j)
F_k = stated_w / true_w - (contradicted_w + false_asserted_w) / true_w   (clipped to [0, 1]).

Transform recipe: take a CLEAN real clip (high SNR, wideband, dry), keep only its VERIFIED voice-axis claims,
render a random Ecology with the renderer, and add the renderer's construction claims. The before/after pair and
its delta description also train the generator (PS suggestion).
"""
from __future__ import annotations

import numpy as np

from rimet2.renderer.render import EcologyRenderer
from rimet2.scene.schema import DEFAULT_TYPE_WEIGHT, Claim, Ecology, EnvEvent, SceneScore

ECO_TYPES = {"Channel", "Space", "Other sounds", "Coupling"}


def type_scores(breakdowns: list[dict]) -> dict[str, float]:
    agg: dict[str, dict] = {}
    for b in breakdowns:
        for t, d in b.items():
            a = agg.setdefault(t, {k: 0.0 for k in d})
            for k, v in d.items():
                a[k] += v
    out = {}
    for t, d in agg.items():
        if d["true_w"] <= 0:
            continue
        f = (d["stated_w"] - d["contra_w"] - d["false_asserted_w"]) / d["true_w"]
        out[t] = float(min(1.0, max(0.0, f)))
    return out


def allocate(F: dict[str, float], N: int, weights: dict | None = None, floor: float = 0.02) -> dict[str, int]:
    w = weights or DEFAULT_TYPE_WEIGHT
    need = {t: w[t] * max(floor, 1 - f) for t, f in F.items()}
    z = sum(need.values()) or 1.0
    alloc = {t: int(round(N * v / z)) for t, v in need.items()}
    return alloc


def random_ecology(rng: np.random.Generator, focus: str | None = None, duration: float = 5.0,
                   event_labels: list[str] | None = None) -> tuple[Ecology, list[dict]]:
    """Sample an ecology; `focus` biases toward an item type that the captioner is weak on."""
    eco = Ecology()
    coupling = []
    if focus in (None, "Channel") or rng.random() < 0.35:
        eco.channel = str(rng.choice(["phone_narrowband", "landline", "voip", "voip_poor", "laptop", "clean"]))
        eco.clipping = float(rng.choice([0.0, 0.0, 0.5]))
    if focus in (None, "Space") or rng.random() < 0.4:
        eco.space = str(rng.choice(["dry", "small_room", "medium_room", "bathroom", "large_hall"]))
    if focus in (None, "Other sounds") or rng.random() < 0.5:
        eco.background = str(rng.choice(["fan hum", "traffic", "rain", "crowd chatter", "pink noise", "kitchen"]))
        eco.snr_db = float(rng.uniform(3, 30))
    if (focus in ("Other sounds", "Event", "Coupling") or rng.random() < 0.3) and event_labels:
        lab = str(rng.choice(event_labels))
        t0 = float(rng.uniform(0.3, max(0.4, duration - 1.2)))
        eco.events.append(EnvEvent(lab, round(t0, 2), round(t0 + rng.uniform(0.3, 1.0), 2),
                                   float(rng.uniform(-6, 3))))
        if focus == "Coupling":
            coupling.append({"t0": round(t0, 2), "effect": "louder", "gain_db": float(rng.choice([4, 6, 8]))})
    return eco, coupling


def transform_example(x: np.ndarray, sr: int, base: SceneScore, renderer: EcologyRenderer, rng: np.random.Generator,
                      focus: str | None = None, event_labels: list[str] | None = None, seed: int = 0):
    """Return (audio, SceneScore with exact labels, transform log)."""
    keep = [c for c in base.claims if c.verified and c.item_type not in ECO_TYPES]
    eco, coupling = random_ecology(rng, focus, len(x) / sr, event_labels)
    y, cons, log = renderer.render(x, eco, coupling, seed=seed)
    sc = SceneScore(base.lang, round(len(y) / sr, 2), keep + cons, base.transcript,
                    {**base.meta, "transform": log, "focus": focus})
    return y, sc, log


def delta_description(cons: list[Claim]) -> str:
    """Before->after instruction text for edit-style training ("Make it sound like ...")."""
    return "Make it sound as if: " + "; ".join(c.text[0].lower() + c.text[1:] for c in cons) + "."
