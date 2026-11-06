# Notes 04: tools that turn audio into checkable description claims, plus automatic quality metrics

Cluster: measurement tools and automatic quality metrics for the Track 2 captioner/generator loop (Hindi and Tamil, Vaani 16 kHz phone speech).
Compiled 2026-11-04. Sources: arXiv full text (PDF text pulled with pdftotext and searched for tables), GitHub READMEs and HF model cards.
`[unverified]` means I did not confirm the item in a primary source during this pass. Every number below comes from the paper or card cited.

Why this matters for us: the rubric pays for true items, subtracts contradicted or false ones, and counts a timed item only if it falls within ±250 ms of the true span. So for each claim type we need (a) a numeric, time-localised measurement, (b) a known error bar on our domain, and (c) a rule for staying silent when the tool is unsure.

The 13 rubric item types from the brief: Voice = Speaker, Source, Morphology, Pitch, Timing, Event. Recording = Channel, Space, Other sounds, Coupling. Intent = Addressee, Subtext, Change.

---

## A. Pitch / F0

### CREPE (ICASSP 2018), arXiv:1802.06182 / github.com/marl/crepe
- What it measures: frame-level F0 of monophonic audio, using a CNN that runs directly on the waveform (360 pitch bins, 20-cent resolution). It also returns a voicing confidence.
- Accuracy: the abstract claims it matches or beats pYIN. Independent numbers: on speech (PTDB), CREPE gets RPA 87.1 (PESTO TISMIR Table 2). On combined PTDB+MDB it gets RPA .9748 and Δ¢ 21.07 (PENN paper Table I). On MIR-1K polyphonic it gets 91.05 RPA (RMVPE Table 1).
- Speed/size: 22.2M params (full model; PESTO TISMIR). RTF 0.0093 on GPU and 0.357 on CPU (PENN paper).
- Licence + pip: MIT, `pip install crepe` (TF) [licence of the TF package unverified]. See torchcrepe below.
- **Takeaway:** a reasonable baseline, but on speech it is beaten by PENN, and it is the slowest option. Do not use as the primary tracker.

### torchcrepe — github.com/maxrmorrison/torchcrepe
- What it measures: a PyTorch port of CREPE ("full"/"tiny"), with Viterbi, weighted-argmax or argmax decoding and `return_periodicity=True`. The README suggests a periodicity threshold of about 0.21 for clean speech, plus median filtering. The example uses a 5 ms hop and fmin/fmax of 50–550 Hz.
- Accuracy: in the PENN paper, torchcrepe scores RPA .9103 and Δ¢ 59.40, which is worse than original CREPE (.9748).
- Speed: RTF 0.0199 GPU and 0.6435 CPU (PENN paper).
- Licence + pip: MIT, `pip install torchcrepe`.
- **Takeaway:** use it only as a cross-check tracker. Measured accuracy is below original CREPE and PENN.

### PENN / FCNF0++ — "Cross-domain Neural Pitch and Periodicity Estimation" (arXiv 2023, v3 2024), arXiv:2301.12258 / github.com/interactiveaudiolab/penn
- What it measures: frame-level F0 plus periodicity (a voicing confidence). The default hop is 10 ms. Decoders are argmax, pyin and viterbi. The pretrained FCNF0++ model was trained on MDB-stem-synth + PTDB (speech).
- Accuracy (Table I, PTDB+MDB combined): FCNF0++ RPA .9825, RCA .9852, Δ¢ 12.72, voicing F1 .9816. For comparison, CREPE scores .9748/21.07 and PYIN .8477/110.5. On speech alone (PTDB), PENN trained on both datasets reaches RPA 95.1 against CREPE's 87.1 (PESTO TISMIR Table 2).
- Speed/size: 8.9M params (PESTO TISMIR). The paper reports 11.2x real-time on an i9 CPU and 408x on an RTX 3090. PESTO TISMIR measured a CPU RTF of 0.1706.
- Licence + pip: MIT, `pip install penn`. The CLI's default `interp_unvoiced_at` is 0.1625. DataSpeech uses 0.065.
- **Takeaway:** **our primary F0 tool.** It is the best measured option on speech, it gives 10 ms frames with a periodicity mask, and it is what DataSpeech and ParaSpeechCaps used. Caveat: DataSpeech computes `pitch.std()` in Hz over all frames, including frames interpolated across unvoiced regions (checked in `dataspeech/gpu_enrichments/pitch.py`). We should compute statistics in semitones over voiced frames only (periodicity > threshold).

### PESTO (ISMIR 2023, Best Paper; TISMIR 2025), arXiv:2309.02265 and arXiv:2508.01488 / github.com/SonyCSLParis/pesto
- What it measures: self-supervised, transposition-equivariant F0 estimation on CQT/VQT input. Outputs are time, F0, confidence and activations. It supports streaming.
- Accuracy (TISMIR Table 2, PTDB speech): RPA 88.5–89.7 depending on training set, against CREPE 87.1 and PENN (MDB+PTDB) 95.1. On MIR-1K it scores 97.7.
- Speed/size: under 30k params in v1 (ISMIR abstract) and 130k in v2. Latency is under 10 ms. CPU RTF is 0.0354, against PENN's 0.1706 (TISMIR Table 3). The README reports a 2m51s file in about 13 s on an i7 laptop, against about 12 min for CREPE.
- Licence + pip: **LGPL-3.0**, `pip install pesto-pitch`. The shipped checkpoint was trained on MIR-1K (music).
- **Takeaway:** a fast CPU fallback and a second tracker for agreement checks. Its speech accuracy is about 5 RPA points below PENN.

### RMVPE (Interspeech 2023), arXiv:2306.15412 / github.com/Dream-High/RMVPE
- What it measures: vocal F0 taken directly from polyphonic or noisy mixtures (U-Net plus BiGRU). It is widely used in RVC voice-conversion stacks.
- Accuracy: MIR-1K polyphonic RPA 95.42 against CREPE 91.05. With 0 dB noise, averaged over white, pink, brown and pub noise, it scores RPA 93.60 against CREPE 81.16 and PYIN 52.98 (Table 2). On clean MIR-1K vocals it scores 97.27. There is no speech-dataset (PTDB) result.
- Speed/size: not reported.
- Licence: [unverified]. Repo only, no pip package.
- **Takeaway:** the best-documented robustness at 0 dB SNR. Use it as a cross-check on very noisy Vaani clips (Brouhaha SNR < 5 dB). Only state pitch claims when PENN and RMVPE agree within about 50 cents.

### Parselmouth / Praat (Journal of Phonetics 2018) — github.com/YannickJadoul/Parselmouth
- What it measures: Python bindings to Praat's C/C++ code, so outputs match Praat exactly. It covers pitch (AC/CC), intensity, formants, harmonicity (HNR), jitter/shimmer (PointProcess), spectral moments and PowerCepstrogram (CPP).
- Accuracy: see 2506.01129 below on how much toolkits disagree. In the DeepFry paper, a Praat-based creak baseline scored only F1 0.31–0.43 on full test sets.
- Speed: CPU DSP, fast [no figures].
- Licence + pip: **GPL-3.0+**, `pip install praat-parselmouth`. Cite Jadoul, Thompson & de Boer 2018, J. Phonetics 71:1–15.
- **Takeaway:** the standard source for intensity contours, HNR, jitter/shimmer, H1–H2 and CPP features. These are inputs to our Source and Coupling claims. Treat the absolute values as specific to this implementation, and always report them relative to the speaker's own baseline.

### Comparative Evaluation of Acoustic Feature Extraction Tools for Clinical Speech (arXiv 2025), arXiv:2506.01129
- What it measures: compares OpenSMILE, Praat (via Parselmouth) and librosa on the same clinical speech with matched parameters (F0 range 55–1000 Hz).
- Accuracy: F0 percentiles agree well across toolkits (r = 0.962–0.999). **F0 standard deviation and formants often agree poorly, sometimes with negative correlation.** MFCC1 correlates 0.98 between OpenSMILE and Praat but only 0.10–0.41 between OpenSMILE and librosa.
- Licence: n/a (paper).
- **Takeaway:** state pitch claims as **percentiles or medians and ranges in semitones**, not as SD. Pin one toolkit and one parameter set in the manifest, because "pitch variability" numbers do not transfer between tools.

---

## B. VAD, diarization, SNR and room acoustics

### Silero VAD — github.com/snakers4/silero-vad (no paper)
- What it measures: frame-level speech probability on 32 ms chunks (512 samples at 16 kHz). `get_speech_timestamps(return_seconds=True)` returns speech segments.
- Accuracy (wiki Quality-Metrics, multi-domain validation): ROC-AUC is 0.97 for v6, 0.96 for v5 and 0.73 for WebRTC. Speech accuracy per 31.25 ms chunk is 0.92 for v6. On MSDWild the ROC-AUC is 0.79. Accuracy on ESC-50 noise-only audio (correctly rejecting non-speech) is 0.87 for v6.
- Speed/size: a JIT model of about 2 MB, under 1 ms per 30+ ms chunk on one CPU thread. Supports 8 and 16 kHz.
- Licence + pip: MIT (the README badge alt-text says CC BY-NC; check the LICENSE file) [partly unverified], `pip install silero-vad`.
- **Takeaway:** the default source for pause and phrase boundaries in Timing and Morphology claims. Its 32 ms resolution is well inside the ±250 ms tolerance. Refine edges with forced alignment when a transcript exists.

### pyannote speaker-diarization-3.1 + powerset segmentation (Interspeech 2023), arXiv:2310.13025 / HF pyannote/speaker-diarization-3.1
- What it measures: who spoke when (RTTM output), including overlapped speech. The segmentation-3.0 model uses a powerset multi-class encoding (7 classes for up to 3 speakers in each 10 s chunk), so no detection threshold needs tuning.
- Accuracy (DER, no collar, overlap scored): AMI headset 18.8, DIHARD3 21.7, VoxConverse 11.3, MSDWild 25.3, AliMeeting 24.4, AVA-AVD 50.0.
- Speed: RTF not reported on the card.
- Licence + pip: MIT, `pip install pyannote.audio`. **HF access is gated**: you must accept the conditions and use a token. Input is 16 kHz mono.
- **Takeaway:** use for "single speaker vs a second voice from 4.1–6.0 s" claims and to filter multi-speaker clips out of training pools. Treat DER of about 20% as a reason to state only speaker counts, plus overlaps longer than 1 s.

### Brouhaha (ASRU 2023 [venue unverified]; arXiv 2022), arXiv:2210.13248 / github.com/marianne-m/brouhaha-vad, HF pyannote/brouhaha
- What it measures: one model that jointly predicts frame-level VAD, **speech-to-noise ratio (dB)** and **C50 (dB)**. Frames are 16 ms per the paper; the HF example timestamps show about 16.9 ms steps. It was trained on 1,250 h of synthetic LibriSpeech mixtures with SNR drawn from 0–30 dB. The output heads span −15 to 80 dB for SNR and −10 to 60 dB for C50.
- Accuracy: on synthetic test data, VAD F-score 93.7, **SNR MAE 2.3 dB** (an oracle-VAD heuristic gets 8.4) and C50 MAE 3.5 dB. On **real BUT ReverbDB rooms, C50 R² = .85 and MAE 1.1 dB**. On real child-centred audio, VAD F-score is 77.2, below pyannote's 80.8.
- Speed: a single small pyannote-style model [no figures].
- Licence + pip: the repo is MIT and the HF card says "openrail". Access is gated. Install by cloning the repo and running `pip install .`. DataSpeech uses `ylacombe/brouhaha-best`.
- **Takeaway:** **our main tool for SNR and reverb claims.** Frame-level SNR lets us localise noise bursts in time and measure Lombard coupling. Caveats: it was trained on English read speech, and its upper SNR range is extrapolated beyond the 0–30 dB training range. Re-calibrate it on Vaani with controlled noise and RIR transforms before turning values into words.

### Impulse Response Data Augmentation and DNNs for Blind Room Acoustic Parameter Estimation (Bryan, ICASSP 2020 [venue unverified]), arXiv:1909.03642
- What it measures: blind T60 and DRR from single-channel speech using a CNN on mel spectrograms. Training data comes from augmented real RIRs (T60 up to 1.5 s, DRR −6 to 18 dB).
- Accuracy (ACE eval): T60 bias −0.026 s, MSE 0.0261, ρ 0.92. DRR bias 0.81 dB, MSE 8.98 dB² (about 3 dB RMSE), ρ 0.71. Both beat the prior single-channel state of the art.
- Speed: RTF 0.0088 for T60.
- Licence: no public weights found [unverified].
- **Takeaway:** shows that we can train our own small T60/DRR regressor from synthetic RIR convolutions of clean Indic speech, which is the brief's "labels for free" idea. Expect about ±0.15 s T60 error. DRR is only good enough for coarse bins.

### A Universal Deep Room Acoustics Estimator (WASPAA 2021), arXiv:2109.14436
- What it measures: a CRNN that jointly estimates SNR, STI, T60, C50 and DRR blindly.
- Accuracy: the abstract claims state-of-the-art and robustness to non-stationary signals. No numbers on the abstract page [full text not read].
- Licence: no code link found.
- **Takeaway:** supports a joint multi-task design if we train our own Space/Channel head. Not usable off the shelf.

### blind_rt60 (PyPI `blind-rt60`), github.com/nuniz/blind_rt60
- What it measures: DSP blind RT60 (Ratnam et al. maximum-likelihood decay fitting). No neural weights.
- Accuracy: none reported [unverified].
- **Takeaway:** a zero-training sanity check alongside Brouhaha C50. Use only for coarse labels such as "dry / small room / reverberant hall".

---

## C. Voice quality and phonation (Source item)

### Data-driven detection and analysis of the patterns of creaky voice (Drugman, Kane, Gobl; Computer Speech & Language 2014), arXiv:2006.00518 / COVAREP
- What it measures: frame-level creak probability from the "KD" features (H2–H1, residual peak prominence) combined with Ishi's features, classified by an ANN. Tested on read and conversational speech in American English, Finnish and Japanese, 11 speakers.
- Accuracy: the All-ANN classifier gives the best F1; the worst speaker scored F1 0.57. Inter-rater agreement for creak patterns was Krippendorff's α 0.718. In DeepFry's re-test, "Kane et al." shows **very high precision and low recall** (ALLSSTAR: P 90.0, R 34.0, F1 49.4).
- Licence/install: MATLAB (COVAREP). The STEPP lab at BU reports a wrapper [unverified]. No pip package.
- **Takeaway:** the high precision suits a scoring rule that punishes false claims. If we can port it, a positive detection is a safe "creaky at 2.1–2.6 s" claim, and a negative is not evidence of no creak.

### DeepFry: Identifying Vocal Fry Using DNNs (Interspeech 2022), arXiv:2203.17019 / github.com/bronichern/DeepFry
- What it measures: frame-level (20 ms) creak detection from the raw waveform, with auxiliary voicing and pitch heads. HubertFry is the variant built on HuBERT features.
- Accuracy (all frames, F1): in-domain, DeepFry 71.6, HubertFry 69.0, Kane 41.5, Praat 42.7. On unseen data, HubertFry gets 73.6 (Prenuclear) and 68.5 (ALLSSTAR), against Kane's 52.3/49.4.
- Licence: [unverified]. Repo with pretrained models.
- **Takeaway:** **the best available time-localised creak detector.** It was trained only on American English, so validate it on about 100 hand-labelled Hindi/Tamil segments before using it. Phrase-final creak is also a Morphology cue.

### CPP / H1–H2 / HNR for breathiness (clinical literature; via Parselmouth or VoiceSauce)
- What it measures: cepstral peak prominence (periodicity), H1–H2 (glottal open quotient, a breathiness cue) and HNR.
- Accuracy: reported correlations of CPP with perceived breathiness are around r = −0.80 (sustained vowels, paralysis patients). H1–H2 shows only weak correlations in some studies. **Absolute CPP depends on the software: 35.0 dB with Hillenbrand's program against 20.5 dB with a MATLAB implementation on the same voices.** H1–H2 also differs strongly by sex and speaker. (From search snippets of PMC and ASHA papers; full texts not read [partly unverified].)
- **Takeaway:** breathiness and pressed-voice claims should be **relative and within-speaker**, e.g. "the voice turns breathier in the last phrase (CPP falls by X dB against the speaker's first 5 s)". Do not compare against a population norm. Low confidence on phone audio, where noise and codecs lower CPP.

### Falsetto / register detection (search-level only)
- Findings: the EGG-free classifiers I found (SVM on MFCC, cepstral and aperiodicity features) work on **sung sustained vowels**, sometimes about 95% for a single singer. I found no validated detector for connected speech, and KTH perceptual work shows register is not always classifiable.
- **Takeaway:** state falsetto only from a rule: a sudden upward F0 jump of 7 or more semitones, against the speaker's median, held for 300 ms or more, together with an H1–H2 rise. Otherwise do not claim it. This is a good item to supply through the generator's controlled transforms rather than through measurement.

### Vox-Profile (TMLR 2026 [venue inferred from the OpenReview/JMLR-style header, unverified]), arXiv:2505.14648 / github.com/tiantiaf0627/vox-profile-release
- What it measures: a benchmark and released classifiers for static traits (sex, age in 3 bins, broad and narrow accent, voice quality) and dynamic traits (categorical emotion, arousal/valence, fluency and disfluency type, expressiveness). Voice quality uses the ParaSpeechCaps tags: shrill, nasal, deep, singsong, pitchy, flowing, monotone, staccato, punctuated, enunciated, hesitant, crisp, slurred, lisp, stammering, silky, husky, raspy, guttural, **vocal-fry**, booming, authoritative, loud, hushed, soft.
- Accuracy (best single model, mostly Whisper-Large): sex 98.0% accuracy. Age (3 bins) 69.5% accuracy, F1 0.643. Broad accent F1 0.889, narrow accent F1 0.724. **Voice quality macro-F1 about 0.70–0.74.** Emotion macro-F1 about 0.39–0.42. Arousal and valence CCC about 0.59/0.67. Fluency accuracy about 80%. Expressiveness F1 up to 0.848.
- Speed/size: WavLM-Large or Whisper-Large-v3 backbones, about 300M+ params. Input is 16 kHz mono, **3–15 s** per clip.
- Licence + ids: **RAIL, no commercial use**. FluencyBank-derived models are CC BY-NC-SA 3.0. HF ids include `tiantiaf/wavlm-large-age-sex`, `tiantiaf/whisper-large-v3-voice-quality`, `tiantiaf/whisper-large-v3-msp-podcast-emotion`, `...-narrow-accent` and `...-speech-flow`. Install by cloning the repo and running `pip install -e .`.
- **Takeaway:** the most complete ready-made "voice adjective" tagger. However, all its accent classes are English-centric (it has a "South Asia" class, but no Hindi or Tamil dialect classes), and it was trained on English. Use it as a weak signal in an ensemble, and only state tags above a calibrated high-precision threshold. The follow-up Voxlect (dialects) may cover Indic varieties [unverified].

---

## D. Speaker traits, emotion and speaker verification

### Speech-based Age and Gender Prediction with Transformers (audEERING, ITG 2023 [venue unverified]), arXiv:2306.16962 / HF audeering/wav2vec2-large-robust-24-ft-age-gender
- What it measures: age as a regression output (0–1, roughly 0–100 years) and three-way gender (female, male, child).
- Accuracy: age MAE between 7.1 and 10.8 years and gender accuracy of at least 91.1% across test sets (CommonVoice, TIMIT, VoxCeleb2, aGender).
- Size: about 0.3B params (all 24 layers), plus an ONNX export. A 6-layer variant exists [unverified].
- Licence: **CC-BY-NC-SA-4.0**.
- **Takeaway:** use it for sex and for a child flag only. Age should be stated as a broad band ("adult", "older adult") because MAE is about 10 years. ParaSpeechCaps used this model for majority-vote gender tags. Prefer Vaani metadata gender when present.

### emotion2vec (ACL Findings 2024 [venue unverified]) and emotion2vec+, arXiv:2312.15185 / github.com/ddlBoJack/emotion2vec
- What it measures: an emotion-specialised SSL representation. Frame-level features are 50 Hz, T×768. The emotion2vec+ classifiers output 9 classes: angry, disgusted, fearful, happy, neutral, other, sad, surprised, unknown.
- Accuracy: on IEMOCAP with a linear probe, WA 71.79% (74.48% under the same-fold protocol), against WavLM-base+ at 67.98%. The paper claims generalisation across 10 languages. The emotion2vec+ READMEs give EmoBox results only as a chart.
- Size: base about 90M, large about 300M. emotion2vec+ large was trained on 42,526 h of pseudo-labelled data.
- Licence + pip: MIT badge. `pip install -U funasr`, HF `emotion2vec/emotion2vec_plus_large`.
- **Takeaway:** treat it as a feature source, with sliding-window class probabilities for Change claims ("shifts from neutral to amused around 12 s"). Given that the best SER macro-F1 is about 0.4 (Vox-Profile), **only assert emotion when the window probability is very high and corroborated by acoustics** (laughter, F0 rise). The brief's warning applies: "shouting != anger".

### ECAPA-TDNN (Interspeech 2020), arXiv:2005.07143 / HF speechbrain/spkrec-ecapa-voxceleb
- What it measures: a speaker embedding (192-d [unverified]) used for verification by cosine scoring.
- Accuracy: on VoxCeleb1-O, EER 0.87% for C=1024 (14.7M params) and 1.01% for C=512 (6.2M params). The SpeechBrain card reports EER 0.80% on Vox1-test (cleaned).
- Licence + pip: Apache-2.0, `pip install speechbrain`. **SpeechBrain's `verify_batch` uses a default threshold of 0.25** (checked in `speechbrain/inference/speaker.py`).
- **Takeaway:** a likely candidate for the brief's "fixed speaker-verification model, standard threshold". Use it to measure distinct-speaker counts across our 10 generator samples (aim for most pairwise cosines below 0.25), and in the captioner for "same voice throughout" claims.

### WavLM (IEEE JSTSP 2022), arXiv:2110.13900 / HF microsoft/wavlm-base-plus-sv
- What it measures: an SSL backbone. Speaker verification uses an x-vector head on WavLM (the HF -sv model).
- Accuracy: WavLM Large reaches EER 0.383% / 0.480% / 0.986% on Vox1-O, E and H, beating ECAPA-TDNN.
- Licence: points to the UniSpeech LICENSE [unverified, likely MIT]. **The HF card recommends a cosine threshold of 0.86 and notes it is dataset-dependent.**
- **Takeaway:** the other likely "standard threshold" model. We should report generator speaker diversity under **both** ECAPA at 0.25 and WavLM-SV at 0.86, because which one Rime uses is unknown.

---

## E. Sound events with timestamps (Event and Other sounds items)

### PANNs (IEEE/ACM TASLP 2020), arXiv:1912.10211 / github.com/qiuqiangkong/panns_inference
- What it measures: 527-class AudioSet tagging (CNN14). The `SoundEventDetection` class returns `framewise_output`, which gives frame-level class probabilities. Classes include Laughter, Cough, Breathing, Music, Vehicle, Dog and Speech.
- Accuracy: AudioSet mAP 0.439 for clip-level tagging. The shipped checkpoint is `Cnn14_mAP=0.431.pth`. No strong-label SED metrics in the paper.
- Speed: 32 kHz input. CNN14 has about 80M params [unverified].
- Licence + pip: MIT, `pip install panns-inference`.
- **Takeaway:** **the only off-the-shelf 527-class model with frame-level output.** Use it to propose onset and offset times for background events (dog bark at 4.1–4.6 s, traffic throughout). Vaani clips are 16 kHz, so resampling to 32 kHz leaves the top band empty. Expect some domain loss.

### AST: Audio Spectrogram Transformer (Interspeech 2021), arXiv:2104.01778 / github.com/YuanGongND/ast
- What it measures: clip-level AudioSet tagging. Input is 10.24 s (1024 frames).
- Accuracy: AudioSet mAP 0.485 (ensemble) and 0.459 (single model with weight averaging). ESC-50 95.6%.
- Licence: BSD-3-Clause. HF transformers id `MIT/ast-finetuned-audioset-10-10-0.4593` [unverified].
- **Takeaway:** clip-level only, so it needs a sliding window (1 s windows, 0.25 s hop) to localise events. Use it as a second opinion on PANNs labels.

### BEATs (ICML 2023 [venue unverified]), arXiv:2212.09058 / microsoft/unilm
- What it measures: an audio SSL model with an acoustic tokenizer. Fine-tuned for AudioSet tagging.
- Accuracy: AS-2M mAP 48.6 (iter3+, 90M params) and AS-20K 38.9. A self-distilled ensemble reaches 50.6.
- Licence: unilm repo, MIT [unverified for the checkpoints].
- **Takeaway:** a strong clip-level tagger and a candidate encoder for a custom frame-level event head trained on spliced events (laughs, coughs, door slams at known times).

### EAT: Efficient Audio Transformer (IJCAI 2024), arXiv:2401.03497 / github.com/cwx-worst-one/EAT
- What it measures: an SSL audio transformer whose pre-training is about 15x faster than prior methods. Fine-tuned AudioSet taggers are available.
- Accuracy: EAT-base AS-2M mAP 48.6–48.9, AS-20K 40.2–41.3. EAT-large AS-2M 49.5.
- Licence + ids: MIT. HF `worstchan/EAT-base_epoch30_finetune_AS2M` and `worstchan/EAT-large_epoch20_finetune_AS2M`.
- **Takeaway:** like BEATs, clip-level. It is efficient, so it suits training a frame-level event head on our synthetic splices.

### LAION-CLAP (ICASSP 2023), arXiv:2211.06687 / github.com/LAION-AI/CLAP
- What it measures: a joint audio-text embedding used for zero-shot classification with arbitrary text labels.
- Accuracy: zero-shot ESC-50 89.1–91.0 (K2C augmentation). Retrieval R@1 on AudioCaps is about 35–36 (text-to-audio).
- Licence + pip: **CC0-1.0**, `pip install laion-clap`. Checkpoints are `630k-audioset-best.pt` and `music_speech_audioset_epoch_15_esc_89.98.pt`. Clip-level only.
- **Takeaway:** use it as an open-vocabulary verifier for unusual "other sounds" ("pressure cooker whistle", "temple bell"), which matters for Indian-domain sounds that AudioSet labels poorly. Use only a windowed score with a high margin over a "silence/speech only" prompt. Also usable as a reward signal for fantastical generator prompts. The Microsoft CLAP paper (arXiv:2206.04769) was downloaded but not read.

### Robust Laughter Detection in Noisy Environments (Interspeech 2021) — github.com/jrgillick/laughter-detection
- What it measures: frame-level laughter probability. `segment_laughter.py` outputs (start, end) segments in seconds, with a default threshold of 0.5 and min_length 0.2 s. It also adds precise laughter annotations to AudioSet.
- Accuracy: the paper shows clean-condition detectors degrading in noise and the new model being more robust. A third-party report gives F1 0.75 on clean and 0.608 on noisy audio [secondary, unverified].
- Licence: MIT. Trained on Switchboard plus AudioSet. Install by cloning the repo. Old dependency pins (PyTorch 1.3).
- **Takeaway:** **the purpose-built laughter timestamp tool.** Laughter is the brief's own Event example ("laugh at 3.2–3.9 s"). Combine it with PANNs Laughter frames, and require both to agree before claiming.

---

## F. Alignment and ASR for Hindi/Tamil (Timing and Morphology support)

### MMS: Scaling Speech Technology to 1,000+ Languages (JMLR 2024 [venue unverified]), arXiv:2305.13516 / torchaudio `MMS_FA`
- What it measures: CTC forced alignment with an alignment model covering 1,130 languages and 31K h (paper §3.1). The paper gives an efficient GPU forced-alignment implementation with O(L) memory and a ⟨∗⟩ star token that absorbs untranscribed audio. The torchaudio `MMS_FA` bundle (23k h, 1,100+ languages) needs **uroman-romanised** text.
- Accuracy: no Indic timing-error numbers found [unverified].
- Licence: MMS weights CC-BY-NC 4.0 [unverified]. The torchaudio tutorial notes the forced-alignment APIs are deprecated in torchaudio 2.8 and removed in 2.9, so pin torchaudio ≤2.8.
- **Takeaway:** word and character timestamps for Hindi/Tamil after romanising Devanagari/Tamil script. The ⟨∗⟩ token suits Vaani's *partial* transcripts. These timestamps drive speaking-rate, pause and phrase-onset claims to well under ±250 ms.

### IndicConformer 600M multilingual (AI4Bharat) — HF ai4bharat/indic-conformer-600m-multilingual
- What it measures: ASR for 22 Indian languages, including Hindi and Tamil, with a hybrid CTC + RNNT decoder.
- Accuracy: Hindi WER 13.2 on the Vaani-Benchmark-V1.0. This is **the brief's intelligibility judge** (CER).
- Licence: MIT, gated. Loaded with `trust_remote_code`. The card does not say whether CTC logits or timestamps are exposed [unverified]. The card now recommends "Indic-Transcribe".
- **Takeaway:** (1) fill in missing transcripts so speaking rate can be computed; (2) its CTC posteriors may give an Indic-native alignment as a cross-check on MMS; (3) run it on generator outputs every round to track CER.

### Praat syllable-nuclei speaking rate (de Jong & Wempe, Behavior Research Methods 2009), doi:10.3758/BRM.41.2.385
- What it measures: syllable nuclei from intensity peaks that have dips on both sides and are voiced. Outputs are speech rate (syllables / total time) and articulation rate (syllables / phonation time), plus pauses. No transcript needed.
- Accuracy: high correlation with human syllable counts on two Dutch corpora [exact r not read].
- **Takeaway:** a transcript-free rate estimate, usable on any clip and portable to Parselmouth. Cross-check it against an alignment-based rate (MMS-FA syllables or phones per second). Report articulation rate in syll/s, e.g. "about 5.5 syll/s, speeding to 7 in the final phrase".

---

## G. MOS and quality predictors (Channel claims and generator QA)

### UTMOS (Interspeech 2022), arXiv:2204.02152
- What it measures: naturalness MOS for TTS. An SSL (wav2vec2) strong learner is ensembled with weak learners.
- Accuracy: VoiceMOS 2022 main track, utterance-level SRCC 0.897 (rank 1) and system-level SRCC 0.936.
- Licence/pip: [unverified]. Commonly used through the `SpeechMOS` torch.hub [unverified].
- **Takeaway:** a cheap naturalness proxy for generator ablations. On zoomed-in high-quality systems (VMC 2024) its utterance-level SRCC falls to 0.41, so it cannot rank good systems.

### UTMOSv2: T05 system for VoiceMOS 2024 (SLT 2024), arXiv:2409.09305 / github.com/sarulab-speech/UTMOSv2
- What it measures: MOS from an EfficientNetV2 spectrogram branch fused with a wav2vec2 SSL branch.
- Accuracy: VMC 2024 Track 1 (zoomed-in 25%), utterance-level SRCC 0.613 and system-level SRCC 0.919, against UTMOS's 0.411/0.615. First place on 7 of 16 metrics and second on the other 9.
- Licence: MIT (per GitHub metadata) [unverified in LICENSE].
- **Takeaway:** **our main naturalness proxy for the CMOS criterion.** Audiobox Aesthetics flags data leakage on BVCC, so its scores there are inflated.

### The VoiceMOS Challenge 2024 (SLT 2024), arXiv:2409.07001
- What it measures: a challenge summary with three tracks (zoomed-in TTS, singing and VC, noisy and enhanced speech).
- Findings: many teams beat the baselines. Retrieval-based methods and non-SSL features (spectrograms, **pitch histograms**) helped. General-purpose MOS prediction is still open.
- **Takeaway:** do not trust a single MOS predictor across domains. Report UTMOSv2 together with Audiobox PQ, and validate against our own small CMOS listening test.

### DNSMOS and DNSMOS P.835 (ICASSP 2021 / ICASSP 2022), arXiv:2010.15258 and arXiv:2110.01763 / github.com/microsoft/DNS-Challenge (DNSMOS/)
- What it measures: P.808 overall MOS, and P.835 **SIG** (speech distortion), **BAK** (background noise intrusiveness) and **OVRL**. Input is a 9 s, 16 kHz log-power spectrogram. Also a personalised mode (`-p`) that penalises interfering talkers.
- Accuracy (P.835): model-level PCC 0.94 (SIG), 0.98 (BAK), 0.98 (OVRL). **Clip-level PCC is only 0.71, 0.83 and 0.82.** Audiobox reports DNSMOS utterance-level PCC of 0.612 on VMC22 TTS.
- Licence: repo licence not stated on the page [unverified]. Run with `dnsmos_local.py` (ONNX).
- **Takeaway:** BAK is a useful second noise signal next to Brouhaha SNR, and SIG flags codec or clipping distortion. Use them at clip level for coarse bins only.

### NISQA (Interspeech 2021), arXiv:2104.09494 / github.com/gabrielmittag/NISQA
- What it measures: overall MOS for transmitted speech, plus **Noisiness, Coloration, Discontinuity and Loudness**. Built from CNN, self-attention and attention pooling, and designed for narrowband through fullband audio. Also NISQA-TTS for naturalness.
- Accuracy: per-condition PCC is about 0.77–0.98 across many telephony test sets, e.g. NISQA_TEST_P501 r 0.95 and LIVETALK real calls.
- Licence: code MIT. **Weights CC BY-NC-SA 4.0.** Installed through a conda env.
- **Takeaway:** **the best fit for Channel claims on phone speech.** Discontinuity points to packet loss or dropouts and Coloration to codec or band-limiting. Map high or low dimension scores to phrases ("choppy", "muffled") only at the extremes.

### Meta Audiobox Aesthetics (arXiv 2025), arXiv:2502.05139 / github.com/facebookresearch/audiobox-aesthetics
- What it measures: four axes: Production Quality (PQ), Production Complexity (PC), Content Enjoyment (CE) and Content Usefulness (CU), for speech, music and sound. A WavLM-style 12-layer encoder.
- Accuracy (VMC22 speech, utterance-level PCC / system-level SRCC): main track PQ 0.689/0.752 and CE 0.775/0.813. On OOD (Chinese), PQ 0.651/0.813 beats UTMOSv2's 0.634/0.707 and DNSMOS's 0.459/0.615.
- Licence + pip: weights CC-BY-4.0, `pip install audiobox-aesthetics`, HF `facebook/audiobox-aesthetics`.
- **Takeaway:** **the most permissive licence and the best cross-language robustness of the MOS family.** Use PQ to filter training audio for the generator and as a generator reward term. PC tracks "how many sources are present", which is a weak cue for Other sounds.

---

## H. Turning measurements into words (DataSpeech and ParaSpeechCaps precedent)

### Natural language guidance of high-fidelity TTS with synthetic annotations (Lyth & King, arXiv 2024; Parler-TTS), arXiv:2402.01912
- Method: annotated **45k h** of MLS English plus LibriTTS-R. Gender comes from metadata. Accent comes from a linear classifier on EdAcc, VCTK and VoxPopuli (53 accents). **SNR and C50 come from Brouhaha. Pitch comes from PENN** (speaker-level mean relative to gender, and utterance-level std as a "monotone vs animated" proxy). **Speaking rate = phonemes (g2p) / duration** after trimming silence. Each continuous variable is cut into **7 bins**, each named with a short phrase ("very fast", "quite fast", "fairly slowly"). If both SNR and C50 fall in the extreme bin, the clip gets "very good / very bad recording". An LLM turns the keywords into sentences.
- Result: the generated speech followed every attribute except C50 reasonably well.
- **Takeaway:** the template we should copy, but with Rime's needs in mind: Parler's bins are **relative to the dataset distribution**. Rime grades against what a listener hears and wants **numbers and times**, so we should state the measured value as well as the bin word ("median F0 about 210 Hz, high for a female voice").

### DataSpeech (Hugging Face), github.com/huggingface/dataspeech
- Method: `main.py` computes `utterance_pitch_mean/std` (PENN), `snr`, `c50` and `speech_duration` (Brouhaha, averaged over VAD frames), `speaking_rate` (phonemes/s), and optional `pesq`/`si-sdr` (torchaudio SQUIM). `scripts/metadata_to_text.py` applies bins. An LLM (Mistral-7B-Instruct-v0.2 or Llama-3-8B-Instruct) writes the descriptions.
- **Actual v02 bin edges** (`examples/tags_to_annotations/v02_bin_edges.json`):
  - Speaking rate (phonemes/s): 0, 3.83, 7.65, 11.48, 15.30, 19.13, 22.95, 26.78. Labels run from "very slowly" to "very fast".
  - Noise (Brouhaha SNR): 17.1, 25.4, 33.7, 41.9, 50.2, 58.5, 66.8, 75.0. Labels run from "very noisy" to "very clean". **Most of these edges sit above Brouhaha's 0–30 dB training range, so they are distribution-relative, not physical dB.**
  - Reverberation (C50): 10, 35, 45, 55, 59, 60. Labels run from "very distant-sounding" to "very close-sounding".
  - Pitch std: 0, 20.4, 40.8, 70, 90, 142.7 (Hz). Labels run from "very monotone" to "very expressive and animated".
  - Male pitch bins: 64.7 to 183.7 Hz. Female pitch bins: 120.2 to 270.3 Hz. Labels run from "very low-pitch" to "very high-pitch".
  - PESQ: 1, 1.7, 2.4, 3.1, 3.6, 4, 4.5. SI-SDR: −17.8 to 34.4.
- Licence: MIT.
- **Takeaway:** ready-to-reuse code. The concrete fixes for us are: semitone and voiced-only statistics; recalibrating the SNR edges against our own controlled-SNR mixtures; and adding time-localised segments rather than only clip means.

### ParaSpeechCaps: Scaling Rich Style-Prompted TTS Datasets (Diwan et al., 2025; EMNLP 2025 [venue unverified]), arXiv:2503.04713
- Method: 59 style tags (33 intrinsic, 26 situational). There are 282 h of human-labelled data (PSC-Base) and **2,427 h auto-annotated** (PSC-Scaled). Intrinsic tags are propagated to Emilia speakers through VoxSim perceptual speaker similarity (threshold set to a similarity of 5/6). Situational tags use a cascade of **expressivity filtering** (dominance/arousal from a classifier), **semantic matching** of transcripts (SFR-Embedding-Mistral) and **acoustic matching** (Gemini 1.5 Flash rates tag adherence on a 5-point Likert scale). Basic tags go through DataSpeech, with gender-dependent pitch thresholds: **low below 115.7 Hz for male / 141.6 Hz for female, high above 149.7 / 184.5 Hz.** Speed is **slow below 11.5 phonemes/s and fast above 19.1**. Noise uses Parler's 7 SNR bins. Gender comes from the audEERING classifier by majority over up to 50 utterances.
- Accuracy: human tag recall is 50.3% (intrinsic) and 71.3% (situational) for PSC-Scaled, against 48.7% and 68.1% for the human PSC-Base. **Even human tags are confirmed by other listeners only about half the time for intrinsic qualities.** Fine-tuning Parler-TTS on it gives +7.9% Consistency MOS and +15.5% Naturalness MOS.
- **Takeaway:** (1) rich timbre adjectives (husky, nasal, shrill) are **inherently low-agreement**, which is dangerous under Rime's false-item penalty; (2) their pipeline used a closed model (Gemini), which our final models may not do, though Qwen3-Omni could play that role; (3) copy the gender-relative pitch thresholds as a sanity prior, then re-estimate them on Vaani Hindi/Tamil.

---

## I. Channel and Coupling (Lombard), where tools are thin

### Bandwidth and codec detection (search-level)
- Findings: 3GPP EVS (TS 26.445 §5.1.6) has a bandwidth detector that compares band energies to thresholds, i.e. simple DSP. Academic codec identification (CNN/LSTM on spectrograms; AMR-NB/WB double-compression detection at about 75–99%) exists, but I found **no open pretrained codec-ID model**.
- **Takeaway:** compute effective bandwidth ourselves. Take the highest frequency where the long-term average spectrum stays above the noise floor by more than X dB, which separates narrowband (about 3.4–4 kHz cutoff) from wideband (about 7–8 kHz) inside the 16 kHz container. Add clipping (fraction of samples near full scale) and DC/hum (50 Hz mains, which matters in India). For codec family, train a small classifier on Vaani-like clean speech passed through ffmpeg AMR-NB, AMR-WB, Opus at low bitrates, GSM and MP3. That gives labels for free.

### Lombard effect acoustics (Korn 1954 via PMC; Ngo et al. J. Signal Processing 2017; Bauer et al. Speech Prosody 2026)
- Findings: vocal level rises about **0.38 dB per 1 dB** of noise above 55 dB SPL (Korn 1954, as cited). With rising noise, vowels lengthen, F0 rises and spectral tilt flattens (Ngo 2017, 0–90 dB pink noise; an abrupt F0 change near 84 dB). Bauer et al. 2026, "Detection of Lombard Speech Using Different Model Architectures and Speech Features", treats detection as regression of the noise level from clean speech. CNNs on WavLM features generalise best, and pitch and spectral tilt features help. No code or numbers on the abstract page.
- **Takeaway:** Coupling cannot be detected off the shelf. Build it as a **derived claim**: windowed Brouhaha SNR (or PANNs noise-event activity) over time, against windowed intensity, F0 median (PENN) and spectral tilt (Parselmouth). State "voice gets louder and higher (≈+3 st) when the traffic noise rises at 8 s" only when the within-clip correlation is strong. The generator side can be trained with synthetic Lombard pairs if a Lombard corpus is available [corpus availability not checked].

---

## Synthesis

**Items read: 42** (36 with a primary source read: paper full text, README or model card; 6 at search or abstract level: blind_rt60, Universal Room Estimator, CPP/H1-H2 validity, falsetto, bandwidth/codec, Lombard).

| Rubric item | Recommended tool(s) | Output (time-localised?) | Confidence |
|---|---|---|---|
| Speaker | Vaani metadata; audEERING age-gender; Vox-Profile sex/age; pyannote 3.1 (speaker count) | sex prob, age band, n speakers + segments | Sex high (~97–98% acc); age low (MAE 7–11 y); accent/dialect: none for Indic, use metadata |
| Source (phonation) | DeepFry / Kane-Drugman creak (20 ms); Parselmouth CPP, H1–H2, HNR within-speaker; Vox-Profile voice quality | creak spans; relative breathiness | Creak medium (F1 ~0.6–0.7; Kane high-P/low-R); breathy/strained/falsetto low |
| Morphology | Silero VAD + MMS-FA boundaries; PENN slope over last 300 ms; creak at phrase end | phrase onset/offset times, final rise/fall in st | Medium |
| Pitch | **PENN** (10 ms, periodicity) + RMVPE in noise; PESTO fallback | median/p10–p90 F0 in Hz and semitones, contour events | High (RPA ~0.95–0.98 on speech) |
| Timing | MMS-FA (uroman) / IndicConformer; de Jong-Wempe nuclei; Silero pauses | syll/s, pause ms, word spans | Medium-high |
| Event | Gillick laughter + PANNs framewise; CLAP/AST windowed check | event label + start–end s | Medium (laughter F1 ~0.6–0.75 [secondary]) |
| Channel | NISQA dims; DNSMOS SIG; DSP bandwidth/clipping; synthetic-trained codec classifier | NB/WB cutoff Hz, distortion type | Bandwidth high; codec low-medium |
| Space | Brouhaha C50 (real MAE 1.1 dB); own T60 regressor (Bryan-style, synthetic RIRs) | C50 dB, T60 s | Medium |
| Other sounds | PANNs framewise; Brouhaha frame SNR; DNSMOS BAK; CLAP open-vocabulary | class + spans; SNR dB | Medium (SNR MAE 2.3 dB synthetic) |
| Coupling (Lombard) | Derived: windowed SNR against intensity, F0 and spectral tilt correlation | "louder/higher when noise rises at t" | Low |
| Addressee | No acoustic tool; ASR transcript + LLM; Vaani prompt context | text inference | Low, so abstain or state generically |
| Subtext | emotion2vec+, Vox-Profile arousal/valence (CCC ~0.6) + acoustic corroboration | windowed class probs | Low (SER macro-F1 ~0.4) |
| Change | Change-points on windowed F0, energy, rate, SNR, emotion probabilities | "from X to Y at t s" | Medium for acoustic change, low for intent |

**Three biggest risks**
1. **Domain shift.** Almost every tool was trained on English, clean or Western audio: PENN on PTDB, Brouhaha on LibriSpeech, creak models on American English, Vox-Profile on English accents. Vaani is spontaneous 16 kHz phone speech in Hindi and Tamil. DataSpeech's SNR bins (17–75 dB) already sit outside Brouhaha's 0–30 dB training range. We must recalibrate with controlled transforms (known SNR, RIR, pitch shift, splices) on Vaani before turning numbers into words.
2. **Low-accuracy perceptual labels meet a penalty for false claims.** Voice-quality F1 is about 0.70, SER about 0.4, age about 65%, and even humans agree on only about 50% of ParaSpeechCaps intrinsic tags. The captioner needs per-claim confidence gating that favours abstaining over guessing. Hedging between alternatives earns no credit.
3. **Licences and gating limit what we can redistribute.** CC-BY-NC-SA applies to audEERING and the NISQA weights, RAIL non-commercial to Vox-Profile, GPL to Parselmouth, LGPL to PESTO, and CC-BY-NC to MMS [unverified]. pyannote and Brouhaha need gated HF tokens. Torchaudio removes the forced-alignment APIs in 2.9. Pin versions and record the labeler of every example in the manifest.
