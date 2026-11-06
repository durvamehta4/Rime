"""Hash-seeded bootstrap, following the PS Appendix A procedure exactly (no RNG library).

Draw j of replicate r selects position int(sha256(f"{seed}|bootstrap|{measure}|{r}|{j}"), 16) mod n.
CI endpoints are the 25th and 975th sorted values (zero-based 24 and 974) of 1,000 replicates.
Track 2 does not mandate Appendix A, but using it makes our CIs reproducible and familiar to judges.
"""
from __future__ import annotations

import hashlib
from typing import Callable, Sequence

import numpy as np


def _h(text: str) -> int:
    return int(hashlib.sha256(text.encode("utf-8")).hexdigest(), 16)


def selection_order(seed: int, selection: str, ids: Sequence[str]) -> list[str]:
    """Appendix A random selection: sort candidates by sha256(seed|selection|id), ties by id bytes."""
    return sorted(ids, key=lambda i: (_h(f"{seed}|{selection}|{i}"), i.encode("utf-8")))


def draw_positions(seed: int, measure: str, r: int, n: int) -> np.ndarray:
    return np.array([_h(f"{seed}|bootstrap|{measure}|{r}|{j}") % n for j in range(n)], dtype=np.int64)


def bootstrap_ci(
    items: Sequence,
    stat: Callable[[list], float],
    seed: int,
    measure: str,
    n_rep: int = 1000,
    sort_key: Callable | None = None,
) -> tuple[float, float, float]:
    """Return (point, lo, hi). `items` are sorted by UTF-8 id (sort_key) before drawing, as in Appendix A."""
    items = list(items)
    if sort_key is not None:
        items = sorted(items, key=lambda it: str(sort_key(it)).encode("utf-8"))
    n = len(items)
    if n == 0:
        return float("nan"), float("nan"), float("nan")
    point = float(stat(items))
    vals = []
    for r in range(1, n_rep + 1):
        pos = draw_positions(seed, measure, r, n)
        vals.append(float(stat([items[p] for p in pos])))
    vals.sort()
    lo_i, hi_i = int(round(0.025 * n_rep)) - 1, int(round(0.975 * n_rep)) - 1
    return point, vals[lo_i], vals[hi_i]


def paired_bootstrap_delta(
    a: Sequence[float], b: Sequence[float], seed: int, measure: str, n_rep: int = 1000
) -> tuple[float, float, float, float]:
    """Paired CI for mean(b) - mean(a) on identical draws. Returns (delta, lo, hi, p_b_not_better)."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    assert a.shape == b.shape
    n = len(a)
    d = b - a
    vals = np.empty(n_rep)
    for r in range(1, n_rep + 1):
        pos = draw_positions(seed, measure, r, n)
        vals[r - 1] = d[pos].mean()
    vals.sort()
    return float(d.mean()), float(vals[24 * n_rep // 1000]), float(vals[974 * n_rep // 1000]), float((vals <= 0).mean())
