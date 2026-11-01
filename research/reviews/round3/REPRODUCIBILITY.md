# Round 3 provenance and reproduction

The pass searches public arXiv metadata, fixes a selection of 103 previously absent publications and reads identified full-text passages critically. It is not a systematic review of every publisher, a citation-network census, an exhaustive appendix/figure reading or an experiment reproduction. The cutoff is 2026-11-01. Titles, versions, authors, URLs and hashes are in [ledger.csv](ledger.csv); each `ID.source.json` preserves acquisition metadata separately from review status.

## What each artifact proves

- `discovered.json` records thematic query results, including irrelevant matches. `seed_metadata.json` and `extra_metadata.json` preserve candidate metadata, including rejected title/ID guesses. Presence in these files is not inclusion or review.
- `selected.json` is the fixed, manually screened 103-record selection. No prior 296-record or round-2 16-record ID is counted again. Exact normalized-title overlap is checked as well; separate follow-up papers remain separate studies.
- `ID.source.json` records the downloaded PDF SHA-256, version evidence, page count and retrieval time. Two PDFs lack an extracted version marker; their v1 identity was verified through cached API entries and matching versioned-URL PDF hashes. Its `not_reviewed_by_acquisition` value is deliberate: downloading is not reading.
- The 13 numbered Markdown files are the curated review record. Each paper has method, author-reported evidence, limitations and a concrete architecture/test decision, with scope stated. General audio, statistical, efficiency and guitar-effect findings are marked as supporting transfer evidence.
- `reading_locators.jsonl` records prepared/inspected method/result/conclusion character/page ranges, reader-requested follow-ups, text hashes and the hash of the associated written note. Locators help find evidence; an automated passage selector cannot certify understanding or exhaustive reading. Some heuristic ranges miss their intended section; follow-ups and the scope notes address observed misses.
- `STATUS.json` counts the actual written review sections. It leaves previous evidence depths intact. No model was trained or benchmarked on T4; no author-reported number was independently reproduced.

Raw PDF/text/packet/query caches remain under ignored `research/papers/round3/`. Long source passages are not committed as a new third-party corpus. The Git artifacts preserve locators, public abstracts/metadata, hashes and critical notes. PDF extraction loses some equation/table/figure layout; uninspected visual figures are not claimed as read.

## Reproduce acquisition and inspect evidence

Use Python 3 and PyMuPDF (`import fitz`); acquisition uses the standard-library HTTP client and the environment's ordinary network trust. No credentials or paid APIs are needed. Run from the repository root:

```bash
python research/tools/round3_acquire.py
python research/tools/round3_packet.py 2111.05095
python research/tools/round3_read.py 2111.05095 7900 3300
python research/tools/round3_finalize.py --check
```

`round3_acquire.py` reuses local PDFs and requests the recorded version for missing snapshots, rejecting a hash mismatch where a source hash already exists. Original arXiv revision bytes can change or be unavailable; report a mismatch instead of silently treating a new snapshot as the reviewed one. Character offsets apply to the saved extracted-text hash; PyMuPDF versions can change extraction order. Save a distinct snapshot/offset set when changing extraction, rather than claiming identical evidence.

`ROUND3_COMPACT=1 python research/tools/round3_packet.py ID` prepares shorter reading passages. Packet creation/re-reading does not create a written review or change its count. Re-running these tools can change packet locators; preserve the original ledger or record an explicitly updated reading pass. `round3_finalize.py` only assembles/verifies counts, hashes and links from existing curated notes, and fails if notes are missing; it cannot generate review conclusions.

The discovery script has cached thematic queries and gentle pacing, and acquisition uses two workers with spaced network requests. Re-running discovery may return a different index snapshot; the committed selection is authoritative for this pass. Bibliographic references are arXiv publications/preprints, not a claim that all 103 are peer-reviewed or direct native-language experiments.
