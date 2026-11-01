import json,pathlib,urllib.request,concurrent.futures,time,hashlib,fitz,re,sys,os
ROOT=pathlib.Path('/workspace/Rime/research');P=ROOT/'papers'
rows=json.loads((P/'discovered.json').read_text())
exclude=re.compile(r'hate speech|political speeches|fear speech|Persian|Romanian|ultrasound|face hallucination|Audio-Visual Speaker Verification|audio-visual speaker verification|HiddenSpeaker|EMG-to-Speech|offensive and hate|Biodiversity|law review|Protein|Bernstein|Molecules|Sokoban|Part-Of-Speech|RASA|Rasa|RaSA|QASP|Huntington|Pathology|Hope Speech|offensive|Agri Farm',re.I)
bad={'2209.11497','2406.02231','1606.05250','2009.14184','1905.09799','2209.15596','2006.05587','2412.04102','1910.10248','2011.01921','2411.15191'}
rows=[r for r in rows if r['id'] not in bad and not exclude.search(r['title']) and r['published'][:10]<='2026-11-01']
priority=['2507.08128','2410.06885','2509.17765','2601.15621','2310.13289','2407.10759','2305.17493','1706.04599','2305.14314','2510.12000','2411.15191','2508.13992','2609.24771','2408.13608','2402.01912','2410.06885','2409.05356','2403.01926','2506.16381','2602.15766','2509.13989','2211.12171','2309.08140','2309.13664']
rows.sort(key=lambda r:(priority.index(r['id']) if r['id'] in priority else 100, r['published']))
(P/'selected.json').write_text(json.dumps(rows,indent=2));print('Selected',len(rows),flush=True)
def fetch(r):
 aid=r['id'];pdf=P/(aid+'.pdf'); txt=P/(aid+'.txt');info=P/(aid+'.source.json')
 if info.exists() and txt.exists():return aid,'cached',len(txt.read_text())
 url='https://arxiv.org/pdf/'+aid
 try:
  if not pdf.exists():
   req=urllib.request.Request(url,headers={'User-Agent':'RimeTrack2LiteratureReview/1.0 (open academic research)'})
   with urllib.request.urlopen(req,timeout=45) as resp:
    b=resp.read(32*1024*1024+1);final_url=resp.url
   if len(b)>32*1024*1024 or not b.startswith(b'%PDF'):raise ValueError('Not a valid PDF or larger than 32MiB')
   pdf.write_bytes(b)
  else:b=pdf.read_bytes();final_url=url
  d=fitz.open(pdf);parts=[]
  for i,page in enumerate(d):parts.append(f'\n[PAGE {i+1}]\n'+page.get_text(sort=True))
  text='\n'.join(parts);txt.write_text(text)
  metadata={**r,'source_url':url,'resolved_url':final_url,'sha256':hashlib.sha256(b).hexdigest(),'pages':len(d),'text_chars':len(text),'retrieved_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'status':'full_text_acquired'}
  info.write_text(json.dumps(metadata,indent=2));return aid,'ok',len(d),len(text)
 except Exception as e:
  (P/(aid+'.error.txt')).write_text(str(e));return aid,'failed',str(e)
with concurrent.futures.ThreadPoolExecutor(2) as ex:
 pending=[]
 for r in rows:
  pending.append(ex.submit(fetch,r));
  if not (P/(r['id']+'.source.json')).exists():time.sleep(3.2)
  done=[f for f in pending if f.done()]
  for f in done:print(*f.result(),flush=True);pending.remove(f)
 for f in concurrent.futures.as_completed(pending):print(*f.result(),flush=True)
