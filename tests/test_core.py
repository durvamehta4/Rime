import json

import numpy as np
import pytest

from rimet2.common.bootstrap import bootstrap_ci, draw_positions, paired_bootstrap_delta, selection_order
from rimet2.common.llm import extract_json, mock_llm
from rimet2.common.textnorm import hindi_number, normalize_for_cer, tamil_number
from rimet2.eval.cer import cer, corpus_cer, edit_distance
from rimet2.eval.diversity import count_distinct, diversity_points
from rimet2.eval.grader import cohen_kappa, grade_and_score
from rimet2.eval.rubric import RubricItem, clip_score, structured_verdicts, within_span
from rimet2.scene.schema import Claim, RenderPlan, SceneScore
from rimet2.scene.verbalize import select_claims, verbalize


# ---------- bootstrap: reproduce the PS Appendix A worked example ----------
def test_bootstrap_worked_example():
    assert list(draw_positions(123, "facts_and_names", 1, 10)[:3]) == [0, 8, 1]


def test_bootstrap_ci_deterministic():
    items = [{"id": f"c{i}", "v": float(i % 3)} for i in range(40)]
    a = bootstrap_ci(items, lambda xs: np.mean([x["v"] for x in xs]), 7, "m", sort_key=lambda x: x["id"])
    b = bootstrap_ci(items, lambda xs: np.mean([x["v"] for x in xs]), 7, "m", sort_key=lambda x: x["id"])
    assert a == b and a[1] <= a[0] <= a[2]
    d, lo, hi, p = paired_bootstrap_delta([0.1] * 30, [0.3] * 30, 1, "x")
    assert abs(d - 0.2) < 1e-9 and lo <= d <= hi and p == 0.0
    assert selection_order(1, "s", ["b", "a"]) == selection_order(1, "s", ["a", "b"])


# ---------- rubric formula ----------
def _items():
    return [RubricItem("i1", "c", "Speaker", "woman", 1.0), RubricItem("i2", "c", "Event", "laugh", 3.0, t0=5.6, t1=6.4),
            RubricItem("f1", "c", "Space", "large hall reverb", 2.0, is_true=False)]


def test_clip_score_formula():
    it = _items()
    assert clip_score(it, {"i1": "stated", "i2": "stated", "f1": "absent"}) == 1.0
    assert clip_score(it, {"i1": "stated", "i2": "absent", "f1": "absent"}) == pytest.approx(0.25)
    assert clip_score(it, {"i1": "stated", "i2": "absent", "f1": "stated"}) == 0.0  # floored
    assert clip_score(it, {"i1": "contradicted", "i2": "stated", "f1": "absent"}) == pytest.approx(0.5)


def test_within_span():
    assert within_span(5.4, 6.6, 5.6, 6.4)
    assert not within_span(5.2, 6.4, 5.6, 6.4)


def test_structured_verdicts():
    items = [RubricItem("g", "c", "Speaker", "female", key="gender", value="female"),
             RubricItem("p", "c", "Pitch", "185 Hz", key="f0_median_hz", value=185, tol=15),
             RubricItem("l", "c", "Event", "laugh", key="event", value="laugh", t0=5.6, t1=6.4)]
    claims = [Claim("a man", "Speaker", value={"gender": "male"}),
              Claim("median pitch 190 Hz", "Pitch", value={"f0_median_hz": 190}),
              Claim("laughs", "Event", t0=5.7, t1=6.3, value={"event": "laugh"})]
    v = structured_verdicts(items, claims)
    assert v == {"g": "contradicted", "p": "stated", "l": "stated"}


def test_grader_with_mock():
    llm = mock_llm({"DESCRIPTION": json.dumps([{"id": "i1", "verdict": "stated"}, {"id": "i2", "verdict": "absent"},
                                               {"id": "f1", "verdict": "absent"}])})
    s, v = grade_and_score(llm, "A woman speaks.", _items())
    assert s == pytest.approx(0.25) and v["i1"] == "stated"
    assert cohen_kappa(["a", "b", "a"], ["a", "b", "a"]) == 1.0


def test_extract_json():
    assert extract_json("<think>x</think>```json\n{\"a\": [1,2,],}\n```trailing") == {"a": [1, 2]}


# ---------- text normalisation / CER ----------
def test_numbers():
    assert hindi_number(25) == "पच्चीस"
    assert hindi_number(250000) == "दो लाख पचास हज़ार"
    assert tamil_number(21) == "இருபத்து ஒன்று"
    assert tamil_number(100) == "நூறு"


def test_cer_normalisation():
    assert normalize_for_cer("नमस्ते, दुनिया।", "hi") == "नमस्ते दुनिया"
    assert normalize_for_cer("ना‍म", "hi") == "नाम"
    assert cer("नमस्ते दुनिया।", "नमस्ते दुनिया", "hi") == 0.0
    assert edit_distance("abc", "abd") == 1
    assert 0 < corpus_cer([("वणक्कम", "वणक्कम"), ("ab", "xb")], "hi") < 1


# ---------- diversity ----------
def test_count_distinct():
    rng = np.random.default_rng(0)
    base = rng.normal(size=(3, 64))
    emb = np.vstack([base[0], base[0] + 0.01, base[1], base[2]])
    assert count_distinct(emb, 0.86) == 3
    assert diversity_points([10, 10]) == 2.0


# ---------- scene / verbalizer ----------
def _scene():
    cl = [Claim("A narrowband phone line, band-limited to about 300–3400 Hz", "Channel", p=0.9),
          Claim("A woman, roughly 50 to 70", "Speaker", p=0.8),
          Claim("Median pitch about 185 Hz", "Pitch", p=0.95),
          Claim("She laughs with three short closed-mouth pulses", "Event", p=0.7, t0=5.6, t1=6.4),
          Claim("She is speaking to a friend", "Addressee", p=0.3)]
    return SceneScore("hi", 9.2, cl)


def test_verbalize_threshold_and_order():
    text = verbalize(_scene(), tau=0.5)
    assert text.startswith("Hindi, 9.2 s.")
    assert "friend" not in text  # p below tau => abstain
    assert text.index("narrowband") < text.index("woman") < text.index("5.6–6.4 s")
    assert len(text.split()) <= 300


def test_budget():
    cl = [Claim(f"claim number {i} " + "word " * 20, "Timing", p=0.9) for i in range(40)]
    chosen = select_claims(cl, 0.5, budget_words=100)
    assert sum(len(c.text.split()) for c in chosen) <= 100


def test_scene_roundtrip():
    s = _scene()
    s2 = SceneScore.from_json(s.to_json())
    assert s2.claims[3].t0 == 5.6 and s2.lang == "hi"
    rp = RenderPlan.from_dict({"lang": "ta", "segments": [{"text": "x", "t0": 0}],
                               "ecology": {"channel": "phone_narrowband", "events": [{"label": "fan", "t0": 0, "t1": 1}]}})
    assert rp.ecology.events[0].label == "fan"


def test_claim_validation():
    with pytest.raises(ValueError):
        Claim("x", "NotAType")
    with pytest.raises(ValueError):
        Claim("x", "Event", t0=1.0)
