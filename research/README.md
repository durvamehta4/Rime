# Rime Track 2: literature and architecture

The breadth-first review inspected **296 distinct publication records**, retained **277 relevant works**, and excluded **19** for scope, duplicate lineage, or unusable extraction. **28 core sources have additional scoped checks and interpretation.**

Review depth is explicit: abstracts plus selected full-text passages for the broad pass, with additional methods/results/limitations checks for core sources. This is **not a claim of 277 cover-to-cover readings**. Some automatically selected passages are introductory context or table captions; the dossier records that limitation. No paper experiments were reproduced and no model was trained. The architecture awaits native-language and T4 validation.

## Start here

- [Literature synthesis](LITERATURE_REVIEW.md): findings that change the design.
- [Recommended architecture, version 2](ARCHITECTURE_V2.md): model shortlist, timed grounding, generation, verified loop, novelty boundaries and compute choices.
- [Experiments and budget](EXPERIMENTS.md): 4×T4, 256 GB RAM, approximately 1,000 GPU-hours.
- [Core-paper findings](reviews/CORE_FINDINGS.md): evidence locations, caveats and architecture consequences.
- [Paper ledger](paper_ledger.csv): all inspected records, exclusions, URLs and snapshot hashes.
- [Paper-by-paper dossier](reviews/PAPER_BY_PAPER.md): abstracts and inspected evidence passages, with review scope.
- [Machine-readable evidence](reviews/paper_evidence.jsonl), [BibTeX](references.bib), and [review counts](REVIEW_STATUS.json).
- [Research protocol](RESEARCH_PROTOCOL.md): original target, search strategy and evidence levels.

The initial [proposal](TRACK2_ARCHITECTURE.md) is preserved for context; version 2 supersedes its backbone ordering. RASMALAI and the verified public Indic Parler model card move description-native Indic Parler-TTS ahead of building new description controls into IndicF5.

## Access and reproducibility

Research sites became accessible after the user's publication. No environment changes were reapplied and nothing was published by the agent. Searches, acquisition scripts, hashes and evidence are saved. Raw PDFs/extracted text are local caches in `papers/`; public documentation snapshots are in `sources/`. They are excluded from Git to avoid committing a large third-party corpus. Original sources and licenses remain authoritative.

Indic Parler's public card/API can be read, but its model is automatically gated and unauthenticated config retrieval returned 401. That affects future execution, not this paper review. No credential values were requested, printed or saved. Indic-Speak is separately gated with a custom license and is not assumed interchangeable with a description-controlled model.

The PS is the user-uploaded **Rime (1).pdf**, `sediment://file_00000000589c82088b96fab02ca758a0`. Its rules are design constraints, not authorization to contact organizers, publish repositories, record people or spend paid GPU compute.
