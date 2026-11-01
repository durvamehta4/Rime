# Experimental plan and compute budget

Status: planned, not executed. Hardware supplied by the user: 4×NVIDIA L4, 256 GB RAM, approximately 1,000 GPU-hours. Confirm actual VRAM and interconnect before execution. Each L4 has 24 GB VRAM; four cards do not form one transparent 96 GB memory pool. Earlier drafts incorrectly assumed T4 hardware; this plan uses the corrected L4 allocation.

Literature update: [architecture v4](ARCHITECTURE_V4.md) is current after [103 new scoped full-text critical reviews](reviews/round3/README.md). V4 supersedes earlier choices and the allocation below is synchronized with it. Compare native description-conditioned Indic Parler releases first, then the IndicF5 alternative if needed. Start with shared frozen-encoder readouts and add a specialist only for a measured native gap. Compute ceilings are allocations, not measured usage. No training or L4 benchmark was run during the literature review.

## Hardware strategy

- Prefer BF16 mixed precision on L4 where the model and installed stack support it; use FP16 with gradient scaling as a compatibility fallback. Check numerical stability of flow matching separately.
- Use tested Ada-compatible attention. L4 hardware supports FlashAttention-2, but model/library compatibility must be verified; keep a compatible fallback. Pin a PyTorch/CUDA/quantization combination supported by the installed driver and L4 compute capability.
- For a 7B captioner, start with 4-bit frozen LLM weights, BF16 audio encoder/projector where supported, and LoRA rank 8 or 16. Compare BF16 frozen-LM loading if it fits; test rank 32 and larger microbatches only after the memory pilot. Profile the actual implementation: not every audio-language-model loader supports quantization plus adapter training correctly.
- Freeze the audio encoder initially; cache audio features for training if augmentation does not invalidate them. Keep global context for 30-second clips. Do not split away the very changes and interactions being tested.
- Start caption training at microbatch 1, short clips, activation checkpointing, and gradient accumulation. Measure 5-, 15-, and 30-second peaks before selecting batches. Target measured peak below approximately 20 GiB/card for a single-card job, allowing runtime overhead; this is a target, not a proven fit.
- Use independent GPU jobs for annotation/evaluation where possible. Use DDP only when each replicated model fits. Investigate sharding or offload when it does not; neither DDP nor four visible GPUs automatically shards weights.
- Run generator adapter training separately from captioner training. A sub-billion-scale speech model may be more tractable, but verify the selected IndicF5 checkpoint's actual configuration and training memory rather than quoting a guessed size.
- A 30B MoE model's active parameter count is not its weight footprint. Qwen3-Omni can be an optional quantized/sharded teacher if supported, not a mandatory replicated L4 model. Skip it if teacher gains do not justify overhead.
- Use RAM to cache manifests/features and stage shards; inspect disk capacity before selecting the pool. Do not store every Vaani waveform and every synthetic derivative by default.

## Proposed budget

GPU-hours sum use across cards, including failed runs. Four fully occupied GPUs for 250 wall-clock hours consume 1,000 GPU-hours. Annotation throughput, training steps, and wall-clock completion dates cannot be promised without a pilot.

| Work | GPU-hour ceiling | Output |
|---|---:|---|
| Compatibility/memory/throughput pilot and C0/G0 measurements | 50 | Working baselines and measured cost/sample |
| Cached evidence and labels | 80 | Versioned training manifests and native claim audit |
| Caption grounding/adaptation development | 120 | Evidence-fusion and claim-selection choice |
| G1 description/delivery adaptation | 200 | Generator and equal-compute caption-quality control |
| Identity conditioning interface and small prior | 80 | Bank/seeds/prior test or documented failure |
| Targeted synthesis, verification, C1 training | 140 | One complete reciprocal improvement round |
| Matched-budget controlled comparisons | 150 | Causal evidence for targeting and verification |
| Final real evaluation, all ten generations, profiling | 80 | Round tables, intervals, Pareto plots |
| Failure reserve and focused reruns | 100 | Recover from measured implementation failures |
| **Total** | **1,000** | |

These are ceilings to rebalance after the pilot. Do not spend the reserve on an optional second round before completing required ablations. Human transcription, native listening, and literature review time are separate resources.

For a candidate pool of `H` hours, audio contains `3600H` seconds. At real-time factor `r`, one annotation pass costs approximately `H*r` accelerator-hours for one device, before batching, load time, and retries. Estimate `r` on representative data. For generation, budget `10*N*mean_duration_s*r_gen/3600` device-hours for `N` prompts, with additional verifier cost. A model sharded across four GPUs consumes four GPU-hours per wall-clock hour.

## Data scale after the pilot

Begin with a small balanced pilot (for example 5 hours/language), then expand by measured error and cost. A working target range is 50–150 unique real hours/language, not a requirement. Do not promise annotation/training on thousands of hours within this budget.

Allocate separately audited real clips across plain reading, spontaneous conversation, pauses/disfluencies, code mixing, phonation/register changes, vocal events, channel/room conditions, background sounds, and coupled changes. Initial planning can use about 100–200 clips/language for development, with enough extra real audit data to avoid repeatedly tuning to the same speakers; final counts depend on annotation capacity and diversity. Every aggregate needs its actual item count. A tiny rare-event subset does not support a precise subgroup claim.

For Tamil/Hindi balance use language-balanced sampling, speaker caps, and stratification by channel/style. Report both per-language results and macro averages; do not hide a Tamil regression inside the much larger Hindi pool.

## Required experiment matrix

Use the same starting checkpoints, real examples, data order where applicable, total optimizer updates, decoding seeds, and compute budget for causal comparisons. Report extra compute for data synthesis and verification as well as training. A separate zero-synthetic baseline may be useful, but the matched-budget real-replay control is more informative than simply allowing the proposed system more updates.

| ID | Comparison | Question answered |
|---|---|---|
| B0 | Frozen C0/G0 | Does a reproducible starting system work at all? |
| C1 | No readouts vs shared-encoder readouts vs one frozen specialist | Does grounding improve real native facts/timing enough to justify its extra compute? |
| C2 | Empirical selection vs nested CRC proxy vs optional LTT over fixed policies | Which useful risk/coverage frontier is supported, and can the stated loss be certified with available independent units? |
| G1 | G0 vs same backbone with global description adapters | Does learned conditioning improve instruction following? |
| G2 | Global-only vs supported aligned local controls | Do requested local changes occur while identity and native phonetic distinctions survive? |
| G3 | Rich C0 captions vs simpler measured/global captions, same real audio and compute | Does C→G teaching improve instruction following beyond extra adaptation? |
| L1 | Extra real replay vs random verified synthesis vs targeted verified synthesis | Is improvement due to targeting rather than training longer or seeing more samples? |
| L2 | Targeted synthesis with/without independent verification | Does verification prevent wrong synthetic labels? |
| L3 | Fixed pre-loop generator vs trained G1 for the same target requests | Is the captioner benefit actually due to an improved generator? |
| D1 | Named/bank/decoder seeds vs conditional identity prior | Do distinct passing identities increase without within-clip drift or native CER loss? |
| R1 | Ordinary held-out real clips and transformation-family holdouts | Is improvement real rather than artefact recognition? |
| R2 | Learned-only vs explicit vs hybrid recording ecology | Are effects audible with correct source/room ownership and no double processing? |
| C3 | Negation, actor, order/overlap, text-delivery and channel-source minimal pairs | Does the system verify the specific claim rather than a correlated caption or teacher cue? |

This matrix is larger than the budget permits at full scale. Use a shared small-scale screening stage and predeclare three headline controlled comparisons: evidence grounding, targeted vs random vs real-replay, and verification on/off. Run generator temporal and identity diagnostics on the same frozen generator if full retraining is unaffordable. Label screened, full-budget, and diagnostic comparisons separately. Do not present an uncontrolled diagnostic as a causal training ablation.

## Measurements

### Captioner

Use native-listener-checked real clips with local development rubrics covering Appendix F3. The team's rubrics are **local proxies**, not the organizers' private rubrics. Measure:

- Weighted supported coverage, false-claim weight, and final clipped rubric-style score.
- Claim precision/recall and omission count, to prevent an empty caption from appearing good because it hallucinates nothing.
- Event onset/offset diagnostic errors plus the PS placement rule: a timed item must be placed inside its rubric span widened by 250 ms per side. Retain raw intervals and do not replace this with an MAE threshold. Local rubrics are still proxies for hidden official items.
- Pitch/rate/pause error where human/tool reference measurements are reliable.
- Word count, fraction truncated, axis/type coverage, and confidence reliability curves.
- Performance on audio/text contradictions: same transcript with different delivery; altered transcript context with unchanged acoustics; audio-only, transcript-only, and shuffled-audio controls.

Intent judgments need bilingual/native review and uncertainty labels. Blindly inferred biography, accent geography, microphone hardware, emotion, or social relationship must not become gold labels. Native listeners should annotate audible support rather than invent a narrative.

### Generator

- Human instruction satisfaction by global and local requirements, broken down by axis/type and language.
- Blinded pairwise naturalness listening with identical text/description across systems; report listener count and items, not just a mean.
- Official-model native-script CER once the specified IndicConformer checkpoint and preprocessing are confirmed. Alternative ASR is a diagnostic and must be labeled as such. CER may exceed 1 before score flooring.
- Speaker diversity among passing samples using the specified verification protocol once available. Until then use a separately labeled local verifier and show threshold sensitivity.
- Within-clip speaker drift, alignment failures, missing/repeated text, clipping, event realism, and output sample rate.
- All ten predetermined final outputs per description. The PS final window forbids choosing between generations: no best-of-N, rejection-resampling or replacing weak outputs. Training-data filtering is separate. A failed or empty output remains in the applicable denominator.

CLAP can be an auxiliary retrieval/similarity diagnostic. It cannot establish exact transcript correctness, event timing, intent, or speaker identity and must not replace them. Likewise, agreement with the training captioner is not an independent quality measurement.

### Confidence intervals and cost

Use paired resampling of the same items for baseline/system comparisons and stratify by language. Ten generations of one prompt are clustered observations, not ten independent prompts. For multi-clip speakers, include a speaker-cluster sensitivity analysis. Use the organizers' prescribed Track 2 bootstrap procedure if supplied; do not assume Track 1-specific keys automatically apply.

Appendix A specifies 1,000 SHA-256-based replicates: sort item IDs in ascending UTF-8 byte order, draw index `int(sha256(seed|bootstrap|measure|r|j),16) mod n`, and use sorted replicate values at zero-based positions 24 and 974, without interpolation. Paired comparisons share draws. Its table does not specify Track 2 measure keys or all Track 2 aggregation details. Declare local development keys, keep every per-item result, and use organizer-supplied Track 2 details when available. Do not label local choices exact official scoring. Keep all ten generations clustered within their request, and add speaker-cluster sensitivity analyses for repeated speakers. Team development listening does not replace organizer-run scored listening.

For each checkpoint report total parameters, trainable parameters, weight precision, peak memory, model size on disk, inference GPU-hours/clip, training GPU-hours, annotation/synthesis/verifier GPU-hours, and all failed-run costs. Plot measured quality against both size and cumulative compute; keep non-dominated candidates instead of assuming largest is best.

## New failure checks from the 103-paper review

- Unknown, absent, normal, requested-only and realized labels remain distinct. Caption omission never supplies a negative label, and rendered assertions retain source, polarity and interval scope.
- A frozen/EMA second model is not independent evidence by definition. Audit shared teacher errors and compare verification policies at matched accepted coverage, including omitted difficult groups.
- Original/restored/transformed audio siblings share a split. Restored speech can support clean generator training but cannot retain ecology labels about noise removed from the original.
- Native CER and identity/delivery metrics remain separate. Score text/style conflicts, whispers, same-speaker laughter, code-switch regions and native short-duration phonetic distinctions. Keep the official verifier threshold; supplementary invariant embeddings are diagnostics.
- One layer of 1,500×1,280 FP16 frames is 3.84 MB per clip. Four such layers across 100,000 clips use ~1.54 TB before metadata. Check disk and cache invalidation, not just available RAM.
- CRC false-count/fixed-M loss and LTT retained-claim FDP are different experiments. Do not apply monotonic CRC to the variable-denominator FDP. Freeze policy families/order before calibration; report insufficient data or no certified policy rather than a guarantee unsupported by the sample.

## Acceptance gates

1. **Compatibility:** full 30-second caption inference and native Hindi/Tamil generation succeed without OOM; audio paths retain timing and sample-rate correctness.
2. **Baseline:** bilingual listeners confirm intelligible text and descriptions tied to actual audio; record failures before adaptation.
3. **Interventions:** controlled changes are measurable and their invalid secondary labels are masked.
4. **Generator:** targeted requested controls are realized often enough to make synthesis economical; compare real vs synthetic artefacts.
5. **Loop:** C1 improves useful grounded description quality on real development clips over matched controls, without unexplained language regressions. Predeclare promotion thresholds after measuring baseline variance, before running comparisons.
6. **Audit:** selected C1/G1 are assessed once on the final real audit set and all ten outputs are retained. Report negative results if the loop fails to improve.
7. **Freeze:** code/checkpoint hashes, dependencies, prompts, seeds, data provenance, and exact commands reproduce outputs. No manual editing or final generator candidate selection; retain all ten seeded outputs.

## Milestones, without inventing a deadline

1. Literature access and core review; compatibility pilot; obtain consented native-language evaluation help.
2. C0/G0 and local held-out evaluation; design contributed test sets.
3. Grounded training labels, simple verified interventions, initial conditioning adapters.
4. G1, targeted synthesis, C1, matched comparisons.
5. Independent real audit, Pareto/cost analysis, reproducible packaging, report/demo.

At mid-term, contribute **30 recorded caption clips and 30 generation descriptions with text per language**, at most 30 seconds/clip, and no speaker in more than five recorded clips. This requires at least six speakers/language if every speaker contributes the maximum. Recruit more for diversity where practical. Speakers sign the PS consent before recording; contributed items never enter training/tuning. Actual competition dates must come from the organizers.

Mid-term also needs the ≤6-page report plus references, results.csv and round0.zip. Freeze captures all round/checkpoint hashes, code, settings, seeds. End-term includes the ≤8-page double-column report plus references and ≤4-page appendix, code, outputs containing caption text and ten generations per description, measurements, data manifest, ≤4-minute demo, and ≤1-page summary. Follow the PS's exact accepted-file list when packaging; research working files are not automatically submission deliverables.
