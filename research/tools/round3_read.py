"""Read additional source ranges and preserve their locators, without review claims."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
aid = sys.argv[1]
text = (ROOT / 'papers/round3' / (aid + '.txt')).read_text()
start = int(sys.argv[2]) if len(sys.argv) > 2 else 0
size = int(sys.argv[3]) if len(sys.argv) > 3 else 12000
end = min(start + size, len(text))
record = {'id': aid, 'start': start, 'end': end, 'reason': 'reader-requested follow-up; not automatic completion'}
with (ROOT / 'reviews/round3/additional_ranges.jsonl').open('a') as handle:
    handle.write(json.dumps(record) + '\n')
print('SOURCE', aid, 'CHARS', start, end, 'OF', len(text))
print(text[start:end])
print('END SOURCE', aid, end)
