# Native language, code switching and alignment

## 2303.00747 — WhisperX

[Source](https://arxiv.org/abs/2303.00747). Read: cut/merge, independent transcription and forced-alignment methods in extra ranges, datasets/metrics and segmentation results.

**Method and evidence.** Cut long VAD regions at low-activity points and merge short ones near Whisper's trained context length. Transcribe without previous-text conditioning, then align the recognized phoneme sequence to acoustic logits. On English meeting/telephone and long-form tests, VAD-aware batching improves speed and reduces boundary-related errors; the reported speedup approaches twelve-fold. Larger alignment models do not consistently outperform the base model, and domain match matters.

**Limits and decision.** The paper lacks quantitative non-English word-segmentation validation. Forced alignment can assign times to incorrect transcripts and unsupported phonemes; it is not evidence that words were actually spoken. Use a native-compatible aligner with transcript-confidence checks, retain an original-time offset map and assess native boundaries manually on development data. VAD cropping is an ASR view only: breaths, whispers and non-speech sounds remain in the captioner's complete original waveform.

## 2305.15386 — Vistaar

[Source](https://arxiv.org/abs/2305.15386). Read: IndicWhisper architecture, dataset/domain comparisons and WER tables.

**Method and evidence.** Fine-tune Whisper-medium separately for 12 Indian languages on about 10,700 hours and evaluate 59 language/domain combinations. Force transcription and a specified language rather than translation. In the focused Hindi table, IndicWhisper's average WER is 13.6 versus IndicWav2Vec's 21.0; Hindi Gramvaani remains harder at 26.8 versus 7.6 on IndicTTS. The broader table uses a separate public-model comparison and should not be silently merged with the focused setting.

**Limits and decision.** Studio, crowd and conversational domains differ greatly, and language-token forcing does not guarantee code-switch preservation. Use released native ASR as a candidate guard and audit its domain-specific mistakes before setting rejection thresholds. Evaluate expressive/noisy real speech alongside synthetic speech to reveal evaluator bias. Preserve original-script text and distinguish caption intent derived from acoustics from speculative interpretation of a possibly incorrect transcript.

## 2408.06227 — FLEURS-R

[Source](https://arxiv.org/abs/2408.06227). Read: multilingual restoration architecture, ASR consistency and synthetic-speech quality tables.

**Method and evidence.** Replace Miipher's English features with intermediate USM features, remove unnecessary text/speaker conditioning and restore 102-language FLEURS to 24 kHz. Mean original/restored CER is similar, 9.67% versus 9.74%, while predicted naturalness improves. TTS trained on restored speech improves predicted MOS overall from 3.79 to 3.89; Tamil's displayed score rises 3.89→4.27. Generated speech still has higher aggregate CER than real speech.

**Limits and decision.** Predicted MOS is not a native human study, restoration can alter individual examples, and a 24 kHz output does not recover every lost acoustic fact. Treat restored data as a separately labeled possible generator-training view. Caption source/ecology labels must refer to original audio; do not train them against restored waveform while retaining the original noise/channel claims. Keep all original/restored siblings in one split and verify release/license availability before adoption.

## 1810.00662 — Hindi-English Code-Switching Speech Corpus

[Source](https://arxiv.org/abs/1810.00662). Read: corpus creation in an extra range, speaker distributions, transcript/LM partition and baseline results.

**Method and evidence.** Construct Hinglish text from context-varied web sources and record 7,005 utterances from 71 speakers. Distinguish phrase-level switching from English words embedded in Hindi with little English context. Split 5,500/1,505 utterances and exclude test sentences from LM text; the best displayed DNN-HMM baseline reaches 25.40% WER versus monophone 53.51%. Speakers cover several regions, with a 44/27 male/female imbalance.

**Limits and decision.** Prompted readings of collected text are not spontaneous pragmatics, and sentence exclusion alone does not establish speaker-disjoint evaluation or licensing for every downstream use. Use the phenomenon to design code-switch stress cases rather than assume this corpus solves conversational coverage. Freeze native/Latin-script normalization rules and report switch-region errors separately. Do not interpret English insertions as an acoustic change of identity, accent or addressee without supporting evidence.

## 2104.00235 — Multilingual and Code-Switching ASR Challenges

[Source](https://arxiv.org/abs/2104.00235). Read: language/data design, shared-lexicon TDNN/LM and end-to-end settings, baseline analysis.

**Method and evidence.** Release roughly 600 hours across six Indian languages plus 150 hours of Hindi-English/Bengali-English code-switched speech. Compare multilingual and monolingual recognizers with shared pronunciation inventories and language models. The multilingual baseline improves Tamil but worsens the other languages in this comparison; shared LM paths can introduce cross-language word errors. Code-switch evaluation additionally uses transliteration-aware T-WER.

**Limits and decision.** Script-equivalence metrics depend on a declared mapping and can conceal pronunciation mistakes. A multilingual model need not outperform a native-specific model, and “phonetic orthography” is not an error-free pronunciation lexicon. Compare native-specific and shared ASR guards on the same held-out cases. Keep official/raw CER alongside a separately reported diagnostic normalization, and freeze that normalization before final evaluation. Split by source/speaker lineage so challenge-domain overlap cannot inflate the measured benefit of synthetic replay.

## 2210.17153 — Signal Processing Aided Alignments for 13 Indian Languages

[Source](https://arxiv.org/abs/2210.17153). Read: HMM/group-delay/sub-band correction, IndicTTS training, Hindi examples and native preference results.

**Method and evidence.** Correct forced phone boundaries using nearby syllable group-delay cues and spectral-flux cues for consonants, then train FastSpeech2 with improved durations. Data are mostly ten-hour single-speaker voices at 22.05 kHz. Comparisons include missed Hindi short vowels/aspirated stops; native preference favors the proposed system in Hindi and Tamil, with some smaller-language results explicitly inconclusive. Training each system takes 1.5–2 days on two A100s.

**Limits and decision.** Better alignment supports native correctness, but independently trained single voices and low sample rate do not meet the full generator task. Signal boundaries can also be spurious and need transcript constraints. Add small native phone-boundary audits and short-vowel/gemination/aspiration tests before learning local duration control. Adapt an eligible ≥24 kHz native backbone instead of reproducing 25 separate systems, and do not claim the paper's subjective preference translates directly to PS relevance or diversity.

## 2507.16875 — Impact of Duration Prediction on Indian-Language TTS

[Source](https://arxiv.org/abs/2507.16875). Read: conditional-flow infilling/duration formulation, filtering, per-language WER table and conclusions.

**Method and evidence.** Adapt Voicebox-style flow matching with aligned repeated characters and compare infilling-style versus speaker-prompted duration prediction. For 50%-masked Tamil speech, displayed overall WER changes 0.31185→0.29455; Hindi instead worsens 0.19303→0.19977. Similarity and intelligibility favor different strategies. Preprocessing removes Latin-script sentences from selected datasets and rejects examples above a native ASR-WER threshold.

**Limits and decision.** This selection omits code switching and may remove expressive/noisy but valid examples, so it cannot justify a universal filter. In-context half-infilling is easier than reference-free full generation and does not establish timed prose control. Treat duration prediction as a per-language ablation, with both identity and CER endpoints. Keep rejected-data coverage statistics and code-switch evaluation; use separate generator-clean and captioner-ecology datasets rather than applying one intelligibility filter to both.
