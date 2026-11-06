import csv
import io
import json
import random

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import pytest
import soundfile as sf

from rimet2.captioner.calibrate import IsotonicCalibrator, analytic_tau, pav, search_tau
from rimet2.captioner.claims import self_consistency, split_caption
from rimet2.captioner.cli import describe
from rimet2.captioner.fuse import fuse
from rimet2.common.llm import mock_llm
from rimet2.data import vaani_index, vaani_tags
from rimet2.eval.rubric import RubricItem, clip_score, structured_verdicts
from rimet2.generator.assemble import assemble, wsola
from rimet2.generator.cli import run_factored
from rimet2.generator.planner import plan, plan_rules, repair, voice_instruct
from rimet2.generator.speaker_prior import SpeakerBank, Voice
from rimet2.renderer.render import EcologyRenderer
from rimet2.scene.schema import Claim, RenderPlan, SceneScore, Segment
from rimet2.testset import lint_descriptions
from rimet2.testset.package import check_lang, package
from rimet2.train.pairs import captioner_dpo_pair, dominant_pairs
from rimet2.train.targeted import allocate, transform_example, type_scores

from synth import utterance, voiced


# ---------------- captioner ----------------
def _omni_split_json(gender="female", t0=1.0):
    return json.dumps([
        {"text": f"A {'woman' if gender == 'female' else 'man'} speaks", "item_type": "Speaker", "key": "gender",
         "value": gender},
        {"text": "She laughs", "item_type": "Event", "t0": t0, "t1": t0 + 0.4, "key": "event", "value": "laugh"},
        {"text": "She sounds very sad", "item_type": "Subtext", "hedged": True},
    ])


def test_split_and_self_consistency():
    llm = mock_llm({"DESCRIPTION": _omni_split_json()})
    cs = split_caption(llm, "a woman speaks and laughs")
    assert len(cs) == 2  # hedged one dropped
    s2 = split_caption(mock_llm({"DESCRIPTION": _omni_split_json(t0=1.2)}), "x")
    s3 = split_caption(mock_llm({"DESCRIPTION": json.dumps([{"text": "A woman speaks", "item_type": "Speaker",
                                                             "key": "gender", "value": "female"}])}), "x")
    merged = self_consistency([cs, s2, s3])
    g = [c for c in merged if "gender" in c.value][0]
    e = [c for c in merged if "event" in c.value][0]
    assert g.p == 1.0 and abs(e.p - 2 / 3) < 1e-9 and e.t0 in (1.0, 1.2)


def test_fuse_drops_conflicts_and_boosts_agreement():
    measured = [Claim("A man speaks", "Speaker", p=0.8, source="measurement", value={"gender": "male"}),
                Claim("Median pitch about 120 Hz", "Pitch", p=0.9, source="measurement", value={"f0_median_hz": 120})]
    model = [Claim("A woman speaks", "Speaker", p=1.0, source="omni", value={"gender": "female"}),
             Claim("Pitch near 125 Hz", "Pitch", p=1.0, source="omni", value={"f0_median_hz": 125}),
             Claim("Rain in the background", "Other sounds", p=0.6, source="omni")]
    s = fuse(measured, model, "hi", 5.0)
    assert not any(c.value.get("gender") == "female" for c in s.claims)
    pitch = [c for c in s.claims if "f0_median_hz" in c.value][0]
    assert pitch.agree == 2 and pitch.p > 0.9
    rain = [c for c in s.claims if "Rain" in c.text][0]
    assert rain.p < 0.6


def test_calibration():
    bx, by = pav(np.array([0.1, 0.2, 0.3, 0.4]), np.array([0, 1, 0, 1]))
    assert np.all(np.diff(by) >= 0)
    rows = [("Speaker", p, int(p > 0.5)) for p in np.linspace(0, 1, 40)]
    cal = IsotonicCalibrator().fit(rows)
    assert cal(Claim("x", "Speaker", p=0.9)) == 1.0 and cal(Claim("x", "Speaker", p=0.1)) == 0.0
    assert cal(Claim("x", "Pitch", p=0.3)) == 0.3  # untouched type
    best, curve = search_tau(lambda t: -abs(t - 0.6))
    assert abs(best - 0.6) < 1e-9 and analytic_tau(0.5, 0.5) == 0.5


def test_describe_evidence_and_fused(tmp_path):
    sr = 16000
    x, _ = utterance(sr, f0=120)
    p = tmp_path / "c.wav"
    sf.write(p, x, sr)
    ev = describe(str(p), "hi", None, "evidence", neural=False)
    assert "Hz" in ev["description"]
    llm = mock_llm({"DESCRIPTION": _omni_split_json(gender="male", t0=0.5)})
    fu = describe(str(p), "hi", ["a man ...", "a man ..."], "fused", llm=llm, neural=False)
    assert "man" in fu["description"].lower()


# ---------------- end-to-end loop property: constructed labels score perfectly ----------------
def test_verified_labels_score_one():
    sr = 24000
    x, _ = utterance(sr)
    base = SceneScore("hi", len(x) / sr, [Claim("A woman speaks", "Speaker", 0.9, source="measurement",
                                                 value={"gender": "female"})])
    y, sc, log = transform_example(x, sr, base, EcologyRenderer(sr), np.random.default_rng(1), focus="Channel")
    items = [RubricItem(f"i{k}", "c", c.item_type, c.text, key=next(iter(c.value)) if c.value else "",
                        value=next(iter(c.value.values())) if c.value else None, t0=c.t0, t1=c.t1, tol=0.5)
             for k, c in enumerate(sc.claims) if c.value]
    v = structured_verdicts(items, sc.claims)
    assert clip_score(items, v) == 1.0


# ---------------- generator ----------------
def test_planner_rules_and_repair():
    p = plan_rules("नमस्ते दोस्तों", "A woman around 210 Hz on a phone call, calm, in a tiled bathroom", "hi")
    assert p.speaker["gender"] == "female" and p.speaker["f0_hz"] == 210
    assert p.ecology.channel == "phone_narrowband" and p.ecology.space == "bathroom"
    bad = RenderPlan("hi", segments=[Segment("नमस्ते")])
    assert repair(bad, "नमस्ते दोस्तों", "hi").segments[0].text == "नमस्ते दोस्तों"
    assert "female" in voice_instruct(p, p.segments[0])
    llm = mock_llm({"render plan": "not json"})
    assert plan("x y", "a man", "hi", llm).speaker["gender"] == "male"  # falls back to rules


def test_assemble_timing():
    sr = 24000
    p = RenderPlan("hi", segments=[Segment("a", t0=0.5, t1=1.5, pause_after_ms=300), Segment("b", t0=2.5)])
    synth = lambda seg: (voiced(200, 200, 1.4 if seg.text == "a" else 0.8, sr), sr)
    tl = assemble(p, synth, sr, event_lib=None)
    sp = [s for s in tl.spans if s["kind"] == "speech"]
    assert sp[0]["t0"] == pytest.approx(0.5, abs=0.01) and sp[0]["t1"] <= 1.5 + 0.25
    assert sp[1]["t0"] == pytest.approx(2.5, abs=0.01)
    y = wsola(voiced(200, 200, 1.0, sr), 1.15, sr)
    assert abs(len(y) / sr - 1.0 / 1.15) < 0.02


def _bank(n=30, dim=32, seed=0):
    rng = np.random.default_rng(seed)
    vs = [Voice(f"s{i}", f"r{i}.wav", "", "hi", "female" if i % 2 else "male", None, None, 150 + i * 3,
                rng.normal(size=dim)) for i in range(n)]
    return SpeakerBank(vs)


def test_speaker_prior_distinct():
    b = _bank()
    vs = b.sample(10, seed=1, lang="hi", gender="female")
    assert len(vs) == 10 and len({v.speaker_id for v in vs}) == 10
    assert all(v.gender == "female" for v in vs)
    E = np.stack([v.emb / np.linalg.norm(v.emb) for v in vs])
    S = E @ E.T
    assert (S[~np.eye(10, dtype=bool)] < 0.86).all()


def test_run_factored_with_mock_tts(tmp_path):
    sr = 24000

    class MockTTS:
        def clone_prompt(self, ref, txt):
            return ref

        def clone(self, text, ref, seed=0, prompt=None):
            return voiced(150 + seed % 7, 150, 1.0, sr, seed=seed), sr

        def design(self, text, instruct, seed=0):
            return voiced(200, 200, 1.0, sr, seed=seed), sr

    item = {"item_id": "d1", "lang": "hi", "text": "नमस्ते", "description": "A woman on a phone call in a small room"}
    outs = run_factored(item, 3, MockTTS(), None, _bank(), EcologyRenderer(sr), 7)
    assert len(outs) == 3 and all(o[1] == sr for o in outs)
    assert any(c["item_type"] == "Channel" for c in outs[0][2]["constructed_claims"])


# ---------------- training data ----------------
def test_pairs_and_allocation():
    s = SceneScore("hi", 5.0, [Claim("A woman speaks", "Speaker", 0.9, source="measurement", value={"gender": "female"}),
                               Claim("Door knock", "Other sounds", 1.0, t0=1.0, t1=1.3, source="construction",
                                     value={"event": "door knock"})])
    pr = captioner_dpo_pair(s, seed=3)
    assert pr["chosen"] != pr["rejected"]
    assert dominant_pairs([{"a": 1, "b": 0.1}, {"a": 0, "b": 0.5}, {"a": 0.5, "b": 0.05}],
                          {"a": 1, "b": -1}) == [(0, 1), (2, 1)]
    F = type_scores([{"Pitch": {"true_w": 2, "stated_w": 2, "contra_w": 0, "false_w": 0, "false_asserted_w": 0},
                      "Event": {"true_w": 2, "stated_w": 0, "contra_w": 0, "false_w": 0, "false_asserted_w": 0}}])
    al = allocate(F, 100)
    assert al["Event"] > al["Pitch"]


# ---------------- data ----------------
def test_vaani_tags():
    t = "मैंने <static_noise> एक पेड़ </static_noise> देखा {dekha} [breathing] --"
    assert vaani_tags.clean(t) == "मैंने एक पेड़ देखा"
    assert ("breathing", "Event", "audible breathing") in vaani_tags.tag_events(t)
    assert not vaani_tags.is_usable("कुछ [unintelligible]")


def test_vaani_index_roundtrip(tmp_path):
    sr = 16000
    rows = []
    for i in range(6):
        b = io.BytesIO()
        sf.write(b, voiced(150, 150, 2.5, sr, seed=i), sr, format="WAV")
        rows.append({"audio": {"bytes": b.getvalue(), "path": f"{i}.wav"}, "language": "Hindi", "duration": 2.5,
                     "speakerID": f"spk{i % 3}", "gender": "female", "state": "Bihar", "district": f"d{i % 2}",
                     "isTranscriptionAvailable": "Yes", "transcript": "नमस्ते"})
    d = tmp_path / "audio" / "Hindi"
    d.mkdir(parents=True)
    pq.write_table(pa.Table.from_pylist(rows), d / "train-00000-of-00001.parquet")
    df = vaani_index.build_index(str(d), "hi", str(tmp_path / "idx.parquet"), workers=1)
    assert len(df) == 6 and set(df.split) <= {"dev", "test", "train"}
    sel = df.head(2)
    paths = vaani_index.export(sel, str(tmp_path / "wav"))
    x, r = sf.read(paths[0])
    assert r == sr and len(x) == int(2.5 * sr)


# ---------------- test set ----------------
def test_testset_package(tmp_path):
    sr = 16000
    for lang, txt in (("hi", "आज मौसम बहुत अच्छा है"), ("ta", "இன்று வானிலை நன்றாக இருக்கிறது")):
        d = tmp_path / "src" / lang / "clips"
        d.mkdir(parents=True)
        with open(tmp_path / "src" / lang / "clips.csv", "w") as f:
            f.write("clip_id,speaker_id,notes\n")
            for i in range(30):
                sf.write(d / f"{lang}_c{i:02d}.wav", voiced(180, 180, 3.0, sr, seed=i), sr, subtype="PCM_16")
                f.write(f"{lang}_c{i:02d},spk{i % 10},staged\n")
        with open(tmp_path / "src" / lang / "descriptions.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["desc_id", "text", "description"])
            for i in range(30):
                w.writerow([f"{lang}_d{i:02d}", txt, "A woman speaks slowly to her son in a small room with a fan."])
    e, wn = check_lang(tmp_path / "src", "hi")
    assert e == []
    package(tmp_path / "src", tmp_path / "t.zip")
    import zipfile
    names = zipfile.ZipFile(tmp_path / "t.zip").namelist()
    assert "hi/captioner/inputs/hi_c00.wav" in names and "ta/generator/inputs/descriptions.csv" in names


def test_lint():
    w = lint_descriptions.lint("Maybe a woman laughs, she is calm so the pitch is low. " + "x " * 70)
    assert any("hedge" in s for s in w) and any("infers" in s for s in w) and any("without times" in s for s in w)
