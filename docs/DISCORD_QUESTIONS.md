# Questions to ask the organisers on Discord (before the mid-term)

1. **Internal reranking.** Is automatic best-of-k selection *inside* the frozen generator (no human, fixed seed)
   allowed, given "do not choose between several generations"? We read that rule as forbidding manual
   cherry-picking only.
2. **Programmable rendering.** May the submitted generator include a DSP renderer (room impulse responses,
   codec simulation) and a licensed sound-effect library (CC0/CC-BY) for background events?
3. **Test-set format.** Exact folder/CSV layout for the Track-2 `test_set.zip` (we propose
   `<lang>/captioner/inputs/*.wav`, `<lang>/captioner/answers/clip_metadata.csv`,
   `<lang>/generator/inputs/descriptions.csv` with `desc_id,text,description`).
4. **Grader and SV model.** Can you name the fixed grader model and the speaker-verification model + threshold
   used for the diversity count?
5. **Relevance gate for diversity.** Does a sample "pass the relevance checks" when *all* checks pass or by a
   majority/share threshold?
6. **Code-mixed text.** In generation items, may the text contain English words in Latin script, and is CER then
   computed on the native-script text only?
7. **Round 0 rows.** May round 0 report reference rows (Indic-Parler-TTS, Qwen3-TTS VoiceDesign) next to the
   suggested pair, with the suggested pair as the official round 0?
