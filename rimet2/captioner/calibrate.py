r"""Calibration of claim confidences + threshold tau.

1) Per item type, fit isotonic regression p_raw -> P(claim correct) on DevReal claims whose correctness was
   judged (by the grader against human rubric items, or directly by annotators).
2) Choose tau (global or per type) maximising the mean dev rubric score; the analytic optimum for one claim is
   tau = q w' / (h w + q w') (h: chance an item covers the claim, q: chance a false claim is caught).
"""
from __future__ import annotations

import json
from collections import defaultdict
from typing import Callable, Iterable

import numpy as np


def pav(x: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Pool-adjacent-violators isotonic fit. Returns breakpoints (xs, ys) for np.interp."""
    o = np.argsort(x)
    x, y = np.asarray(x, float)[o], np.asarray(y, float)[o]
    vals, wts, xs = list(y), [1.0] * len(y), list(x)
    i = 0
    blocks = [[v, w, xx, xx] for v, w, xx in zip(vals, wts, xs)]
    while i < len(blocks) - 1:
        if blocks[i][0] > blocks[i + 1][0]:
            a, b = blocks[i], blocks[i + 1]
            w = a[1] + b[1]
            blocks[i] = [(a[0] * a[1] + b[0] * b[1]) / w, w, a[2], b[3]]
            del blocks[i + 1]
            i = max(i - 1, 0)
        else:
            i += 1
    bx = np.array([(b[2] + b[3]) / 2 for b in blocks])
    by = np.array([b[0] for b in blocks])
    return bx, by


class IsotonicCalibrator:
    def __init__(self, tables: dict | None = None, min_n: int = 15):
        self.tables = tables or {}
        self.min_n = min_n

    def fit(self, rows: Iterable[tuple[str, float, int]]) -> "IsotonicCalibrator":
        """rows: (item_type, p_raw, correct 0/1)."""
        by = defaultdict(list)
        for t, p, c in rows:
            by[t].append((p, c))
        for t, v in by.items():
            if len(v) < self.min_n:
                continue
            x, y = np.array([a for a, _ in v]), np.array([b for _, b in v])
            bx, byy = pav(x, y)
            self.tables[t] = (bx.tolist(), byy.tolist())
        return self

    def __call__(self, claim) -> float:
        tab = self.tables.get(claim.item_type)
        if not tab:
            return claim.p
        return float(np.interp(claim.p, tab[0], tab[1]))

    def save(self, path: str) -> None:
        with open(path, "w") as f:
            json.dump(self.tables, f)

    @classmethod
    def load(cls, path: str) -> "IsotonicCalibrator":
        with open(path) as f:
            return cls({k: tuple(v) for k, v in json.load(f).items()})


def search_tau(score_fn: Callable[[float], float], grid=None) -> tuple[float, dict]:
    """score_fn(tau) -> mean dev rubric score. Returns best tau and the full curve (report it in the paper)."""
    grid = grid if grid is not None else np.round(np.arange(0.2, 0.91, 0.05), 2)
    curve = {float(t): float(score_fn(float(t))) for t in grid}
    best = max(curve, key=lambda t: (curve[t], -abs(t - 0.5)))
    return best, curve


def analytic_tau(h: float, q: float, w: float = 1.0, w_pen: float = 1.0) -> float:
    return q * w_pen / (h * w + q * w_pen)
