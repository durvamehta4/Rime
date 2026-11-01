import pathlib, json, csv, urllib.request, urllib.parse, xml.etree.ElementTree as E, time, re
R = pathlib.Path(__file__).resolve().parents[1]
P = R / 'papers'
D = R / 'reviews' / 'round2'
ns = {'a': 'http://www.w3.org/2005/Atom'}
P.mkdir(parents=True, exist_ok=True)
D.mkdir(parents=True, exist_ok=True)
old = {r['id'] for r in csv.DictReader((R / 'paper_ledger.csv').open())}
found = {}
qs = [('control', 'ti:"PromptTTS 2" OR ti:InstructTTS OR ti:VoxInstruct OR ti:ControlSpeech OR ti:Vevo OR ti:CapSpeech'), ('paralinguistics', 'ti:ParaCLAP OR ti:SECap OR ti:"LibriTTS-P" OR ti:StyleCap OR ti:Brouhaha OR ti:"Cross-domain neural pitch"'), ('risk', 'ti:"Conformal Risk Control" OR ti:"Risk-Controlling Prediction Sets" OR ti:SelectiveNet'), ('collapse', 'ti:"Self-Consuming Generative Models" OR ti:"Self-Improving Diffusion Models" OR ti:"AI Models Collapse When Trained on Recursively Generated Data"')]
for topic, q in qs:
    u = 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'search_query': q, 'max_results': 20})
    b = urllib.request.urlopen(u, timeout=45).read()
    (P / ('round2_search_' + topic + '.xml')).write_bytes(b)
    for e in E.fromstring(b).findall('a:entry', ns):
        aid = re.sub('v\\d+$', '', e.findtext('a:id', '', ns).rsplit('/', 1)[-1])
        title = ' '.join(e.findtext('a:title', '', ns).split())
        row = {'id': aid, 'title': title, 'abstract': ' '.join(e.findtext('a:summary', '', ns).split()), 'published': e.findtext('a:published', '', ns), 'updated': e.findtext('a:updated', '', ns), 'authors': [a.findtext('a:name', '', ns) for a in e.findall('a:author', ns)], 'topics': [topic], 'new_to_prior_ledger': aid not in old}
        found[aid] = row
        print(aid, 'NEW' if aid not in old else 'OLD', title, flush=True)
    time.sleep(3.2)
(D / 'discovered.json').write_text(json.dumps(list(found.values()), indent=2))
