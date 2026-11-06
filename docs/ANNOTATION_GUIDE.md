# DevReal rubric annotation guide (internal stand-in for Rime's private rubric)

Goal: for each dev clip, write rubric items like Rime would, so we can score captioners with the PS formula.
60 clips per language; 20 of them annotated independently by two native speakers (for κ and noise ceilings).

## Output: `data/rubric_<lang>.csv`
`clip_id,item_id,item_type,text,weight,is_true,t0,t1[,key,value,tol]`

- **item_type**: one of Speaker, Source, Morphology, Pitch, Timing, Event, Channel, Space, Other sounds,
  Coupling, Addressee, Subtext, Change (PS Appendix F3).
- **True items (6–15 per clip)**: things a careful listener can confirm by ear. Global (no times) or local with
  `t0,t1` in seconds (graded with ±0.25 s widening). Use Audacity/Praat to read times and pitch.
- **False items (2–4 per clip)**: plausible but wrong statements a captioner might hallucinate (e.g. "large
  reverberant hall" for a dry phone recording, "the speaker laughs" when nobody does, wrong gender, "music in the
  background"). Asserting them costs points.
- **weight** by difficulty: 1 = obvious (gender, phone vs. not); 2 = needs attention (pause positions, room size,
  background type); 3 = expert (phonation changes, pitch numbers, coupling, subtext).
- **key/value/tol** (optional): when the item is numeric/categorical, fill for structured checks, e.g.
  `key=f0_median_hz,value=185,tol=20`; `key=gender,value=female`; `key=event,value=laugh`.

## Rules
1. Only write what you can hear. Calm ≠ low pitch; shouting ≠ anger.
2. Plain clips deserve exact items too ("no background noise", "steady pace", "nothing else happens").
3. One fact per item. No hedges.
4. Do not look at any model's caption before writing items for a clip.
5. Time spans: start/end of the audible thing, not of the word around it.

## Example (Hindi, 6.4 s, Vaani phone recording)
```
clip_id,item_id,item_type,text,weight,is_true,t0,t1,key,value,tol
v1,v1_1,Speaker,A man speaks,1,1,,,gender,male,
v1,v1_2,Pitch,Median pitch around 120 Hz,3,1,,,f0_median_hz,120,20
v1,v1_3,Timing,A pause of about half a second,2,1,2.9,3.4,,,
v1,v1_4,Other sounds,Traffic noise audible throughout,2,1,,,,,
v1,v1_5,Channel,Phone microphone with full speech bandwidth (not a call),2,1,,,channel,wideband,
v1,v1_6,Addressee,Describing a picture to an unseen listener,2,1,,,,,
v1,v1_7,Space,Large echoing hall,1,0,,,,,
v1,v1_8,Event,The speaker laughs,2,0,,,event,laugh,
```
