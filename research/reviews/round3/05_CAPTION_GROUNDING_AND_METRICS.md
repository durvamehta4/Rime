# Caption grounding, factuality and evaluation

Detailed scoped full-text reviews; all numerical results are author-reported. A metric benchmark is not the competition's private rubric.

## 2403.18572 — ACES

[Source](https://arxiv.org/abs/2403.18572). Read: semantic token classifier, metric construction, annotation/evaluation protocol, comparison table and discussion passages.

**Method and evidence.** Parse descriptions into sound-oriented semantic roles, embed aligned role contents and aggregate their similarities. The token classifier is trained on small manually labeled Clotho subsets. ACES has useful role-level interpretability and wins selected comparison categories, but its overall AudioCaps agreement is 83.0 versus FENSE 85.3, and Clotho 74.0 versus 75.7. The conclusion's broad superiority language exceeds that table.

**Limits and decision.** Text-reference similarity cannot establish audible truth, and role parsing errors propagate. A missing role overlap may yield zero even for a useful caption; matching the most similar entity can conceal extra false entities. Use role/claim decomposition for error analysis, then verify individual claims against audio. Do not substitute ACES for the weighted factual rubric or reward an added plausible entity merely because another entity matches. Include negation, actor swaps and extra-claim perturbations in native verifier validation.

## 2505.07609 — TACOS

[Source](https://arxiv.org/abs/2505.07609). Read: timed annotation/cleaning, frame-wise loss in a follow-up range, encoder/training protocol and event-detection comparisons.

**Method and evidence.** TACOS provides 12,358 recordings with 47,748 region captions. Frame-aligned contrastive learning normalizes each region's contribution by length and draws text negatives from other recordings, avoiding some overlapping same-clip descriptions as negatives. Strong-caption fine-tuning improves PSDS1 by about 5.5 points over weak-caption fine-tuning; a fully supervised detector remains substantially stronger. Output hops are approximately 20 ms, but evaluation includes one-second segments.

**Limits and decision.** Dataset collection favors energetic segments and has a finite ontology; cleaning removes transcribed speech and cannot supply the PS's intent supervision. Twenty-millisecond embeddings do not prove ±250 ms localization accuracy. Adopt length-balanced local supervision with overlap-aware negative masks and separate real timing evaluation. Check source overlap before using external audio. Preserve quiet events in our pool rather than copying highest-energy cropping, and treat temporal claims separately from clip-wide semantic similarity.

## 2306.01533 — Temporal Relations via Sound Event Detection

[Source](https://arxiv.org/abs/2306.01533). Read: SED integration, temporal-tag construction, evaluation definitions and dataset-specific results.

**Method and evidence.** Convert independently predicted event intervals into four coarse relation-complexity tags and condition caption decoding. AudioCaps temporal F1 rises from 23.4 to 75.2, but CIDEr drops from 72.6 to 68.2. On Clotho, several general-caption metrics decline because the detector produces overly complex tags under domain mismatch. The temporal metric chiefly checks the presence of sequential conjunctions, not whether event identities/order/times are correct.

**Limits and decision.** A sentence containing “then” is not proven temporally grounded. Coarse simultaneous/sequential classification also loses partial overlap. Keep an interval graph with explicit directed relations and uncertainty, and evaluate actual event-time/order matches. Do not hard-force detector suggestions into captions. Include domain-shifted plain clips where no extra event exists, so an overactive temporal helper can be rejected before it increases false claims.

## 2210.06354 — Text-to-Audio-Grounding Caption Similarity

[Source](https://arxiv.org/abs/2210.06354). Read: phrase extraction/TAG model, datasets, co-caption-pair validation, component studies and conclusion.

**Method and evidence.** Extract noun/verb phrases and embed them with a text-to-audio-grounding-trained encoder, then compare candidate/reference phrase representations. The TAG training set has 4,590 clips and 13,958 timed phrases. Reported same-recording-pair similarity improves over BERT-based comparison; phrase extraction quality also matters. The paper explicitly treats acoustically similar but semantically different descriptions, such as machinery versus insects, as a beneficial match.

**Limits and decision.** Same-recording membership is not a human factuality label, and its reported correlation-like scores do not establish per-claim correctness. Confusing sound causes can be acceptable embedding similarity yet be a false assertion under the PS. Use phrase grounding only as evidence, preserving entity identity, source attribution, negation and timing in the claim verifier. Test acoustically similar hard negatives rather than allowing broad sound similarity to certify a precise object or room claim.

## 2409.08489 — Resource-Efficient Reference-Free Caption Evaluation

[Source](https://arxiv.org/abs/2409.08489). Read: pooled token-confidence definitions, temperature validation, metric-alignment results and limitations.

**Method and evidence.** Arithmetic/geometric token-probability pooling, optionally restricted to content words, offers a cheap confidence signal. Compare those signals with reference metrics such as CIDEr/FENSE/CLAP-text similarity and a text judge, using one CNN/Transformer captioner. Temperature tuning can roughly halve average reported Brier scores, but the optimal temperature changes with the target metric's distribution.

**Limits and decision.** Alignment to a soft reference score is not calibrated probability of an audible claim being true. The authors acknowledge reference-metric limitations and uncertainty about applying these calibration statistics to natural-language outputs. Use token entropy/probability only as inexpensive features for a native-labeled claim selector. Preserve separate fit, calibration and audit splits and test genuine binary claim correctness. Do not advertise a low ECE against a caption-similarity score as a formal false-assertion guarantee.

## 2110.04684 — FENSE / Can Image Metrics Evaluate Audio Captions?

[Source](https://arxiv.org/abs/2110.04684). Read: human-pair benchmark construction, semantic/fluency scoring, error-detector evaluation, comparisons and conclusion.

**Method and evidence.** Combine Sentence-BERT reference similarity with a learned fluency-error penalty. Pairwise human comparisons form AudioCaps-Eval/Clotho-Eval, avoiding unreliable absolute judgments. FENSE reaches overall comparison accuracy 85.3/75.7 versus SPICE 59.7/56.3. The separate error detector has precision 96.8%, recall 76.4% on 723 annotated generated captions. N-gram metrics can reward meaningless appended words.

**Limits and decision.** Fluency and semantic similarity still do not establish acoustic relevance; the authors explicitly state this. Global preference agreement can hide missed local or numerical facts. Keep a small prose/format validator, but ground factual claims with audio and measurements. Do not optimize caption wording primarily for BLEU/CIDEr/FENSE or compare against one supposedly exhaustive reference. Audit concise, well-supported prose and each false extra assertion under the actual PS-style scoring rule.

## 2409.12962 — CLAIR-A

[Source](https://arxiv.org/abs/2409.12962). Read: score/prompt construction, constrained JSON generation, human comparison, tie-breaking/Chinese-transfer results and conclusion-related passages. Extra reads corrected a reference heading inside a figure that initially truncated extraction.

**Method and evidence.** Ask a text LLM to compare a candidate with reference captions, optionally adding a semantic tie-breaker. Clotho preference accuracy is 79.7 versus FENSE 75.7. However, no tie-breaker gives 68.3 and random tie-breaking already gives 77.6, so much of the apparent gain is a scoring/tie-handling effect. Their Chinese experiment translates English text and retains the original judgments; it does not test understanding Chinese audio.

**Limits and decision.** This judge never hears the candidate audio. Plausible explanations are not evidence of faithful reasoning, and reference omissions remain unresolved. Grammar constraints ensure parseable outputs, not truthful scores. Keep text-reference metrics for diagnostics only. Preserve ties/uncertainty when systems are indistinguishable, report bootstrap differences, and calibrate actual audio-claim decisions with native judgments. Do not replace a measured acoustic verifier with an eloquent explanation or transfer Chinese-text results to Hindi/Tamil acoustic evaluation.

## 2406.06295 — Zero-Shot Audio Captioning with Soft and Hard Prompts

[Source](https://arxiv.org/abs/2406.06295). Read: modality-gap augmentation, event retrieval/dropout, matched architecture/setup and quantitative/qualitative cross-domain sections.

**Method and evidence.** Train a GPT-2 decoder to reconstruct captions from CLAP text embeddings, then substitute audio embeddings at inference. Similar-caption replacement and Gaussian perturbation bridge the modality gap; AudioSet-label hard prompts and prompt dropout provide imperfect event guidance. AudioCaps SPIDEr reaches 40.0 versus the compared WSAC 36.3, below several paired-data models. The authors' qualitative analysis explicitly identifies speculative text such as imagined passengers when using unconstrained generated-caption training.

**Limits and decision.** Text-only decoder training still relies on CLAP's paired pretraining, a 527-label retrieval vocabulary and ten-second audio views. It does not supply open temporal speech detail or intent. Use retrieval/dropout as robustness ideas, not a replacement captioner. Prevent helper labels from becoming unquestioned assertions; train with corrupted/missing helper evidence and source-linked claim masks. Test unsupported causes/addressees generated from familiar sound associations, especially when a rich language prior overwhelms weak audio evidence.

## 2410.09472 — DRCap

[Source](https://arxiv.org/abs/2410.09472). Read: projection/retrieval objective, leakage precautions, cross-domain protocol, component ablations and conclusion.

**Method and evidence.** Project CLAP audio embeddings onto text support and decode with a LoRA-adapted LLM plus retrieved captions. Training samples references from a similarity band to prevent copying near-identical text. In an AudioCaps ablation, CIDEr is 70.5, 69.2 without retrieval and 31.2 without projection; projection contributes much more than adding retrieval alone. Cross-domain setups also use target-domain caption support, whose removal reduces performance.

**Limits and decision.** The model is not independent of paired CLAP pretraining, and “zero-shot” variants differ in dataset overlap and target text access. The authors explicitly distinguish LAION pretraining that already includes target datasets. Apply the same provenance discipline to our teachers, retrieval store and evaluation clips. Retrieval can suggest candidate claims, but exact speaker/timing/intent must come from the current audio. Compare a no-retrieval baseline and deliberately misleading retrieved descriptions; reject improvements attributable to test leakage or copying.

## 2506.00800 — CLAP-ART

[Source](https://arxiv.org/abs/2506.00800). Read: semantic/acoustic tokenizer comparison, RVQ detail in an extra range, matched training and six-seed ablations.

**Method and evidence.** Quantize BEATs semantic features into discrete tokens for a BART captioner, replacing waveform-reconstruction codec tokens while keeping global CLAP features. AudioCaps SPIDEr rises from 46.3 for EnCLAP-base to 49.8 for BEATs-RVQ; FENSE rises from 64.2 to 65.5. Removing the global CLAP vector hurts the semantic-token model much less than the codec-token baseline. Six-run averages are explicitly separated from best-run reference scores.

**Limits and decision.** Semantic event tokens and phonetic content tokens encode different information; neither guarantees phonation, local measurements or intent. More RVQ layers add diminishing gains and data/cache cost. Do not build a new tokenizer just to unify captioner/generator interfaces. Reuse native-capable audio features with small task-specific heads, keeping waveform/codec and semantic representations distinct. Report mean/repeat variability for decisive comparisons and distinguish best-of-seed diagnostics from deployable gains.

## 2501.11378 — Whisper Hallucinations from Non-Speech Audio

[Source](https://arxiv.org/abs/2501.11378). Read: non-speech construction, duration/noise experiments, hallucination dictionary and mitigation comparison.

**Method and evidence.** Run Whisper-large-v3 on 301,317 filtered non-speech clips; 40.3% produce textual hallucinations under that setup. Many outputs recur, motivating a bag-of-hallucinations filter, delooping and optional alignment confirmation. Higher beam sizes can increase errors; VAD plus output checks helps more than some parameter tweaks. Augmentation experiments also show dependence on noise duration and position.

**Limits and decision.** These English-specific non-speech inputs do not predict the rate on native real speech, and a phrase dictionary can delete genuine words. A VAD pipeline that concatenates speech segments destroys original timing and ecology. Keep timestamps mapped to the original file; validate ASR against activity/alignment and retain uncertainty near laughter, silence and soft speech. Never use hallucinated transcripts as proof of addressee or intent, and avoid blindly banning common spoken phrases.

## 2211.08983 — SPIDEr-max

[Source](https://arxiv.org/abs/2211.08983). Read: model/likelihood comparison plus follow-up covering candidate examples, max metric, beam-size experiment and conclusion after an early table-reference extraction boundary.

**Method and evidence.** Score the best candidate among multiple beams against known reference captions. On AudioCaps, two candidates raise the oracle metric from 0.401 to 0.473; a beam of 100 reaches 0.953. Likelihood/SPIDEr correlations are only 0.224/0.259 on Clotho/AudioCaps, and attempted automatic ranking does not substantially solve selection. Rare matching n-grams explain much of the metric boost.

**Limits and decision.** Oracle reference selection is unavailable during PS inference and does not demonstrate human-level deployed captions. More candidates increase a maximum even without better autonomous selection. Report one frozen automatic caption, with optional multi-candidate results labeled as diagnostics and all inference costs counted. Never tune/select against sealed rubrics, and do not confuse ten required generator realizations with permission to report an oracle caption score. Record candidate counts and retry budgets for training-data verification. Final PS generation retains all ten predetermined outputs without choosing replacements.
