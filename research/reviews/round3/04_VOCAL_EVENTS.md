# Vocal events, whisper and noise response

Scoped full-text reviews; no reproduced experiments or assumed native-language transfer.

## 2008.09483 — Laughter Synthesis with Seq2seq and Transfer Learning

[Source](https://arxiv.org/abs/2008.09483). Read: laughter data/annotations, DCTTS adaptation in an extra range, waveform correction and perception results.

**Method and evidence.** Adapt a speech-trained DCTTS model to annotated voiced/unvoiced laughter sequences, then fine-tune on one speaker's amused speech and laughs. The laughter material has 112 examples totaling 202 seconds across three vowel contexts. MelGAN waveform correction improves MOS by about 0.78 over Griffin-Lim synthesis; 24 participants supply 1,696 ratings. Comments identify duration, repetitive pulse structure and waveform distortion as distinct naturalness failures.

**Limits and decision.** This is a small isolated-laughter study; integrated amused speech remains future work, and improvement partly comes from waveform rendering. It cannot establish arbitrary same-speaker laughter insertion. Treat laughter as structured speaker-owned vocal activity, with pulse/duration and speech-transition checks. Evaluate the final codec/vocoder output, not only a predicted event token. Prefer released native-compatible vocal capability or licensed same-speaker training examples over unrelated pasted laughs, and document coverage gaps explicitly.

## 1912.05289 — Voice Conversion for Whispered Speech Synthesis

[Source](https://arxiv.org/abs/1912.05289). Read: DSP/source-filter changes, aligned GMM/DNN conversion, held-out-speaker/corpus/gender tests and conclusion.

**Method and evidence.** Convert normal speech to whisper using either a source/filter DSP recipe or a small DNN trained on aligned normal/whisper pairs. Features include spectral shape as well as voicing; a gain reduction is insufficient. Multi-speaker learned conversion approaches vocoded whisper quality and exceeds the DSP baseline in the tested conditions. Excluding a target speaker has modest effects, but cross-corpus recording conditions and cross-gender training materially affect identity and quality.

**Limits and decision.** The data are English and partly proprietary, with manually selected cleaner wTIMIT speakers. Copy-synthesis is an upper bound imposed by the vocoder, not perfect natural whisper. Do not label quiet speech as whisper or force pitch extraction onto it. If a native whisper conversion branch is necessary, test it independently for lexical correctness and identity; retain the original signal for captioning. Do not assume a model trained on one voice range generalizes universally.

## 2212.01775 — Generative Conversion of Whisper to Normal Speech

[Source](https://arxiv.org/abs/2212.01775). Read: alignment/objective modifications, held-out-speaker setup, objective/subjective disagreement and discussion.

**Method and evidence.** Adapt MelGAN and VQ-VAE systems to reconstruct normal targets from whispered input, using DTW-aligned wTIMIT pairs. Ten speakers are held out. VQ-based models improve MCD by roughly 27–34% relative to DiscoGAN but produce substantially worse perceived speech. SC-MelGAN obtains positive intelligibility/naturalness/voicing CMOS, while the compared VQ-GAN variant scores -1.21/-1.62/-0.34. A favorable distortion metric can hide absent or unnatural voicing.

**Limits and decision.** Whisper-to-normal conversion is the opposite of preserving the PS's audible phonation. Aggressive silence trimming/alignment also changes timings. A restored view may help lexical evidence, but must never replace original audio for voice, ecology or event captioning. Keep resynthesis and conversion costs optional; use CER/native listening alongside acoustic metrics. The counterexample is particularly useful when validating any proposed objective proxy for expressive quality.

## 2303.07442 — Accessing Whispered Speech in ASMR

[Source](https://arxiv.org/abs/2303.07442). Read: WAD/CWAD pipeline, feature/window construction, synthetic noise setup, confusion results and data yield.

**Method and evidence.** RASTA-PLP features and a short LSTM detect whisper activity; human-assisted grouping identifies clean/noisy examples, then augmentation trains clean-whisper detection. At 0 dB in the synthetic test, the specialized RNN reaches F1 91.34% versus generic VAD 74.89%. Clean-whisper detection is harder, with reported accuracy 82.10%. The pipeline obtains about twenty hours from sixty downloaded ASMR hours.

**Limits and decision.** Genre, recording intimacy and noise-trigger confounds limit transfer. The reported 6.4% false-positive confusion cell should not be copied as a conventional class-conditional FPR without checking its denominator. Ordinary VAD can discard whispers, breaths and soft events that the captioner needs. Preserve full input duration and use activity scores as uncertain features rather than a hard preprocessing deletion gate. Acquire only eligible recordings; public availability alone does not settle reuse rights.

## 2502.16298 — voc2vec

[Source](https://arxiv.org/abs/2502.16298). Read: nonverbal corpus/architecture, pretraining initialization, downstream protocol and complete benchmark tables.

**Method and evidence.** Continue wav2vec2-style pretraining on 125.19 hours of nonverbal vocal data, then fine-tune task heads. Speech-initialized pretraining performs better than scratch or the compared general-audio initialization. On NonVerbal Vocalization, UAR reaches 0.872 versus speech-wav2vec2's 0.838; on VIVAE, 0.573 versus 0.365. Some improvements are small or uncertain, and the model does not win every metric on every corpus. Pretraining takes two A6000s for 10.6 days.

**Limits and decision.** Infant cries, imitations and brief isolated bursts are not timed native conversational vocalizations; small cross-validation datasets may share speaker/recording cues. Do not reproduce its pretraining within our budget. A released eligible model is an optional targeted teacher if shared-encoder heads demonstrably miss vocal events. Evaluate event detection on mixed real speech, retain timing/audibility masks, and distinguish a classified vocal burst from its communicative interpretation.

## 2507.09310 — Lombard Voice Conversion with Implicit/Explicit Conditioning

[Source](https://arxiv.org/abs/2507.09310). Read: CopyCat-derived conversion, spectral features/style loss, target-speaker evaluations, interactions and limitations.

**Method and evidence.** Preserve Lombard style during identity conversion using explicit F0/energy/spectral-tilt conditioning or a frozen classifier's style-reconstruction loss. Training uses 52 speakers; two target voices receive detailed evaluation. Energy and spectral tilt help consistently, but F0 effects vary with source/target voice conditions; some feature/loss combinations are harmful. The model does not modify duration, despite duration being part of real Lombard behavior.

**Limits and decision.** Constrained English Grid speech, two targets and a trained classifier do not prove complete noise-response generation. Explicit feature increases alone cannot guarantee an intelligibility benefit. For Coupling, link the background transition to a learned delivery response upstream of mixing and check voice energy/tilt/rate changes alongside content and identity. Compare true joint adaptation with gain-only mixing under matched scenes; use native listeners to verify the response rather than allowing the style-training classifier to certify itself.
