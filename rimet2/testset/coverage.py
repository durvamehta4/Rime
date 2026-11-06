"""Item-type coverage matrix for the contributed test set (goes in the report: 'test sets cover hard cases').

Input CSV (filled by the team while recording/writing): id,kind(clip|desc),lang,item_types(semicolon list),hard(0/1)
  python -m rimet2.testset.coverage --tags testset_src/coverage_tags.csv
"""
from __future__ import annotations

import argparse
import csv
from collections import Counter

from rimet2.scene.schema import ITEM_TYPES


def matrix(rows: list[dict]) -> dict:
    out = {}
    for kind in ("clip", "desc"):
        for lang in ("hi", "ta"):
            c = Counter()
            n = hard = 0
            for r in rows:
                if r["kind"] != kind or r["lang"] != lang:
                    continue
                n += 1
                hard += int(r.get("hard", 0) or 0)
                for t in r["item_types"].split(";"):
                    if t.strip():
                        c[t.strip()] += 1
            out[(kind, lang)] = {"n": n, "hard": hard, **{t: c.get(t, 0) for t in ITEM_TYPES}}
    return out


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--tags", required=True)
    a = ap.parse_args(argv)
    m = matrix(list(csv.DictReader(open(a.tags, encoding="utf-8"))))
    hdr = ["kind", "lang", "n", "hard"] + ITEM_TYPES
    print(",".join(hdr))
    for (k, l), d in m.items():
        print(",".join([k, l] + [str(d[h]) for h in hdr[2:]]))
    gaps = [(k, l, t) for (k, l), d in m.items() for t in ITEM_TYPES if d["n"] and d[t] < 3]
    if gaps:
        print("\nTypes with < 3 items:", "; ".join(f"{k}/{l}:{t}" for k, l, t in gaps))


if __name__ == "__main__":
    main()
