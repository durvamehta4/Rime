# Prosody, representation and local control

These reviews inspect cited full-text methods, evaluation and limitations. Reported results are not reproduced Rime measurements.

## 2208.13191 — Towards Disentangled Speech Representations

[Source](https://arxiv.org/abs/2208.13191). Read: architecture, representation probes, correlation-loss follow-up, experiment/conclusion passages.

**Method and evidence.** A joint audio/text encoder plus an audio-only encoder supports ASR, TTS and reconstruction. Fifteen independent training runs expose very different solutions; speaker-information probes and singular-value analysis characterize them. A correlation penalty decorrelates the secondary embedding. Average WER falls from 15.5% for the compared non-disentangled solutions to 11.7% with this loss, while the naturally stronger disentangled solution reaches 9.8%.

**Limits and decision.** Clean LibriSpeech, a reduced training schedule and worse-than-specialist ASR restrict the inference. The authors explicitly leave open whether decorrelation actually causes disentanglement. This supports auditing branch utilization, not adding a joint ASR/TTS foundation model or assuming zero correlation proves independence. In our adapters, measure whether identity, delivery and ecology inputs are used through controlled removal/swaps; retain task performance as the criterion. A few unusually successful seeds do not establish a reliable architecture, so budget a repeat of decisive pilot comparisons.

## 2311.03389 — Learning Disentangled Speech Representations

[Source](https://arxiv.org/abs/2311.03389). Read: SynSpeech construction, RAVE evaluation, probing/metric interpretation and conclusion passages.

**Method and evidence.** SynSpeech supplies controlled speaker/content/style combinations synthesized with OpenVoice at 16 kHz. Its three versions total 184,560 utterances; the large version has 249 identities, 110 contents and four requested styles. RAVE representations are evaluated using linear probes and modularity/compactness/explicitness metrics. The inspected analysis finds simpler gender/style information more separable than full speaker identity, and metric families disagree.

**Limits and decision.** Generator control labels do not automatically prove audible independence, synthetic artifacts may reveal factors, and 16 kHz speech cannot establish our ≥24 kHz generation quality. Probe accessibility is also not causal editability. Adopt a small factorial diagnostic grid for our real-supported identity/delivery controls, with independent realized-label checks and held-out combinations. Do not use synthetic factor labels as an unquestioned calibration truth set or infer real Hindi/Tamil disentanglement from a neat embedding plot. Validate on real same-speaker contrasts separately.

## 2406.00022 — Multilingual Prosody Transfer: Supervised versus Transfer Learning

[Source](https://arxiv.org/abs/2406.00022). Read: complete short main methodology/results, selected appendix implementation and listening-protocol passages.

**Method and evidence.** Compare fine-tuned SpeechT5 plus x-vectors against pretrained multilingual MMS followed by FreeVC. Reported Hindi MOS is 2.32 versus 4.01 and Tamil 2.12 versus 3.85. Thirty-five respondents assess generated/reference samples; recognition accuracy and DTW-based MCD accompany MOS. The appendix transliterates unsupported scripts and reports a fine-tuning schedule, while embedding selection uses emotion/gender classification.

**Limits and decision.** This comparison changes backbone, pretraining-language coverage and voice-conversion pipeline simultaneously. It cannot establish that transfer learning universally beats supervised fine-tuning. Speaker recognition is not proof of preserved local prosody, and MCD is sensitive to alignment. The practical lesson is to start with genuine native-language coverage and compare adaptations on the same checkpoint. Keep Indic Parler ahead of an English-only model retrofit, but run native pronunciation, delivery and identity tests rather than importing these MOS values as expected performance.

## 2106.08321 — ADEPT

[Source](https://arxiv.org/abs/2106.08321). Read: local/global prosodic classes, task design, final evaluation protocol and complete comparison table in a follow-up range.

**Method and evidence.** ADEPT uses perceptually disambiguated renditions of identical or ambiguous sentences to test emotion, interpersonal/propositional attitude, emphasis, phrasing and tonicity. Natural speech supplies a reference for distinguishability. Compare an unsupervised fixed reference vector against Ctrl-P's phone-level F0/energy/duration. For the female voice, syntactic-phrasing recognition is 84% natural, 77% Ctrl-P and 66% reference-encoder; anger recognition is 95%, 31% and 17%. Local timing success and global emotion success diverge substantially.

**Limits and decision.** English, two target voices and a demonstration using Griffin-Lim do not establish native transfer or modern system rankings. Import the evaluation design: same words with different intended readings, listener checks that real references are distinguishable, and separate local/global outcomes. For intent, test sarcasm/uncertainty/addressee contrasts using native judgments; never infer them from a pitch threshold or emotion label. Preserve the public free-text interface even if internal diagnostic contrasts use fixed categories.

## 2111.04730 — Emotional Prosody Control for Speech Generation

[Source](https://arxiv.org/abs/2111.04730). Read: FastSpeech2/controller design, two-stage training, complete user-study results in a follow-up range.

**Method and evidence.** Add a continuous arousal/valence controller to phoneme-level duration, pitch and energy predictors, keeping affect out of the final content representation. Train the backbone on LibriSpeech, then freeze it while adapting the controller/variance paths on roughly 71 hours of filtered MSP-Podcast. Reported naturalness MOS is 3.62±0.13 versus FastSpeech2's 3.65±0.09; listeners choose the stronger affective rendition in 86% of the tested pairs. Evaluation uses 30 unseen phrases and twenty English-proficient listeners.

**Limits and decision.** A two-dimensional affect wheel cannot represent all phonation, local timing, intent or recording ecology. A speaker reference is still required in the original model. Use its staged, restricted control interface as a precedent for adapter placement, not its emotion semantics as our ground truth. Test identity/text preservation while changing duration/F0/energy controls, then add phonation separately. Retain an internal identity source so the submitted generator needs no evaluation reference.

## 2307.04123 — Towards Cross-Language Prosody Transfer for Dialog

[Source](https://arxiv.org/abs/2307.04123). Read: collection protocol, feature representation, dissimilarity analysis, baseline results and qualitative errors; follow-up covered the comparison section.

**Method and evidence.** Bilingual speakers re-enact spontaneous English/Spanish utterances, yielding 1,871 pairs from 42 speakers. A 100-feature representation spans pitch, rate, lengthening, creak, intensity and cepstral prominence over relative-time windows. On their metric, EN→ES errors are 12.65 for a transcript-only synthesizer, 11.35 for identical prosody and 9.23 for linear mapping. Human inspection also finds missing nasality and syllable alignment in the metric.

**Limits and decision.** The metric is exploratory and only 56 pairs receive the described detailed similarity inspection. Direct contour copying does not necessarily preserve pragmatic function across languages. Give Hindi and Tamil separate native delivery/intent validation and word-level anchors; do not enforce an English prosodic template. Include breathiness/creak and turn-end behavior, while treating semantic intent as context-dependent. Test matched text with alternative delivery and language-specific phrasing before adopting shared control normalization.

## 2306.11658 — Cross-Lingual Prosody Transfer for Expressive Machine Dubbing

[Source](https://arxiv.org/abs/2306.11658). Read: VITS-derived architecture, noise modeling, multilingual protocol and subjective-result passages.

**Method and evidence.** A variational prosody reference encoder conditions a modified VITS model; a separate noise path or additional clean training support prevents reference noise from leaking into synthesis. The primary corpus has 118 hours from 127 speakers across five European locales. On 100 English-to-Spanish dubbing clips rated by 25 native listeners, plain reference transfer can underperform the centroid baseline on noisy references; explicit noise modeling improves the comparison and reportedly closes 11.2% of the human-dubbing gap.

**Limits and decision.** Proprietary data, reference-based dubbing and European languages limit direct transfer. Absence of language clusters in t-SNE does not prove invariance, and denoising can remove useful voice evidence. Keep an original-audio caption view and a separate generation-conditioning view; assign room/noise ownership explicitly. Test noisy-reference/clean-output and clean-reference/noisy-output contrasts, with independent noise and native-delivery checks. Do not treat a noise residual as a pure environmental source without examining leaked speech.

## 2408.06827 — PRESENT

[Source](https://arxiv.org/abs/2408.06827). Read: explicit duration/pitch/energy editing, phoneme mapping, subphoneme control and evaluation passages.

**Method and evidence.** Modify an existing FastSpeech2/JETS inference interface without retraining, mapping text annotations to aligned phoneme duration, pitch and energy changes. Repeated subphonemes allow within-phone contours. English-only JETS obtains reported German/Hungarian/Spanish CER of 12.82/18.73/5.92%; ten question examples improve MOS from 3.73 to 3.92. Mandarin tests need explicit tone mapping and show substantially larger errors.

**Limits and decision.** Results are American-accented, language mapping is engineered, and small listening tests do not establish broad expressive fidelity. These controls require explicit predictors; an autoregressive codec TTS model does not inherit them. Before budgeting local-control training, inspect the actual Indic backbone interface. Use a compatible control path or train an aligned adapter, rather than labeling waveform pitch/time manipulation as equivalent. Test native consonant/vowel duration and lexical preservation under edits, especially around code-switch boundaries.

## 2211.13533 — Prosody-Controllable Spontaneous TTS with Neural HMMs

[Source](https://arxiv.org/abs/2211.13533). Read: breath-group preparation, monotonic HMM conditioning, feature sweep, creak and listening tests.

**Method and evidence.** A no-skip left-to-right neural HMM stabilizes text/acoustic alignment on spontaneous speech, conditioned on mean F0, F0 variability and rate. The spontaneous data comprise 4,009 breath-group-derived examples. Sweeping controls works over supported ranges, but very low pitch settings produce creak and unreliable pitch readings. MOS is 3.48 versus baseline 3.60 with overlapping intervals; an expert test distinguishes modal from creaky outputs, but not both creak types reliably.

**Limits and decision.** One spontaneous speaker and hand-adjusted creak examples do not prove automatic control or noninferiority. Breath boundaries are useful anchors, not a rule that style cannot change within a breath group. Use real spontaneous groups and alignment diagnostics for local supervision. Verify phonation separately from F0, and never require a person to tune a submitted output until it sounds correct. Include failed alignments and low-support control extremes in evaluation.

## 2306.17199 — Multilingual Expressive Representation without Parallel Data

[Source](https://arxiv.org/abs/2306.17199). Read: discrete units/emotion encoders, pitch-duration prediction, cross-language experiments and error analysis.

**Method and evidence.** Frozen HuBERT-like units preserve content; a multilingual emotion bottleneck conditions separate duration, F0 and vocoder models. English/French resynthesis compares a unit-only baseline with emotional conditioning and an oracle. Reported English MOS rises from 1.75 to 3.14; cross-language emotion embeddings improve some F0 concordance values but remain below oracle controls. Recognition of happy/sad emotions still degrades relative to original speech.

**Limits and decision.** This is resynthesis, not a complete emotion-preserving translation system, despite broader motivation. Four shared emotion categories and single-vector pooling omit local intent changes. The language setup is European and unit representations can discard phonation. Preserve a distinct local acoustic path beside content/ASR features, and test whether content-centric tokenization loses creak, breath or register changes. Do not use an emotion classifier alone to certify preservation or equate a high MOS with correct requested affect.

## 2305.16749 — Diffusion-Based Diverse Prosody Prediction

[Source](https://arxiv.org/abs/2305.16749). Read: frozen-backbone training, stochastic prosody objective, Mandarin experiments, diversity analysis and latency limits.

**Method and evidence.** A small DDPM predicts joint phone-level pitch, energy and log-duration rather than deterministic MSE predictions. The pretrained FastSpeech2 backbone stays frozen. On a private 28.23-hour single-male Mandarin corpus, listeners favor the proposed expressiveness in 76.65% of pairs versus 13.22% for the baseline; feature-distribution JS divergence improves, especially for pitch/duration. Five hundred denoising steps cost RTF 0.47 on a 2080Ti versus 0.00031 for the original predictor.

**Limits and decision.** One training run, one speaker and marginal feature distributions do not establish instruction-constrained or speaker diversity. Fewer parameters do not imply faster inference. For Rime, prioritize small mixture/distributional control heads and measured sample cost; adopt diffusion only if conditional realism gains survive L4 profiling. Compare distributions under a fixed description and verify constraints, rather than rewarding arbitrary prosodic variance or quoting 2080Ti timings as L4 performance.

## 1803.09047 — End-to-End Prosody Transfer with Tacotron

[Source](https://arxiv.org/abs/1803.09047). Read: reference encoder/bottleneck, datasets and metrics, cross-speaker analysis and discussion passages.

**Method and evidence.** A reconstruction-trained reference encoder broadcasts a prosody embedding beside text and speaker embeddings. Experiments include 147-hour single-speaker and 296-hour/44-speaker English corpora. A critical negative result: a classifier identifies the reference speaker in 61% of cross-speaker outputs and target speaker in only 21%. MFCC-based probing reduces but does not remove leakage. Larger bottlenecks improve reference reconstruction while risking identity leakage.

**Limits and decision.** A good reference match is not independent style transfer. Absolute pitch is one identity shortcut, and inference originally needs a reference. Use speaker-relative contours only where meaningful and a constrained generation-compatible identity path. Evaluate cross-speaker and cross-text swaps independently, including different voice ranges. This supplies concrete evidence against treating a single rich reference embedding as both identity and delivery, or using reconstruction loss alone as proof of disentanglement.

## 1907.02479 — Fine-Grained Robust Prosody Transfer

[Source](https://arxiv.org/abs/1907.02479). Read: pre-aligned phone aggregation, VAE extension, unseen-speaker and neutral-data results, transcript-free variant.

**Method and evidence.** Precompute phone boundaries and aggregate pitch/power/duration per phone, avoiding unstable secondary attention. On a 20-hour expressive female English voice, unseen-speaker F0-frame error drops from 20.18% for secondary attention to 15.05% for aggregation and 14.98% with VAE. The VAE's incremental gain is small. Training on a neutral corpus severely degrades transfer, with reported FFE above 50%, despite useful contour correlation.

**Limits and decision.** Two female English voices, proprietary data and DTW-aligned metrics cannot establish free-description performance. Fine-grained control needs alignment and expressive support; normalization alone cannot manufacture missing regimes. Use word/phone-aligned auxiliary targets where native alignment is reliable, then verify generated placement in absolute time. Compare explicit alignment against learned timing on the same examples, and report alignment failures rather than filtering them away from results.

## 2108.02271 — Daft-Exprt

[Source](https://arxiv.org/abs/2108.02271). Read: FiLM placement, adversarial objective, matched-data baselines and disentanglement sweep.

**Method and evidence.** Condition phoneme encoder, low-level prosody predictor and decoder separately using FiLM; combine explicit pitch/energy/duration with a reference prosody representation. Against compared GST/VAE/Flowtron models, prosody-transfer MUSHRA reaches 58.0, but naturalness is not highest. Increasing adversarial weight from zero to 0.01 improves target-speaker classification from 40.5% to 97.6% while reducing prosody MUSHRA from 61.1 to 55.0; weight one further suppresses expressive transfer.

**Limits and decision.** The study uses English/private expressive data and a closed speaker set. Its evaluation explicitly separates prosody from naturalness; we should too. Use weakly regularized, separate conditioning projections and native swap tests, not maximal identity-invariance penalties. Check codec/vocoder artifacts on the most expressive examples: accurate delivery can be damaged downstream. Select a trade-off jointly on relevance, identity and naturalness rather than a single latent-classification metric.

## 1911.09645 — Global Pitch and Loudness Prosody Features

[Source](https://arxiv.org/abs/1911.09645). Read: seven-feature conditioning, single-speaker protocol, subjective/objective comparisons and conclusion-related passages.

**Method and evidence.** Project global statistics of log-F0 and RMS into Tacotron2 conditioning with one small linear layer. A ten-hour expressive British-English voice supports the experiment. Pitch DTW distance improves from 0.540 to 0.306, whereas RMS DTW remains 0.019 for both models. Naturalness MOS falls from 3.76 to 3.62 with large reported dispersion; stronger global feature matching is not uniformly better speech.

**Limits and decision.** Global moments discard order: early whisper then shout and the reverse can share statistics. RMS-based voicing and zero-filled pitch are fragile on noise/whispers. Keep this as a cheap global-control baseline, then require local masks and timing evidence for the proposed system. Test paired clips with identical global distributions but opposite local trajectories; any captioner/generator that treats them identically fails the PS's Change and timed-item requirements.

## 2110.02854 — Prosody-TTS

[Source](https://arxiv.org/abs/2110.02854). Read: architecture, Telugu setup, objective metrics/control experiments and conclusion passages.

**Method and evidence.** Explicit phone durations upsample linguistic states; frame F0/aperiodicity and mel features condition a non-autoregressive waveform generator. A four-hour, single-male Telugu corpus supports supervised auxiliary losses. The paper reports MOS 4.08, F0-frame error 4.23% and duration correlation 0.816; global factor edits and reference-prosody incorporation are evaluated separately.

**Limits and decision.** Twenty held-out utterances and 16 kHz single-speaker Telugu do not establish Hindi/Tamil multi-identity control, natural local transitions or ≥24 kHz quality. Predicted duration/F0 interfaces are useful precedents, not drop-in components for a codec decoder. Preserve native-script handling and actual model sample rate, and test controls before committing to an adaptation. Feature-level duration edits are preferable to calling arbitrary waveform stretching equivalent, but need a compatible synthesis path and audible realization checks.
