"""Preference pairs.

Captioner (anti-hallucination DPO, AHA-style): chosen = verbalised verified scene; rejected = same scene with ONE
injected false claim (flip gender, shift pitch, wrong channel, move/insert an event). This trains directly against
the rubric's false items.

Generator (DPO on own samples): for one (text, description), rank K samples on several metrics; keep only
DOMINANT pairs (winner better on every metric by a margin) - Koel-TTS / Tian et al. recipe.
"""
from __future__ import annotations

import copy
import random

from rimet2.scene.schema import Claim, SceneScore
from rimet2.scene.verbalize import verbalize

FALSE_EVENTS = ["a door slams", "a dog barks", "a phone rings", "a child shouts", "a pressure-cooker whistle"]


def corrupt(scene: SceneScore, rng: random.Random) -> tuple[SceneScore, str]:
    s = copy.deepcopy(scene)
    ops = []
    for i, c in enumerate(s.claims):
        if "gender" in c.value:
            ops.append(("gender", i))
        if "f0_median_hz" in c.value:
            ops.append(("pitch", i))
        if "channel" in c.value:
            ops.append(("channel", i))
        if c.timed and c.item_type in ("Event", "Other sounds"):
            ops.append(("move", i))
    ops.append(("insert", -1))
    op, i = rng.choice(ops)
    if op == "gender":
        g = "male" if s.claims[i].value["gender"] == "female" else "female"
        s.claims[i] = Claim(f"A {'man' if g == 'male' else 'woman'} speaks", "Speaker", 1.0, value={"gender": g})
    elif op == "pitch":
        f = s.claims[i].value["f0_median_hz"] * rng.choice([0.6, 1.6])
        s.claims[i] = Claim(f"Median pitch about {f:.0f} Hz", "Pitch", 1.0, value={"f0_median_hz": f})
    elif op == "channel":
        nb = s.claims[i].value["channel"] == "narrowband"
        s.claims[i] = Claim("A wideband studio recording, not a phone line" if nb else
                            "A narrowband phone line, band-limited to about 300–3400 Hz", "Channel", 1.0,
                            value={"channel": "wideband" if nb else "narrowband"})
    elif op == "move":
        c = s.claims[i]
        shift = rng.choice([-1, 1]) * max(1.0, (c.t1 - c.t0) + 0.8)
        t0 = min(max(0.0, c.t0 + shift), max(0.0, s.duration_s - 0.3))
        s.claims[i] = Claim(c.text, c.item_type, 1.0, t0=round(t0, 2), t1=round(min(s.duration_s, t0 + c.t1 - c.t0), 2),
                            source=c.source, value=c.value)
    else:
        t0 = round(rng.uniform(0, max(0.1, s.duration_s - 0.5)), 1)
        s.claims.append(Claim(rng.choice(FALSE_EVENTS).capitalize(), "Other sounds", 1.0, t0=t0, t1=round(t0 + 0.4, 1)))
    for c in s.claims:
        c.p = 1.0
    return s, op


def captioner_dpo_pair(scene: SceneScore, seed: int = 0) -> dict:
    rng = random.Random(seed)
    v = SceneScore(scene.lang, scene.duration_s, [c for c in scene.claims if c.verified], scene.transcript)
    for c in v.claims:
        c.p = 1.0
    bad, op = corrupt(v, rng)
    return {"chosen": verbalize(v, tau=0.0), "rejected": verbalize(bad, tau=0.0), "corruption": op}


def dominant_pairs(samples: list[dict], metrics: dict[str, int], margin: dict[str, float] | None = None
                   ) -> list[tuple[int, int]]:
    """samples: [{metric: value}], metrics: {name: +1 (higher better) | -1 (lower better)}. Returns (win, lose)."""
    margin = margin or {}
    pairs = []
    for i, a in enumerate(samples):
        for j, b in enumerate(samples):
            if i == j:
                continue
            if all(sign * (a[m] - b[m]) > margin.get(m, 0.0) for m, sign in metrics.items()):
                pairs.append((i, j))
    return pairs
