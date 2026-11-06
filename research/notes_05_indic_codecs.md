# Notes 05 — Indian-language speech resources/models and neural audio codecs

Cluster owner: lit-review subagent. Written 2026-11-04 for Track 2 (Hindi + Tamil captioner <-> generator loop).
Sources: arXiv abstract/HTML pages, HF dataset/model cards and HF API metadata (`/api/datasets/<id>` gives the
feature schema and split row counts even for gated sets), GitHub READMEs, and one direct inspection of the
IndicConformer vocabulary (from an ungated community mirror). `[unverified]` = not confirmed from a primary source
in this session. Row counts are not hours; I did not convert them.

---

## A. Hindi/Tamil speech corpora

### VAANI: Capturing the language landscape for an inclusive digital India (arXiv 2026), arXiv:2603.28714 / HF `ARTPARK-IISc/Vaani`
- **What it is:** Speech elicited by images and recorded on phones by IISc/ARTPARK (with Google), district by district. Phase 1 + 2 cover 165 districts. Speakers describe pictures, so most of it is spontaneous description.
- **Size:** HF card: about 31,278 h of audio, 156K speakers, 288K images, 105 languages, 2,122 h transcribed. Paper v2: about 31,270 h, about 158K speakers, about 2,067 h transcribed, 109 languages.
  - **Hindi:** 14,923.7 h of audio, of which 1,003.78 h are transcribed.
  - **Tamil:** 848.208 h of audio, of which 24.35 h are transcribed. Tamil is very thin on transcripts.
- **Recording protocol (paper):** 16 kHz, 16-bit, mono, "raw — free from any transcoding." The phone is held about 1 ft from the mouth, in a quiet place. Speakers are aged 20–70 and must be native residents of the pincode (checked against ID). Each speaker gives at most 15 min, and each district aims for at least 800 speakers, gender balanced.
- **Licence:** CC-BY-4.0. The HF repo is gated (accept the terms, then use a token).
- **Metadata fields (HF features, the same for every `audio/<Language>` config):** `audio`, `language`, `duration`, `speakerID`, `languagesKnown` (list), `gender`, `state`, `district`, `pincode`, `stay(years)`, `isTranscriptionAvailable`, `transcript`, `referenceImage`, `speakerImageHash`, `UtteranceSequenceID`.
  - There is **no age column** in the HF schema, although the paper says age, education and socio-economic status were collected at onboarding.
  - Configs are named `audio/<Language>`, plus `images`. Load with `load_dataset("ARTPARK-IISc/Vaani", "audio/Hindi", streaming=True, token=...)`. The card example writes "Hindi". Check the exact config string.
  - There is also a transcribed-only repo, `ARTPARK-IISc/Vaani-transcription-part` (CC-BY-4.0; Hindi 1,003.78 h, Tamil 24.35 h).
- **Transcript tag conventions:**
  - **From the paper guidelines:**
    - `[unintelligible]`, `[inaudible]`, `<UNKNOWN_SEGMENT>`, `<PAUSE>` (a pause longer than 0.5 s).
    - A misspoken word is followed by the correct form in `{}`.
    - Stutters are hyphenated (`w-w-went`). Fillers are kept verbatim.
    - Non-speech sounds follow the SWITCHBOARD categories.
  - **Observed in real Hindi rows** (community mirror `psk/vaani-asr`, read through the HF datasets-server):
    - Span tags wrap the speech they overlap: `<noise> … </noise>`, `<static_noise>…</static_noise>`, `<vehicle_noise>`, `<baby_crying>`, `<female_talking>`, `<people talking>`, `<lips _smack>`, `<unknown sound>`.
    - Point tags: `[breathing]`, `[inhaling]`, `[unintelligible]`.
    - Pause tags appear as both `<pause>` and `<PAUSE>`.
    - English loanwords are written in Devanagari followed by the Latin form in braces: `फ्रीज़ {fridge}`, `ट्रेन {train}`. Non-standard spellings are followed by the standard form: `बहोत {बहुत}`.
    - A trailing `--` marks a truncated utterance. Danda is written as `।` or `|`.
    - Casing and spacing of tags are inconsistent (`<Noise>`, `{unintelligible ]`).
  - The official ARTPARK-IISc/Vaani-Noise-Event-Dataset exists separately. It is gated and has timestamped noise events. Its exact schema is [unverified].
- **Takeaway for our Track 2 design:**
  - Vaani is the in-domain pool the captioner will be judged on: phone channel, 16 kHz, outdoor and indoor noise, image-description register.
  - The span tags (`<vehicle_noise>`, `<baby_crying>`, `<female_talking>`, `[breathing]`) give **free, weak "Other sounds"/"Event" labels** for captioner training. They have no timestamps, so locate events with a sound-event detector or CLAP before turning them into timed claims.
  - `state`/`district`/`pincode` give **region labels for an accent probe** (Hindi: many states; Tamil: Tamil Nadu districts).
  - Before using a transcript as TTS text or as a CER reference:
    - strip all `<…>`/`[…]` tags;
    - keep the Devanagari form and drop the `{…}` Latin and spelling corrections (or the reverse, but consistently);
    - drop `--`.
  - Do **not** use Vaani as the main generator target: it is 16 kHz, so it carries no energy above 8 kHz, while the output must be at least 24 kHz. It also has background noise. Use it as the captioner pool and as "phone channel" generation targets only.

### Vaani Benchmark V1.0 (arXiv 2026), arXiv:2606.21408
- **What it is:** A Hindi benchmark subset of Vaani with three independent transcriptions per segment. Tasks are ASR (multi-reference) and image retrieval.
- **Size:** 5,050 utterances, 1,062 speakers, 10.91 h, 102 districts, 20 states + 2 UTs (search-snippet numbers; the abstract confirms the 102 districts).
- **Licence:** CC-BY-4.0.
- **Metadata:** image prompt, 3 transcripts, real-world acoustics.
- **Note:** The IndicConformer card reports Hindi WER 13.2 on this benchmark.
- **Takeaway:** A ready, held-out Hindi in-domain eval set with district spread. Use it for the captioner test clips and the accent-probe test, and keep it out of training. Multi-reference scoring shows that single-reference WER/CER overstates errors.

### IndicVoices (ACL Findings 2024 [unverified venue]), arXiv:2403.01926 / HF `ai4bharat/IndicVoices`
- **What it is:** Natural speech across 22 languages. The mix is about 74% extempore, 17% conversational and 9% read.
  - Smartphone recordings use a 44.1 kHz channel.
  - Telephone conversations are recorded at **8 kHz**.
- **Size:**
  - **Paper v1:** 7,348 h, 16,237 speakers, 145 districts, 1,639 h transcribed. Table 6 (an early split) lists Hindi as 287 train speakers / 65 h + 63 test speakers / 5 h, and Tamil as 863 / 100 h + 195 / 5 h.
  - **HF card now:** about 23.7K h, of which 11.2K h are transcribed (update of 23 Dec 2025). It gives no per-language hours.
  - **HF API row counts:** Hindi train 445,160 / valid 5,530; Tamil train 422,963 / valid 5,276.
- **Licence:** CC-BY-4.0, gated.
- **Metadata fields:** `audio_filepath`, `text`, `duration`, `lang`, `samples`, `verbatim`, `normalized`, `speaker_id`, `scenario`, `task_name`, `gender`, `age_group`, `job_type`, `qualification`, `area` (rural/urban [unverified]), `district`, `state`, `occupation`, `verification_report`, `unsanitized_verbatim`, `unsanitized_normalized`.
- **Transcript tags:** 89 bracketed non-speech tags, for example `[baby_crying]`, `[barking]`, `[hmm]`, `[horn]`.
- **ASR results:** IndicASR WER is Hindi 15.0 and Tamil 31.2.
- **Takeaway:**
  - This is the **best source of region labels with demographics for Tamil**: thousands of speakers, plus district, state, age_group, gender and area.
  - `verbatim` vs `normalized` columns: use `normalized` as the reference for CER.
  - The 8 kHz conversational part gives real narrowband/telephone examples for the captioner's "Channel" axis. Filter it out for the generator.

### IndicVoices-R (NeurIPS 2024 D&B), arXiv:2409.05356 / HF `ai4bharat/indicvoices_r`
- **What it is:** The 44.1 kHz read and extempore part of IndicVoices, restored to TTS quality.
  - Restoration: HTDemucs (demix/denoise), then VoiceFixer (dereverberation), then DeepFilterNet3. The 8 kHz conversations are excluded.
  - Filters: C50 ≥ 30 dB, SNR ≥ 25 dB, 0.2–30 s, mean F0 ≤ 350 Hz, F0 std ≤ 150 Hz, rate ≤ 30 chars/s, verbatim-vs-normalized CER ≤ 5%.
  - SNR and C50 come from Brouhaha. F0 comes from PENN via DataSpeech.
- **Size:** 1,704.34 h, 10,496 speakers, 22 languages.
  - **Hindi: 74.60 h (read 4.31 + extempore 70.28), 399 speakers.**
  - **Tamil: 99.47 h (11.94 + 87.53), 1,084 speakers.** The paper's table alignment is slightly ambiguous, but the speaker column sums to the total.
  - HF rows: Hindi train 26,318 / test 376; Tamil train 39,292 / test 293.
  - Released at 48 kHz WAV (HF card).
- **Licence:** CC-BY-4.0, gated.
- **Metadata fields:** the IndicVoices fields (`speaker_id`, `gender`, `age_group`, `district`, `state`, `area`, `scenario`, `task_name`, `verbatim`, `normalized`, …) **plus `utterance_pitch_mean`, `utterance_pitch_std`, `snr`, `c50`, `speaking_rate`, `cer`, `duration`**. These are DataSpeech-style descriptors that are ready to verbalise.
- **Benchmark:** Zero-shot VoiceCraft fine-tuned on IV-R scores S-SIM 88.18 vs 78.93 for IndicTTS. NORESQA is 3.64 vs 3.83.
- **Takeaway:**
  - This is **the core clean, multi-speaker Hindi/Tamil set for the generator**.
  - Many speakers serve the diversity score. District/state/age/gender support an accent probe and verifiable "Speaker" claims.
  - The pitch/SNR/C50/rate columns let us build template descriptions with exact numbers (Hz, dB) for round 0.
  - Caveat: restoration artefacts (VoiceFixer/DeepFilterNet). The captioner should not learn "studio" from restored audio.

### Rasa (INTERSPEECH 2024), arXiv:2407.14056 / HF `ai4bharat/Rasa`
- **What it is:** Expressive studio TTS data. The paper version covers Assamese, Bengali and Tamil. The HF release covers 22 languages with one female and one male voice artist each.
  - Styles: the 6 Ekman emotions (happy, sad, angry, fear, disgust, surprise), neutral (Wikipedia/IndicTTS text), commands (Alexa, BigBasket, UMANG, DigiPay), conversation, news and book narration.
- **Size:** 1,145.44 h in total, 640,950 utterances.
  - **Hindi 50.83 h** (F 27.05 / M 23.78).
  - **Tamil 56.12 h** (F 29.94 / M 26.18).
  - HF rows: Hindi 25,713 train / 2,858 test; Tamil 33,005 / 3,656.
  - 48 kHz mono.
- **Licence:** CC-BY-4.0, gated.
- **Metadata fields:** `filename`, `text`, `language`, `gender`, `style`, `duration`, `wav_path`, `audio`.
- **Paper finding:** 1 h neutral + 30 min expressive data gives a "Fair" MUSHRA system.
- **Takeaway:**
  - The only open **acted-emotion/style labels in Hindi and Tamil**. Use them for the generator's "intent/affect" control and as captioner training data for style.
  - Only 2 speakers per language, so it adds nothing to speaker diversity, and the captioner may learn speaker = emotion shortcuts. Balance it with IV-R.
  - Per the brief, "angry" must still be described acoustically (pitch, level, tempo), not only as a label.

### IndicTTS database (IIT Madras) + "Towards Building TTS Systems for the Next Billion Users" (ICASSP 2023), arXiv:2211.09536
- **What it is:** Studio single-speaker read speech. 13 languages in the paper, with Hindi and Tamil each having a male and a female speaker.
- **Size:** more than 272 h over 13 languages, and at least 8 h per speaker. Hindi/Tamil hours are not stated in the paper.
  - The paper downsampled to 22.05 kHz. The original rate is [unverified].
- **Licence:** Not stated in the paper. The IITM IndicTTS licence terms are [unverified] and **must be checked before use**. Indic-Parler-TTS and IndicF5 trained on it.
- **Paper results:** FastPitch + HiFiGAN.
  - MOS: Hindi 4.00 (ground truth 4.33), Tamil 3.84 (ground truth 4.16).
  - CER with Google ASR: Hindi 0.094 (ground truth 0.104), Tamil 0.107 (ground truth 0.108).
- **Takeaway:** Clean, read, neutral speech from 2 speakers per language. Use it as a minor generator source only after the licence is checked. **Ground-truth CER of about 0.10 with a commercial ASR** is a useful sanity anchor: intelligibility CER near 0.1 is roughly the ceiling of real speech for that ASR.

### LIMMITS'23/'24 / SYSPIN (IISc; ICASSP 2023 SPGC; IEEE OJSP 2024)
- **What it is:** Studio TTS corpora from IISc's SYSPIN project, recorded by voice artists at 48 kHz/24-bit.
  - LIMMITS'23: Hindi, Marathi, Telugu.
  - LIMMITS'24 adds Bengali, Chhattisgarhi, Kannada and English.
  - SYSPIN_S1.0 covers 9 languages (Hindi, Bengali, Marathi, Telugu, Kannada, Bhojpuri, Magahi, Chhattisgarhi, Maithili).
- **Size:** about 40 h per voice artist, with 1 male and 1 female per language (so about 80 h of Hindi). Source totals disagree (720 h vs 920 h).
- **Tamil is not included.**
- **Licence:** CC-BY-4.0 according to the SYSPIN/IISc page and the AIKosh listing. LIMMITS-specific terms are [unverified].
- **Metadata:** speaker (M/F), text.
- **Indic-Parler-TTS** used 568 h of LIMMITS.
- **Takeaway:** A large, clean Hindi set from 2 speakers. Good for generator naturalness and intelligibility, useless for diversity. It is the only clean Hindi-belt dialect TTS data (Bhojpuri, Magahi, Chhattisgarhi), which matters if we ever describe "Bhojpuri-accented Hindi" [unverified quality].

### Kathbath / IndicSUPERB (AAAI 2023 [unverified venue]), arXiv:2208.11761 / HF `ai4bharat/Kathbath`
- **What it is:** Read speech recorded on phones through crowdsourcing, in 12 languages, from 1,218 contributors in 203 districts.
  - Splits: clean (train / valid / test-known / test-unknown) and noisy (test only).
  - IndicSUPERB tasks: ASR, speaker verification, speaker identification, LID, query-by-example, keyword spotting.
- **Size:** 1,684 h in total.
  - **Hindi 150.2 h** (58 male / 63 female speakers).
  - **Tamil 185.1 h** (116 male / 42 female).
  - HF rows: Hindi 91,752 train / 3,151 valid; Tamil 95,762 / 2,770.
  - Distributed as m4a.
- **Licence:** The HF tag says CC-BY-4.0; the README says CC0 packaging. Code is MIT.
- **Metadata fields (HF):** `fname`, `text`, `audio_filepath`, `lang`, `duration`, `gender`, `speaker_id`. There is **no district/state** in the HF schema.
- **Takeaway:** Read, intelligible phone-quality speech with speaker IDs. Useful for:
  - captioner coverage of "phone, read-speech" channels;
  - speaker-verification negatives for the diversity metric.

  It is not useful as an accent probe on HF, and not good enough for generator targets.

### Shrutilipi (AI4Bharat; IndicWav2Vec paper arXiv:2111.03945 and "Effectiveness of mining audio-text pairs") / HF `ai4bharat/Shrutilipi`
- **What it is:** All India Radio news bulletins with mined transcripts.
- **Size:** more than 6,400 h over 12 languages. Hindi has 734,675 rows and Tamil 281,508 rows; hours per language are not on the card.
- **Licence:** CC-BY-4.0, gated.
- **Metadata fields:** `audio_filepath`, `text`, `duration`, `lang` only (no speaker).
- **Takeaway:** A large source of the "newsreader" register. The text is useful for an LM or text pool. Because transcripts were mined, alignment errors exist [unverified rate]. It has no speaker or region labels, so use it at most as a **Hindi/Tamil text source for generator prompts** or for "broadcast/radio channel" captioner examples.

### LAHAJA (INTERSPEECH 2024 [unverified venue]), arXiv:2408.11440 / HF `ai4bharat/Lahaja`
- **What it is:** A Hindi ASR benchmark designed for accent diversity: read and extempore speech by speakers with many first languages.
- **Size:** 12.5 h, 132 speakers, 83 districts. HF test split has 6,152 rows.
- **Licence:** The HF tag says MIT; the card text says CC-BY-4.0.
- **Metadata fields:** `audio_filepath`, `text`, `lang`, `verbatim`, `normalized`, `duration`, `scenario`, `fname`, **`native_language`, `gender`, `age_group`, `native_state`, `native_district`**, `sp_id`.
- **Finding:** ASR degrades for speakers from the North-East and South India.
- **Takeaway:** A **ready evaluation set for an L1/region accent probe on Hindi speech**: Hindi spoken by L1 Tamil, Bengali and other speakers. Do not train on it; keep it as probe test data.

### Svarah (INTERSPEECH 2023 [unverified venue]), arXiv:2305.15760 / HF `ai4bharat/Svarah`
- **What it is:** Indian-accented **English**: read and spontaneous speech.
- **Size:** 9.6 h, 117 speakers, 65 districts, 19 states, 19 native languages.
- **Licence:** CC-BY-4.0 per the card text (the HF API licence field is empty).
- **Metadata:** `gender`, `age-group`, `primary_language`, `native_place_state`, `native_place_district`, `highest_qualification`, `job_category`, `occupation_domain`. Test split only: 6,656 rows.
- **Takeaway:** Only relevant if code-mixed English segments in Vaani need accent descriptions. It could serve as a cross-check of an L1 probe (does the probe detect Tamil L1 from English speech?). Low priority.

### RESPIN-S1.0 (NeurIPS 2025 D&B)
- **What it is:** Read speech recorded on mobile phones in dialects of 9 languages, including Hindi, Bhojpuri, Magahi, Maithili and Chhattisgarhi. **No Tamil.**
- **Size:** more than 10,000 h, more than 38 dialects, more than 200K sentences. Text was written by native dialect speakers. Clean, semi-noisy and noisy tiers.
- **Licence:** not stated on the NeurIPS page [unverified]. Data is at spiredatasets.ee.iisc.ac.in.
- **Metadata:** speaker metadata, dialect labels/lexicons, splits.
- **Takeaway:** The **only large dialect-labelled Hindi-belt speech corpus**. It is a candidate for training a Hindi dialect/region probe beyond Vaani's district labels. Check the licence first.

### Tamil dialect ID work: DravidianLangTech-2026 shared task (ACL Anthology 2026.dravidianlangtech-*) + Bharathi et al. 2025 multi-dialect corpus + Nanmalar et al. arXiv:2408.13739 / 2408.14887
- **What it is:**
  - **Shared task:** classify Tamil speech into 4 regional dialects (Northern / Southern / Western / Central) and transcribe it.
  - **Bharathi et al.:** 24 h 27 min from 240 speakers across the same 4 regions of Tamil Nadu.
  - **Nanmalar et al.:** literary vs colloquial Tamil, 79 speakers, 4,387 literary + 5,214 colloquial utterances (MFCC + GMM, then a 1D-CNN).
- **Numbers:**
  - The best reported dialect accuracy is **73.4%** (DLRG, Whisper-medium encoder fine-tuned with a classifier head; a frozen encoder gives about 52.8%).
  - Zero-shot Whisper-large-v3 reaches 0.49 accuracy, macro-F1 0.41.
- **Licence:** shared-task data terms [unverified].
- **Takeaway:**
  - Tamil 4-way regional dialect ID is hard: about 73% even with a fine-tuned encoder, and only about 50% frozen.
  - Any **"region/dialect" claim the captioner makes about Tamil will be unreliable and is risky under the hallucination penalty**. Prefer state-level or "Tamil Nadu vs Sri Lankan" claims, or omit them, unless a probe reaches high precision on a held-out speaker split.
  - For Vaani Tamil, district metadata can be mapped to these 4 regions.

### Hindi dialect/text resources (HinDialect 1.1; VarDial 2018 ILI shared task)
- **What they are:** **Text-only** corpora:
  - HinDialect: folk songs in 26 Hindi-belt varieties, CC-BY-NC-SA 4.0.
  - ILI: Hindi, Awadhi, Bhojpuri, Braj, Magahi, 15K sentences each.
- **Takeaway:** No speech. Not usable for an accent probe, apart from possible text-side LID of transcripts.

---

## B. Models and tools

### IndicConformer-600M multilingual — HF `ai4bharat/indic-conformer-600m-multilingual` (the official Track-2 intelligibility judge)
- **What it is:** A hybrid CTC + RNNT Conformer, 600M parameters, 22 languages, shipped as ONNX/TorchScript with custom code. The repo is gated and MIT-licensed.
  - Training data is not on the card. It is presumably IndicVoices-based [unverified].
  - The card points to a newer model, "Indic-Transcribe" (25 languages), as better. Our scoring uses IndicConformer anyway.
- **How to run (card):**
  1. Install `transformers`, `torchaudio`, `onnxruntime-gpu==1.20.1` (and `onnx`).
  2. Load: `model = AutoModel.from_pretrained("ai4bharat/indic-conformer-600m-multilingual", trust_remote_code=True)`.
  3. Read the audio, downmix to mono, and **resample to 16 kHz**.
  4. Call `model(wav, "hi", "ctc")` or `model(wav, "hi", "rnnt")`. Use `"ta"` for Tamil.
  - A community comparison Space peak-normalises the waveform and uses RNNT.
- **Reported numbers:**
  - Hindi WER 13.2 on Vaani-Benchmark-V1.0 (card).
  - Third-party: FLEURS-Tamil CER 9.33 / WER 25.49 (lemuralabs card, own normaliser).
  - Kathbath-Hindi CER 5.2 from a GGUF quantised port [unverified relevance].
- **Output alphabet (inspected `vocab.json` from the ungated mirror `atharva-again/indic-conformer-600m-quantized`):**
  - Per-language SentencePiece with 257 tokens (256 + `<unk>`).
  - Hindi/Tamil tokens contain **no digits, no Latin letters, no danda `।`/`॥` and no punctuation**, except an ASCII `|` token (both languages) and `॰` (Hindi).
  - Hindi nukta appears as a separate combining U+093C. There are no precomposed U+0958–095F characters, which matches NFC because those are composition exclusions.
  - So the model **cannot output numerals, English words in Latin, or punctuation**.
- **Takeaway: how to compute CER correctly and robustly:**
  1. Audio: decode the generated WAV, downmix to mono, resample 24k→16k with a good resampler. Do not peak-clip.
  2. Fix one decoder for all reporting (RNNT is what public demos use; also report CTC as a robustness check). Batch size 1 avoids padding effects [unverified].
  3. **Normalise the reference and the hypothesis identically:**
     - Unicode NFC.
     - Remove ZWJ/ZWNJ.
     - Map `|`, `।`, `॥` and all Unicode P/S categories to space.
     - Collapse whitespace.
     - **Verbalise digits into native-script words.**
     - Transliterate or remove Latin-script tokens (IndicXlit, or Vaani's `{}` convention reversed).
     - Strip annotation tags.
  4. **Never use Whisper's `BasicTextNormalizer`.** It deletes Indic matras and virama (Manohar et al., arXiv:2409.02449).
  5. CER = total character edits / total reference characters over the corpus (not a mean of per-utterance CERs), with spaces either included or excluded consistently. jiwer on code points; also report grapheme-cluster CER for Indic. Bootstrap 95% CIs over utterances.
  6. **Generator-side implication:** write generator input text in native script, with digits spelled out and no Latin. Anything the ASR cannot emit becomes pure CER loss.
  7. Calibration: run the judge on ground-truth IV-R/Rasa clips to get the "real speech" CER floor. IndicTTS ground truth with Google ASR was about 0.10; IndicConformer will differ.

### Vistaar / IndicWhisper (INTERSPEECH 2023), arXiv:2305.15386 / GitHub AI4Bharat/vistaar
- **What it is:** 59 Indic ASR benchmarks, plus Whisper fine-tuned on 10.7K h covering 12 languages.
- **Numbers:**
  - Hindi average WER 13.6 (Kathbath 10.3, FLEURS 11.4, IndicTTS 7.6, Gramvaani 26.8).
  - Tamil average 25.3 (Kathbath 24.2, FLEURS 25.2, IndicTTS 17.2, MUCS 28.3).
- **Licence:** open (exact licence [unverified]).
- **Takeaway:**
  - Tamil WER is about twice Hindi WER across systems because Tamil is agglutinative. **Expect Tamil CER/WER from the judge to be structurally higher.** Compare our generator against the ground-truth floor per language, never across languages.
  - IndicWhisper is an alternative ASR for filtering generated data, so we do not overfit the judge.

### "What is lost in Normalization?" (arXiv 2024), arXiv:2409.02449
- **What it is:** Shows that Whisper/HF multilingual normalisation strips Unicode marks: Indic vowel signs and virama. This produces spuriously low WER for Hindi and Tamil (Malayalam is worst).
- **Takeaway:** Hard rule: our CER/WER code must keep M-category characters. Add a unit test: `norm("किताब") == "किताब"`.

### IndicLID (ACL 2023), arXiv:2305.15814 / GitHub AI4Bharat/IndicLID
- **What it is:** **Text** language ID for 22 languages plus romanised text (47 classes).
  - Native-script models: fastText (IndicLID-FTN).
  - Romanised models: fastText (IndicLID-FTR) plus fine-tuned IndicBERT (IndicLID-BERT).
- **Numbers:**
  - Native script: 0.98 accuracy at about 30–48K sentences/s.
  - Romanised: 0.71 (fastText) / 0.80 (BERT ensemble, about 10 sentences/s).
- **Licence:** MIT.
- **Takeaway:** Use it to filter Vaani/IndicVoices transcripts by script and language (Vaani "Hindi" configs contain Bhojpuri/Chhattisgarhi-like varieties; see the Chhattisgarh rows above). Speech LID is a separate problem: IndicSUPERB has an LID task, and Vaani paper reports LID experiments [numbers unverified].

### IndicXlit / Aksharantar (EMNLP Findings 2023), arXiv:2205.03018
- **What it is:** 26M transliteration pairs, 21 languages, 12 scripts. IndicXlit is a transformer for Roman↔Indic transliteration.
- **Numbers:** the abstract reports +15% accuracy on Dakshina; absolute accuracy is [unverified].
- **Licence:** open; exact licence [unverified] (the GitHub repo is MIT per memory [unverified]).
- **Takeaway:** Use it to convert English loanwords and Latin tokens into Devanagari/Tamil script for:
  - generator input text (CER judge cannot output Latin);
  - CER references.

### Indic NLP Library — GitHub anoopkunchukuttan/indic_nlp_library
- **What it is:** Normaliser (`IndicNormalizerFactory`), tokeniser, sentence splitter, script conversion, romanisation.
- **Licence:** MIT.
- **Details:** The README does not document exactly what the normaliser does (nukta, chandrabindu, …) [unverified].
- **Takeaway:** Use its tokeniser and normaliser in the CER pipeline, but verify that its nukta and chandrabindu handling matches the judge's alphabet. The vocab keeps both U+093C and U+0901, so do not fold them away.

### Indic-Parler-TTS — HF `ai4bharat/indic-parler-tts` (team has locally)
- **What it is:** Parler-TTS (description-conditioned) fine-tuned on Indic data. Architecture: Parler mini on DAC 44.1 kHz [unverified; config is gated].
- **Training data:** 1,806 h: GLOBE 535 h + IndicTTS 382 h + LIMMITS 568 h + Rasa 288 h. **Hindi 107.00 h (46,135 utterances), Tamil 52.25 h (29,204 utterances).**
- **Languages:** 21 official (+3 unofficial).
- **Named speakers:**
  - Hindi: Rohit, Divya, Aman, Rani (recommended: Rohit, Divya).
  - Tamil: Kavitha, Jaya (recommended: Jaya).
- **Description attributes:**
  - gender, pitch (high/low/moderate), speaking rate, reverberation (close/distant), background noise (clear/noisy), expressivity (monotone/expressive), recording quality.
  - emotion/style: Command, Anger, Narration, Conversation, Disgust, Fear, Happy, Neutral, Proper Noun, News, Sad, Surprise. Officially for 10 languages, **including Tamil but not Hindi**.
  - accent (Indian English).
- **Licence:** Apache-2.0.
- **Native Speaker Score:** Hindi 84.79 ± 2.09; Tamil 75.48 ± 2.18 (fine-tuned).
- **Takeaway:**
  - Strong round-0 or alternative generator that already speaks Hindi/Tamil with coarse description control.
  - **But only 2–4 seen voices per language**: very weak for the speaker-diversity score (10 samples per description should be distinct speakers).
  - Its descriptions are binned tags, far coarser than the rubric axes (Hz, ms, timed events).
  - Useful as (a) a data generator for controlled-attribute pairs and (b) an ablation baseline against Qwen3-TTS.

### Parler-TTS / "Natural language guidance of high-fidelity TTS with synthetic annotations" (arXiv 2024), arXiv:2402.01912
- **What it is:** Labels a 45K h corpus with speaker, style and recording-condition descriptors. Per the DataSpeech repo [unverified detail], these are binned pitch, rate, SNR and C50 values, which an LLM then rewrites into prose.
- **Takeaway:** The template is directly applicable. IV-R already ships these columns for Hindi/Tamil. For the rubric we should keep **exact numbers** (median F0 in Hz, rate in syllables/s, SNR in dB) rather than bins, because the grader rewards precise, true statements.

### IndicF5 — HF `ai4bharat/IndicF5`
- **What it is:** F5-TTS (flow matching) zero-shot voice-cloning TTS for 11 Indic languages, including Hindi and Tamil. It needs a reference audio clip plus its transcript.
- **Training data:** about 1,417 h from Rasa, IndicTTS, LIMMITS and IndicVoices-R. Output is 24 kHz.
- **Licence:** MIT, gated. The card recommends the newer "Indic-Speak" (22 languages).
- **Takeaway:**
  - Open Hindi/Tamil TTS that clones a prompt voice. **Prompting with many different IV-R/Vaani speakers gives easy speaker diversity.**
  - It cannot follow free-text descriptions, so pair it with a voice-prompt selector chosen from the description (gender, age, pitch, region) as a strong baseline or data generator.
  - Also: SPRINGLab F5-Hindi-24kHz and community fine-tunes exist [unverified quality].

### Qwen3-TTS Technical Report (arXiv 2026), arXiv:2601.15621 / HF `Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice`
- **What it is:** Discrete-token TTS in 0.6B and 1.7B sizes.
  - Variants: Base, VoiceDesign (12 Hz 1.7B), CustomVoice, VoiceEditing (25 Hz).
  - Trained on more than 5M h. **Officially 10 languages:** zh, en, ja, ko, de, fr, ru, pt, es, it.
  - **Hindi and Tamil are not supported or evaluated**, and the report lists expansion beyond 10 languages as future work. Cross-lingual eval covers only zh/en/ja/ko.
- **CustomVoice speakers:** **9 fixed preset speakers** (Vivian, Serena, Uncle_Fu, Dylan, Eric, Ryan, Aiden, Ono_Anna, Sohee) with instruction-based style control.
- **VoiceDesign:** claimed SOTA among open models on InstructTTSEval.
- **Licence:** Apache-2.0.
- **Community evidence:** Hindi LoRA fine-tunes exist (aguken-ai, a blog by ravk1234) with only anecdotal quality and no CER.
- **Takeaway:**
  - Round-0 Qwen3-TTS will likely produce **non-native or wrong-language speech for Devanagari/Tamil text** (zero pretraining exposure). A substantial fine-tune on IV-R + Rasa + LIMMITS is needed before any CER is meaningful.
  - **CustomVoice's 9 fixed speakers cap speaker diversity**, since at most 9 distinct speakers can appear across 10 samples. Fine-tune from **Base or VoiceDesign** so the description controls timbre, or add speaker-embedding/voice-prompt sampling.
  - Verify how the text tokenizer segments Devanagari/Tamil: the byte-level BPE probably gives long sequences [unverified].

### Qwen3-TTS-Tokenizer-12Hz — HF `Qwen/Qwen3-TTS-Tokenizer-12Hz`
- **What it is:** A causal codec in the Mimi style. From `config.json`:
  - input/output **24,000 Hz**, hop 1,920, so a **12.5 Hz** frame rate;
  - the encoder has 32 quantizers, of which `encoder_valid_num_quantizers`=**16** are used;
  - **codebook size 2,048**;
  - 1 semantic quantizer (WavLM-distilled; the decoder-side semantic codebook is 4,096);
  - the remaining 15 are acoustic RVQ;
  - causal conv plus a sliding-window transformer.
  - Bitrate by our calculation: 16 × 11 bits × 12.5 = **2.2 kbps** (not stated by Qwen).
- **Reconstruction (LibriSpeech test-clean, English):** PESQ-WB 3.21, PESQ-NB 3.68, STOI 0.96, UTMOS 4.16, SIM 0.95. Mimi scores 2.88 / 3.42 / 0.94 / 3.87 / 0.87.
- **Licence:** Apache-2.0.
- **Training languages for the tokenizer:** not stated.
- **Takeaway:**
  - The output rate of 24 kHz just meets the brief's 24 kHz floor. Never resample generator output below that.
  - **Codec fidelity on Hindi/Tamil is unmeasured.** Run a resynthesis test before training: about 200 IV-R + Rasa clips per language, measuring IndicConformer CER (original vs resynthesised), ECAPA/WavLM SIM and UTMOS. This sets the generator's CER/SIM ceiling.
  - Expect retroflex/dental contrasts, Tamil geminates and aspiration (Hindi) to be the stress points [unverified].
  - The 16 kHz Vaani audio, encoded at 24 kHz, will stay band-limited. Fine as "phone channel" targets, bad for naturalness CMOS.

---

## C. Neural audio codecs

### SoundStream (IEEE/ACM TASLP 2022 [venue unverified]), arXiv:2107.03312
- **What it is:** The first end-to-end neural codec with RVQ. A fully convolutional encoder/decoder is trained adversarially. Quantizer dropout lets one model cover 3–18 kbps.
- **Numbers:** 24 kHz. At 3 kbps it beats Opus at 12 kbps and nears EVS at 9.6 kbps. Supports joint denoising.
- **Licence:** paper only; no official weights [unverified].
- **Takeaway:** The conceptual base: RVQ depth trades bitrate for quality. Also, "joint denoising" means a codec can silently remove noise that the description claims is there, which matters for the Recording axis.

### EnCodec (TMLR 2023 [unverified venue]), arXiv:2210.13438
- **What it is:** Meta's RVQ codec for 24 kHz mono and 48 kHz stereo, with a transformer entropy model (up to 40% smaller).
- **Numbers:** In the DAC paper's comparison, EnCodec at 6 kbps scores ViSQOL 3.05 / SI-SDR 5.99, and at 12 kbps 3.13 / 8.36. Per-bitrate codebooks are [unverified here].
- **Licence:** code MIT; weights CC-BY-NC [unverified].
- **Indic evidence (blog, 10 clips):** Hindi WER 0.184, Tamil WER 0.508 after resynthesis, vs DAC 0.178 / 0.359.
- **Takeaway:** Baseline only. Its NC weights licence [unverified] may conflict with open release.

### DAC — Improved RVQGAN (NeurIPS 2023 spotlight), arXiv:2306.06546 / GitHub descriptinc/descript-audio-codec
- **What it is:** Universal RVQGAN covering speech, environmental sound and music.
  - 44.1 kHz at 8 kbps: **9 codebooks × 1,024, codebook dim 8, 86 Hz (stride 512)**, quantizer dropout p=0.5.
  - Speech training data: DAPS, DNS4 clean, Common Voice, VCTK.
- **Numbers:** ViSQOL 4.18, SI-SDR 10.75 at 8 kbps, vs EnCodec 3.13 / 8.36 at 12 kbps.
- **Licence:** code and weights MIT. Variants at 16, 24 and 44 kHz.
- **Takeaway:**
  - Highest-fidelity open codec. Parler and Indic-Parler build on it [unverified for the Indic checkpoint].
  - Its 86 Hz × 9 tokens is far too long a sequence for an LM-TTS at our compute.
  - Good as a **reconstruction-quality reference** and for "codec artefact" captioner augmentations: encode at a low bitrate to create known channel degradations with exact labels.

### Mimi (in Moshi; arXiv 2024), arXiv:2410.00037 / HF `kyutai/mimi`
- **What it is:** Causal streaming codec at 24 kHz, 12.5 Hz frames.
  - Split RVQ: 1 semantic VQ distilled from WavLM-large plus 7 acoustic RVQ levels, so 8 × 2,048 codes. More levels are available, but Moshi uses 8.
  - About 1.1 kbps. Trained adversarially; quantisation applied 50% of the time.
- **Numbers:** In Qwen's 16-quantizer comparison, Mimi scores PESQ-WB 2.88, STOI 0.94, UTMOS 3.87, SIM 0.87.
- **Licence:** CC-BY-4.0 (HF).
- **Training data:** language and hours not found in the part of the paper read [unverified; English-dominant per common knowledge].
- **Takeaway:** The direct ancestor of the Qwen3 12 Hz tokenizer. Semantic distillation from English WavLM may under-represent Indic phonetic contrasts [hypothesis, unverified]. Measure, don't assume.

### X-Codec 2.0 (Llasa paper; arXiv 2025), arXiv:2502.04128 / HF `HKUSTAudio/xcodec2`
- **What it is:** 16 kHz codec with a single FSQ codebook of **65,536** entries at **50 Hz** (about 0.8 kbps). It combines a Wav2Vec2-BERT semantic encoder with an acoustic encoder.
- **Training data:** about 150K h of Emilia (en/zh/de/fr/ja/ko) + MLS (8 European languages). **No Indic.**
- **Numbers (LibriSpeech test-clean):** WER 2.47 (ground truth 1.96), STOI 0.92, PESQ-WB 2.43, SIM 0.82, UTMOS 4.13. Llasa TTS was trained on 250K h zh/en.
- **Licence:** **CC-BY-NC-4.0** (weights).
- **Takeaway:** The 16 kHz output fails the 24 kHz requirement, and NC weights are bad for an "open" submission. Not recommended as our generator codec.

### WavTokenizer (ICLR 2025), arXiv:2408.16532
- **What it is:** Single-codebook codec at 24 kHz with 40 or 75 tokens/s. Trained on speech, audio and music.
- **Numbers:** "outstanding UTMOS" (no numbers in the abstract). Codebook size is [unverified; 4,096 from memory].
- **Licence:** [unverified] (MIT per memory).
- **Takeaway:** The shortest sequences at 24 kHz with one codebook. Only consider it if building our own LM-TTS from scratch, which is not our plan. Single-codebook codecs tend to lose speaker detail (SIM), which works against the diversity score [general finding, unverified for WavTokenizer].

### BigCodec (arXiv 2024), arXiv:2409.05377
- **What it is:** 159M-parameter, 16 kHz, single-VQ codebook of 8,192 (dim 8), 80 Hz, **1.04 kbps**. Trained only on LibriSpeech 960 h.
- **Numbers:**
  - LibriSpeech: PESQ-WB 2.68, STOI 0.93, SIM 0.84, MUSHRA 92.33 (ground truth 91.84).
  - **Unseen languages (MLS, 7 European):** PESQ-WB 2.47, SIM 0.86 vs DAC-1k 1.12 / 0.33.
- **Licence:** [unverified].
- **Takeaway:** Evidence that low-bitrate codecs trained on English can still transfer to unseen languages, though only European ones were tested. 16 kHz again fails the output-rate requirement.

### Do Neural Codecs Generalize? (arXiv 2026), arXiv:2601.12205
- **What it is:** A controlled study: SoundStream-style codecs trained from scratch (ESPnet-Codec) on English-only, multilingual, or multilingual + audio data, then tested on unseen languages (de, es only) and non-speech audio.
- **Numbers:** The English-only codec was best on 8/9 metrics for Spanish and 7/9 for German. TTS WER on Spanish was 4.04% (English codec) vs 6.89% (multilingual codec).
- **Takeaway:** Codecs mostly transfer across languages, unlike SSL encoders. Adding non-speech audio to pretraining helps non-speech reconstruction. **No Indic test**, so our resynthesis check is still required.

### Indian-language codec evaluation (blog, Aman Agrawal, r4plh.github.io 2025/26; not peer reviewed)
- **What it is:** 10 clips × 5 languages through DAC, EnCodec and SNAC, all at 24 kHz.
- **Numbers:**

  | Codec | Hindi PESQ / WER | Tamil PESQ / WER |
  |---|---|---|
  | DAC | 4.55 / 0.178 | 4.46 / 0.359 |
  | EnCodec | 3.19 / 0.184 | 2.82 / 0.508 |
  | SNAC | 2.37 / 0.340 | 2.00 / 0.829 |

  - Speaker SIM: DAC 0.98–0.99, EnCodec about 0.90, SNAC about 0.76.
- **Caveats:** tiny sample; Hindi source was 48 kHz studio while Tamil was 16 kHz.
- **Takeaway:** The only Hindi/Tamil codec numbers found. Directionally, **Tamil suffers more from low-bitrate codecs** than Hindi, and **no study evaluates Mimi or the Qwen3 12 Hz tokenizer on Indic**. We must run it ourselves; this is a contribution we can claim in the report.

### Indic-CodecFake meets SATYAM (ACL Findings 2026), arXiv:2604.19949; SEA-CF (arXiv 2606.15968)
- **What it is:** Deepfake-detection benchmarks of codec-resynthesised Indic speech, built from IndicSUPERB. They use DAC 16/24/44 kHz and others, and include Hindi and Tamil.
- **Takeaway:** Not a fidelity benchmark. It does confirm that codec artefacts in Indic speech are detectable, so the captioner can learn a "Channel: neural-codec artefacts" statement from paired original/resynthesised clips. These are free labels.

---

## Synthesis

### Recommended data mix

| Dataset | Lang | Hours (verified) | Licence | Use |
|---|---|---|---|---|
| IndicVoices-R | hi / ta | 74.6 h, 399 spk / 99.5 h, 1,084 spk | CC-BY-4.0 | **Generator core** (48 kHz, many speakers); captioner (pitch/SNR/C50/rate columns -> numeric descriptions); accent probe (district/state) |
| Rasa | hi / ta | 50.8 h / 56.1 h (2 spk each) | CC-BY-4.0 | Generator style/emotion control; captioner affect (balanced with IV-R) |
| LIMMITS / SYSPIN | hi | about 40 h × 2 spk | CC-BY-4.0 (SYSPIN) [LIMMITS terms unverified] | Generator naturalness (Hindi only) |
| IndicTTS (IITM) | hi / ta | ≥8 h/spk, 2 spk each | [unverified — check] | Generator, only if the licence permits |
| Vaani (transcribed part) | hi / ta | 1,003.8 h / 24.4 h transcribed (14,923.7 h / 848.2 h total) | CC-BY-4.0 | **Captioner** (in-domain phone/noise; tag-derived event labels); accent probe (state/district); phone-channel generator targets |
| IndicVoices (incl. 8 kHz conversations) | hi / ta | 445K / 423K train rows (hours not on card) | CC-BY-4.0 | Captioner (channel/space variety, age_group/area); Tamil accent probe |
| Kathbath | hi / ta | 150.2 h / 185.1 h | CC-BY-4.0 / CC0 | Captioner (read phone speech); SV negatives |
| Vaani-Benchmark-V1.0 | hi | 10.9 h, 1,062 spk | CC-BY-4.0 | **Eval only** (captioner test clips, CER sanity) |
| Lahaja | hi | 12.5 h, 132 spk | CC-BY-4.0 / MIT tag | **Eval only**: L1/region accent probe |
| Tamil dialect shared-task / Bharathi corpus | ta | about 24.5 h, 240 spk | [unverified] | Accent probe eval (4 regions) |

### Three biggest risks

1. **Qwen3-TTS has never seen Hindi or Tamil.** It officially supports 10 languages, and its Hindi/Tamil codec fidelity is unmeasured. CustomVoice has only 9 fixed speakers, which caps the speaker-diversity score. Mitigation:
   - fine-tune Base/VoiceDesign on IV-R + Rasa + LIMMITS;
   - run a tokenizer resynthesis CER/SIM test first;
   - keep Indic-Parler-TTS and IndicF5 as fallbacks.
2. **CER mismeasurement.** IndicConformer's vocabulary has no digits, no Latin and no punctuation. Whisper-style normalisers delete matras. Use NFC, strip punctuation, verbalise numerals, transliterate English, compute corpus-level CER, and calibrate against ground truth (Tamil is structurally about 2× higher).
3. **Weak and unbalanced labels.**
   - Tamil Vaani has only 24 h transcribed.
   - Tamil dialect ID tops out around 73%, so region claims risk hallucination penalties.
   - Vaani is 16 kHz noisy phone audio, and Rasa emotions come from 2 speakers, which invites shortcut learning.
