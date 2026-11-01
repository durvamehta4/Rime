# Speaking-style and contextual supervision

Full-text scoped reviews below separate author-reported evidence from the proposed Rime transfer. They do not claim exhaustive appendix reading or experimental reproduction.

## 2308.16021 — CALM

[Source](https://arxiv.org/abs/2308.16021). Read: contrastive pair construction, retrieval-weighted conditioning, datasets, objective/subjective results and conclusion.

**Method and evidence.** Train a style encoder and BERT/GRU text encoder against an acoustic-style-derived similarity target. Retrieve multiple internal references using style-related text features, then average their embeddings with similarity weights. Mandarin emotion-reference precision improves from 0.523 to 0.776; style-appropriateness MOS rises from 2.804 to 3.812. English audiobook improvement is smaller. The reference style encoder supplies both contrastive targets and part of the evaluation.

**Limits and decision.** Content-associated style is not the externally requested delivery, and a single-speaker corpus confounds lexical and style patterns. Average references can erase uncommon extremes. Use retrieval only as an automatic internal conditioning/data-selection option, with explicit user descriptions taking priority over content priors. Evaluate “positive words spoken sadly” and other mismatched content/delivery pairs. Do not use the retrieval encoder as the sole verifier or mistake its high similarity for correct local timing or intent.

## 2406.18910 — Factor-Conditioned Speaking-Style Captioning

[Source](https://arxiv.org/abs/2406.18910). Read: frozen encoder/bridge/LoRA architecture, factor-first training, decoding, component ablations and complete result tables.

**Method and evidence.** Predict an internal factor phrase before a fluent caption; greedy factor decoding followed by sampled wording preserves factor accuracy better than sampling both. The matched original-caption model has 95.1% mean factor accuracy versus 96.5% for factor-first greedy-then-sampling. PromptSpeech contains 26,588 utterances but only 154 unique captions. Whisper-large intermediate layers plus a time/layer bridge outperform the compared WavLM-base configuration. The bridge itself has 90.7M trainable parameters.

**Limits and decision.** A four-factor closed benchmark does not establish open-set temporal or intent captioning. Their conversion treats unspecified factors as normal, which is inappropriate for incomplete PS labels. Adopt evidence/factor-first supervision with explicit unknown masks. First test intermediate layers of the already selected caption backbone before adding another frozen encoder. Keep proposed claim content fixed during final wording; sampling a fluent sentence is not automatically safe after risk calibration. Compare useful facts and false assertions on native open descriptions, not only lexical overlap.

## 2211.14548 — Contextual Expressive TTS

[Source](https://arxiv.org/abs/2211.14548). Read: synthetic context construction, context/content inputs, staged training, evaluation and limitations of demonstrated cases.

**Method and evidence.** Join expressive speech and unrelated emotional text through a shared emotion label, then train a context-conditioned Transformer TTS using separate context and content embeddings. Its constructed set has 5,912 examples, four voices and two emotions. Contextual MOS is approximately 3.70/3.88 for amused/angry speech, below explicit-label control at 3.99/4.12. Text-only pretraining matters; the no-pretraining version has substantially worse WER. Out-of-domain use is chiefly demonstrated with selected examples.

**Limits and decision.** Joining Yelp sentiment to acted speech is weak context supervision, not evidence of the true addressee or subtext. Model and training cost are unsuitable as a new backbone. Distinguish a generator's requested fictional context from a captioner's inferred observed intent. Never manufacture intent labels by assigning a narrative to a matching emotion class. Build native same-content/context counterexamples and audit whether descriptions add unsupported people, motives or events.

## 2305.10321 — Controllable Speaking Styles Using an LLM

[Source](https://arxiv.org/abs/2305.10321). Read: global/word control equations, bounded edits, baseline/random/oracle protocol and appropriateness results.

**Method and evidence.** An LLM suggests relative duration/energy/F0 edits for an explicit FastSpeech2-style interface, at global and word levels. Global pitch scaling and pause edits caused artifacts, so the implementation constrains them. Style-appropriateness preference is 51.4% versus baseline 30.9% and random 17.7%; dialogue preference is 48.4/31.0/20.6%. Neutral naturalness stays around MOS 3.1, below the best reference-conditioned oracle. Backbones were trained using eight A100-80GB GPUs for 24 hours each.

**Limits and decision.** Small English-specific scenarios and an external LLM do not establish native control or an eligible submitted pipeline. The random-control baseline is valuable: added variation alone can bias perception. Reuse an eligible open planner only if it maps to a supported, bounded synthesis interface; constrain and verify native edits. Include random but equally sized edits in the pilot to isolate meaningful instruction control from simple expressiveness.

## 1808.01410 — Text-Predicted Global Style Tokens

[Source](https://arxiv.org/abs/1808.01410). Read: stopped-gradient style targets, single/multispeaker setup, listener comparison, noise observation and discussion.

**Method and evidence.** Predict either GST mixture weights or a style embedding from text, using stopped-gradient acoustic targets. A 147-hour expressive audiobook voice and a 22-female-speaker mixture illustrate text-only style generation. Listeners do not clearly prefer the two prediction variants over each other. Automatic background-noise removal is an informal observation, not a counted noise benchmark. The paper explicitly lacks a full multispeaker quantitative comparison.

**Limits and decision.** One expressive speaker dominates the multispeaker training; text prediction still yields limited dynamics for otherwise neutral voices. It cannot establish style independence across language or gender. Balance speaker/style support before attributing improvements to a new latent architecture. A text-only prior may fill unspecified delivery, but explicit description clauses must override it. Keep ecology labels even if a generator learns to omit incidental training noise: removing noise is beneficial only when the requested scene calls for it.

## 2203.12201 — Hierarchical Context for Mandarin Speaking Style

[Source](https://arxiv.org/abs/2203.12201). Read: phrase/sentence encoder, reference distillation, seven-hour setup, component ablations and case analysis.

**Method and evidence.** XLNet phrase features pass through inter-phrase/inter-sentence attention, then predict a reference-derived style embedding for FastSpeech2. A male Mandarin lecture corpus has 4,700 clips. Proposed MOS is 4.067 versus 3.842 for plain contextual encoding and 3.679 for FastSpeech2. Removing reference distillation or inter-sentence context reduces the reported comparison score; matched-text case studies show different stress patterns with different contexts.

**Limits and decision.** One voice and access to neighboring sentences do not establish a general input interface. Lexical context predicts a plausible performance, not uniquely correct intent. Use only text/context present in the evaluation item and an explicit within-clip hierarchy. Do not invent prior dialogue, a social relationship or unrestricted future context. Separate phrase-local evidence from global priors, and test whether a small hierarchical control readout improves native transitions enough to justify cost.

## 2304.06359 — Coherent Style Prediction with Hierarchical Transformers

[Source](https://arxiv.org/abs/2304.06359). Read: text/style-history inputs, mixture mask, single/multisentence evaluation and ablations.

**Method and evidence.** Predict current GST style from hierarchical text context plus previously synthesized style embeddings. On a 30-hour single-male Mandarin audiobook, single-sentence MOS is 3.990 versus HCE's 3.923, but multi-sentence MOS is 3.917 versus 3.761. Removing previous style context reduces CMOS by 0.172. An expressive sentence scorer alone can miss awkward transitions between adjacent sentences.

**Limits and decision.** Previous generated style can accumulate errors, and smoothness is undesirable when a description explicitly requests a rupture. Do not import the paper's unrestricted-context language literally; released encoders have finite inputs. Maintain a clip-level identity/state and default continuity across phrase synthesis, with explicit event/Change instructions allowed to override it. Evaluate concatenation boundaries and deliberate register switches separately. Never smooth away a required interruption or whispered reversal to improve global continuity.

## 2408.13891 — SpeechCaps

[Source](https://arxiv.org/abs/2408.13891). Read: multi-talker synthesis and description generation, relabeling/filtering, instruction-tuning comparisons and result tables; generation details received an extra range read.

**Method and evidence.** Combine two or three generated talkers with gaps/overlap, record metadata and turn it into captions, then use staged single/multitalker caption training. DeSTA+ improves Dynamic-SUPERB speaker-verification overall accuracy from 0.580 to 0.645. Yet on its own harder SpeechCaps questions, instruction-following falls from 0.607 to 0.483 and overall accuracy from 0.159 to 0.127, despite a slightly higher conditional accuracy. The paper acknowledges training/evaluation alignment bias.

**Limits and decision.** Metadata labels initially overlap acoustically; selecting only extreme/middle 15% bands simplifies the test. Synthetic talker overlap is not a naturally grounded conversation. Use mixtures as training curricula with realized timing/attribute checks, while preserving ambiguous real cases in evaluation. Report unconditional accuracy and failure-to-answer, not only accuracy among compliant outputs. Speaker count should be inferred from audio, not from an assumed single-voice input wrapper.

## 2207.12262 — Conversational Style Transplantation with Interjections

[Source](https://arxiv.org/abs/2207.12262). Read: tagged non-attentive synthesis, style/speaker confounding, augmentation, listening and automated-checkpoint protocol.

**Method and evidence.** A duration-controlled Tacotron variant uses separate speaker, dialogue-act, emphasis and interjection inputs. Voice conversion augments conversational style into otherwise neutral identities. Style preference favors augmentation over baseline, for example 61.11% versus 28.39% for one target voice. However, the augmented system shifts perceived identity; adversarial training preserves identity better but is less effective stylistically.

**Limits and decision.** Synthetic augmentation can reproduce a source persona instead of a target speaker's style; the demonstrations also rely on manually marked test inputs. A final intonation-slope check measures only one narrow failure type. Adopt separate realization tests for interjection/word emphasis and identity, counterbalance styles across speakers where feasible, and compile public free descriptions automatically into supported controls. Do not claim that augmentation or a rising/falling contour automatically solves conversational naturalness.

## 2506.05984 — Audio-Aware LLMs as Speaking-Style Judges

[Source](https://arxiv.org/abs/2506.05984). Read: StyleSet tasks, judge/human protocol, correlation results and explicit limitations.

**Method and evidence.** Twenty fine-grained instruction tasks and twenty role-playing contexts compare four speech models using human and audio-LLM ratings, with five sampled judge responses per item. Gemini/human Pearson correlation is 0.640 for style instruction following versus human/human 0.596; another judge reaches only 0.355. Role-playing human agreement is much lower at 0.253. Speech systems sometimes literally say “sigh” instead of realizing it and fail within-utterance pace changes.

**Limits and decision.** Correlation does not establish per-claim accuracy, native transfer or reliable ranking of near-equal systems. Strong closed-API judge results do not justify substituting an unvalidated open judge. Use this benchmark's local instructions and spoken-control-token failure cases in native audits, while calibrating eligible open verifiers against native listeners. Runtime remains fully automatic/open; teacher ensembling is training/evaluation cost that must be counted, not a free correctness guarantee.
