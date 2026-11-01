# Experimental plan and compute budget

Status: planned, not executed. Hardware supplied by the user: 4×NVIDIA T4, 256 GB RAM, approximately 1,000 GPU-hours. Confirm actual VRAM and interconnect before execution. A standard T4 has 16 GB; four cards do not form one transparent 64 GB memory pool.

Literature update: compare Indic Parler-TTS's description-native pretrained/fine-tuned releases first, with IndicF5 adapters as the alternative. Prioritize access, native pronunciation, relevant diversity and control tests before selecting the training branch. [Architecture version 2](ARCHITECTURE_V2.md) supersedes the initial ordering. Compute ceilings below are allocations, not measured usage.

## Hardware strategy

- Use FP16 mixed precision with gradient scaling for trainable modules; do not assume native BF16 support. Check numerical stability of flow matching separately.
- Use tested Turing-compatible attention. Do not make FlashAttention-2 a prerequisite. Pin a PyTorch/CUDA/quantization combination supported by the installed driver and T4 compute capability.
- For a 7B captioner, start with 4-bit frozen LLM weights, FP16 audio encoder/projector, and LoRA rank 8 or 16. Profile the actual implementation: not every audio-language-model loader supports quantization plus adapter training correctly.
- Freeze the audio encoder initially; cache audio features for training if augmentation does not invalidate them. Keep global context for 30-second clips. Do not split away the very changes and interactions being tested.
- Start caption training at microbatch 1, short clips, activation checkpointing, and gradient accumulation. Measure 5-, 15-, and 30-second peaks before selecting batches. Target measured peak below approximately 14 GiB/card for a single-card job, allowing runtime overhead; this is a target, not a proven fit.
- Use independent GPU jobs for annotation/evaluation where possible. Use DDP only when each replicated model fits. Investigate sharding or offload when it does not; neither DDP nor four visible GPUs automatically shards weights.
- Run generator adapter training separately from captioner training. A sub-billion-scale speech model may be more tractable, but verify the selected IndicF5 checkpoint's actual configuration and training memory rather than quoting a guessed size.
- A 30B MoE model's active parameter count is not its weight footprint. Qwen3-Omni can be an optional quantized/sharded teacher if supported, not a mandatory replicated T4 model. Skip it if teacher gains do not justify overhead.
- Use RAM to cache manifests/features and stage shards; inspect disk capacity before selecting the pool. Do not store every Vaani waveform and every synthetic derivative by default.

## Proposed budget

GPU-hours sum use across cards, including failed runs. Four fully occupied GPUs for 250 wall-clock hours consume 1,000 GPU-hours. Annotation throughput, training steps, and wall-clock completion dates cannot be promised without a pilot.

| Work | GPU-hour ceiling | Output |
|---|---:|---|
| Compatibility/memory/throughput pilot and C0/G0 measurements | 50 | Working baselines and measured cost/sample |
| Cached evidence, labels, optional open teacher | 100 | Versioned training manifests and claim audit |
| Caption grounding/adaptation development | 130 | Evidence-fusion and calibration choice |
| G1 description/temporal-control training | 220 | Generator capable of useful targeted examples |
| Targeted synthesis, verification, C1 training | 140 | One complete recursive improvement round |
| Matched-budget controlled comparisons | 160 | Causal evidence for targeting and verification |
| Final real evaluation, all ten generations, profiling | 100 | Round tables, intervals, Pareto plots |
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
| C1 | Captioner with/without measured evidence | Does grounding improve real claim accuracy and timing? |
| C2 | Calibrated claim selection vs same writer without it | Does it reduce unsupported claims at comparable useful coverage? |
| G1 | G0 vs same backbone with global description adapters | Does learned conditioning improve instruction following? |
| G2 | Global-only vs global+temporal controls | Do local timed controls help beyond a longer prompt? |
| L1 | Extra real replay vs random verified synthesis vs targeted verified synthesis | Is improvement due to targeting rather than training longer or seeing more samples? |
| L2 | Targeted synthesis with/without independent verification | Does verification prevent wrong synthetic labels? |
| L3 | Fixed pre-loop generator vs trained G1 for the same target requests | Is the captioner benefit actually due to an improved generator? |
| D1 | Fixed identity vs compatible per-sample identity sampling | Does relevant diversity increase without within-clip drift? |
| R1 | Ordinary held-out real clips and transformation-family holdouts | Is improvement real rather than artefact recognition? |

This matrix is larger than the budget permits at full scale. Use a shared small-scale screening stage and predeclare three headline controlled comparisons: evidence grounding, targeted vs random vs real-replay, and verification on/off. Run generator temporal and identity diagnostics on the same frozen generator if full retraining is unaffordable. Label screened, full-budget, and diagnostic comparisons separately. Do not present an uncontrolled diagnostic as a causal training ablation.

## Measurements

### Captioner

Use native-listener-checked real clips with local development rubrics covering Appendix F3. The team's rubrics are **local proxies**, not the organizers' private rubrics. Measure:

- Weighted supported coverage, false-claim weight, and final clipped rubric-style score.
- Claim precision/recall and omission count, to prevent an empty caption from appearing good because it hallucinates nothing.
- Event onset/offset errors and proportion within a PS-inspired tolerance; retain raw intervals. A local temporal matching rule is a proxy until organizers confirm their exact rule.
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
- All ten generated outputs per description, not only best-of-ten. A failed or empty output remains in the denominator under the applicable rules.

CLAP can be an auxiliary retrieval/similarity diagnostic. It cannot establish exact transcript correctness, event timing, intent, or speaker identity and must not replace them. Likewise, agreement with the training captioner is not an independent quality measurement.

### Confidence intervals and cost

Use paired resampling of the same items for baseline/system comparisons and stratify by language. Ten generations of one prompt are clustered observations, not ten independent prompts. For multi-clip speakers, include a speaker-cluster sensitivity analysis. Use the organizers' prescribed Track 2 bootstrap procedure if supplied; do not assume Track 1-specific keys automatically apply.

Until clarified, predeclare a local 1,000-replicate item/prompt bootstrap with fixed seed and percentile intervals, label it a local proxy, and retain all per-item measurements. Report effect sizes and uncertainty rather than significance based only on aggregate means.

For each checkpoint report total parameters, trainable parameters, weight precision, peak memory, model size on disk, inference GPU-hours/clip, training GPU-hours, annotation/synthesis/verifier GPU-hours, and all failed-run costs. Plot measured quality against both size and cumulative compute; keep non-dominated candidates instead of assuming largest is best.

## Acceptance gates

1. **Compatibility:** full 30-second caption inference and native Hindi/Tamil generation succeed without OOM; audio paths retain timing and sample-rate correctness.
2. **Baseline:** bilingual listeners confirm intelligible text and descriptions tied to actual audio; record failures before adaptation.
3. **Interventions:** controlled changes are measurable and their invalid secondary labels are masked.
4. **Generator:** targeted requested controls are realized often enough to make synthesis economical; compare real vs synthetic artefacts.
5. **Loop:** C1 improves useful grounded description quality on real development clips over matched controls, without unexplained language regressions. Predeclare promotion thresholds after measuring baseline variance, before running comparisons.
6. **Audit:** selected C1/G1 are assessed once on the final real audit set and all ten outputs are retained. Report negative results if the loop fails to improve.
7. **Freeze:** code/checkpoint hashes, dependencies, prompts, seeds, data provenance, and exact commands reproduce outputs. No manual post-selection.

## Milestones, without inventing a deadline

1. Literature access and core review; compatibility pilot; obtain consented native-language evaluation help.
2. C0/G0 and local held-out evaluation; design contributed test sets.
3. Grounded training labels, simple verified interventions, initial conditioning adapters.
4. G1, targeted synthesis, C1, matched comparisons.
5. Independent real audit, Pareto/cost analysis, reproducible packaging, report/demo.

At mid-term, contribute **30 recorded caption clips and 30 generation descriptions with text per language**, at most 30 seconds/clip, and no speaker in more than five recorded clips. This requires at least six speakers/language if every speaker contributes the maximum. Recruit more for diversity where practical. Speakers sign the PS consent before recording; contributed items never enter training/tuning. Actual competition dates must come from the organizers.

Mid-term also needs the ≤6-page report plus references, results.csv and round0.zip. Freeze captures all round/checkpoint hashes, code, settings, seeds. End-term includes the ≤8-page double-column report plus references and ≤4-page appendix, code, outputs containing caption text and ten generations per description, measurements, data manifest, ≤4-minute demo, and ≤1-page summary. Follow the PS's exact accepted-file list when packaging; research working files are not automatically submission deliverables.
