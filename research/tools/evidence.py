import pathlib,fitz,re,json,sys
P=pathlib.Path('/workspace/Rime/research/papers')
def extract(aid):
 d=fitz.open(P/(aid+'.pdf'));blocks=[];full=[];refs=False
 for i,p in enumerate(d):
  text=p.get_text(sort=False);full.append(f'\n[PAGE {i+1}]\n'+text)
  for b in p.get_text('blocks'):
   t=' '.join(b[4].split())
   if re.match(r'^(?:\d+\s*)?References$',t,re.I):refs=True
   if not refs and len(t)>170:blocks.append((i+1,t))
 (P/(aid+'.clean.txt')).write_text('\n'.join(full))
 def choose(pattern,excluded=set()):
  scored=[]
  for n,t in blocks:
   if (n,t) in excluded:continue
   score=sum(bool(re.search(p,t,re.I)) for p in pattern)
   if n>1:score+=0.1
   if score>=1:scored.append((score,n,t))
  return max(scored,default=(0,1,blocks[0][1] if blocks else ''),key=lambda x:x[0])[1:]
 m=choose([r'we propose|we introduce|our framework|our approach',r'train|architect|encoder|objective',r'condition|label|token|feature'])
 e=choose([r'results|outperform|improv|compared',r'\d+(?:\.\d+)?\s*%|table\s*\d',r'evaluat|ablat|benchmark|baseline'],{m})
 l=choose([r'limitation|limitations',r'however|future work|challenge|remains|limited|not yet'],{m,e})
 info=json.loads((P/(aid+'.source.json')).read_text())
 result={**info,'evidence':{'method':{'page':m[0],'excerpt':m[1][:650]},'results':{'page':e[0],'excerpt':e[1][:650]},'caveat':{'page':l[0],'excerpt':l[1][:350]}}}
 (P/(aid+'.evidence.json')).write_text(json.dumps(result,indent=2));return result
if __name__=='__main__':
 ids=sys.argv[1:]
 if not ids:ids=[p.stem.replace('.source','') for p in P.glob('*.source.json')]
 for aid in ids:
  try:
   r=extract(aid)
   print('\nID',aid,r['title'],'TOPICS',','.join(r['topics']),'PAGES',r['pages'])
   print('ABSTRACT',r['abstract'][:350])
   for k,v in r['evidence'].items():print(k.upper(),'p'+str(v['page']),v['excerpt'])
  except Exception as e:print(aid,'ERROR',str(e))
