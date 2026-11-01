# Rime Track 2: literature and architecture

**Current recommendation: [architecture v4](ARCHITECTURE_V4.md)** for **4×T4, 256 GB RAM and 1,000 GPU-hours**.

The latest pass adds **103 distinct scoped full-text critical reviews**, with methods, author-reported results, limitations and concrete design decisions. None repeats an ID from the previous 312-record corpus. See the [103-paper index](reviews/round3/README.md), [evidence ledger](reviews/round3/ledger.csv), [decision matrix](reviews/round3/DECISIONS.md) and [review status](reviews/round3/STATUS.json).

These are selected method/result/limitation passage reviews, **not cover-to-cover readings of all 103 papers and appendices**. No experiment was reproduced, model trained or T4 benchmark run. The architecture's expected improvements require the proposed native-language tests.

## Read first

- [Architecture v4](ARCHITECTURE_V4.md): shared encoder readouts, source/polarity-aware claims, stable identity, native delivery, scene rendering and one controlled reciprocal round.
- [What changed and why](reviews/round3/DECISIONS.md): supporting and conflicting evidence, tests and novelty boundaries.
- [All 103 additional reviews](reviews/round3/README.md): 13 topic files, source versions/hashes and reading locators.
- [Experiments and compute allocation](EXPERIMENTS.md): 1,000 GPU-hours, matched controls, all ten final generations and sealed real audits.
- [Literature synthesis](LITERATURE_REVIEW.md): current findings alongside earlier evidence.
- [Reproduce this research pass](reviews/round3/REPRODUCIBILITY.md): acquisition, passage inspection, provenance and validation.

## Evidence depth across passes

| Pass | Distinct records | What was done |
|---|---:|---|
| Original broad review | 296 | Abstracts and selected passages; 277 retained, 19 excluded; 28 core sources received additional scoped checks |
| Previous deeper pass | 16 additional | Ten main-text reviews; six acquired-only leads remain unfinished |
| Latest pass | 103 additional | 103 curated scoped full-text critical reviews, no prior-ID overlap |
| **All passes** | **415 unique records** | Different evidence depths, not 415 detailed or exhaustive readings |

The two additional passes contain **113 detailed reviews with their separately stated scopes**. This does not upgrade the original screening or the six acquired-only leads. [Original counts](REVIEW_STATUS.json), [previous-pass counts](reviews/round2/STATUS.json), [original ledger](paper_ledger.csv), [original dossier](reviews/PAPER_BY_PAPER.md), [core findings](reviews/CORE_FINDINGS.md), [previous detailed readings](reviews/round2/DETAILED_REVIEWS.md) and [protocol](RESEARCH_PROTOCOL.md) preserve the history. The original [BibTeX](references.bib) and [103 new references](reviews/round3/references.bib) are separate.

Versions [3](ARCHITECTURE_V3.md), [2](ARCHITECTURE_V2.md) and the [initial proposal](TRACK2_ARCHITECTURE.md) are historical. V4 supersedes their current recommendations and allocation. The identity prior, local adapters, optional specialists and calibration policies are experiments with stop gates, not proven improvements.

## Access and source boundaries

Research access works after the user's environment publication. This pass did not reapply onboarding changes or publish environment configuration. Raw PDFs/extracted passages are local ignored caches under `papers/`; source/label provenance and critical notes are tracked. Public metadata and a paper's claims do not establish released weights, native-language support or license eligibility.

The previously inspected Indic Parler card reports Hindi/Tamil, about 938M parameters, Apache-2.0 and automatic gated access; authenticated checkpoint retrieval/execution remains a future feasibility gate. No credential values were requested or saved by the research work.

The PS is the uploaded **Rime (1).pdf**, `sediment://file_00000000589c82088b96fab02ca758a0`. Its rules are reference constraints, not authorization to contact people, record speakers, spend paid GPU compute or publish a cloud environment. The proposed final inference uses open models and no human output selection. All ten final generations are retained under the PS's final-window rule.
