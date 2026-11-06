# Mid-term runbook (≈ 2–3 weeks, 4 × L4)

Sub-teams: **A** data & test set · **B** captioner · **C** generator · **D** eval & infra.
Every GPU job goes through `rimet2.common.ledger.gpu_job` → `runs/compute_ledger.csv` (GPU-hours per round).

## Mid-term points and how this plan earns them
| Criterion (pts) | Evidence we produce |
|---|---|
| Problem framing & prior work (10) | Precise gap (unverified pseudo-labels compound under a precision-penalised rubric; tag-vocabulary vs. timed numeric claims; no Hindi/Tamil ecology), hypotheses H1–H3, literature map (248 entries) |
| Baselines & eval setup (5) | Round 0 (suggested pair) + reference rows; internal rubric with grader κ vs humans; exact CER/diversity metrics; bootstrap CIs; errors by axis/item type |
| Contributed test sets (5) | 30 clips + 30 descriptions per language, validated by `rimet2.testset.package`, coverage matrix, hard cases |
| Early results & revised plan (10) | E1–E6 with CIs and failure analysis → decision gates below |

## Week 1
| Day | Owner | Task | Command / output |
|---|---|---|---|
| 1 | D | Setup, extra models, CPU tests green | `bash scripts/00_setup_server.sh` |
| 1 | A | Consent forms out (docs/CONSENT_TEMPLATE.md); book ≥ 10 speakers per language | signed forms kept offline |
| 1–2 | D | **E0** Vaani index + speaker-disjoint splits + 300 dev clips/lang | `bash scripts/01_index_and_dev.sh` |
| 2 | C | Write 40 dev generation items/lang (our own, NOT the test set) | `data/gen_items_{hi,ta}.csv` |
| 2–3 | B,C | **E1** round 0 (captioner raw; generator CustomVoice) + reference rows | `bash scripts/02_round0.sh hi` (then `ta`) |
| 2–3 | C | **E2** codec ceiling on 200 clean clips/lang | `python scripts/codec_ceiling.py --list data/hi_dev.list` |
| 3–5 | A,B | Annotate **DevReal** rubric: 60 clips/lang, 2 annotators on 20 of them | docs/ANNOTATION_GUIDE.md → `data/rubric_{hi,ta}.csv` |
| 3–7 | A | Record test-set clips (≤ 5 per speaker), write 30 descriptions/lang | `testset_src/<lang>/...` |
| 4–5 | D | Foley/bed/RIR libraries (CC0/CC-BY only; licences in CSV) | `data/foley.csv`, `data/beds.csv`, `data/rirs/` |

## Week 2
| Day | Owner | Task | Command / output |
|---|---|---|---|
| 6 | D | **E3** grader validation: grader verdicts vs annotator verdicts on the double-annotated clips → Cohen's κ | `rimet2.eval.grader.cohen_kappa` |
| 6–7 | B | **E4** captioner comparison raw vs evidence vs fused (same clips) | `scripts/eval_captions.py` → per-type table, paired Δ |
| 7–8 | B | Fit calibrator on DevReal half A, tune τ, evaluate on half B | `rimet2.captioner.calibrate` |
| 6–9 | C | Speaker bank (IndicVoices-R + clean Vaani) | `scripts/build_speaker_bank.py` |
| 6–10 | C | Start Qwen3-TTS language adaptation (Base) on IV-R + Rasa + clean Vaani | `train/build_tts_sft.py`, `scripts/qwen3tts_language_adapt.sh` |
| 8–10 | C,D | **E5** generator comparison: round0 vs parler vs design vs factored | `scripts/eval_generation.py` |
| 8–10 | D | **E6** renderer exactness: re-detect constructed events ±250 ms after channel | evidence toolkit on renderer outputs |

## Week 3
| Task | Owner |
|---|---|
| Round-1 slice: weak-area transform data → editor/fuser LoRA (Qwen3-8B) → re-run E4 | B (`scripts/make_transform_data.py`, `train/lora_llm.py`) |
| Adapted generator checkpoint → re-run E5 (CER, diversity, relevance proxy) | C |
| Package test set | A: `python -m rimet2.testset.package --src testset_src --out test_set.zip` |
| round0.zip: code at commit, configs, SHA-256 of every checkpoint, exact commands + seeds | D: `sha256sum models/*/*.safetensors` |
| results.csv (all rows from eval scripts), Pareto plots, report (docs/report_skeleton.md) | all |

## Decision gates (the "revised plan" must follow from these)
1. **Backbone gate (E2 + E5):** if Qwen3-TTS tokenizer round-trip CER disagreement > 5 points on clean clips, or the
   adapted Base CER is > 15 % on Tamil after the first epoch → Indic-Parler-TTS becomes the voice backend
   (planner, prior, renderer unchanged).
2. **Captioner gate (E4):** if fused ≤ raw + CI on DevReal, inspect per-type table: drop item types where
   evidence hurts, and raise τ for intent types.
3. **Grader gate (E3):** κ < 0.6 → rewrite rubric items to be more explicit before trusting any automatic numbers.
4. **Renderer gate (E6):** events re-detected < 80 % → raise min event level / salience thresholds.

## Rules hygiene
- Never train or tune on our own contributed test set, and never on DevReal *test half*.
- Every training example → `ManifestRow` (source + labeler). Non-commercial assets (ESC-50, audEERING) =
  research only; record them in `data_manifest.csv`.
- Anonymity: no institute names in any submitted file. Team ID only.
