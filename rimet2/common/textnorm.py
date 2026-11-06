"""Text normalisation for Hindi/Tamil CER and TTS input.

CER normalisation (identical for reference and hypothesis):
  Unicode NFC -> remove ZWJ/ZWNJ/ZWSP -> digits to native number words -> strip punctuation incl. danda (। ॥ |)
  -> lowercase (affects Latin only) -> collapse whitespace.
Never use Whisper's English normaliser on Indic text: it deletes matras and virama.
"""
from __future__ import annotations

import re
import unicodedata

ZW = dict.fromkeys(map(ord, "‌‍​﻿"), None)
_PUNCT_RE = re.compile(r"[।॥|॰,.;:!?\"'“”‘’()\[\]{}<>/\\\-–—_*#@&%^~`+=…]")

# ---------------- Hindi number words ----------------
_HI_1_99 = (
    "एक दो तीन चार पाँच छह सात आठ नौ दस ग्यारह बारह तेरह चौदह पंद्रह सोलह सत्रह अठारह उन्नीस बीस "
    "इक्कीस बाईस तेईस चौबीस पच्चीस छब्बीस सत्ताईस अट्ठाईस उनतीस तीस इकतीस बत्तीस तैंतीस चौंतीस पैंतीस "
    "छत्तीस सैंतीस अड़तीस उनतालीस चालीस इकतालीस बयालीस तैंतालीस चवालीस पैंतालीस छियालीस सैंतालीस "
    "अड़तालीस उनचास पचास इक्यावन बावन तिरेपन चौवन पचपन छप्पन सत्तावन अट्ठावन उनसठ साठ इकसठ बासठ "
    "तिरेसठ चौंसठ पैंसठ छियासठ सड़सठ अड़सठ उनहत्तर सत्तर इकहत्तर बहत्तर तिहत्तर चौहत्तर पचहत्तर "
    "छिहत्तर सतहत्तर अठहत्तर उन्यासी अस्सी इक्यासी बयासी तिरासी चौरासी पचासी छियासी सत्तासी अट्ठासी "
    "नवासी नब्बे इक्यानवे बानवे तिरानवे चौरानवे पचानवे छियानवे सत्तानवे अट्ठानवे निन्यानवे"
).split()
assert len(_HI_1_99) == 99


def hindi_number(n: int) -> str:
    if n == 0:
        return "शून्य"
    parts = []
    for val, word in ((10**7, "करोड़"), (10**5, "लाख"), (1000, "हज़ार"), (100, "सौ")):
        q, n = divmod(n, val)
        if q:
            parts.append(f"{hindi_number(q)} {word}")
    if n:
        parts.append(_HI_1_99[n - 1])
    return " ".join(parts)


# ---------------- Tamil number words ----------------
_TA_UNITS = ["", "ஒன்று", "இரண்டு", "மூன்று", "நான்கு", "ஐந்து", "ஆறு", "ஏழு", "எட்டு", "ஒன்பது"]
_TA_TEENS = ["பத்து", "பதினொன்று", "பன்னிரண்டு", "பதின்மூன்று", "பதினான்கு", "பதினைந்து", "பதினாறு",
             "பதினேழு", "பதினெட்டு", "பத்தொன்பது"]
_TA_TENS = ["", "", "இருபது", "முப்பது", "நாற்பது", "ஐம்பது", "அறுபது", "எழுபது", "எண்பது", "தொண்ணூறு"]
_TA_TENS_C = ["", "", "இருபத்து", "முப்பத்து", "நாற்பத்து", "ஐம்பத்து", "அறுபத்து", "எழுபத்து", "எண்பத்து",
              "தொண்ணூற்று"]
_TA_HUND = ["", "நூறு", "இருநூறு", "முந்நூறு", "நானூறு", "ஐந்நூறு", "அறுநூறு", "எழுநூறு", "எண்ணூறு", "தொள்ளாயிரம்"]
_TA_HUND_C = ["", "நூற்று", "இருநூற்று", "முந்நூற்று", "நானூற்று", "ஐந்நூற்று", "அறுநூற்று", "எழுநூற்று",
              "எண்ணூற்று", "தொள்ளாயிரத்து"]


def _ta_lt100(n: int) -> str:
    if n < 10:
        return _TA_UNITS[n]
    if n < 20:
        return _TA_TEENS[n - 10]
    t, u = divmod(n, 10)
    return _TA_TENS[t] if u == 0 else f"{_TA_TENS_C[t]} {_TA_UNITS[u]}"


def tamil_number(n: int) -> str:
    if n == 0:
        return "பூஜ்ஜியம்"
    parts = []
    for val, word, word_c in ((10**7, "கோடி", "கோடியே"), (10**5, "லட்சம்", "லட்சத்து"), (1000, "ஆயிரம்", "ஆயிரத்து")):
        q, n = divmod(n, val)
        if q:
            head = "" if (q == 1 and val == 1000) else tamil_number(q) + " "
            parts.append(head + (word_c if n else word))
    h, n = divmod(n, 100)
    if h:
        parts.append(_TA_HUND_C[h] if n else _TA_HUND[h])
    if n:
        parts.append(_ta_lt100(n))
    return " ".join(p.strip() for p in parts)


_DEV_DIGITS = str.maketrans("०१२३४५६७८९", "0123456789")
_TA_DIGITS = str.maketrans("௦௧௨௩௪௫௬௭௮௯", "0123456789")


def digits_to_words(text: str, lang: str) -> str:
    text = text.translate(_DEV_DIGITS).translate(_TA_DIGITS)
    fn = hindi_number if lang == "hi" else tamil_number
    return re.sub(r"\d+", lambda m: f" {fn(int(m.group()))} " if len(m.group()) <= 9 else
                  " " + " ".join(fn(int(c)) for c in m.group()) + " ", text)


def normalize_for_cer(text: str, lang: str) -> str:
    t = unicodedata.normalize("NFC", text).translate(ZW)
    t = digits_to_words(t, lang)
    t = _PUNCT_RE.sub(" ", t)
    t = t.lower()
    t = re.sub(r"\s+", " ", t).strip()
    return unicodedata.normalize("NFC", t)


def word_count(text: str) -> int:
    return len(text.split())
