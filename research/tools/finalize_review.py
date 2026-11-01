import json,pathlib,csv,hashlib,re,collections
ROOT=pathlib.Path('/workspace/Rime/research');P=ROOT/'papers';R=ROOT/'reviews'
seen=set(json.loads((R/'inspected_ids.json').read_text()))
# HTML fallback was inspected separately; preserve source format explicitly.
aid='2609.12663';meta=next(x for x in json.loads((P/'discovered.json').read_text()) if x['id']==aid)
b=(P/(aid+'.html')).read_bytes();t=(P/(aid+'.html.txt')).read_text()
e={'method':{'page':None,'excerpt':'STAG estimates temporal support using targeted white-box attribution, combined with black-box Frequency-Band Occlusion.'},'results':{'page':None,'excerpt':t[t.find('Conclusion'):t.find('Conclusion')+900]},'caveat':{'page':None,'excerpt':'HTML fallback; no PDF page references. Post-hoc explanation is not itself a calibrated correctness probability.'}}
# Method summary above is a reviewer paraphrase, not a source quote.
meta={**meta,'source_url':'https://arxiv.org/html/'+aid,'sha256':hashlib.sha256(b).hexdigest(),'format':'html','pages':None,'status':'full_text_acquired','evidence':e}
(P/(aid+'.source.json')).write_text(json.dumps({k:v for k,v in meta.items() if k!='evidence'},indent=2));(P/(aid+'.evidence.json')).write_text(json.dumps(meta,indent=2));seen.add(aid)
seen.add('fugatto');(R/'inspected_ids.json').write_text(json.dumps(sorted(seen),indent=2))
excluded={
'2110.10103':'Related earlier RemixIT version; count the later 2202.08862 work once',
'2310.00283':'Earlier conference AFTER framework; count extended 2405.00307 once',
'2401.11771':'Insufficient usable extracted body passages; do not count as a full-text excerpt review',
'2204.00977':'Weakly relevant Indian-English ASR overview; excluded from architecture evidence',
'2401.06183':'Hindi-to-English translation application; weak fit to the requested caption/control task',
'2406.18135':'Hindi ASR annotation application; insufficient task-specific evidence in inspected passages',
'2503.11315':'Audio-visual speech compression; outside the audio-only design scope',
'2604.12145':'Video-conditioned tokenizer fusion; outside chosen audio-only scope',
'2604.23860':'Egocentric audio-visual hallucination; peripheral to the selected task',
'2606.02642':'Speech-vision hallucination; outside audio-only scope',
'2608.24707':'Factual alteration detection in spoken news differs from acoustic grounding',
'2610.09408':'Audio-visual multi-segment grounding; outside audio-only scope',
'2610.32268':'Video-grounding benchmark; outside audio-only scope',
'2409.13382':'Watermark robustness is outside the selected Track 2 research question',
'2604.19949':'Codec deepfake detection; peripheral, not used as architecture evidence',
'2607.14753':'Spoof-aware authentication; not the competition diversity protocol',
'2203.03706':'Synthetic Hindi detection; peripheral to captioning/generation objectives',
'2506.06756':'Quantized spoof detection; no direct evidence of caption/control quality',
'2510.08078':'Video-to-audio insertion hallucination; outside chosen audio-only generation design'
}
core={'2510.12000','2609.24771','2602.15766','2402.01912','2410.06885','2507.08128','fugatto','2509.17765','2601.15621','2211.12171','2309.08140','2309.13664','2408.13608','2506.16381','2509.13989','2403.01926','2409.05356','1706.04599','2110.11479','2305.17493','2011.13439','2106.09685','2305.14314','2008.02487','2304.03515','2505.18609','2610.36568','2609.15215'}
def theme(title):
 s=title.lower()
 if any(k in s for k in ['qlora','lora:','gptq','llm.int8','quantization for audio diffusion','rank-sharing']):return 'Efficiency/adaptation'
 if any(k in s for k in ['self-training','back-translation','back translation','synthetic data','synthetic speech data','synthetic supervision','active learning','recursion']):return 'Loop/data selection'
 if any(k in s for k in ['codec','tokenizer','tokenization','rvq','quantizer']):return 'Representations/codecs'
 if any(k in s for k in ['speaker verification','quality','mos','evaluation','benchmark','speechbertscore','calibration']):return 'Evaluation/reliability'
 if any(k in s for k in ['dataset','corpus','indicvoices','rasmalai','vaani','clsr','fleurs','common voice','emilia']):return 'Data/Indic speech'
 if any(k in s for k in ['caption','audio language','audio-language','hallucination','grounding','qwen-audio','qwen2-audio','flamingo','salmonn']):return 'Captioning/grounding'
 return 'Speech/audio generation and control'
records=[]
for aid in sorted(seen):
 f=P/(aid+'.evidence.json');s=P/(aid+'.source.json')
 if not s.exists():raise RuntimeError('Missing source '+aid)
 r=json.loads(f.read_text()) if f.exists() else json.loads(s.read_text())
 if aid=='fugatto':
  r['abstract']='Official Fugatto project PDF; see scoped core findings.';r['authors']=[];r['published']='2025';r['evidence']={}
 status='excluded_after_screening' if aid in excluded else 'abstract_and_selected_fulltext_passages_reviewed'
 if aid in core and aid not in excluded:status='selected_fulltext_review_plus_scoped_core_crosscheck'
 records.append({**r,'review_status':status,'exclusion_reason':excluded.get(aid,''),'theme':theme(r['title'])})
retained=[r for r in records if not r['exclusion_reason']]
fields=['id','title','authors','published','theme','review_status','exclusion_reason','source_url','sha256','pages','evidence_file','core_notes']
with (ROOT/'paper_ledger.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
 for r in records:
  w.writerow({k:('; '.join(r.get('authors',[])) if k=='authors' else 'papers/'+r['id']+'.evidence.json' if k=='evidence_file' else 'reviews/CORE_FINDINGS.md' if k=='core_notes' and r['id'] in core else r.get(k,'')) for k in fields})
with (R/'paper_evidence.jsonl').open('w') as f:
 for r in records:f.write(json.dumps(r,ensure_ascii=False)+'\n')
lines=['# Paper-by-paper first-pass evidence','',
'This dossier records abstracts and algorithmically selected body passages that were inspected. Passage selectors are heuristic: a method-oriented passage can come from introductory context, and an evaluation-oriented passage can be a table caption or setup rather than an experimental result. The dossier does not assert that all methods, tables, appendices, or every sentence were read. Core architectural claims rely on the additional scoped checks in CORE_FINDINGS.md. Author-reported results are not reproduced results. Excluded records do not count toward the retained corpus.','',
'The HTML-fallback STAG method entry is a reviewer paraphrase; its conclusion passage is extracted. Other excerpt fields below are extracted text, possibly truncated.','']
for i,r in enumerate(records,1):
 aid=r['id'];lines += [f"## {i}. {r['title']}",'',f"ID: `{aid}` | Theme: {r['theme']} | Status: `{r['review_status']}`",'',f"Source: {r['source_url']}",'',f"Snapshot SHA-256: `{r['sha256']}`",'']
 if r['exclusion_reason']:lines+=['Excluded: '+r['exclusion_reason'],'']
 lines+=['Abstract extract: '+r.get('abstract','')[:700],'']
 for key,v in r.get('evidence',{}).items():
  loc='PDF p. '+str(v['page']) if v.get('page') else 'HTML / no PDF page'
  lines += [f"**{key.capitalize()}-oriented passage ({loc})**",'',v['excerpt'],'']
 if aid in core:lines+=['Additional interpretation and limitations: [core findings](CORE_FINDINGS.md).','']
(R/'PAPER_BY_PAPER.md').write_text('\n'.join(lines))
def tex(s):return s.replace('&',r'\&').replace('%',r'\%').replace('_',r'\_')
with (ROOT/'references.bib').open('w') as f:
 for r in retained:
  aid=r['id'];key='rime'+aid.replace('.','');authors=' and '.join(r.get('authors',[])) or 'Anonymous'
  f.write('@misc{'+key+',\n  title={'+tex(r['title'])+'},\n  author={'+tex(authors)+'},\n  year={'+r.get('published','2025')[:4]+'},\n  url={'+r['source_url']+'},\n  note={Reviewed as abstract and selected full-text passages; not reproduced}\n}\n\n')
counts=collections.Counter(r['theme'] for r in retained)
summary={'distinct_records_inspected':len(records),'excluded_records':len(records)-len(retained),'retained_distinct_works':len(retained),'core_sources_with_additional_scoped_notes':len(core & {r['id'] for r in retained}),'review_mode':'Abstracts plus selected full-text passages; additional scoped checks for core works. Not cover-to-cover readings.','reproduced_paper_experiments':0,'theme_counts':dict(counts),'search_cutoff':'2026-11-01','network_blocker_resolved':True,'model_training_run':False}
(ROOT/'REVIEW_STATUS.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
