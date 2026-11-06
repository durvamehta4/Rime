"""LLM rubric grader (stand-in for Rime's private fixed grader). Validate against humans (Cohen's kappa) before use.

For each clip: given a description and its rubric items, the LLM returns one verdict per item:
  stated        - the description commits to the item (no hedge); for timed items, places it within span +-0.25 s
  contradicted  - the description commits to something incompatible with the item
  absent        - otherwise (not mentioned, or only hedged "A or B")
"""
from __future__ import annotations

import json
from typing import Iterable

from rimet2.common.llm import LLMFn, extract_json
from .rubric import VERDICTS, RubricItem, clip_score

PROMPT = """You are grading an English description of an audio clip against rubric items.
For EACH item decide exactly one verdict:
- "stated": the description clearly commits to this item's content (paraphrase is fine). Hedges such as
  "either X or Y", "possibly X" do NOT count. If the item has a time span, the description must place it
  inside [start-0.25 s, end+0.25 s].
- "contradicted": the description commits to something that is incompatible with the item.
- "absent": neither.
Judge only what the description says. Numbers count as matching when they agree within about 10% (pitch,
rate) or 1 semitone (pitch ranges) or 0.25 s (times).

DESCRIPTION:
<<<{description}>>>

ITEMS:
{items}

Return ONLY a JSON list: [{{"id": "<item id>", "verdict": "stated|contradicted|absent"}}, ...]"""


def format_items(items: Iterable[RubricItem]) -> str:
    lines = []
    for it in items:
        span = f" [span {it.t0:.2f}-{it.t1:.2f} s]" if it.t0 is not None else ""
        lines.append(f'- id={it.item_id}{span}: {it.text}')
    return "\n".join(lines)


def grade_clip(llm: LLMFn, description: str, items: list[RubricItem], retries: int = 2) -> dict[str, str]:
    words = description.split()
    if len(words) > 300:  # PS: description is cut at 300 words before grading
        description = " ".join(words[:300])
    prompt = PROMPT.format(description=description, items=format_items(items))
    last_err = None
    for _ in range(retries + 1):
        try:
            out = extract_json(llm(prompt))
            v = {str(d["id"]): str(d["verdict"]).strip().lower() for d in out}
            return {it.item_id: (v.get(it.item_id) if v.get(it.item_id) in VERDICTS else "absent") for it in items}
        except Exception as e:  # malformed JSON -> retry
            last_err = e
    raise RuntimeError(f"grader failed: {last_err}")


def grade_and_score(llm: LLMFn, description: str, items: list[RubricItem]) -> tuple[float, dict[str, str]]:
    v = grade_clip(llm, description, items)
    return clip_score(items, v), v


def cohen_kappa(a: list[str], b: list[str]) -> float:
    assert len(a) == len(b) and a
    labels = sorted(set(a) | set(b))
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    pe = sum((a.count(l) / n) * (b.count(l) / n) for l in labels)
    return 1.0 if pe == 1 else (po - pe) / (1 - pe)


def dump_verdicts(path: str, rows: list[dict]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
