"""Naturalness proxies (the real measure is a blind CMOS against other teams).

- UTMOSv2 (pip: utmosv2; MIT)       - sarulab-speech/UTMOSv2
- Audiobox Aesthetics (CC-BY-4.0)   - facebookresearch/audiobox-aesthetics: CE/CU/PC/PQ axes
Both were trained mostly on English: use them for RELATIVE comparisons between our own rounds only,
and back them with an internal blind A/B among native-speaker team members.
"""
from __future__ import annotations

from functools import lru_cache


@lru_cache(maxsize=1)
def _utmos():
    import utmosv2

    return utmosv2.create_model(pretrained=True)


def utmos(path: str) -> float | None:
    try:
        return float(_utmos().predict(input_path=path))
    except Exception:
        return None


@lru_cache(maxsize=1)
def _aes():
    from audiobox_aesthetics.infer import initialize_predictor

    return initialize_predictor()


def aesthetics(path: str) -> dict | None:
    try:
        return _aes().forward([{"path": path}])[0]
    except Exception:
        return None


def cmos_points(mean_cmos: float, weight: float = 2.0) -> float:
    return weight * (mean_cmos + 3) / 6
