"""Validate manually written reviews and assemble navigation/provenance only.

This does not read, summarize, adjudicate, or mark an acquired PDF reviewed.
A review must already exist in a curated Markdown section, with critical notes.
Run after actual reading; --check validates saved artifacts without rewriting.
"""
from pathlib import Path
import argparse
import collections
import csv
import hashlib
import io
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'reviews/round3'
CACHE = ROOT / 'papers/round3'
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--check', action='store_true')
args = parser.parse_args()

selected = json.loads((OUT / 'selected.json').read_text())
selected_ids = {row['id'] for row in selected}
assert len(selected) == len(selected_ids) == 103
prior = list(csv.DictReader((ROOT / 'paper_ledger.csv').open()))
prior += list(csv.DictReader((ROOT / 'reviews/round2/ledger.csv').open()))
prior_ids = {row['id'] for row in prior}
assert len(prior_ids) == 312
assert not (prior_ids & selected_ids), 'New pass overlaps prior IDs'

def normalized_title(value):
    return re.sub(r'[^a-z0-9]', '', value.lower())

prior_titles = {normalized_title(row['title']) for row in prior}
assert not any(normalized_title(row['title']) in prior_titles for row in selected)
assert len({normalized_title(row['title']) for row in selected}) == len(selected)
assert all(row['published'][:10] <= '2026-11-01' for row in selected)
prior_hashes = {row['sha256'] for row in prior if row.get('sha256')}
notes = {}
counts = {}
for path in sorted(OUT.glob('[0-9][0-9]_*.md')):
    content = path.read_text()
    matches = list(re.finditer(r'^## (\d{4}\.\d{4,5})\s+—\s+(.+)$', content, re.M))
    counts[path.name] = len(matches)
    for i, match in enumerate(matches):
        aid = match.group(1)
        assert aid not in notes, f'Duplicate review {aid}'
        section = content[match.start():matches[i+1].start() if i+1 < len(matches) else len(content)]
        assert '**Method and evidence.**' in section or ('**Method.**' in section and '**Evidence.**' in section), aid
        assert '**Limits and decision.**' in section
        assert f'https://arxiv.org/abs/{aid}' in section
        assert len(section.split()) >= 100, f'Incomplete curated note {aid}'
        notes[aid] = {'file': path.name, 'section': section}
assert set(notes) == selected_ids, 'Missing or unselected curated reviews'
extra = collections.defaultdict(list)
for line in (OUT / 'additional_ranges.jsonl').read_text().splitlines():
    row = json.loads(line)
    assert row['id'] in selected_ids
    extra[row['id']].append(row)

rows, locators, bib = [], [], []
for item in selected:
    aid = item['id']
    source = json.loads((OUT / f'{aid}.source.json').read_text())
    assert source['sha256'] not in prior_hashes, f'Duplicate prior snapshot: {aid}'
    assert source['id'] == aid and source['title'] == item['title']
    assert source['acquisition_status'] == 'acquired'
    packet = json.loads((CACHE / f'{aid}.packet.json').read_text())
    raw_text = (CACHE / f'{aid}.txt').read_text()
    assert hashlib.sha256((CACHE / f'{aid}.pdf').read_bytes()).hexdigest() == source['sha256']
    assert packet['source_sha256'] == source['sha256']
    assert packet['text_sha256'] == hashlib.sha256(raw_text.encode()).hexdigest()
    passages = [{key: value for key, value in passage.items() if key != 'text'} for passage in packet['passages']]
    assert any(p['end'] > p['start'] for p in passages)
    for passage in passages + extra[aid]:
        assert 0 <= passage['start'] <= passage['end'] <= len(raw_text)
    locators.append({
        'id': aid, 'source_sha256': source['sha256'],
        'text_sha256': packet['text_sha256'],
        'scope': 'Selected main-text method, evaluation/result and limitation passages; reader-requested followups where needed. Not cover-to-cover or all appendices/visual figures.',
        'packet_ranges': passages, 'additional_ranges': extra[aid],
        'notes': notes[aid]['file'],
        'curated_section_sha256': hashlib.sha256(notes[aid]['section'].encode()).hexdigest(),
        'evidence_boundary': 'Range preparation/extraction is not reading; the independently written critical review is the review record. No experiment reproduction.'
    })
    rows.append({
        'id': aid, 'title': item['title'], 'authors': '; '.join(item['authors']),
        'published': item['published'], 'updated': item['updated'],
        'url': f'https://arxiv.org/abs/{aid}', 'pdf_url': source['pdf_url'],
        'snapshot_version': source['snapshot_version'], 'sha256': source['sha256'],
        'pages': source['pages'], 'review_group': item['review_group'],
        'new_to_prior_ids': True,
        'review_status': 'curated_scoped_fulltext_critical_review',
        'notes': notes[aid]['file'], 'reading_locators': 'reading_locators.jsonl',
    })
    title = item['title'].replace('{', '').replace('}', '')
    authors = ' and '.join(item['authors'])
    bib.append('@misc{rime_round3_' + aid.replace('.', '_') + ',\n'
               + '  title = {{' + title + '}},\n'
               + '  author = {' + authors + '},\n'
               + '  year = {' + item['published'][:4] + '},\n'
               + '  eprint = {' + aid + '},\n'
               + '  archivePrefix = {arXiv},\n'
               + '  url = {https://arxiv.org/abs/' + aid + '}\n}\n')
status = {
    'date': '2026-11-01', 'target_minimum_new_reviews': 101,
    'prior_unique_records': 312, 'new_distinct_pdfs_acquired': len(rows),
    'new_curated_scoped_fulltext_reviews': len(notes), 'overlap_with_prior_ids': 0,
    'total_unique_records_across_passes': len(prior_ids | selected_ids),
    'prior_round2_main_text_reviews': 10,
    'additional_detailed_reviews_round2_and_round3': 10 + len(notes),
    'prior_round2_acquired_only_leads_unchanged': 6,
    'review_files': counts,
    'depth': 'Critical scoped full-text passage reviews, methods/results/limitations and concrete decisions; not exhaustive full-paper/appendix/visual-figure readings. Original 296-record broad screening retains its original depth.',
    'supporting_evidence': 'General audio, statistics, efficiency and non-speech studies are identified as transfer evidence, not Hindi/Tamil validation.',
    'reproduced_experiments': 0, 'model_training_run': False, 'l4_benchmark_run': False,
    'current_architecture': '../../ARCHITECTURE_V4.md',
}
stream = io.StringIO(newline='')
writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator='\n')
writer.writeheader()
writer.writerows(rows)
outputs = {
    'ledger.csv': stream.getvalue(),
    'reading_locators.jsonl': ''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in locators),
    'references.bib': '\n'.join(bib),
    'STATUS.json': json.dumps(status, indent=2, ensure_ascii=False) + '\n',
    'PROGRESS.json': json.dumps({
        'target_minimum': 101, 'selected': 103,
        'curated_fulltext_scoped_reviews': len(notes), 'reviewed_ids': list(notes),
        'remaining_ids': [], 'not_cover_to_cover': True, 'models_trained': 0
    }, indent=2) + '\n',
}
for name, content in outputs.items():
    path = OUT / name
    if args.check:
        assert path.read_text() == content, f'Stale artifact: {name}'
    else:
        path.write_text(content)
print(json.dumps({'validated_reviews': len(notes), 'prior_overlap': 0,
                  'unique_total': len(prior_ids | selected_ids),
                  'mode': 'check' if args.check else 'assemble'}))
