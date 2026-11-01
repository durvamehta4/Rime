import pathlib,json,sys
R=pathlib.Path('/workspace/Rime/research/reviews');p=R/'inspected_ids.json';seen=set(json.loads(p.read_text())) if p.exists() else set();ids=json.loads((R/'pending_batch.json').read_text());seen.update(ids);p.write_text(json.dumps(sorted(seen),indent=2));print('Distinct section-review packets inspected:',len(seen))
