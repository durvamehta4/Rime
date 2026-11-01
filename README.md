# Rime — Inter IIT Track 2

Research and architecture for a Hindi/Tamil speech captioner and description-conditioned speech generator, developed around the Rime Track 2 problem statement.

The proposed system describes audible voice, recording conditions and intent in English prose, generates speech from text plus a description, and uses verified targeted synthesis to improve captioning through a reciprocal learning round.

## Start here

- [Architecture v4](research/ARCHITECTURE_V4.md): the current system design, component choices and implementation gates.
- [Research overview](research/README.md): navigation and review scope across all literature passes.
- [103 additional paper reviews](research/reviews/round3/README.md): critical methods, results, limitations and design implications.
- [Evidence-to-design decisions](research/reviews/round3/DECISIONS.md): why the architecture changed and what needs testing.
- [Experiments and compute budget](research/EXPERIMENTS.md): validation plan for **4×L4 GPUs, 256 GB RAM and approximately 1,000 GPU-hours**.

## Current status

This repository currently contains research documentation and literature-review tooling. Architecture v4 is a proposal awaiting implementation and native-language validation; no model training or L4 benchmarking has been performed as part of these research passes.

The literature collection contains **415 distinct records across passes with different review depths**. The latest pass adds **103 scoped full-text critical reviews** without repeating prior IDs. These cover selected methods, results and limitations rather than exhaustive readings of every appendix. Counts, source hashes and reading locators are available in the [latest review ledger](research/reviews/round3/ledger.csv) and [status](research/reviews/round3/STATUS.json).

## Repository layout

```text
research/
├── ARCHITECTURE_V4.md       Current architecture
├── EXPERIMENTS.md           Evaluation and compute plan
├── LITERATURE_REVIEW.md     Cross-paper synthesis
├── reviews/                Paper reviews, ledgers and provenance
└── tools/                  Literature acquisition and validation scripts
```

Earlier architecture versions remain available for context. Raw third-party PDFs and extracted-text caches are excluded from Git. See the [research reproduction instructions](research/reviews/round3/REPRODUCIBILITY.md) for dependencies, acquisition commands and evidence limitations.
