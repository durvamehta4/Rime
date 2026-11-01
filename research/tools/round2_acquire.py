import json, pathlib, urllib.request, time, fitz, hashlib, re, datetime
R = pathlib.Path(__file__).resolve().parents[1]
P = R / 'papers'
D = R / 'reviews' / 'round2'
P.mkdir(parents=True, exist_ok=True)
D.mkdir(parents=True, exist_ok=True)
ids = '2309.02285 2506.02863 2502.07243 2301.13662 2408.15676 2406.01205 2406.07969 2312.10381 2406.07203 2210.13248 2301.12258 2311.16509 2208.02814 2101.02703 2307.01850 2408.16333'.split()
rows = {x['id']: x for x in json.loads((D / 'discovered.json').read_text())}
selected = [rows[i] for i in ids]
assert all((r['new_to_prior_ledger'] for r in selected))
(D / 'selected.json').write_text(json.dumps(selected, indent=2))
for r in selected:
    aid = r['id']
    u = 'https://arxiv.org/pdf/' + aid
    try:
        p = P / (aid + '.pdf')
        if not p.exists():
            b = urllib.request.urlopen(u, timeout=45).read(32 * 1024 * 1024)
            if not b.startswith(b'%PDF'):
                raise ValueError('Response was not PDF')
            p.write_bytes(b)
        else:
            b = p.read_bytes()
        d = fitz.open(p)
        t = '\n'.join((f'\n[PAGE {i + 1}]\n' + page.get_text(sort=False) for i, page in enumerate(d)))
        (P / (aid + '.clean.txt')).write_text(t)
        record = {**r, 'source_url': u, 'sha256': hashlib.sha256(b).hexdigest(), 'pages': len(d), 'text_chars': len(t), 'status': 'acquired', 'acquired_on': datetime.datetime.now(datetime.timezone.utc).date().isoformat(), 'snapshot_version': 'v' + m.group(1) if (m := re.search('arXiv:' + re.escape(aid) + 'v(\\d+)', t)) else 'not_detected'}
        (D / (aid + '.source.json')).write_text(json.dumps(record, indent=2))
        print(aid, len(d), len(t), r['title'], flush=True)
    except Exception as e:
        print(aid, 'FAILED', str(e), flush=True)
    time.sleep(3.3)
