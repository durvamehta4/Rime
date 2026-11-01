import pathlib,json,sys,re
from evidence import extract
P=pathlib.Path('/workspace/Rime/research/papers');R=pathlib.Path('/workspace/Rime/research/reviews')
N=int(sys.argv[1]) if len(sys.argv)>1 else 15
valid={r['id'] for r in json.loads((P/'selected.json').read_text())}
seen=set(json.loads((R/'inspected_ids.json').read_text())) if (R/'inspected_ids.json').exists() else set()
rows=[]
for f in sorted(P.glob('*.source.json')):
 aid=f.name.replace('.source.json','')
 if aid in seen or aid not in valid:continue
 rows.append(aid)
 if len(rows)>=N:break
(R/'pending_batch.json').write_text(json.dumps(rows))
for aid in rows:
 r=extract(aid)
 print('\nID',aid,'|',r['title'])
 print('A:',r.get('abstract','')[:240])
 for k in ['method','results']:
  v=r['evidence'][k]; print(k[0].upper()+f"[p{v['page']}]:",v['excerpt'][:560])
print('\nBATCH_IDS',','.join(rows))
