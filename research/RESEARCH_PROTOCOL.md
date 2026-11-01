# Protocol for the requested 200+ paper review

**Current status:** the network blocker below is historical and resolved. The original breadth-first pass inspected 296 records and retained 277, with 28 additional core scoped checks. Round 2 added ten main-text reviews and six acquired-only leads. [Round 3](reviews/round3/README.md) adds 103 distinct scoped full-text critical reviews, giving 415 distinct records across passes and 113 detailed reviews across the two additional passes with separately declared scopes. No pass is represented as exhaustive cover-to-cover/appendix reading. [V4](ARCHITECTURE_V4.md) is current. See the original [counts](REVIEW_STATUS.json), round-2 [status](reviews/round2/STATUS.json), and round-3 [status/locators](reviews/round3/STATUS.json). The original target below is preserved; it is not a claim of 230 exhaustive readings.

## Historical evidence boundary at initial setup

At initial setup, full research papers reviewed: **0**. This paragraph records the initial blocker, not the current review count. The uploaded PS and official repository documentation/selected code were consulted. None of these repository reads is counted as full-paper reading. The architecture is a hypothesis to refine with the requested review and experiments.

The first scholarly-index requests failed with HTTP CONNECT 403. This is a network-policy blocker, not evidence that papers do not exist. Draft additions were saved for arxiv.org, export.arxiv.org, api.openalex.org, api.semanticscholar.org, aclanthology.org, openreview.net, api2.openreview.net, and huggingface.co. Preserve existing presets/custom rules. Review/save and publish through environment settings before treating these as accessible. Some PDFs or publisher redirects may need additional destinations after observing actual failures.

Do not route blocked research sites through an unrelated allowed host or disable TLS verification. Do not claim a draft save applied runtime access. GitHub documentation remains useful primary implementation evidence, but is not a substitute for the paper corpus.

## Review target

Target **230 distinct full papers** to allow exclusion of duplicates or weakly relevant work while retaining at least 201 relevant full-text reviews. This is a target allocation, not a list of papers already located/read:

| Theme | Target | Main design question |
|---|---:|---|
| Speech/audio-language understanding and grounded captioning | 35 | What evidence fusion and training reduce acoustic hallucination? |
| Controllable, expressive, multilingual and Indic TTS | 45 | How to condition language, identity, phonation, timing, and descriptions? |
| Audio codecs, flow/diffusion, representations and vocoders | 20 | Which representation fits fidelity, controls, and T4 memory? |
| Temporal sound/event localization, prosody and phonation | 25 | How to support timed and numerical claims? |
| Self-training, back-translation, mutual/dual learning, active curricula | 30 | How can reciprocal models improve without reinforcing errors? |
| Synthetic data reliability, calibration and distribution collapse | 20 | How to select valid labels and retain real-data grounding? |
| Evaluation, speech quality, speaker verification and human judgments | 20 | Which tests demonstrate useful improvement and avoid reward gaming? |
| Indian speech datasets, ASR, code switching and sociophonetics | 25 | What is specifically required for Hindi and Tamil? |
| Efficient adaptation, quantization and training | 10 | What can actually be trained on four T4s? |
| **Total** | **230** | |

Cross-topic papers count once toward the total. Do not pad with unrelated music/image papers or duplicate arXiv/conference versions. Include foundational older work when it materially explains dual learning, uncertainty, or prosody. Search through the client date and record the search date; verify purported 2026 papers and venue claims rather than trusting the PS or a collection README as bibliographic authority.

## Discovery and screening

1. Begin with PS-named Fugatto, UALM, Audio Flamingo 3, MMAU, MMAU-Pro. Resolve exact titles, IDs, public full text, release dates, licenses, and implementations. Those names in the PS are leads, not proof of their claims.
2. Add F5-TTS/IndicF5, Parler-TTS's underlying synthetic-annotation work, Qwen3-Omni/Qwen3-TTS, CLAP, audio codecs, and Indian speech datasets.
3. Search thematic queries in OpenAlex, Semantic Scholar, arXiv, ACL Anthology and OpenReview; record query, date, endpoint, and returned identifiers. Respect service rate limits; cache results and handle 429 without aggressive retries.
4. Follow references and forward citations from the core set. Screen title/abstract for relevance before acquiring full text.
5. Deduplicate using DOI, arXiv base identifier, exact/normalized title, author overlap and version lineage. Distinguish a substantively separate follow-up from a venue version of the same paper.
6. Acquire lawful open full text, preserve URL and hash, extract text, and inspect extraction quality. Scanned or failed extraction is not a completed read. Request permission/access only for content still unavailable; do not bypass paywalls.

## Evidence levels and review record

Use statuses `discovered`, `abstract_reviewed`, `full_text_acquired`, `full_text_reviewed`, `deep_reviewed`, `excluded`, `unavailable`. Only the last two reviewed statuses count toward the user's 200+ full-paper request. The distinction between full-text and deep review records depth; it does not excuse treating a skim as a full read.

Every completed review must record:

```text
paper_id, canonical_title, authors, year, venue, doi, arxiv_id,
source_url, full_text_url, sha256, retrieval_date, evidence_level,
topic, task, languages, training_data, model_size, compute,
method_summary, exact_evidence_location, reported_results,
baseline_and_controls, limitations, replication_status,
track2_relevance, adopted_or_rejected_idea, architecture_section,
conflicting_evidence, reviewer_notes
```

Summaries distinguish author-reported results from reproduced results. Include section/table/page evidence for the particular claim, not just a generic link. State when compute, languages, or dataset contamination controls are unreported. For critical backbone papers, read architecture, training, experiments, limitations, and appendix. Preserve negative results and rejected ideas.

## Required synthesis

The final review should produce:

- A deduplicated 201+ paper ledger with explicit evidence levels and per-paper review notes.
- A compact evidence matrix connecting architecture decisions to supporting and conflicting papers.
- A backbone comparison on Hindi/Tamil support, description conditioning, timed control, speaker diversity, openness/license, trainability and T4 cost.
- A loop comparison covering dual learning, pseudo-labeling, curriculum selection, real replay, calibration, and independent verification.
- A novelty audit separating prior methods, PS suggestions, and the proposed contribution.
- Revisions to the provisional architecture when papers contradict current assumptions.

The architecture cannot honestly be called literature-complete until this evidence exists. Even a completed review cannot establish “best possible” without task-specific controlled tests.

## Historical core-source leads at initial setup

These were bibliographic leads at setup, before the review passes. Current reading scope is given by each pass's ledger; this historical list does not override it:

- Qwen3-Omni Technical Report — arXiv:2509.17765.
- Qwen3-TTS report — arXiv:2601.15621; verify canonical title from the paper.
- Audio Flamingo — arXiv:2402.01831.
- Audio Flamingo 2 — arXiv:2503.03983.
- Audio Flamingo 3 — arXiv:2507.08128.
- MMAU — arXiv:2410.19168.
- F5-TTS — arXiv:2410.06885.
- E2 TTS — arXiv:2406.18009.
- Natural language guidance of high-fidelity text-to-speech with synthetic annotations — arXiv:2402.01912.
- Large-Scale Contrastive Language-Audio Pretraining with Feature Fusion and Keyword-to-Caption Augmentation — arXiv:2211.06687.
- High-Fidelity Audio Compression with Improved RVQGAN — arXiv:2306.06546.
- High Fidelity Neural Audio Compression — arXiv:2210.13438.
- Whisper paper — arXiv:2212.04356; verify canonical title from paper.

IndicF5 is documented as a repository/model release; do not manufacture a standalone peer-reviewed paper for it. Treat source collections as discovery aids, never as the underlying evidence for model performance.
