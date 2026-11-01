import pathlib, sys, re, json
R = pathlib.Path(__file__).resolve().parents[1]
P = R / 'papers'
D = R / 'reviews' / 'round2'
P.mkdir(parents=True, exist_ok=True)
D.mkdir(parents=True, exist_ok=True)
if len(sys.argv) == 1:
    for r in json.loads((D / 'selected.json').read_text()):
        p = P / (r['id'] + '.clean.txt')
        if not p.exists():
            continue
        t = p.read_text()
        m = re.search('(?mi)^(?:(?:[0-9]+|[IVX]+)\\.?\\s+)?(?:REFERENCES|BIBLIOGRAPHY)\\s*$', t)
        body = t[:m.start()] if m else t
        (P / (r['id'] + '.main.txt')).write_text(body)
        print(r['id'], len(body), 'main chars', r['title'])
else:
    aid = sys.argv[1]
    t = (P / (aid + '.main.txt')).read_text()
    start = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    size = int(sys.argv[3]) if len(sys.argv) > 3 else 17000
    end = min(start + size, len(t))
    print('PAPER', aid, 'CHAR RANGE', start, end, 'OF', len(t))
    print(t[start:end])
    print('END RANGE', start, end)
