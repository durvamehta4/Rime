# Notes 06: Controllable acoustic scenes, timed audio events, non-verbal vocalisations, audio editing

Cluster owner: lit-review subagent. Written for the Track 2 brief (Hindi/Tamil captioner + generator loop, Rime PS).
Date of reading: 2026-11-04. Sources are arXiv abstract/HTML pages, GitHub READMEs, dataset cards and one paper PDF read in full text (Fugatto, Ko et al. 2017).
Anything I did not confirm from a primary page is marked **[unverified]**. Licences are for the artefact named; per-clip licences can differ.

Legend: NC = non-commercial. "Research OK" means a licence that permits non-commercial research use. Every training example still needs its licence in the manifest.

---

## A. Room acoustics simulation and real RIR data

### Pyroomacoustics: A Python package for audio room simulations and array processing algorithms (ICASSP 2018) — arXiv:1710.04196 / github.com/LCAV/pyroomacoustics
- Key idea: Object-oriented Python front end with a fast C/C++ image-source model (ISM) for 2D/3D polyhedral rooms (convex and non-convex). The README also lists a C++ ray tracer. Includes beamforming, DOA and adaptive-filtering reference code.
- Key numbers: No speed benchmarks in the abstract. Without a compiler the package falls back to pure Python, which the README calls "much slower".
- Licence: MIT (code). Paper CC BY 4.0.
- **Takeaway for our Track 2 design:** Use it as the default CPU room simulator. Every room parameter (dimensions, absorption, source/mic positions) is known, so we can compute the labels (T60, DRR, C50) directly from the generated RIR rather than from the requested target. ISM alone gives weak late reverb (see Ko et al. 2017 and TS-RIR), so use the ISM + ray-tracing hybrid or mix in real RIRs. I did not see an inverse-Sabine or material database on the README page **[unverified that these exist in the current version]**.

### gpuRIR: A Python library for room impulse response simulation with GPU acceleration (Multimedia Tools and Applications 2020) — arXiv:1810.11359 / github.com/DavidDiazGuerra/gpuRIR
- Key idea: Parallelises ISM over RIRs and over image sources on CUDA, with mixed precision and a sinc lookup table. `Tdiff` switches from ISM to a diffuse-tail model, so late reverb is cheap. `beta_SabineEstimation` gives wall reflection coefficients for a target T60.
- Key numbers: Claims "about 100 times faster than other state of the art CPU libraries" (abstract; no table read).
- Licence: **AGPL-3.0**. Research use is fine; it is copyleft if we ship code that links it.
- **Takeaway for our Track 2 design:** Worth it only if we render about 10^5 or more RIRs on the 4×L4. Mixed precision needs a Pascal or newer GPU, which the L4 (Ada) satisfies. Keep it optional in the submitted code because of AGPL. Pyroomacoustics (MIT) is the safe default.

### A Study on Data Augmentation of Reverberant Speech for Robust Speech Recognition (ICASSP 2017), Ko, Peddinti, Povey, Seltzer, Khudanpur — no arXiv; danielpovey.com/files/2017_icassp_reverberation.pdf (read full text)
- Key idea: A probabilistic far-field simulator: sample room → RIR → point-source noises (foreground at a sampled time, or background looped over the whole utterance) plus the room's isotropic noise, at an SNR drawn from {20, 15, 10, 5, 0} dB. Simulated RIRs: rooms 1–10 m (small), 10–30 m (medium) or 30–50 m (large); height 2–5 m; absorption U[0.2, 0.8] on all walls; 200 rooms × 100 RIRs per set. Point-source noises are the 843 MUSAN Freesound noises.
- Key numbers: Simulated RIRs lack "rich late-reverberations" compared with real ones. On ASpIRE dev (TDNN LF-MMI), WER is 40.9 (clean only), 27.8 (real RIR + isotropic) and 27.0 (sim RIR + point-source). BLSTM: 25.7 → 24.6. The gap between simulated and real RIRs closes once point-source noises are added.
- Licence: The resulting data release is OpenSLR 26/28 (Apache 2.0, see next item).
- **Takeaway for our Track 2 design:** This is the template for our "ecology renderer": sampled room, foreground events at a known time, background bed, sampled SNR. Copy its separation of point-source foreground events (timed, which suits our "Event"/"Other sounds" axes) from isotropic background. Simulated RIRs are acceptable if mixed with real ones and with point-source events.

### OpenSLR 26 (Simulated RIR database) and OpenSLR 28 (RIRS_NOISES) — openslr.org/26, openslr.org/28
- Key idea: SLR26 holds the simulated RIRs from Ko et al., at 8 kHz (128 MB) and 16 kHz (178 MB). SLR28 (rirs_noises.zip, about 1.3 GB) holds real RIRs and isotropic noises from RWCP, REVERB 2014 and the Aachen AIR database, the simulated RIRs, and MUSAN point-source noises. All files are 16 kHz, 16-bit.
- Key numbers: See Ko et al. above.
- Licence: **Apache 2.0** (both).
- **Takeaway for our Track 2 design:** These are first-choice RIRs because the licence is permissive and the format is ready to use. Because they are 16 kHz only, the generator's ≥24 kHz training targets need either RIRs at higher rates (MIT survey, BUT ReverbDB, our own pyroomacoustics renders at 24/48 kHz) or band-limiting labelled as such.

### Building and Evaluation of a Real Room Impulse Response Dataset, BUT ReverbDB (IEEE JSTSP 2019) — arXiv:1811.06795 / speech.fit.vut.cz
- Key idea: Real RIRs, background noise and retransmitted speech (LibriSpeech test-clean, HUB5, part of NIST SRE 2010). The paper also works as a recipe for measuring your own RIRs.
- Key numbers: The database page lists 9 rooms (the paper says 8 and "growing") and 31 microphones per room. Summing the page's per-room counts gives about 4.7k RIRs; some counts are approximate. The RIR-only archive is 8.7 GB. ASR finding: a few real RIRs matched to the target environment do about as well as many simulated RIRs, and combining real and simulated RIRs is best.
- Licence: **CC BY 4.0**.
- **Takeaway for our Track 2 design:** This is the best permissive real-RIR set with many mic positions per room. The positions let us render "same room, different distance" contrastive pairs, which suit relative statements ("more distant than before"). Its retransmitted LibriSpeech is a real replayed-speech test of renderer realism.

### Statistics of natural reverberation enable perceptual separation of sound and space, MIT IR Survey (PNAS 2016), Traer & McDermott — mcdermottlab.mit.edu/Reverb/IR_Survey.html (no arXiv)
- Key idea: 271 IRs measured in the everyday places (from 301 unique locations) that 7 volunteers reported when texted at random times over two weeks, so the set samples the reverb people actually experience.
- Key numbers: 271 IRs. The paper's main result is that real-world reverb decay is frequency-dependent in a regular way that listeners rely on.
- Licence: **CC BY 4.0**, per the search summary of the lab page. The download URL and SHA1 come from a third-party mirror listing, so check them on download.
- **Takeaway for our Track 2 design:** This is the most ecologically valid prior over spaces, which matters because the rubric describes what a careful listener hears. Use it to set the distribution of room types and T60 (most everyday spaces are small or medium rooms) and as a real-RIR pool. Hindi/Tamil phone speech recorded at home or outdoors fits this "everyday space" prior better than lecture-hall corpora.

### ACE Challenge corpus (WASPAA 2015 / IEEE TASLP 2016), Eaton, Gaubitch, Moore, Naylor — arXiv:1606.03365 (results report) / Zenodo 6257551
- Key idea: RIRs and matched ambient, fan and babble noise from 7 rooms at Imperial College, recorded with several mic configurations from single-channel to a 32-channel spherical array. The corpus was built for blind T60 and DRR estimation.
- Key numbers: The 32-channel set is about 14.2 GB (search summary). The arXiv page is only a results report, with no numbers in the abstract.
- Licence: **CC BY-ND 4.0** per IEEE DataPort and the Imperial page; registration may be needed. **[licence wording not read on the primary page]**.
- **Takeaway for our Track 2 design:** It has ground-truth T60/DRR and noise recorded in the same room, so it is good for **validating** our blind room-parameter estimators (needed to calibrate captioner statements like "small reverberant room, RT60 about 0.6 s"). The ND licence makes redistributing derived mixtures in test_set.zip doubtful, so use it for internal evaluation only.

### TS-RIR: Translated synthetic room impulse responses for speech augmentation (ASRU 2021) — arXiv:2103.16804
- Key idea: A CycleGAN (TS-RIRGAN) translates simulated RIRs toward real ones, followed by sub-band room equalisation to restore the low-frequency wave effects that geometric simulators miss.
- Key numbers: Up to 19.9% WER reduction on the Kaldi far-field benchmark compared with unmodified synthetic RIRs.
- Licence: Paper only; code licence not checked **[unverified]**.
- **Takeaway for our Track 2 design:** It confirms a known artefact: geometric RIRs have an unnaturally flat spectrum and a weak low-frequency/late tail. A cheap fix is random sub-band EQ on simulated RIRs plus a 50% share of real RIRs. Otherwise the captioner may learn "simulated reverb" and not reverb in general.

---

## B. Noise and event sources

### MUSAN: A Music, Speech, and Noise Corpus — arXiv:1510.08484 / openslr.org/17
- Key idea: A general corpus of music, speech in twelve languages, and technical and non-technical noises, built for VAD and augmentation. It is the de facto noise source for Kaldi-style speaker-verification augmentation.
- Key numbers: 11 GB archive. Hours per subset not on the pages read. I recall about 109 h in total (about 42 music, 60 speech, 6 noise) **[unverified]**.
- Licence: **CC BY 4.0** on OpenSLR (single licence listed).
- **Takeaway for our Track 2 design:** Its babble speech is not Indic and contains intelligible speech, so captions would need "background talkers" when it is used. Its noise subset is the standard point-source pool (843 Freesound noises, per Ko et al.). The labels are coarse, so use it for unlabelled "other sounds" only, never for named timed events.

### Deep Noise Suppression (DNS) Challenge data (Interspeech 2021 / ICASSP 2023) — arXiv:2101.01902 / github.com/microsoft/DNS-Challenge
- Key idea: A large noise and RIR pool for speech enhancement. Noise comes from AudioSet, Freesound (only CC0 files selected) and DEMAND. RIRs are OpenSLR 26/28.
- Key numbers: ICASSP 2023 layout: noise_fullband 58 GB, impulse_responses 5.9 GB, whole set about 1 TB unpacked. Clip, hour and class counts not on the README. I recall about 181 h / 150 classes for 2021 **[unverified]**.
- Licence: Code MIT, docs CC BY 4.0. Data: AudioSet portion CC BY 4.0, Freesound portion CC0, DEMAND CC BY-SA 3.0, RIRs Apache 2.0. Provided "as is".
- **Takeaway for our Track 2 design:** This is a large, mostly permissive, fullband stationary/background pool for the "Other sounds" bed. AudioSet-derived clips have only weak (clip-level) labels, so treat them as unlabeled "background noise" and never as named events.

### FSD50K: An Open Dataset of Human-Labeled Sound Events (IEEE/ACM TASLP 2022) — arXiv:2010.00475 / zenodo.org/records/4060432
- Key idea: Freesound clips with human labels from 200 AudioSet-ontology classes.
- Key numbers: 51,197 clips, about 108.3 h (dev 40,966 clips / 80.4 h; eval 10,231 / 27.9 h). 44.1 kHz, 16-bit mono. Per-clip licences (dev / eval): CC0 14,959 / 4,914; CC-BY 20,017 / 3,489; CC-BY-NC 4,616 / 1,425; CC Sampling+ 1,374 / 403.
- Licence: Dataset CC BY 4.0, but each clip keeps its uploader's licence (listed in `*_clips_info_FSD50K.json`).
- **Takeaway for our Track 2 design:** This is our **primary named-event bank** (door, knock, footsteps, dog, vehicle, laughter, cough, breathing...). Filter to CC0 + CC-BY (about 43k clips) for anything we redistribute. Clips often contain several events or silence, so trim each event with an energy/onset detector or FlexSED before claiming a span.

### ESC-50: Dataset for Environmental Sound Classification (ACM MM 2015), Piczak — github.com/karolpiczak/ESC-50
- Key idea: 2,000 clean 5 s clips, 50 classes × 40, 44.1 kHz mono. Classes useful for us include Laughing, Breathing, Coughing, Sneezing, Snoring, Crying baby, Door knock, Door wood creaks, Footsteps, Clock alarm, Keyboard typing, Glass breaking and Car horn.
- Key numbers: 2,000 clips. The repo reports human accuracy of about 81% **[unverified, not read this session]**.
- Licence: **CC BY-NC** (ESC-10 subset CC BY). Per-clip attribution is in the LICENSE file.
- **Takeaway for our Track 2 design:** These clips are clean and single-event, so the timestamps can be trusted after trimming. Use for internal training only. Prefer FSD50K CC0/CC-BY clips for anything in test_set.zip.

### WHAM! Extending Speech Separation to Noisy Environments (Interspeech 2019) — arXiv:1907.01160
- Key idea: Real ambient noise from coffee shops, restaurants and bars in the San Francisco Bay Area, recorded with a binaural rig, for noisy separation. WHAMR! adds reverberation.
- Key numbers: Hours and SNR range are not in the abstract. The noise set is 17.6 GB (DCASE listing). Segments containing intelligible speech were removed (audEERING catalogue).
- Licence: **CC BY-NC 4.0** (two secondary catalogues; the official site returned 503) **[unverified on primary page]**.
- **Takeaway for our Track 2 design:** These are realistic non-stationary "café/restaurant" beds that sound like where people make phone calls, and they come with intelligible speech already removed. Use for internal training (NC). Good for teaching the captioner to say "busy café/restaurant ambience" correctly.

### Scaper: A library for soundscape synthesis and augmentation (WASPAA 2017), Salamon et al. — github.com/justinsalamon/scaper
- Key idea: Declarative soundscape specification. Each foreground event has distributions over label, source file, onset, duration, SNR, pitch shift and time stretch, over a background. `generate()` writes audio plus a **JAMS annotation** of what was actually rendered.
- Key numbers: N/A (tool). The AudioTime corpus was built with Scaper.
- Licence: **BSD-3-Clause**.
- **Takeaway for our Track 2 design:** Use Scaper (or copy its design) for the event layer of the renderer. The important property is that the annotation records the *realised* values (onset after trimming, actual SNR) rather than the requested ones. Scaper has no forced-alignment awareness of speech, so we need our own speech-aware placement (see CapSpeech below).

---

## C. Telephone and codec channel simulation

### Deep Feature CycleGANs: Speaker identity preserving non-parallel microphone–telephone domain adaptation for speaker verification (2021) — arXiv:2104.01433
- Key idea: Maps microphone speech toward telephone speech in feature space, compared against the standard practice of noise augmentation plus passing mic speech through telephone codecs (GSM, AMR-NB per the search summary).
- Key numbers: About 5–10% relative EER improvement from the 3D-conv discriminators. According to the search summary, codec effects were inconsistent across test sets **[not read in full text]**.
- Licence: Paper only.
- **Takeaway for our Track 2 design:** Codec simulation alone does not fully reproduce real telephone channels, because real handset and network chains add AGC, noise suppression and packet loss. For the "Channel" axis, captions should describe audible properties (narrowband, around 3.4 kHz cutoff, compression artefacts, dropouts) and not codec names. A model cannot reliably tell AMR from GSM by ear, and asserting a codec name risks a FALSE item.

### Analysis of Speaker Verification Performance Trade-offs with Neural Audio Codec Transmission (APSIPA ASC 2025) — arXiv:2509.02771
- Key idea: Measures SV degradation on VoxCeleb1 under Opus and neural codecs at several bitrates.
- Key numbers: SV gets worse as bitrate drops for every codec. Neural codecs beat Opus at below 12 kbps (by 6–8%, absolute vs relative not stated). Around 24 kbps neural codecs trail slightly (EER up 0.4–0.7%).
- Licence: Paper only.
- **Takeaway for our Track 2 design:** This matters for the **speaker-diversity score**: the eval SV model will see our generated audio. If the generator renders strong codec or low-bitrate conditions, speaker embeddings may collapse or shift, which could raise false "same speaker" decisions. Measure speaker-count stability under each channel preset. Our own 12 Hz Qwen3-TTS tokenizer is itself a neural codec, so expect the same effect.

### Codec tooling check (local environment, verified this session) — ffmpeg on this machine; torchaudio AudioEffector tutorial (docs.pytorch.org/audio/2.3.0)
- Key idea: Local `ffmpeg -encoders` lists G.711 μ-law/A-law (`pcm_mulaw`, `pcm_alaw`), G.722, G.726, G.723.1, GSM (`libgsm`), Opus (`libopus`), Speex and Codec2. **There is no AMR-NB encoder** (`libopencore_amrnb` is absent), so AMR-NB needs a rebuilt ffmpeg or another encoder. The torchaudio `AudioEffector` tutorial shows ffmpeg filter strings (lowpass/highpass/aecho) and codecs (ogg/vorbis/opus, mp3 with bit_rate/qscale).
- Key numbers: AMR-NB modes 4.75–12.2 kbit/s at 8 kHz are from 3GPP spec knowledge, not fetched **[unverified this session]**. torchaudio's ffmpeg-based I/O may be deprecated in recent releases **[unverified]**, so call the ffmpeg CLI directly.
- Licence: ffmpeg is LGPL/GPL depending on build; libopencore-amrnb is Apache 2.0 but needs `--enable-version3` **[unverified]**.
- **Takeaway for our Track 2 design:** The channel stage should be an ffmpeg chain: resample → band-pass → codec encode/decode at sampled bitrate → optional packet-loss (zeroed or repeated 20 ms frames) → resample back. Log the exact command per clip in the manifest for reproducibility. Vaani is already 16 kHz phone speech, so a second narrowband pass on Vaani is "phone on phone". Apply codec labels only on wideband/clean sources.

---

## D. Timestamp- and temporally-controlled text-to-audio

### PicoAudio: Enabling precise timestamp and frequency controllability of audio events in text-to-audio generation (arXiv 2024) — arXiv:2407.02869
- Key idea: Freesound clips are segmented into single-occurrence events with a text-to-audio grounding model (threshold 0.5) and CLAP filter (0.3), giving 636 segments for 18 events. These are randomly placed (1/2/3 occurrences in a 2:2:1 ratio) to simulate 5k training clips. Timestamps are a one-hot event×time matrix at 40 ms resolution, concatenated to the diffusion latent. GPT-4 turns free text into timestamp captions.
- Key numbers: Single-event segment F1 / L1-frequency: PicoAudio 0.783 / 0.537, AudioLDM2 0.675 / 2.408, ground truth 0.797 / 0.302. Multi-event: 0.772 / 0.713. FAD 3.175 vs 10.853 (AudioLDM2).
- Licence: Paper; no code licence found (an Amphion HF Space exists) **[unverified]**.
- **Takeaway for our Track 2 design:** It shows that (a) a timestamp matrix at 40 ms easily meets our ±250 ms tolerance, and (b) the label comes for free when you simulate the mix. The evaluation is also usable: run an SED/grounding model on generated audio and compute segment F1 against requested spans. Use the same metric for our generator's "Event at t" relevance.

### AudioTime: A temporally-aligned audio-text benchmark dataset (arXiv 2024) — arXiv:2407.02857
- Key idea: Clean single-event segments from AudioSet-Strong (filtered by CLAP 0.3 and grounding 0.6) are mixed with Scaper at controlled onsets and durations. GPT generator–discriminator loops write captions covering four signals: ordering, duration, frequency and timestamp. It also proposes STEAM, a grounding-model-based metric.
- Key numbers: 5,000 train + 500 test clips per signal, each ≤10 s. Curation kept about 48% of segments. Ground-truth STEAM: timestamp F1 0.910, ordering error 0.220, duration L1 0.792 s. The best TTA model (Make-An-Audio 2) gets timestamp F1 0.559, ordering error 0.758 and duration L1 3.400 s, so free-text temporal control is weak.
- Licence: Not stated (GitHub repo linked); AudioSet sources are YouTube-derived **[unverified]**.
- **Takeaway for our Track 2 design:** Even ground-truth audio scores well below 1.0 on automatic timing metrics, so the checker is noisy. Calibrate our timed-event verifier on real ground truth before using it as a reward or filter. Our captions should also cover the same four temporal signals (order, duration, count, onset), and each can be derived from the render log.

### AudioComposer: Towards fine-grained audio generation with natural language descriptions (ICASSP 2025) — arXiv:2409.12560
- Key idea: Timing, pitch and energy are written into plain text ("Dog bark, Start at 3.6s and End at 7.4s, it has Normal Pitch and Low Energy"), with no extra control network. It uses a flow-based DiT. The AudioTPE simulated data is mixed from FSD50K, ESC-50, UrbanSound8K and ODEON SFX (49k clips, about 140 h), with pitch and energy binned at quantiles.
- Key numbers: On AudioCondition, AudioComposer-L reaches F1_event 44.4 and F1_seg 63.3 (ground truth 43.36 / 63.46), against 21.46 / 55.15 for Tango+LControl. Models are 272M (S) and 743M (L). Removing AudioCaps real data drops F1_seg from 60.83 to 47.84.
- Licence: Paper; code availability not confirmed **[unverified]**.
- **Takeaway for our Track 2 design:** This is the closest analogue to our generator interface (text + description with times, no special tokens). Numeric times in free text are learnable at this scale, which supports conditioning Qwen3-TTS on descriptions that contain "laugh at 3.2–3.9 s". The real-data ablation (–13 F1_seg) shows simulated data must be mixed with real data.

### Make-An-Audio 2: Temporal-enhanced text-to-audio generation (arXiv 2023) — arXiv:2305.18474 / github.com/bytedance/Make-An-Audio-2
- Key idea: An LLM parses captions into structured `<event& start|mid|end>` pairs joined by `@`. A second structured-text encoder and a 1D feed-forward-Transformer diffusion backbone handle variable length. An LLM also converts label-only datasets into captions.
- Key numbers: No numbers on the abstract page. It was the best baseline on AudioTime but still poor (timestamp F1 0.559).
- Licence: **MIT** (repo), checkpoints on HF.
- **Takeaway for our Track 2 design:** Coarse start/mid/end placement is too coarse for our ±250 ms rubric. Use it only as an open, MIT-licensed SFX generator for event content, then place the result ourselves.

### PicoAudio2: Temporal controllable text-to-audio generation with natural language description (arXiv 2025) — arXiv:2509.00683
- Key idea: Per-event descriptions go into a timestamp encoder (matrix) alongside a coarse caption. Training mixes about 64k simulated clips with about 49k real AudioCaps/WavCaps clips whose timestamps come from a text-to-audio grounding model.
- Key numbers: AudioCaps-DJ Seg-F1 0.857 vs AudioComposer 0.690 and MAA2 0.647; CLAP 0.370. **Simulated-only ablation: Seg-F1 0.857 → 0.589, CLAP 0.370 → 0.256, FD 39.96 → 41.86.** The authors write that "a significant distribution gap remains between simulated and real data".
- Licence: Demo page only; code/weights not confirmed **[unverified]**.
- **Takeaway for our Track 2 design:** This is the strongest quantitative evidence for our main risk: training on simulated mixes alone transfers poorly. Every round's training set needs real clips with pseudo-labelled timestamps (from an SED/grounding model) next to rendered clips.

### FreeAudio: Training-free timing planning for controllable long-form text-to-audio generation (arXiv 2025) — arXiv:2507.08557
- Key idea: An LLM (GPT-4o) plans non-overlapping time windows and recaptions each one. "Decoupling & Aggregating Attention Control" in cross-attention renders each window, and contextual latent composition plus reference guidance handle long-form output. No training on the in-house DiT.
- Key numbers: AudioCondition event F1 44.34 (AudioComposer-L 44.40, ground truth 43.37); clip-level F1 68.50; subjective temporal alignment 4.10 vs 2.63. Weak on short or faint events (cat, dog, dishes).
- Licence: Not found **[unverified]**.
- **Takeaway for our Track 2 design:** Training-free timing control is possible with attention masking. In principle it could be applied to an existing TTS/TTA backbone to place events, but for speech + NV the simpler choice is to render speech and events separately and composite them. The "short, faint events are poorly placed" failure suggests our captioner and our checker will also miss short events like a breath or click. Set a minimum event loudness or duration before writing it into a label.

### FlexSED: Towards open-vocabulary sound event detection (WASPAA 2025) — arXiv:2509.18606 / github.com/JHU-LCAP/FlexSED
- Key idea: Dasheng SSL encoder plus a frozen CLAP text encoder and a prompt-fusion decoder (AdaLN-One), giving frame-level detection for any text prompt. It is trained on AudioSet-Strong with LLM-filtered negatives.
- Key numbers: PSDS1A 0.448 vs Dasheng-SED 0.399; PSDS1T 0.586. Zero-shot retention on 20 held-out classes is about 88% (PSDS1T) / 65% (PSDS1A). 25 Hz latent (about 40 ms frames), median filter 7.
- Licence: Code and checkpoints released; licence not seen **[unverified]**.
- **Takeaway for our Track 2 design:** Use it as the **QC verifier** in the renderer (does the inserted "door slam" register at the intended span after mixing, reverb and codec?) and as the **timestamp pseudo-labeller** for real Vaani clips. 40 ms frames are well inside ±250 ms. The authors also suggest using it to evaluate TTA output, which fits our generator-relevance self-check.

---

## E. Open-weight text-to-audio models (as event-content generators)

### Stable Audio Open (arXiv 2024) — arXiv:2407.14358 / huggingface.co/stabilityai/stable-audio-open-1.0
- Key idea: Open-weights latent-diffusion TTA trained only on Creative Commons audio. It generates variable-length (up to 47 s) stereo audio at 44.1 kHz.
- Key numbers: The paper claims competitive FD_openl3. Model card limitations: no realistic vocals, English prompts only, better at SFX and field recordings than music.
- Licence: **Stability AI Community License** (gated). Commercial use is governed by stability.ai/license; I did not read the revenue threshold text **[unverified]**.
- **Takeaway for our Track 2 design:** Good for generating background ambiences and SFX with arbitrary or "fantastical" descriptions (Fugatto-style) at 44.1 kHz, more than our 24 kHz target. It cannot make laughs or breaths in a speaker's voice. Generated events have no inherent onsets, so trim them with an onset detector and then place them ourselves.

### AudioLDM 2 (arXiv 2023) — arXiv:2308.05734 / github.com/haoheliu/AudioLDM2 / huggingface.co/cvssp/audioldm2
- Key idea: Latent diffusion conditioned on an AudioMAE-based "language of audio". Checkpoints for general, music, 48 kHz SFX and speech (GigaSpeech/LJSpeech).
- Key numbers: HF card lists 1150k h training data for audioldm2 and the large variant. Examples run at 16 kHz. PicoAudio reports AudioLDM2 timestamp F1 0.675 (single event).
- Licence: **CC BY-NC-SA 4.0** (HF model card). I did not read the arXiv abstract this session; ID from memory **[unverified ID]**.
- **Takeaway for our Track 2 design:** It is NC and SA, so research-only, and the 16 kHz output is below our generator's 24 kHz target. Low priority; use it only as a baseline in ablations.

### TangoFlux: Super fast and faithful text to audio generation with flow matching and CLAP-ranked preference optimization (arXiv 2024) — arXiv:2412.21037 / github.com/declare-lab/TangoFlux
- Key idea: 515M flow-matching TTA. CRPO generates candidates, ranks them with CLAP and trains with DPO-style preference optimisation.
- Key numbers: Up to 30 s of 44.1 kHz stereo in about 3.7 s on one A40 (50 steps).
- Licence: Non-commercial research use; Stability AI Community License + WavCaps academic-only + training-data licences.
- **Takeaway for our Track 2 design:** CRPO is a recipe we can copy for **our generator loop**: sample N outputs, rank them with an automatic judge (our captioner + rubric-style fact checker in place of CLAP), and run DPO. That is the "captioner as reward" idea from the PS. As an SFX source it is fast enough to make thousands of event clips on an L4.

### AudioX: A unified framework for anything-to-audio generation (ICLR 2026) — arXiv:2503.10522 / huggingface.co/HKUSTAudio/AudioX
- Key idea: One model for text-, video- and audio-conditioned audio and music generation, with a multimodal adaptive fusion module. IF-caps has more than 7M samples.
- Key numbers: The abstract has no figures. The card example uses 10 s and 250 steps.
- Licence: **CC BY-NC 4.0**.
- **Takeaway for our Track 2 design:** Its audio-conditioned mode could continue or inpaint an ambience bed. NC licence and heavy sampling (250 steps) make it secondary to Stable Audio Open and TangoFlux.

---

## F. Audio and speech editing

### AUDIT: Audio editing by following instructions with latent diffusion models (NeurIPS 2023) — arXiv:2304.00830
- Key idea: Trains on (instruction, input audio, output audio) triplets built by mixing. Add: A → A+B, "Add {B} in the background". Drop: the reverse. Replace: B or C inserted into the same region of A. Inpaint: mask. Super-resolution: downsample.
- Key numbers: Triplets: add 71k, drop 71k, replace 50k, inpaint 193k, super-resolution 193k (about 0.6M) from AudioSet, AudioCaps, FSD50K and ESC-50. Adding LSD/KL/FD: 1.35 / 0.92 / 21.80 vs SDEdit 1.38 / 1.30 / 28.25. NeurIPS venue from memory **[unverified]**.
- Licence: Demo only; code licence not confirmed **[unverified]**.
- **Takeaway for our Track 2 design:** The "add/drop" construction is the same as our renderer: the before/after pair gives a free **relative** instruction or description ("a door slams at 2.1 s that was not there before"). Keep both the dry and wet versions of every render so we can create Fugatto-style relative instructions and contrastive captioner training pairs at no extra cost.

### AudioEditor: A training-free diffusion-based audio editing framework (arXiv 2024) — arXiv:2409.12466 / github.com/NKU-HLT/AudioEditor
- Key idea: Null-text inversion plus EOT-suppression on a pretrained Auffusion TTA model gives add, delete and replace edits while keeping unedited regions.
- Key numbers: No figures on the abstract page.
- Licence: MIT (code), stated "for academic and other non-commercial uses".
- **Takeaway for our Track 2 design:** Diffusion editing changes the whole clip slightly, so labels for the untouched parts are no longer exact. For label-exactness, prefer **explicit additive mixing** over generative editing in the renderer. Generative editing is only useful for removing events from real recordings, and its results would need re-verification.

### VoiceCraft: Zero-shot speech editing and text-to-speech in the wild (ACL 2024) — arXiv:2403.16973 / github.com/jasonppy/VoiceCraft
- Key idea: Token-infilling neural codec LM with causal masking and delayed stacking. It edits spans of real, noisy, accented speech and introduces the RealEdit benchmark.
- Key numbers: Human raters find edited speech "nearly indistinguishable" from unedited speech (no percentages on the page). Checkpoints are 330M and 830M (GigaSpeech; the TTS finetune adds 1/5 of LibriLight); prompt + generation ≤16 s.
- Licence: Code **CC BY-NC-SA 4.0**; weights **Coqui Public Model License 1.0.0** (NC). English (MFA English dictionary, espeak) **[English-only likely, not confirmed]**.
- **Takeaway for our Track 2 design:** The infilling idea is how we could insert a non-verbal event into a speaker's own voice at an exact word boundary: mask the span between two words and infill "[laugh]" conditioned on the context. It needs an Indic-trained codec LM, though; Qwen3-TTS on 12 Hz tokens could be fine-tuned for infilling. The released VoiceCraft is English-only and NC.

### SSR-Speech: Towards stable, safe and robust zero-shot text-based speech editing and synthesis (ICASSP 2025) — arXiv:2409.07556 / github.com/WangHelin1997/SSR-Speech
- Key idea: AR Transformer codec LM with classifier-free guidance for stability, a watermark Encodec that marks edited frames, and waveform reconstruction that reuses the original unedited segments.
- Key numbers: Claims state of the art on RealEdit and LibriTTS TTS (no figures on the abstract page). Models: English (GigaSpeech XL) and Mandarin (internal 25k h).
- Licence: Code **MIT** (some files Apache-2.0; phonemizer GPL-3.0). Weights licence not stated **[unverified]**.
- **Takeaway for our Track 2 design:** Copy the "reuse original waveform outside the edit span" step. When we splice a laugh or breath into real or generated speech, everything outside the edit window stays bit-exact, so all other labels remain valid. The frame-level edit mask is also exact metadata for "Event at t1–t2".

---

## G. Non-verbal vocalisations (NV) and expressive speech data

### NonverbalTTS: A public English corpus of text-aligned nonverbal vocalizations with emotion annotations for TTS (arXiv 2025) — arXiv:2507.13155 / huggingface.co/datasets/deepvk/NonverbalTTS
- Key idea: 17 h from VoxCeleb and Expresso with 10 NV types and 8 emotions. Pipeline: ASR + NV tagging + emotion classification, then human validation and multi-annotator fusion. NV tags are inline emoji in the transcript.
- Key numbers: Fine-tuned open TTS reaches parity with closed CosyVoice2 on human evaluation and automatic metrics. The HF card shows about 6.26k rows (train 3.64k, dev 46, test 359, other 2.21k) and clips of 0.5–29.9 s with DNSMOS scores.
- Licence: HF card says **Apache-2.0**. The underlying VoxCeleb/Expresso audio carries its own terms (Expresso CC BY-NC 4.0), so treat it as research-only **[licence interaction unverified]**.
- **Takeaway for our Track 2 design:** It is English, but NV events are largely language-independent acoustically. Use it as a source of real NV segments (laugh, cough, sigh, breath) for splicing and to teach the captioner NV categories. Inline tags tell us *which word* an NV follows, not the ms span, so forced alignment is still needed to get times.

### NVSpeech: An integrated and scalable pipeline for human-like speech modeling with paralinguistic vocalizations (arXiv 2025) — arXiv:2508.04195
- Key idea: Mandarin. 48,430 manually word-level-annotated utterances in 18 paralinguistic categories ([Laughter], [Breathing], [Cough], [Crying], fillers, interjections...). A paralinguistic-aware ASR then auto-labels 174,179 utterances (573.4 h), and CosyVoice/CosyVoice2 are fine-tuned to insert NV at token positions.
- Key numbers: NV-token F1: SenseVoice 0.83 (in-domain) / 0.85 (open-domain) vs Whisper 0.71 / 0.50. TTS para-recall 0.60–0.62. Human preference for para-enhanced output 78.7% (CosyVoice). Cohen's κ > 0.85 on major categories.
- Licence: Dataset licence not confirmed (the CC BY-NC-SA shown is the paper's) **[unverified]**.
- **Takeaway for our Track 2 design:** This is the recipe to copy for Hindi/Tamil: small manual NV annotation → fine-tune an NV-aware tagger → auto-label Vaani at scale → TTS with inline NV tokens. Spontaneous image-prompted Vaani speech should contain natural laughs, fillers and breaths. Even the best tagger gets about 0.6 NV recall in TTS, so the generator will often omit requested NVs. The relevance score needs a verify-and-resample step.

### CapSpeech: Enabling downstream applications in style-captioned text-to-speech (arXiv 2025) — arXiv:2506.02863
- Key idea: Benchmark covering CapTTS, CapTTS-SE (with sound events), AccCapTTS, EmoCapTTS and AgentTTS. For CapTTS-SE pretraining, events from VGGSound, FSDKaggle2018 and ESC-50 (394 events) are mixed into LibriTTS-R. In *insertion* mode, events go at MFA word boundaries (beginning/middle/end, ≥0.3 s apart); in *background* mode, under the speech. Random SNR is −3 to 6 dB, with 5 simulations per utterance. Transcripts mark events with `<event>`, `<B>…</B>` and `<I>`. A human set of 500 mixes was made by audio engineers with fades, EQ and compression. The NV list for AgentDB is aww, throat-clearing, cheering, gasp, groan, laughter, panting, scream, sigh, sob, yawn and others.
- Key numbers: About 10.05M pretraining pairs. CapTTS-SE WER 7.7% (AR) / 3.0% (NAR). The authors note good WER but **poor IMOS**: sound events come out at lower quality than speech. No separate event-accuracy metric. I found no "CapSpeech-NV" subset in the paper **[if the PS lead meant a different resource, unverified]**.
- Licence: **CC BY-NC 4.0** for all resources.
- **Takeaway for our Track 2 design:** This is the most directly reusable recipe: forced-align, pick inter-word gaps, insert the event with a fade, and record the exact span. Copy two refinements from their human set: engineer-style fades/EQ make inserts natural, and engineered mixes beat raw overlay. Their −3 to 6 dB SNR is harsh for a captioner meant to describe phone speech. We should sample SNR per event class (door slam loud, breath quiet relative to speech) from realistic level priors.

### EXPRESSO: A benchmark and analysis of discrete expressive speech resynthesis (Interspeech 2023) — arXiv:2308.05725 / speechbot.github.io/expresso
- Key idea: 4 speakers (2M/2F), read speech in 8 styles plus improvised dialogues in 26 styles, including laughing, whisper, non_verbal, projected, sleepy, child_directed, fast, sarcastic and others. 48 kHz, 24-bit.
- Key numbers: 40 h per the abstract (11 read + 30 improvised); the stats table says 45.9 h. Interspeech venue from memory **[unverified]**.
- Licence: **CC BY-NC 4.0**.
- **Takeaway for our Track 2 design:** Its parallel same-speaker, different-style recordings (Fugatto's "transmuting datasets" pillar) give exact relative labels such as "same speaker, now whispering" and "projected voice". That is useful for the Source and Coupling axes ("projected" works as a Lombard-like proxy). English and NC, so use it for the captioner's acoustic vocabulary, not as Indic training targets.

### Laughter synthesis using pseudo phonetic tokens with a large-scale in-the-wild laughter corpus (Interspeech 2023) — arXiv:2305.12442
- Key idea: k-means on SSL features of laughter gives "pseudo phonetic tokens", which serve as TTS input. A token LM also generates laughter unconditionally. The corpus is 3.5 h of Japanese in-the-wild laughter; speech-laughs were filtered out.
- Key numbers: Significantly outperforms the baseline (MOS not on the abstract page).
- Licence: Corpus licence not stated **[unverified]**.
- **Takeaway for our Track 2 design:** Laughter is not phonetic text, so a TTS conditioned on "[laugh]" gives generic laughs. Token-level control (number of bursts, duration) is possible and would let descriptions like "three short laugh bursts 3.2–3.9 s" be exact. Speech-laughs (laughing *while* talking) are a separate, harder category, and the captioner should not confuse them with standalone laughs.

### LaughNet: Synthesizing laughter utterances from waveform silhouettes and a single laughter example (arXiv 2021) — arXiv:2110.04946 (search-result abstract only)
- Key idea: Controls laughter shape through a frame-level "waveform silhouette" (an amplitude envelope) plus one example laugh.
- Key numbers: Basic listening tests show moderate quality.
- Licence: Not checked **[unverified]**.
- **Takeaway for our Track 2 design:** Envelope-level control supports a renderer-friendly design: the event's temporal envelope is the label (onset, number of bursts, peak time). Even without LaughNet, we can describe spliced real laughs from their measured envelope.

---

## H. Coupling: Lombard effect

### Speaking style adaptation in TTS using seq2seq models with attention / Lombard speech synthesis using transfer learning in a Tacotron TTS system (ICASSP 2019 prep. / Interspeech 2019), Bollepalli, Juvela, Alku — arXiv:1810.12051
- Key idea: Lombard speech is hard to record in volume, so a normal-style Tacotron is adapted to Lombard with a small Lombard set plus a WaveNet vocoder.
- Key numbers: In listening tests the adapted system "clearly outperformed" a DNN-TTS baseline for Lombard style (no numbers on the abstract page).
- Licence: Paper only.
- **Takeaway for our Track 2 design:** Lombard is a *speaking-style* change, not a mix-time effect. Adding noise to clean speech gives the wrong coupling: normal-effort speech in loud noise. For training labels this is a trap. If the renderer adds 75 dB-equivalent café noise to calm read speech, the honest description is "speech does not rise to the noise", and the captioner must not learn that loud noise implies Lombard. For generator data we need the generator to *produce* Lombard speech (raised level, higher F0, flatter tilt, longer vowels; see next item) when the description says so, followed by mixing.

### Lombard acoustic correlates and voice conversion (arXiv:2507.09310, Clarity Challenge 2023; arXiv:2309.10485; plus search summaries)
- Key idea: Lombard speech shows higher intensity and F0, reduced spectral tilt (energy moved to mid frequencies), changed formants and longer phoneme/vowel durations. Flattened tilt drives much of the intelligibility gain, but not all of it. The 2025 VC paper converts speaker identity while keeping Lombard style, to augment Lombard TTS data, and finds implicit conditioning comparable to explicit acoustic features.
- Key numbers: No dB-per-dB slope found in sources read this session. The common "≈0.3–0.5 dB vocal increase per dB noise" figure is **[unverified]**.
- Licence: Papers only.
- **Takeaway for our Track 2 design:** We can produce a "Coupling" label *only* when the speech was produced (or generated) under the noise condition. Two paths: (1) prompt the generator with a Lombard description, verify F0 rise, level rise and tilt flattening with DSP measurements, then mix noise at a level consistent with the effort; (2) DSP pseudo-Lombard (gain + tilt EQ + F0 shift + time-stretch) is cheap but artificial and should be labelled as a transform, not coupling. Captions should describe the measurable changes ("voice gets louder and higher, about +2 semitones, when the noise starts at 4 s") and not the word "Lombard".

---

## I. Instruction-data construction (Fugatto)

### Fugatto 1: Foundational Generative Audio Transformer Opus 1 (ICLR 2025), NVIDIA — openreview B2Fqu7Y2cd / proceedings.iclr.cc (full text read from proceedings PDF)
- Key idea: Five data pillars. (I) An LLM writes Python *instruction generators* per task, with personas (standard, young crowd, thirty-somethings, professional) and varied lengths. (II) Absolute instructions use one sample ("synthesize a happy voice"); relative instructions use two samples ("increase the happiness"), also from LLM-written Python. (III) Audio understanding models caption audio; for speech, the "Prompt-to-Voice" pipeline turns predicted attributes (gender, emotion, quality) into descriptions via LLM-written templates. (IV) "Transmuting" datasets uses pairs where one factor varies (same speaker/text with different emotion, as in RAVDESS; stems for separation). (V) Praat and Pedalboard produce controlled transforms, with each parameter range binned into "a little / moderate / a lot", including relative pairs ("reduce the room size for the reverb moderately").
- Key numbers: At least 20M rows and at least 50k h (assuming 10 s per row). Model sizes 0.8B / 1.4B / 2.5B, with emergent novel sounds only at the larger sizes. Training with t ~ U(0,1) works across tasks; sigmoid-normal t sampling hurts TTS transcript attention. Training starts with template instructions, then moves to an equal template/free-form mix. ComposableART is compositional classifier-free guidance at inference.
- Licence: Paper; weights not released. The authors say they plan to release captions, instructions and code **[release status unverified]**.
- **Takeaway for our Track 2 design:** This is the blueprint for the label compiler. (a) Have Qwen3-8B write *instruction-generator code* once, run offline. That is cheap, reproducible and deterministic with seeds, which helps the manifest, compared with per-clip LLM rewrites. (b) Quantise every measured parameter into graded words *and* keep numbers, since our rubric wants numbers. (c) Generate relative instructions from dry/wet pairs. (d) Curriculum: templates first, then a free-form mix. (e) Pedalboard (GPL-3.0 **[unverified]**) and Praat are the right DSP tools for pitch/rate/effects transforms with known magnitudes.

---

## J. Separation and residual-noise analysis

### ClearerVoice-Studio (MossFormer2 / FRCRN; toolkit paper arXiv:2506.19398) — github.com/modelscope/ClearerVoice-Studio
- Key idea: Open toolkit for speech enhancement (16/48 kHz), separation (8/16 kHz), super-resolution to 48 kHz and target-speaker extraction, plus SpeechScore (SNR, PESQ, STOI, DNSMOS, SI-SDR, NISQA, DistillMOS).
- Key numbers: Bandwidth extension needs an effective input rate of at least 16 kHz. No benchmark numbers read.
- Licence: **Apache-2.0** (repo; HF card for MossFormer2_SR_48K also apache-2.0).
- **Takeaway for our Track 2 design:** Use it for **residual-noise analysis of source clips before rendering**. Enhance the Vaani clip, take residual = input − enhanced, and measure residual level, stationarity and event content (FlexSED on the residual). Two uses: (1) estimating what the source already contains, so that added-noise labels are not contradicted by pre-existing noise; (2) giving cleaner Vaani speech as renderer input (with artefact risk, see pitfalls). Super-resolution to 48 kHz could lift 16 kHz Vaani toward the generator's 24 kHz target, but that adds invented high-band content.

---

## Synthesis

### Renderer spec ("ecology renderer"; every label is computed from the render log, not from the request)
1. **Source gate.** Inputs are clean-ish speech (generator outputs, Expresso-style studio data, or best-DNSMOS Vaani). Run MossFormer2 enhancement and measure residual SNR, blind T60 (validated on ACE), bandwidth and FlexSED events on the residual. Record a "pre-existing condition" record. Only state an added property when it clearly dominates what the source already had (e.g., added SNR at least 10 dB below the residual SNR; T60 increase of 0.3 s or more).
2. **Vocal-event insertion.** Forced-align, choose inter-word gaps (≥0.3 s apart, as in CapSpeech), and splice same-speaker NV (generator with inline NV tag, or NV clips from NonverbalTTS/NVSpeech-style tagged Vaani) with 10–30 ms fades. Keep audio outside the edit bit-exact (SSR-Speech principle). Log the span in ms.
3. **Point-source events.** Scaper-style plan: class, file, onset, duration and level relative to speech, from per-class level priors. Sources: FSD50K CC0/CC-BY, ESC-50 (internal only), Stable Audio Open/TangoFlux for fantastical prompts, trimmed by an onset detector.
4. **Room.** 50% real RIRs (OpenSLR 28, BUT ReverbDB, MIT survey) and 50% pyroomacoustics ISM+ray at 24/48 kHz with random sub-band EQ (TS-RIR lesson). Use different source positions for speech and events. Labels: T60, DRR, C50 computed from the RIR.
5. **Background bed.** DNS CC0/CC-BY noise, WHAM! (internal), MUSAN noise. SNR is defined on active-speech loudness, sampled 0–30 dB, with the *achieved* SNR logged.
6. **Coupling.** Lombard only when generated under the condition; otherwise the label says "no effort change".
7. **Channel.** ffmpeg chain: band-pass, then G.711, GSM, Opus 6–24 kbps, G.722 or Codec2 (AMR-NB needs an ffmpeg rebuild), then packet loss, then AGC. Describe audible properties, not codec names.
8. **Label compiler and QC.** Salience thresholds, then Fugatto-style LLM-written instruction generators (Qwen3-8B), absolute and relative (dry/wet). QC: FlexSED must re-detect each event within ±250 ms after the channel; drop failures.

### Three biggest risks
1. **Sim-to-real gap and shortcut learning.** PicoAudio2 simulated-only training dropped Seg-F1 from 0.857 to 0.589, and AudioComposer lost 13 F1_seg without real data. Mitigation: mix real pseudo-labelled clips every round; keep a held-out real test set.
2. **Label ≠ percept on noisy Vaani bases**, plus masked events that become hallucinated "true" items the grader marks false. Mitigation: source gate, salience thresholds, re-detection QC.
3. **Unnatural edits.** Splice artefacts, poor event quality (CapSpeech IMOS) and missing Lombard coupling hurt naturalness CMOS and could teach the captioner wrong correlations. Licence hygiene (NC/ND/AGPL) is a secondary manifest risk.
