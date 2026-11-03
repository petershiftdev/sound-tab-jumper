"""Generate original looping stems: beat, vocal, instruments."""

from __future__ import annotations

from pathlib import Path

import lameenc
import numpy as np

SR = 44100
BPM = 120
BARS = 8
BEATS = BARS * 4
SECONDS = BEATS * 60.0 / BPM
N = int(round(SECONDS * SR))
RNG = np.random.default_rng(11)

ROOT = Path(__file__).resolve().parent


def midi_hz(m: float) -> float:
    return 440.0 * (2.0 ** ((m - 69.0) / 12.0))


def beat_to_sample(beat: float) -> int:
    return int(round(beat * (60.0 / BPM) * SR))


def adsr(n: int, attack: float, decay: float, sustain: float, release: float) -> np.ndarray:
    a = max(1, int(attack * SR))
    d = max(1, int(decay * SR))
    r = max(1, int(release * SR))
    s = max(0, n - a - d - r)
    env = np.concatenate(
        [
            np.linspace(0.0, 1.0, a, endpoint=False),
            np.linspace(1.0, sustain, d, endpoint=False),
            np.full(s, sustain, dtype=np.float64),
            np.linspace(sustain, 0.0, r),
        ]
    )
    if len(env) < n:
        env = np.pad(env, (0, n - len(env)))
    return env[:n]


def one_pole(x: np.ndarray, cutoff: float, highpass: bool = False) -> np.ndarray:
    a = 1.0 - np.exp(-2.0 * np.pi * cutoff / SR)
    y = np.empty_like(x)
    acc = 0.0
    for i, sample in enumerate(x):
        acc += a * (sample - acc)
        y[i] = acc
    return x - y if highpass else y


def comb_reverb(x: np.ndarray, delays_ms: tuple[float, ...], decay: float) -> np.ndarray:
    y = x.copy()
    for i, ms in enumerate(delays_ms, start=1):
        d = int(SR * ms / 1000.0)
        if 0 < d < len(x):
            y[d:] += x[:-d] * (decay ** i)
    peak = np.max(np.abs(y))
    if peak > 1e-6:
        y *= np.max(np.abs(x)) / peak
    return y


def mix_at(dest: np.ndarray, src: np.ndarray, start: int, gain: float = 1.0, pan: float = 0.0) -> None:
    if src.ndim == 1:
        left = src * (gain * np.sqrt(0.5 * (1.0 - pan)))
        right = src * (gain * np.sqrt(0.5 * (1.0 + pan)))
        stereo = np.stack([left, right], axis=1)
    else:
        stereo = src * gain
    end = min(len(dest), start + len(stereo))
    chunk = stereo[: end - start]
    dest[start:end] += chunk


def render_kick() -> np.ndarray:
    n = int(0.45 * SR)
    t = np.arange(n) / SR
    freq = 42.0 + 130.0 * np.exp(-t * 20.0)
    body = np.sin(2.0 * np.pi * np.cumsum(freq) / SR) * np.exp(-t * 6.2)
    sub = np.sin(2.0 * np.pi * 48.0 * t) * np.exp(-t * 4.8) * 0.55
    click = np.sin(2.0 * np.pi * 1800.0 * t) * np.exp(-t * 70.0) * 0.28
    return body + sub + click


def render_snare() -> np.ndarray:
    n = int(0.28 * SR)
    t = np.arange(n) / SR
    noise = one_pole(RNG.standard_normal(n), 1800.0, highpass=True)
    snap = noise * np.exp(-t * 16.0)
    tone = np.sin(2.0 * np.pi * 186.0 * t) * np.exp(-t * 14.0)
    tone2 = np.sin(2.0 * np.pi * 330.0 * t) * np.exp(-t * 18.0) * 0.4
    return snap * 0.72 + tone * 0.38 + tone2


def render_hat(open_hat: bool = False) -> np.ndarray:
    n = int((0.18 if open_hat else 0.055) * SR)
    t = np.arange(n) / SR
    noise = one_pole(RNG.standard_normal(n), 6500.0, highpass=True)
    decay = 9.0 if open_hat else 55.0
    return noise * np.exp(-t * decay)


def render_tom(midi: float) -> np.ndarray:
    n = int(0.22 * SR)
    t = np.arange(n) / SR
    f0 = midi_hz(midi)
    freq = f0 * (1.0 + 0.35 * np.exp(-t * 28.0))
    return np.sin(2.0 * np.pi * np.cumsum(freq) / SR) * np.exp(-t * 11.0)


def make_beat() -> np.ndarray:
    out = np.zeros((N, 2), dtype=np.float64)
    kick = render_kick()
    snare = render_snare()
    hat_c = render_hat(False)
    hat_o = render_hat(True)
    tom = render_tom(52)

    for bar in range(BARS):
        base = bar * 16
        mix_at(out, kick, beat_to_sample(base / 4), 0.95)
        mix_at(out, kick, beat_to_sample((base + 8) / 4), 0.88)
        if bar % 2 == 1:
            mix_at(out, kick, beat_to_sample((base + 14) / 4), 0.62)
        mix_at(out, snare, beat_to_sample((base + 4) / 4), 0.72, pan=0.05)
        mix_at(out, snare, beat_to_sample((base + 12) / 4), 0.78, pan=-0.05)
        if bar in (3, 7):
            mix_at(out, tom, beat_to_sample((base + 10) / 4), 0.4, pan=-0.25)
        for step in range(16):
            if step % 2:
                mix_at(
                    out,
                    hat_o if step % 8 == 7 else hat_c,
                    beat_to_sample((base + step) / 4),
                    0.16 if step % 8 == 7 else 0.11,
                    pan=0.35 if step % 4 < 2 else -0.35,
                )
    return out


def voice_wave(freq: float, t: np.ndarray) -> np.ndarray:
    vib = freq * (1.0 + 0.011 * np.sin(2.0 * np.pi * 5.4 * t))
    phase = 2.0 * np.pi * np.cumsum(vib) / SR
    harmonics = (
        1.00 * np.sin(phase)
        + 0.42 * np.sin(2 * phase)
        + 0.28 * np.sin(3 * phase)
        + 0.12 * np.sin(4 * phase)
        + 0.06 * np.sin(5 * phase)
    )
    breath = one_pole(RNG.standard_normal(len(t)), 2500.0, highpass=True) * 0.03
    return harmonics + breath


def make_vocal() -> np.ndarray:
    out = np.zeros((N, 2), dtype=np.float64)
    melody = [
        (0.0, 1.0, 69, 0.72),
        (1.0, 1.0, 72, 0.76),
        (2.0, 2.0, 76, 0.88),
        (4.0, 1.0, 77, 0.62),
        (5.0, 1.0, 76, 0.74),
        (6.0, 2.0, 72, 0.78),
        (8.0, 2.0, 74, 0.74),
        (10.0, 1.0, 72, 0.66),
        (11.0, 1.0, 69, 0.70),
        (12.0, 4.0, 64, 0.82),
        (16.0, 0.5, 69, 0.70),
        (16.5, 0.5, 72, 0.74),
        (17.0, 0.5, 76, 0.82),
        (17.5, 0.5, 79, 0.78),
        (18.0, 1.0, 76, 0.84),
        (19.0, 1.0, 72, 0.72),
        (20.0, 2.0, 74, 0.76),
        (22.0, 2.0, 72, 0.70),
        (24.0, 3.0, 69, 0.86),
        (27.0, 1.0, 67, 0.64),
        (28.0, 4.0, 69, 0.90),
    ]
    mono = np.zeros(N, dtype=np.float64)
    for start, length, note, vel in melody:
        n = beat_to_sample(length)
        t = np.arange(n) / SR
        wave = voice_wave(midi_hz(note), t)
        env = adsr(n, 0.045, 0.12, 0.72, min(0.28, length * 60.0 / BPM * 0.45))
        mix_start = beat_to_sample(start)
        end = min(N, mix_start + n)
        mono[mix_start:end] += wave[: end - mix_start] * env[: end - mix_start] * vel
    mono = one_pole(mono, 4200.0)
    mono = comb_reverb(mono, (38, 67, 96, 128), 0.38)
    delay = int(0.086 * SR)
    left = mono.copy()
    right = np.zeros_like(mono)
    right[delay:] = mono[:-delay] * 0.55
    right += mono * 0.45
    out[:, 0] = left
    out[:, 1] = right
    return out * 0.55


def additive_pad(freq: float, n: int, detune: float) -> np.ndarray:
    t = np.arange(n) / SR
    s = np.zeros(n, dtype=np.float64)
    for ratio, amp in ((1.0, 0.55), (2.0, 0.18), (3.0, 0.08), (4.0, 0.04)):
        s += amp * np.sin(2.0 * np.pi * freq * ratio * (1.0 + detune) * t)
    return s


def rhodes(freq: float, n: int) -> np.ndarray:
    t = np.arange(n) / SR
    mod = np.sin(2.0 * np.pi * freq * t)
    carrier = np.sin(2.0 * np.pi * freq * t + 2.4 * mod * np.exp(-t * 3.5))
    bell = np.sin(2.0 * np.pi * freq * 4.0 * t) * np.exp(-t * 8.0) * 0.12
    return (carrier + bell) * np.exp(-t * 1.8)


def make_instruments() -> np.ndarray:
    out = np.zeros((N, 2), dtype=np.float64)
    chords = [
        (0, [57, 60, 64, 67]),   # Am7
        (8, [53, 57, 60, 65]),   # F
        (16, [48, 52, 55, 60]),  # C
        (24, [55, 59, 62, 67]),  # G
    ]
    bass = [(0, 45), (8, 41), (16, 48), (24, 43)]

    for start_beat, notes in chords:
        n = beat_to_sample(8.2)
        env = adsr(n, 0.9, 0.4, 0.62, 1.4)
        start = beat_to_sample(start_beat)
        for i, note in enumerate(notes):
            pad_l = additive_pad(midi_hz(note), n, -0.0018)
            pad_r = additive_pad(midi_hz(note), n, 0.0021)
            g = 0.16 * env
            end = min(N, start + n)
            sl = end - start
            out[start:end, 0] += pad_l[:sl] * g[:sl]
            out[start:end, 1] += pad_r[:sl] * g[:sl]
            key = rhodes(midi_hz(note), beat_to_sample(3.2))
            mix_at(out, key, start, 0.11, pan=-0.2 + i * 0.12)

        arp = notes[1:] + notes[1:2]
        for step in range(16):
            note = arp[step % len(arp)]
            nn = beat_to_sample(0.55)
            t = np.arange(nn) / SR
            pluck = np.sin(2.0 * np.pi * midi_hz(note + 12) * t) * np.exp(-t * 7.5)
            mix_at(
                out,
                pluck,
                beat_to_sample(start_beat + step * 0.5),
                0.07,
                pan=-0.4 + (step % 4) * 0.25,
            )

    for start_beat, note in bass:
        for extra in (0.0, 2.0, 4.0, 6.0):
            n = beat_to_sample(1.8)
            t = np.arange(n) / SR
            f = midi_hz(note)
            body = np.sin(2.0 * np.pi * f * t) + 0.25 * np.sin(2.0 * np.pi * f * 2.0 * t)
            env = np.exp(-t * 2.4) * adsr(n, 0.01, 0.08, 0.7, 0.4)
            mix_at(out, body * env, beat_to_sample(start_beat + extra), 0.42)

    out[:, 0] = comb_reverb(out[:, 0], (29, 53, 81), 0.28)
    out[:, 1] = comb_reverb(out[:, 1], (31, 58, 88), 0.28)
    return out * 0.85


def peak_normalize(x: np.ndarray, peak: float = 0.92) -> np.ndarray:
    m = np.max(np.abs(x))
    if m < 1e-9:
        return x
    return x * (peak / m)


def encode_mp3(path: Path, stereo: np.ndarray) -> None:
    rms = float(np.sqrt(np.mean(np.square(stereo))))
    print(f"{path.name} rms={rms:.4f}")
    pcm = np.clip(peak_normalize(stereo), -1.0, 1.0)
    interleaved = (pcm * 32767.0).astype(np.int16).reshape(-1)
    encoder = lameenc.Encoder()
    encoder.set_bit_rate(192)
    encoder.set_in_sample_rate(SR)
    encoder.set_channels(2)
    encoder.set_quality(2)
    data = encoder.encode(interleaved.tobytes())
    data += encoder.flush()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    print(f"wrote {path} ({len(data)} bytes)")


def main() -> None:
    encode_mp3(ROOT / "beat" / "beat.mp3", make_beat())
    encode_mp3(ROOT / "vocal" / "vocal.mp3", make_vocal())
    encode_mp3(ROOT / "instruments" / "instruments.mp3", make_instruments())


if __name__ == "__main__":
    main()
