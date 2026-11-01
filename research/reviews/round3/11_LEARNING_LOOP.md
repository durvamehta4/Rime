# Pseudo-labeling, synthetic replay and recursive learning

These ASR/general-learning results motivate controls; they do not establish reciprocal caption/TTS gains on the PS.

## 2005.09629 — Improved Noisy Student Training for ASR

[Source](https://arxiv.org/abs/2005.09629). Read: teacher/LM/filter/balance pipeline and normalized score in an extra range, training scale, filtering/augmentation discussion.

**Method and evidence.** Generate LM-fused pseudo-transcripts, normalize decoding scores by fitted length-dependent mean/variance, filter and balance them, then train an augmented student alongside real labels. Gradually relax filters in the low-supervision setting. The reported 100-hour setup improves test clean/other WER to 4.2/8.6. Gradational changes help that setting but bring little benefit in the high-supervision LibriLight condition. A high-score blank transcript is an explicit filtering failure.

**Limits and decision.** Fusion scores are not probabilities, repeated rounds are costly, and six generations with 32 TPUs for ten days each are outside this budget. Use one required reciprocal round with fixed real replay and label-quality checks. Calibrate length effects and reject empty/incomplete pseudo-records explicitly. Do not assume gradual filter relaxation always helps or add rounds because synthetic agreement rises; compare against matched-compute real-only training.

## 2005.09267 — Iterative Pseudo-Labeling

[Source](https://arxiv.org/abs/2005.09267). Read: subset-refresh algorithm, supervised/pseudo losses, LM role, text-overlap exclusion and result tables.

**Method and evidence.** Repeatedly refresh labels for subsets of unlabeled audio and continue training the current acoustic model on real plus pseudo-labeled data, rather than restarting every round. External LM decoding and augmentation break self-confirming local solutions. The paper excludes audiobook-overlapping books from its text LM corpus. With 100 labeled hours and 54k unlabeled hours, final LM-rescored test-other WER is 7.11; greedy/no-LM numbers are different and higher.

**Limits and decision.** Final rescoring gains and pseudo-label-generation gains must be separated, and the method's no-filter setting is not evidence that arbitrary acoustic descriptions are trustworthy. Refresh only targeted weak claim groups, keep teacher and lineage versions, and include a stale-label control. Exclude test-transcript and source-family leakage as well as exact audio duplicates. For the PS, synthetic-request labels require realized-claim verification, not automatic inheritance of every text request.

## 2111.00161 — Pseudo-Labeling for Massively Multilingual ASR

[Source](https://arxiv.org/abs/2111.00161). Read: shared CTC/LID architecture, language-specific teacher/distillation procedure, domain and duration analyses.

**Method and evidence.** Start with a 60-language model, adapt teachers to individual languages with unlabeled data, then combine their labels into a multilingual student. Pseudo-labeled VoxPopuli improves coverage and out-of-domain LibriSpeech recognition, but can worsen Common Voice performance even for English. Languages without new unlabeled data are especially diluted; subsequent clean-data fine-tuning helps. Longer-utterance generalization also changes substantially.

**Limits and decision.** More pseudo-data can improve a new domain while harming the original one, so a single overall result is insufficient. Native labels are not interchangeable across languages, nor is full per-language teacher training affordable here. Use per-language sampling floors, real replay and fixed domain slices. Track short/long duration, channel and delivery coverage as well as aggregate accuracy. Promote C1 only when real held-out Hindi/Tamil precision and coverage gates pass, with rollback to C0 otherwise.

## 2106.08922 — Momentum Pseudo-Labeling

[Source](https://arxiv.org/abs/2106.08922). Read: supervised/unsupervised CTC objectives, EMA update in an extra range, online/offline averaging and augmentation results.

**Method and evidence.** An EMA teacher generates unaugmented greedy pseudo-labels, while a student learns them under augmentation plus available real labels. Momentum smooths updates. In the shown LS-360 setting, the online model without checkpoint averaging trails the offline model, but averaging nearly removes the gap. Removing SpecAugment substantially reduces WER recovery. Performance gains depend on initialization and whether final decoding uses an LM.

**Limits and decision.** EMA stabilizes labels but is not an independent source of truth, and augmentation must preserve the target. Speed/pitch changes can invalidate the very delivery labels this project learns. Keep frozen C0/G0 snapshots for the first causal round and use label-preserving transformations or recompute transformed claims/timestamps. Test EMA only as an optional later training ablation, without treating teacher/student consensus as evidence that unsupported intent or noise labels became correct.

## 2211.07795 — Uncertainty-Driven Pseudo-Label Filtering and Calibration

[Source](https://arxiv.org/abs/2211.07795). Read: DUST disagreement criterion, severe-domain-shift failure, character-level filtering and robustness comparisons.

**Method and evidence.** Compare dropout-sampled transcripts against an unperturbed reference and reject large maximum normalized edit distance. Under severe read-speech→YouTube shift, low disagreement can still select confidently wrong labels. More samples, smaller tokens, robust augmentation and diverse source data improve selection. Word- versus character-based criteria must be compared at equal acceptance fractions, since their threshold scales differ; CER improves more consistently than WER.

**Limits and decision.** Stable predictions can share the same error, directly challenging self-consistency as the PS's verifier. Require real labeled calibration and acoustic contradiction tests, especially on shifted channels/whispers. Compare filtering policies at matched coverage and report excluded claim groups. Dropout inference has a compute cost and cannot replace a native audit. Avoid conflating a monotonic threshold or lower uncertainty score with a guarantee of retained factual precision.

## 2106.07803 — SynthASR

[Source](https://arxiv.org/abs/2106.07803). Read: multi-context synthesis, real/synthetic sampling, staged adaptation and normalized WER results.

**Method and evidence.** Generate diverse voices/prosodies and train RNN-T on weighted mixtures of synthetic and real speech, with staged freezing/unfreezing and later real-only consolidation. The medication-name experiment uses 50k real hours and 5k synthetic hours; a 98:2 sampling stage gives normalized medication WER 13.70, but later real-only stages worsen it to 21.47 and 34.56 while general-domain behavior recovers. NWER is relative to a baseline, not absolute error percent.

**Limits and decision.** Synthetic data is targeted lexical support, not an equal replacement for real acoustic coverage, and consolidation can erase the new skill. Use a capped synthetic mixture and monitor both weak-condition gain and real baseline regression throughout C1 training. Match text/voice counts across loop controls. Stop based on real held-out utility and preserve the earlier checkpoint when later replay improves the average but loses the targeted claim behavior.

## 2404.01413 — Is Model Collapse Inevitable?

[Source](https://arxiv.org/abs/2404.01413). Read: replace/accumulate experimental design, text/image/molecule examples, linear-model theorem and limitations.

**Method and evidence.** Compare replacing each training corpus with generated data against retaining and accumulating previous data. Empirical error remains bounded in the tested accumulation settings. For isotropic ridgeless linear regression with sufficient samples, added-noise error scales with a summable series ∑1/i² rather than linearly in iteration count under replacement. The paper distinguishes error blowup from mode collapse, uniformity and artifact amplification.

**Limits and decision.** This theorem's Gaussian/linear assumptions do not prove a speech loop safe. The accumulated dataset grows and costs more to train, whereas this project has fixed compute and may cap replay. Keep immutable real anchors and per-source sampling floors, retain synthetic provenance and enforce real-only checkpoint gates. Describe this as an empirical safeguard to test, not a mathematical guarantee that fixed-budget reciprocal training avoids every form of collapse or speaker-mode loss.
