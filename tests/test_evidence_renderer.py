import numpy as np
import pytest

from rimet2.evidence import dsp, pitch, timing
from rimet2.evidence.run import claims_from_evidence, collect, scene_from_audio
from rimet2.renderer import channel, mix, rir, splice
from rimet2.renderer.render import EcologyRenderer, FoleyLibrary
from rimet2.scene.schema import Ecology, EnvEvent
from rimet2.scene.verbalize import verbalize

from synth import utterance, voiced


def test_yin_tracks_glide():
    sr = 16000
    x = voiced(150, 150, 1.0, sr)
    t, f0, ap = pitch.yin(x, sr)
    st = pitch.stats(f0)
    assert abs(st.median_hz - 150) / 150 < 0.02
    assert pitch.semitones(100, 200) == pytest.approx(12.0)


def test_vad_and_pause():
    sr = 16000
    x, spans = utterance(sr, pause=0.6)
    segs = dsp.energy_vad(x, sr)
    assert len(segs) == 2
    assert abs(segs[0][1] - spans[0][1]) < 0.1 and abs(segs[1][0] - spans[1][0]) < 0.1
    tm = timing.timing(x, sr, segs)
    assert len(tm.pauses) == 1 and abs((tm.pauses[0][1] - tm.pauses[0][0]) - 0.6) < 0.15
    assert 3 <= tm.rate_syl_s <= 7  # synthetic syllable rate is 5/s


def test_bandwidth_narrowband_after_phone_channel():
    sr = 16000
    x, _ = utterance(sr)
    assert not dsp.bandwidth(x, sr).narrowband
    y, info = channel.apply_channel(x, sr, "phone_narrowband")
    assert info["codec"] == "gsm"
    assert dsp.bandwidth(y, sr).narrowband


def test_codecs_roundtrip_length():
    sr = 24000
    x = voiced(180, 180, 1.0, sr)
    for c in ["g711", "gsm", "g722", "opus_16k"]:
        y = channel.ffmpeg_codec(x, sr, c)
        assert len(y) == len(x) and np.isfinite(y).all()


def test_polack_rt60_measured():
    sr = 16000
    rng = np.random.default_rng(0)
    for target in [0.3, 0.8]:
        r = rir.polack_rir(target, sr, rng)
        assert abs(dsp.rt60_from_rir(r, sr) - target) / target < 0.2


def test_bed_snr_exact():
    sr = 16000
    x, _ = utterance(sr)
    rng = np.random.default_rng(0)
    y, info = mix.add_bed(x, sr, rng.standard_normal(sr), 10.0, rng)
    assert abs(info["bed_snr_db"] - 10.0) < 0.5


def test_splice_shift():
    sr = 16000
    x = np.ones(sr, np.float32)
    y, info = splice.insert_at(x, sr, np.zeros(sr // 2, np.float32), 0.5)
    assert len(y) == int(1.5 * sr) and info["shift_s"] == 0.5
    assert np.all(y[:8000] == 1) and np.all(y[16000:] == 1)
    assert splice.shift_spans([(0.2, 0.3), (0.7, 0.9)], 0.5, 0.5) == [(0.2, 0.3), (1.2, 1.4)]


def test_renderer_labels_are_true(tmp_path):
    sr = 24000
    x, _ = utterance(sr)
    # Foley library with one synthetic "door knock" file
    import soundfile as sf
    knock = (np.random.default_rng(1).standard_normal(int(0.3 * sr)) * np.exp(-np.linspace(0, 8, int(0.3 * sr))))
    sf.write(tmp_path / "knock.wav", knock.astype(np.float32), sr)
    (tmp_path / "foley.csv").write_text(f"path,label,licence\n{tmp_path / 'knock.wav'},door knock,CC0\n")
    R = EcologyRenderer(sr, foley=FoleyLibrary.from_csv(tmp_path / "foley.csv", sr))
    eco = Ecology(channel="phone_narrowband", space="bathroom", background="fan hum", snr_db=8,
                  events=[EnvEvent("door knock", 1.0, 1.3, level_db_rel_speech=0)])
    y, claims, log = R.render(x, eco, coupling=[{"t0": 2.0, "gain_db": 6}], seed=3)
    types = {c.item_type for c in claims}
    assert {"Space", "Other sounds", "Channel", "Coupling"} <= types
    ev = [c for c in claims if c.value.get("event") == "door knock"][0]
    assert ev.t0 == pytest.approx(1.0, abs=0.01)
    room = [s["room"] for s in log["steps"] if "room" in s][0]
    assert 0.5 < room["rt60_s"] < 1.2
    # measured evidence on the rendered audio agrees with the constructed channel label
    from rimet2.common.audio import resample
    assert dsp.bandwidth(resample(y, sr, 16000), 16000).narrowband


def test_evidence_pipeline_cpu():
    sr = 16000
    x, _ = utterance(sr, f0=210)
    scene, ev = scene_from_audio(x, "hi", sr=sr)
    types = {c.item_type for c in scene.claims}
    assert "Pitch" in types and "Timing" in types
    pc = [c for c in scene.claims if "f0_median_hz" in c.value][0]
    assert abs(pc.value["f0_median_hz"] - 210) < 15
    text = verbalize(scene)
    assert "Hz" in text and len(text.split()) <= 300
