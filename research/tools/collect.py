import urllib.request, urllib.parse, xml.etree.ElementTree as ET, json, pathlib, time, re, sys
ROOT=pathlib.Path('/workspace/Rime/research')
NS={'a':'http://www.w3.org/2005/Atom'}
queries=[
 ('core','ti:Fugatto OR ti:UALM OR ti:"MMAU-Pro" OR ti:"IndicVoices" OR ti:"Vaani" OR ti:"Indic Parler"',18),
 ('captioning','(ti:"audio captioning" OR ti:"speech captioning" OR ti:"audio language") AND (cat:cs.SD OR cat:eess.AS)',32),
 ('controllable_tts','(ti:"controllable speech" OR ti:"expressive speech" OR ti:"text-to-speech") AND (all:"description" OR all:"instruction" OR all:"natural language")',36),
 ('temporal','(ti:"audio" OR ti:"speech") AND (all:"temporal grounding" OR all:"hallucination" OR ti:"prosody" OR ti:"phonation")',24),
 ('indic','(ti:"Indic" OR ti:"Hindi" OR ti:"Tamil" OR ti:"Indian") AND (all:"speech" OR all:"text-to-speech")',28),
 ('loop','(ti:"speech" OR ti:"audio") AND (all:"dual learning" OR all:"self-training" OR all:"back-translation" OR all:"synthetic data")',25),
 ('evaluation','(ti:"speech" OR ti:"audio") AND (all:"quality assessment" OR all:"speaker verification" OR all:"instruction following")',22),
 ('codec','(ti:"audio codec" OR ti:"neural codec" OR ti:"speech tokenizer" OR ti:"flow matching") AND (all:"speech" OR all:"audio")',20),
 ('efficient','(ti:"QLoRA" OR ti:"LoRA" OR ti:"Quantization") AND (all:"language model" OR all:"audio")',12),
]
rows={}
for topic,q,n in queries:
 u='https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':q,'start':0,'max_results':n,'sortBy':'relevance'})
 try:
  b=urllib.request.urlopen(u,timeout=60).read(); (ROOT/'papers'/('search_'+topic+'.xml')).write_bytes(b)
  doc=ET.fromstring(b)
  entries=doc.findall('a:entry',NS)
  for e in entries:
   aid=e.findtext('a:id','',NS).rsplit('/',1)[-1];aid=re.sub(r'v\d+$','',aid)
   if not re.match(r'\d{4}\.\d{4,5}$',aid):continue
   row={'id':aid,'title':' '.join(e.findtext('a:title','',NS).split()),'abstract':' '.join(e.findtext('a:summary','',NS).split()),'published':e.findtext('a:published','',NS),'authors':[a.findtext('a:name','',NS) for a in e.findall('a:author',NS)],'topics':[topic]}
   if aid in rows:rows[aid]['topics'].append(topic)
   else:rows[aid]=row
  print(topic,len(entries),'unique_total',len(rows),flush=True)
 except Exception as e:print(topic,type(e).__name__,str(e),flush=True)
 time.sleep(3.2)
 (ROOT/'papers'/'discovered.json').write_text(json.dumps(list(rows.values()),indent=2))
