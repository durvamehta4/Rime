# Composition, hard negatives and negation

Scoped method/result/limitation readings of distinct publications; no reproduced experiments.

## 2409.09619 — Compositional Audio Representation Learning

[Source](https://arxiv.org/abs/2409.09619). Read: source slots, reconstruction/classification objectives in an extra range, synthetic-polyphony experiments and ablations.

**Method and evidence.** Transform AudioMAE patches into source-centric slots, trained through semantic-feature or spectrogram reconstruction and optionally permutation-matched source labels. On synthetic one-second OST mixtures, the inspected unsupervised feature-reconstruction setup reaches mAP 0.578 versus the AudioMAE baseline's 0.476. Feature reconstruction exceeds spectrogram reconstruction. Removing disjointness can improve results, partly because inactive slots should not be forced apart.

**Limits and decision.** Synthetic one-second mixtures, a fixed slot budget and classification do not prove timed source separation in real 30-second Hindi/Tamil speech. Audio sources overlap in time/frequency; visual exclusive-mask intuitions can fail. Represent multiple simultaneous claims/events without forcing exclusive frame ownership. Use source grouping as an optional small readout experiment only if overlap errors justify it; do not add a separator/slot backbone by default. Evaluate actor attribution and overlapping vocal/background events on held-out real mixtures.

## 2401.04935 — Learning Audio Concepts from Counterfactual Language

[Source](https://arxiv.org/abs/2401.04935). Read: prompt-based substitutions and angular/factual losses in a follow-up range, downstream results, loss trade-offs and conclusion.

**Method and evidence.** Generate alternative caption sources with an LLM and train audio/text embeddings to prefer the factual description through a margin loss plus factual alignment. Improvements in Clotho retrieval coexist with poor transfer: ESC-50 zero-shot accuracy is 0.744 versus CLAP's 0.729, but UrbanSound8K is 0.475 versus 0.798. Loss terms trade factual retrieval against distinguishing substituted descriptions; adding both is not universally best.

**Limits and decision.** Text substitutions are linguistic hard negatives, not observed causal interventions on audio, and a plausible substitution may actually be present elsewhere in a clip. Do not call this causal identification from captions alone. Use independently verified, minimal changes to one claim at a time—source, polarity, timing or actor—with masks for unknown co-occurrence. Test improvement on native unseen combinations and ordinary accuracy together, so a specialized negative-training gain cannot hide broader degradation.

## 2607.12290 — The Sound of Absence

[Source](https://arxiv.org/abs/2607.12290). Read: negative proposal/audio verification in an extra range, retrieval/choice protocol, controlled mixture diagnosis and limitations.

**Method and evidence.** Add verified absent sound concepts to existing captions and test negated retrieval/choice matching across audio-text embedding models. Average AudioCaps R@1 drops from 34.1 to 26.1 under negation. A separate 1,000-item controlled mixture diagnostic finds affirmative/negated queries nearly equivalent in text space. Audio-side negative labels receive a limited manual audit: 445/460 judgments agree. Embedding steering helps local choices more than full retrieval.

**Limits and decision.** One absent concept, environmental datasets and a single-annotator subset do not establish reliable arbitrary negation or speech-intent inference. An unmentioned event is not an absent event. Add explicit polarity and scope to the internal claim record and validate absence against audio; do not feed “no laughter” into a generic cosine threshold as if it were reliable. Negative instructions need their own generator checks. Include same-concepts/different-negation-scope examples and distinguish unobserved, absent and contradicted claims.
