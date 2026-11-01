"""Prepare auditable reading passages; this does not mark a source reviewed.

Heuristic selection needs inspection and follow-up when it misses the relevant
method, table, assumptions or limitations. Exact ranges are saved with hashes.
"""
from pathlib import Path
import hashlib
import json
import re
import sys
import os

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / 'papers/round3'
OUT = ROOT / 'reviews/round3'

def page_at(text, offset):
    matches = list(re.finditer(r'\[PAGE (\d+)\]', text[:offset + 1]))
    return int(matches[-1].group(1)) if matches else 1

for aid in sys.argv[1:]:
    info = json.loads((OUT / (aid + '.source.json')).read_text())
    text = (CACHE / (aid + '.txt')).read_text()
    reference_matches = list(re.finditer(r'(?mi)^\s*(?:(?:\d+|[IVX]+)\.?\s+)?(?:REFERENCES|BIBLIOGRAPHY)\s*$', text))
    verified_refs = [m for m in reference_matches if m.start() > min(8000, len(text) * 0.35) and re.search(r'^\s*(?:\[\d+\]|\d{1,3}\.\s)', text[m.end():m.end()+300], re.M)]
    end_refs = verified_refs[0] if verified_refs else (reference_matches[-1] if reference_matches else None)
    body = text[:end_refs.start()] if end_refs else text
    headings = []
    for match in re.finditer(r'(?m)^[ \t]*(?:\d+(?:\.\d+)*\.?|[IVX]+\.?)(?:[ \t]*\n[ \t]*|[ \t]+)([A-Za-z][A-Za-z0-9 ,:()&/\-–]{3,100})[ \t]*$', body):
        heading = match.group(1)
        if re.search(r'method|approach|model|architect|framework|proposed|system|experimen|evaluat|result|ablation|limitation|conclusion|discussion', heading, re.I):
            headings.append((match.start(), heading))
    method = next((p for p, h in headings if p > 2000 and re.search(r'method|approach|architect|proposed|framework|model', h, re.I) and not re.search(r'evaluat|result|compar|baseline|ablation|performance|language model|generative models', h, re.I)), min(4000, len(body) // 5))
    experiments = next((p for p, h in headings if p > method + 1200 and re.search(r'experimen|evaluat', h, re.I)), max(method + 4000, len(body) // 2))
    result = max(experiments, len(body) - 6500)
    conclusion = next((p for p, h in reversed(headings) if p > len(body) * 0.55 and re.search(r'conclusion|limitation', h, re.I)), max(0, len(body) - 2000))
    ranges = [('method', method, 4800), ('experiments', experiments, 2600), ('results', result, 4800), ('limits_or_conclusion', conclusion, 2000)]
    if os.environ.get('ROUND3_COMPACT'):
        ranges = [('method', method, 2500), ('experiments', experiments, 1300), ('results', result, 2700), ('limits_or_conclusion', conclusion, 1000)]
    chunks = []
    for name, start, size in ranges:
        start = min(max(0, start), len(body))
        end = min(start + size, len(body))
        chunks.append({'name': name, 'start': start, 'end': end, 'page': page_at(body, start), 'end_page': page_at(body, end), 'text': body[start:end]})
    record = {'id': aid, 'title': info['title'], 'source_sha256': info['sha256'], 'text_sha256': hashlib.sha256(text.encode()).hexdigest(), 'selection': 'heuristic passages, require reader validation', 'body_chars': len(body), 'abstract': info['abstract'], 'headings': [{'offset': p, 'text': h, 'page': page_at(body, p)} for p, h in headings], 'passages': chunks}
    (CACHE / (aid + '.packet.json')).write_text(json.dumps(record, indent=2) + '\n')
    print('\nPAPER', aid, info['title'], '|', info['pages'], 'PDF pages,', len(body), 'pre-reference chars')
    print('ABSTRACT:', info['abstract'][:700] if os.environ.get('ROUND3_COMPACT') else info['abstract'][:1600])
    print('HEADINGS:', ' | '.join(f'{p}@{page_at(body,p)}:{h}' for p,h in headings))
    for chunk in chunks:
        print(f"\n{chunk['name'].upper()} [p{chunk['page']}–{chunk['end_page']}; chars {chunk['start']}:{chunk['end']}]\n{chunk['text']}")
