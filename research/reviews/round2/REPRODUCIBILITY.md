# Round-two acquisition and review scope

The search focused on gaps in the first architecture: missing voice variation, identity/style separation, delivery captioning, measurement validity, claim-risk calibration, event TTS and synthetic feedback. It is a purposive technical review, not an exhaustive or preregistered systematic review.

Run from any checkout with Python, PyMuPDF (`fitz`) and permitted arXiv access:

```bash
python research/tools/round2_collect.py
python research/tools/round2_acquire.py
python research/tools/round2_read.py
python research/tools/round2_read.py 2309.02285 0 17000
```

The first script saves query responses to the ignored PDF cache and metadata to `discovered.json`. The second selects the 16 fixed IDs in `selected.json`, checks absence from the prior ledger, downloads PDFs and saves extraction/hash metadata. The third creates pre-reference text views and displays bounded character ranges. Reference-heading extraction is heuristic: some appendices precede references and some headings may be missed. A `.main.txt` file is a reading aid, not proof that every character was reviewed.

Acquisition scripts use unversioned arXiv download URLs. The committed source records include a detected snapshot version where available and a SHA-256 hash; later downloads may differ. Compare the hash and publication/update dates before claiming to reproduce the same evidence. Raw PDFs, extraction and query caches are excluded from Git. The sources' own licenses and terms remain authoritative.

`ledger.csv` and `STATUS.json` are curated reading records, not outputs of an automatic “paper read” classifier. Ten main-text readings produced the method/result/limitation/transfer notes in `DETAILED_REVIEWS.md`. Six remaining PDFs were acquired, with metadata/abstract screening only; their detailed review is unfinished. No figure-by-figure visual inspection, complete appendix/proof verification, experiment reproduction, Hindi/Tamil benchmark or T4 profile is claimed.

The earlier breadth ledger remains unchanged: 296 records, 277 retained, 28 additional scoped core checks. This pass adds 16 distinct IDs, so there are 312 unique records across passes, but **312 is not a count of detailed full-paper reviews**. Source `status` means acquisition; review depth is the separate ledger field.

The new design is [architecture version 3](../../ARCHITECTURE_V3.md); its budget replaces version 2 rather than adding another 1,000 hours. The actual work in this change is research and documentation, with no training compute spent or environment configuration published.
