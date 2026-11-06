"""results.csv (mid-term deliverable) + Pareto frontier of score vs size/compute.

Columns: round,model,system,lang,measure,value,ci_low,ci_high,n_items,params_b,active_params_b,gpu_hours,notes
"""
from __future__ import annotations

import csv
from pathlib import Path

COLS = ["round", "model", "system", "lang", "measure", "value", "ci_low", "ci_high", "n_items", "params_b",
        "active_params_b", "gpu_hours", "notes"]


def append(path: str | Path, rows: list[dict]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    new = not path.exists()
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        if new:
            w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in COLS})


def pareto_front(points: list[tuple[float, float, str]]) -> list[tuple[float, float, str]]:
    """points = (cost, score, name); returns non-dominated set (lower cost, higher score), sorted by cost."""
    pts = sorted(points, key=lambda p: (p[0], -p[1]))
    front, best = [], float("-inf")
    for c, s, n in pts:
        if s > best:
            front.append((c, s, n))
            best = s
    return front


def plot_pareto(points: list[tuple[float, float, str]], out: str, xlabel: str = "active params (B)",
                ylabel: str = "rubric score") -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fr = pareto_front(points)
    fig, ax = plt.subplots(figsize=(4.5, 3.2), dpi=150)
    ax.scatter([p[0] for p in points], [p[1] for p in points], s=18, color="#888")
    ax.plot([p[0] for p in fr], [p[1] for p in fr], "-o", ms=4, color="#1f5fa8")
    for c, s, n in points:
        ax.annotate(n, (c, s), fontsize=6, xytext=(3, 3), textcoords="offset points")
    ax.set_xscale("log")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(out)
