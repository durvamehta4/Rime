r"""Rubric scoring exactly as in the PS (Track 2, description rubric).

    S(d) = max(0, [ sum_{i in T} w_i 1[stated_i] - sum_{i in T} w_i 1[contradicted_i] - sum_{j in F} w_j 1[asserted_j] ]
                  / sum_{i in T} w_i )
A timed item counts as stated only if the description places it within [t0-0.25, t1+0.25].
Points = 10 * mean_clip S.
"""
from __future__ import annotations

import csv
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Optional

TIME_TOL = 0.25
VERDICTS = ("stated", "contradicted", "absent")


@dataclass
class RubricItem:
    item_id: str
    clip_id: str
    item_type: str
    text: str
    weight: float = 1.0
    is_true: bool = True  # False => a "false statement" item; asserting it is penalised
    t0: Optional[float] = None
    t1: Optional[float] = None
    key: str = ""  # optional machine key for structured grading (e.g. "gender", "f0_median_hz", "event:laugh")
    value: object = None
    tol: float = 0.0  # numeric tolerance for structured grading (absolute)

    @property
    def axis(self) -> str:
        from rimet2.scene.schema import AXES
        return AXES.get(self.item_type, "?")


def clip_score(items: list[RubricItem], verdicts: dict[str, str]) -> float:
    true_w = sum(i.weight for i in items if i.is_true)
    if true_w <= 0:
        return 0.0
    gain = sum(i.weight for i in items if i.is_true and verdicts.get(i.item_id) == "stated")
    loss = sum(i.weight for i in items if i.is_true and verdicts.get(i.item_id) == "contradicted")
    loss += sum(i.weight for i in items if not i.is_true and verdicts.get(i.item_id) == "stated")
    return max(0.0, (gain - loss) / true_w)


def score_breakdown(items: list[RubricItem], verdicts: dict[str, str]) -> dict:
    """Per-item-type recall / contradiction / false-assertion weights (for failure analysis by axis)."""
    out: dict[str, dict] = {}
    for i in items:
        d = out.setdefault(i.item_type, {"true_w": 0.0, "stated_w": 0.0, "contra_w": 0.0, "false_w": 0.0,
                                         "false_asserted_w": 0.0})
        v = verdicts.get(i.item_id, "absent")
        if i.is_true:
            d["true_w"] += i.weight
            d["stated_w"] += i.weight * (v == "stated")
            d["contra_w"] += i.weight * (v == "contradicted")
        else:
            d["false_w"] += i.weight
            d["false_asserted_w"] += i.weight * (v == "stated")
    return out


def within_span(c_t0: float, c_t1: float, i_t0: float, i_t1: float, tol: float = TIME_TOL) -> bool:
    """A timed claim counts if it is placed inside the item span widened by `tol` on each side."""
    return c_t0 >= i_t0 - tol and c_t1 <= i_t1 + tol


def overlaps(c_t0: float, c_t1: float, i_t0: float, i_t1: float, tol: float = TIME_TOL) -> bool:
    return c_t0 <= i_t1 + tol and c_t1 >= i_t0 - tol


# ---------------- structured (oracle) grading for synthetic / constructed clips ----------------
def structured_verdicts(items: list[RubricItem], claims) -> dict[str, str]:
    """Grade machine-readable claims against machine-readable items (exact labels known by construction).

    claim.value is a dict; item.key/value/tol define the check. Timed items also need span agreement.
    """
    verdicts = {}
    for it in items:
        v = "absent"
        if it.key:
            for c in claims:
                if it.key not in c.value:
                    continue
                cv = c.value[it.key]
                if it.t0 is not None and c.timed and not overlaps(c.t0, c.t1, it.t0, it.t1):
                    continue  # different moment: not about this item
                if isinstance(it.value, (int, float)) and isinstance(cv, (int, float)):
                    match = abs(float(cv) - float(it.value)) <= it.tol
                else:
                    match = str(cv).lower() == str(it.value).lower()
                if match and it.t0 is not None:
                    match = c.timed and within_span(c.t0, c.t1, it.t0, it.t1)
                    if not match:
                        continue
                v = "stated" if match else "contradicted"
                if v == "stated":
                    break
        verdicts[it.item_id] = v
    return verdicts


# ---------------- IO ----------------
def load_rubric_csv(path: str | Path) -> dict[str, list[RubricItem]]:
    """CSV columns: clip_id,item_id,item_type,text,weight,is_true,t0,t1[,key,value,tol]."""
    by_clip: dict[str, list[RubricItem]] = {}
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            def fnum(x):
                return float(x) if x not in (None, "") else None
            val = r.get("value", "")
            try:
                val = json.loads(val) if val not in ("", None) else None
            except json.JSONDecodeError:
                pass
            it = RubricItem(item_id=r["item_id"], clip_id=r["clip_id"], item_type=r["item_type"], text=r["text"],
                            weight=float(r.get("weight") or 1), is_true=str(r.get("is_true", "1")).lower() in
                            ("1", "true", "yes", "t"), t0=fnum(r.get("t0")), t1=fnum(r.get("t1")),
                            key=r.get("key", "") or "", value=val, tol=float(r.get("tol") or 0))
            by_clip.setdefault(it.clip_id, []).append(it)
    return by_clip


def mean_points(scores: Iterable[float], weight: float = 10.0) -> float:
    s = list(scores)
    return weight * sum(s) / len(s) if s else 0.0
