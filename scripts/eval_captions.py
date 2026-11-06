"""Score caption files against the internal DevReal rubric with the LLM grader; bootstrap CIs; per-type breakdown.

  RIMET2_LLM_URL=http://localhost:8001/v1 RIMET2_LLM_MODEL=grader \
  python scripts/eval_captions.py --rubric data/rubric_hi.csv --captions runs/r0/cap_raw_hi.jsonl \
      runs/r0/cap_evidence_hi.jsonl runs/r0/cap_fused_hi.jsonl --round 0 --results results.csv

Outputs per system: mean rubric score (x10 = points), 95% CI, false-claim weight share, per-item-type table,
and a PAIRED bootstrap delta of each system vs the first one (round 0).
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from rimet2.common.bootstrap import bootstrap_ci, paired_bootstrap_delta
from rimet2.common.llm import openai_chat
from rimet2.eval import results
from rimet2.eval.grader import grade_clip
from rimet2.eval.rubric import clip_score, load_rubric_csv, score_breakdown
from rimet2.train.targeted import type_scores


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rubric", required=True)
    ap.add_argument("--captions", nargs="+", required=True)
    ap.add_argument("--round", default="0")
    ap.add_argument("--seed", type=int, default=20261104)
    ap.add_argument("--results", default="results.csv")
    ap.add_argument("--cache", default="runs/grader_cache.jsonl")
    a = ap.parse_args()
    rub = load_rubric_csv(a.rubric)
    llm = openai_chat(max_tokens=4096)
    cache = {}
    if Path(a.cache).exists():
        for l in open(a.cache, encoding="utf-8"):
            d = json.loads(l)
            cache[(d["clip_id"], d["description"])] = d["verdicts"]
    cf = open(a.cache, "a", encoding="utf-8")
    per_sys = {}
    for path in a.captions:
        name = Path(path).stem
        rows = [json.loads(l) for l in open(path, encoding="utf-8")]
        scores, bds = {}, []
        for r in rows:
            cid = r["clip_id"]
            if cid not in rub:
                continue
            key = (cid, r["description"])
            if key not in cache:
                cache[key] = grade_clip(llm, r["description"], rub[cid])
                cf.write(json.dumps({"clip_id": cid, "description": r["description"], "verdicts": cache[key]},
                                    ensure_ascii=False) + "\n")
            v = cache[key]
            scores[cid] = clip_score(rub[cid], v)
            bds.append(score_breakdown(rub[cid], v))
        ids = sorted(scores)
        pt, lo, hi = bootstrap_ci(ids, lambda xs: float(np.mean([scores[i] for i in xs])), a.seed, f"cap/{name}")
        fw = sum(sum(d["false_asserted_w"] + d["contra_w"] for d in b.values()) for b in bds)
        tw = sum(sum(d["true_w"] for d in b.values()) for b in bds)
        per_sys[name] = scores
        print(f"\n== {name}: rubric {pt:.3f} [{lo:.3f}, {hi:.3f}]  points {10 * pt:.2f}  n={len(ids)}  "
              f"false/contradicted weight share {fw / max(tw, 1e-9):.3f}")
        ts = type_scores(bds)
        for t, f in sorted(ts.items(), key=lambda kv: kv[1]):
            print(f"   {t:<13} F={f:.2f}")
        json.dump(ts, open(Path(path).with_name(f"type_scores_{name}.json"), "w"), indent=1)  # -> targeting
        results.append(a.results, [{"round": a.round, "model": "captioner", "system": name, "lang": rows[0]["lang"],
                                    "measure": "rubric_score_internal", "value": f"{pt:.4f}", "ci_low": f"{lo:.4f}",
                                    "ci_high": f"{hi:.4f}", "n_items": len(ids)}])
    names = list(per_sys)
    for n in names[1:]:
        common = sorted(set(per_sys[names[0]]) & set(per_sys[n]))
        d, lo, hi, p = paired_bootstrap_delta([per_sys[names[0]][i] for i in common],
                                              [per_sys[n][i] for i in common], a.seed, f"delta/{n}")
        print(f"\n{n} - {names[0]}: {d:+.3f} [{lo:+.3f}, {hi:+.3f}]  P(no gain)={p:.3f}")


if __name__ == "__main__":
    main()
