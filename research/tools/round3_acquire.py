"""Acquire fixed selected sources. Review status is curated separately."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import datetime
import hashlib
import json
import re
import time
import urllib.request
import fitz

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'reviews/round3'
CACHE = ROOT / 'papers/round3'
CACHE.mkdir(parents=True, exist_ok=True)
selected = json.loads((OUT / 'selected.json').read_text())

def acquire(row):
    aid = row['id']
    destination = CACHE / (aid + '.pdf')
    try:
        record_path = OUT / (aid + '.source.json')
        existing = json.loads(record_path.read_text()) if record_path.exists() else None
        version = existing.get('snapshot_version', '') if existing else ''
        suffix = version if re.fullmatch(r'v\d+', version) else ''
        url = 'https://arxiv.org/pdf/' + aid + suffix
        if destination.exists():
            data = destination.read_bytes()
        else:
            with urllib.request.urlopen(url, timeout=45) as response:
                data = response.read(32 * 1024 * 1024 + 1)
        if len(data) > 32 * 1024 * 1024 or not data.startswith(b'%PDF'):
            raise ValueError('Invalid or oversized PDF')
        if existing and hashlib.sha256(data).hexdigest() != existing['sha256']:
            raise ValueError('Snapshot hash mismatch; preserve the reviewed source record')
        with fitz.open(stream=data, filetype='pdf') as document:
            text = '\n'.join(f'\n[PAGE {i+1}]\n' + page.get_text(sort=False) for i, page in enumerate(document))
            pages = len(document)
        destination.write_bytes(data)
        (CACHE / (aid + '.txt')).write_text(text)
        version = re.search('arXiv:' + re.escape(aid) + r'v(\d+)', text)
        info = {**row, 'pdf_url': 'https://arxiv.org/pdf/' + aid, 'sha256': hashlib.sha256(data).hexdigest(), 'pages': pages, 'text_chars': len(text), 'snapshot_version': 'v' + version.group(1) if version else 'not_detected', 'retrieved_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'acquisition_status': 'acquired', 'review_status': 'not_reviewed_by_acquisition'}
        if not existing:
            record_path.write_text(json.dumps(info, indent=2) + '\n')
        return aid, 'acquired', pages, len(text)
    except Exception as exc:
        return aid, 'FAILED', type(exc).__name__, str(exc)

with ThreadPoolExecutor(max_workers=2) as pool:
    futures = []
    for row in selected:
        futures.append(pool.submit(acquire, row))
        if not (CACHE / (row['id'] + '.pdf')).exists():
            time.sleep(3.3)
        done = [future for future in futures if future.done()]
        for future in done:
            print(*future.result(), flush=True)
            futures.remove(future)
    for future in as_completed(futures):
        print(*future.result(), flush=True)
