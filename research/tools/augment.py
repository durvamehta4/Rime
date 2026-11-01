exec(open('/workspace/Rime/research/tools/collect.py').read().split('rows={}')[0])
p=ROOT/'papers'/'discovered.json'; rows={r['id']:r for r in json.loads(p.read_text())}
ids='2507.08128 2509.17765 2601.15621 2411.15191 2410.19168 2410.06885 2406.18009 2402.01912 2211.06687 2306.06546 2210.13438 2212.04356 2209.03143 2301.02111 2306.15687 2304.09116 2403.03100 2306.07691 2110.07205 2305.11000 2306.12925 2310.13289 2311.07919 2407.10759 2503.20215 2310.00704 2308.16692 2410.00037 2406.02430 2407.05407 2412.10117 2409.00750 2403.16973 2406.04904 2312.01479 2206.04769 1912.10211 2104.01778 2212.09058 2006.11477 2106.07447 2110.13900 2305.13516 2308.11596 2205.12446 1912.06670 2106.09685 2305.14314 2208.07339 2210.17323 1606.05250 1706.04599 2011.01921 2006.05587 2009.14184 2305.17493 2404.18930 1905.09799 1910.10248 2006.04558 1803.09017 1809.08895 1712.05884 2209.15596 2302.03540 2407.05361 1904.02882 2307.14335 2304.13731 2301.12503 2209.11497 2306.05284 2209.15352 2301.11325 2412.04102 2406.02231 2405.05904'.split()
queries=[('seed','id_list='+','.join(ids)),
('prosody','search_query='+urllib.parse.quote('(ti:"prosody" OR ti:"phonation" OR ti:"Lombard" OR ti:"laughter") AND cat:cs.SD')+'&max_results=12'),
('temporal_grounding','search_query='+urllib.parse.quote('ti:"audio" AND (ti:"grounding" OR ti:"timestamp" OR ti:"temporal")')+'&max_results=14'),
('quality','search_query='+urllib.parse.quote('ti:"UTMOS" OR ti:"NISQA" OR ti:"DNSMOS" OR ti:"SpeechBERTScore" OR ti:"SQUIM" OR ti:"Audiobox"')+'&max_results=12'),
('indic_datasets','search_query='+urllib.parse.quote('ti:"Rasa" OR ti:"Kathbath" OR ti:"IndicSUPERB" OR ti:"IndicTTS" OR ti:"IndicF5" OR ti:"IndicParler" OR ti:"LIMMITS"')+'&max_results=12'),
('reciprocal','search_query='+urllib.parse.quote('ti:"speech chain" OR ti:"dual learning" OR ti:"model collapse" OR ti:"active learning" AND all:"speech"')+'&max_results=14')]
for topic,args in queries:
 try:
  b=urllib.request.urlopen('https://export.arxiv.org/api/query?'+args,timeout=60).read();(ROOT/'papers'/('search_'+topic+'.xml')).write_bytes(b)
  entries=ET.fromstring(b).findall('a:entry',NS)
  for e in entries:
   aid=re.sub(r'v\d+$','',e.findtext('a:id','',NS).rsplit('/',1)[-1])
   if not re.match(r'\d{4}\.\d{4,5}$',aid):continue
   row={'id':aid,'title':' '.join(e.findtext('a:title','',NS).split()),'abstract':' '.join(e.findtext('a:summary','',NS).split()),'published':e.findtext('a:published','',NS),'authors':[a.findtext('a:name','',NS) for a in e.findall('a:author',NS)],'topics':[topic]}
   if aid in rows:rows[aid]['topics'].append(topic)
   else:rows[aid]=row
  print(topic,len(entries),'unique',len(rows),flush=True)
 except Exception as e:print(topic,str(e),flush=True)
 p.write_text(json.dumps(list(rows.values()),indent=2));time.sleep(3.2)
