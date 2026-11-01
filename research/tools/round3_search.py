"""Discover candidates; downloading or extracting a paper does not mark it read."""
from pathlib import Path
import csv
import json
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'reviews' / 'round3'
CACHE = ROOT / 'papers' / 'round3'
OUT.mkdir(parents=True, exist_ok=True)
CACHE.mkdir(parents=True, exist_ok=True)
NS = {'a': 'http://www.w3.org/2005/Atom'}
seen = {r['id'] for r in csv.DictReader((ROOT / 'paper_ledger.csv').open())}
seen.update(r['id'] for r in csv.DictReader((ROOT / 'reviews/round2/ledger.csv').open()))
queries = [
 ('voice_design', 'ti:"voice design" OR ti:"speaker generation" OR ti:"speaker embedding" OR ti:"voice identity"', 40),
 ('prosody', 'ti:"prosody transfer" OR ti:"prosody control" OR ti:"prosody prediction" OR ti:"prosodic control" OR ti:"disentangled speech"', 40),
 ('expressive', 'ti:"expressive text" OR ti:"emotional text" OR ti:"controllable text" OR ti:"speaking style"', 45),
 ('vocal_events', 'ti:"nonverbal" OR ti:"non-verbal" OR ti:"laughter synthesis" OR ti:"whispered speech" OR ti:"Lombard"', 35),
 ('caption_grounding', '(ti:"audio captioning" OR ti:"audio grounding") AND (all:"temporal" OR all:"contrastive" OR all:"semantic" OR all:"evaluation")', 40),
 ('caption_truth', '(ti:"audio" OR ti:"speech") AND (ti:"hallucination" OR ti:"negation" OR ti:"counterfactual" OR ti:"compositional")', 35),
 ('scene_generation', 'ti:"audio generation" OR ti:"sound generation" OR ti:"environmental speech" OR ti:"acoustic scene synthesis"', 40),
 ('audio_representations', 'ti:"BEATs" OR ti:"WavLM" OR ti:"HuBERT" OR ti:"wav2vec 2.0" OR ti:"emotion2vec" OR ti:"SpeechT5" OR ti:"AudioMAE" OR ti:"HTS-AT" OR ti:"PaSST" OR ti:"CLAP"', 35),
 ('audio_models', 'ti:"Audio Flamingo" OR ti:"LTU" OR ti:"Pengi" OR ti:"GAMA" OR ti:"SALMONN" OR ti:"AudioPaLM" OR ti:"SpeechGPT" OR ti:"Dynamic-SUPERB" OR ti:"AudioBench" OR ti:"SUPERB"', 35),
 ('tts_backbones', 'ti:"Voicebox" OR ti:"YourTTS" OR ti:"XTTS" OR ti:"CosyVoice" OR ti:"StyleTTS" OR ti:"E2 TTS" OR ti:"NaturalSpeech" OR ti:"VALL-E" OR ti:"VoiceCraft"', 35),
 ('native_data', 'ti:"Kathbath" OR ti:"Svarah" OR ti:"Vistaar" OR ti:"Shrutilipi" OR ti:"Bhasha" OR ti:"FLEURS" OR ti:"Seamless" OR ti:"WhisperX" OR ti:"MMS" OR ti:"IndicConformer"', 35),
 ('native_expressive', '(ti:"Hindi" OR ti:"Tamil" OR ti:"Indian") AND (all:"emotion" OR all:"prosody" OR all:"code-switch" OR all:"spontaneous")', 30),
 ('speaker_metrics', 'ti:"ECAPA" OR ti:"Wespeaker" OR ti:"speaker verification" AND (all:"domain" OR all:"emotion" OR all:"disentanglement")', 30),
 ('quality_metrics', 'ti:"NISQA" OR ti:"UTMOS" OR ti:"DNSMOS" OR ti:"SQUIM" OR ti:"FENSE" OR ti:"CLAPScore" OR ti:"SPIDEr" OR ti:"Wav2Vec-MOS" OR ti:"SpeechBERTScore"', 30),
 ('synthetic_loop', '(ti:"speech" OR ti:"audio") AND (ti:"self-training" OR ti:"pseudo-label" OR ti:"back-translation" OR ti:"noisy student" OR ti:"synthetic data")', 35),
 ('synthetic_general', 'ti:"model collapse" OR ti:"synthetic data" AND (ti:"curation" OR ti:"diversity" OR ti:"accumulating" OR ti:"feedback")', 25),
 ('risk_selection', 'ti:"conformal language" OR ti:"Learn then Test" OR ti:"SelectiveNet" OR ti:"selective prediction" OR ti:"conformal risk" OR ti:"uncertainty in language"', 25),
 ('adaptation', 'ti:"DoRA" OR ti:"AdaLoRA" OR ti:"LoftQ" OR ti:"rsLoRA" OR ti:"PiSSA" OR ti:"LoRA-FA" OR ti:"ReLoRA"', 20),
]
found = {}
for topic, query, count in queries:
    cache = CACHE / ('query_' + topic + '.xml')
    try:
        if cache.exists():
            data = cache.read_bytes()
        else:
            url = 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'search_query': query, 'max_results': count, 'sortBy': 'relevance'})
            with urllib.request.urlopen(url, timeout=45) as response:
                data = response.read()
            cache.write_bytes(data)
        entries = ET.fromstring(data).findall('a:entry', NS)
        for entry in entries:
            aid = re.sub(r'v\d+$', '', entry.findtext('a:id', '', NS).rsplit('/', 1)[-1])
            if not re.fullmatch(r'\d{4}\.\d{4,5}', aid):
                continue
            published = entry.findtext('a:published', '', NS)
            if not published or published[:10] > '2026-11-01':
                continue
            if aid in found:
                found[aid]['topics'].append(topic)
                continue
            found[aid] = {'id': aid, 'title': ' '.join(entry.findtext('a:title', '', NS).split()), 'abstract': ' '.join(entry.findtext('a:summary', '', NS).split()), 'published': published, 'updated': entry.findtext('a:updated', '', NS), 'authors': [e.findtext('a:name', '', NS) for e in entry.findall('a:author', NS)], 'topics': [topic], 'new_to_prior_corpus': aid not in seen}
        print(topic, len(entries), 'new_unique', sum(r['new_to_prior_corpus'] for r in found.values()), flush=True)
    except Exception as exc:
        print(topic, 'FAILED', type(exc).__name__, str(exc), flush=True)
    (OUT / 'discovered.json').write_text(json.dumps(list(found.values()), indent=2) + '\n')
    time.sleep(3.3)
