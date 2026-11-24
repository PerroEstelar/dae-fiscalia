# -*- coding: utf-8 -*-
"""Mide una voz grabada y arma su cadena de ecualización y dinámica (Delitos informáticos, 24 nov 2026).

Sebastián: «me recomendaron que mejorara los niveles y ecualización de estos videos». La cadena fija de los profes
(`srpa_audio.CADENA`: paso alto 80 Hz, −2 dB a 250 Hz, +3 dB a 3 kHz, compresor) se pensó para otra grabación. Esta
mide cada voz contra la curva media de voz hablada (LTASS de Byrne et al., 1994, por tercios de octava) y corrige la
diferencia, con topes, más reducción de ruido, de-esser y compresión.

    python3 voz_analisis.py <voz.wav> [...]         → medidas, curva y cadena propuesta (JSON)

Lo que se mide (voz a 48 kHz, mono):
- **piso de ruido y voz**: percentiles 10 y 90 del RMS en ventanas de 50 ms (dBFS); `snr` es la resta.
- **sonoridad** integrada (`I`, LUFS) con ebur128 de ffmpeg si se pasa `--lufs` (la usa la ganancia previa).
- **espectro largo de la voz** (LTAS) en tercios de octava, solo en ventanas con voz (RMS sobre piso + 15 dB),
  normalizado a la media de 500–2000 Hz; la referencia se normaliza igual.

La cadena (sin loudnorm, que pone después la cadena de composición en dos pasadas), ver `cadena()`:
paso alto 90 Hz → ganancia previa a −20 LUFS → `firequalizer` con la curva (70 % de la diferencia con la
referencia, suavizada, topes −8/+7 dB, nada sobre 12,5 kHz) → `afftdn` suave → expansor → compresor de picos →
de-esser suave → limitador.
"""
import json
import subprocess
import sys
import wave

import numpy as np

BANDAS = [100, 125, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250, 1600, 2000, 2500, 3150, 4000, 5000, 6300,
          8000, 10000, 12500]
# LTASS media (Byrne et al. 1994, voz masculina y femenina, 70 dB SPL) en dB por tercio de octava
BYRNE = {100: 54.0, 125: 57.5, 160: 59.0, 200: 60.0, 250: 60.5, 315: 60.0, 400: 59.5, 500: 58.5, 630: 56.0,
         800: 54.0, 1000: 52.5, 1250: 51.0, 1600: 49.5, 2000: 48.0, 2500: 47.0, 3150: 46.0, 4000: 45.0, 5000: 43.5,
         6300: 42.0, 8000: 40.0, 10000: 38.0, 12500: 36.0}
NORMA = [500, 630, 800, 1000, 1250, 1600, 2000]
PROPORCION, TOPE_MENOS, TOPE_MAS = 0.7, -8.0, 7.0


def leer(p):
    w = wave.open(p)
    x = np.frombuffer(w.readframes(w.getnframes()), dtype='<i2').astype(np.float64) / 32768.0
    if w.getnchannels() > 1:
        x = x.reshape(-1, w.getnchannels()).mean(axis=1)
    return x, w.getframerate()


def rel(d):
    base = np.mean([d[b] for b in NORMA])
    return {b: d[b] - base for b in BANDAS}


def lufs(p):
    r = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-i', p, '-af', 'ebur128', '-f', 'null', '-'],
                       capture_output=True, text=True, errors='replace').stderr
    t = r[r.rfind('Summary'):]
    return float(t.split('I:')[1].split('LUFS')[0])


def medir(p, con_lufs=True):
    x, sr = leer(p)
    n = int(0.05 * sr)
    k = len(x) // n
    v = x[:k * n].reshape(k, n)
    rms = 20 * np.log10(np.sqrt((v ** 2).mean(axis=1)) + 1e-12)
    piso, voz = np.percentile(rms, 10), np.percentile(rms, 90)
    hab = v[rms > piso + 15]
    S = (np.abs(np.fft.rfft(hab * np.hanning(n), axis=1)) ** 2).mean(axis=0)
    f = np.fft.rfftfreq(n, 1 / sr)
    db = {}
    for c in BANDAS:
        lo, hi = c / 2 ** (1 / 6), c * 2 ** (1 / 6)
        db[c] = 10 * np.log10(S[(f >= lo) & (f < hi)].sum() + 1e-20)
    m = dict(piso=round(float(piso), 1), voz=round(float(voz), 1), snr=round(float(voz - piso), 1),
             ltas={c: round(float(v), 1) for c, v in rel(db).items()})
    if con_lufs:
        m['I'] = lufs(p)
    return m


def curva(m):
    """Ganancia por banda: el 70 % de lo que falta o sobra frente a la referencia, suavizada (media de tres bandas
    vecinas) y con topes; 0 dB sobre 12,5 kHz."""
    ref = rel(BYRNE)
    d = np.array([m['ltas'][b] - ref[b] for b in BANDAS])
    g = -PROPORCION * d
    g = np.convolve(np.pad(g, 1, mode='edge'), np.ones(3) / 3, mode='valid')
    g = np.clip(g, TOPE_MENOS, TOPE_MAS)
    g[-1] = min(g[-1], 3.0)
    return {b: round(float(x), 1) for b, x in zip(BANDAS, g)}


def cadena(m, meta_previa=-20.0):
    """Probada en la nube sobre 2 min de cada grabación (24 nov), contra la cadena de siempre, ambas con loudnorm
    I=-16:TP=-3: el desvío espectral frente a la referencia (RMS de 125 Hz a 8 kHz) baja de 8–9 dB (original) y 7
    (cadena de siempre) a 3–3,6; el piso de ruido en las pausas, 2 a 9 dB más abajo.
    - `afftdn` va DESPUÉS de la curva y suave (nr 6): antes de la curva y con nr 12 se comía los agudos (que en estas
      grabaciones tienen solo 8–10 dB sobre el ruido) y el desvío quedaba igual que sin ecualizar.
    - `agate` como expansor suave (2:1, rango −10 dB) baja el ambiente entre frase y frase.
    - El compresor solo toca los picos (−12 dB sobre una voz llevada a −20 LUFS) y el limitador deja margen para
      que loudnorm llegue cerca de −16 con techo −3 (el de siempre, por el AAC de Resolve)."""
    g = curva(m)
    fs = ['highpass=f=90:poles=2']
    if 'I' in m:
        fs.append('volume=%.1fdB' % (meta_previa - m['I']))
    ent = ';'.join('entry(%d,%.1f)' % (b, x) for b, x in g.items()) + ';entry(16000,0);entry(20000,0)'
    fs.append("firequalizer=gain_entry='%s'" % ent)
    if m['piso'] > -66:
        fs.append('afftdn=nr=6:nf=-50:tn=1')
    fs.append('agate=threshold=0.025:ratio=2:range=0.3:attack=10:release=300:knee=2')
    fs.append('acompressor=threshold=-12dB:ratio=3:attack=5:release=120:makeup=1:knee=4')
    fs.append('deesser=i=0.2:m=0.5:f=0.5:s=o')
    fs.append('alimiter=limit=0.35:attack=5:release=80:level=disabled')
    return ','.join(fs), g


if __name__ == '__main__':
    out = {}
    for p in sys.argv[1:]:
        m = medir(p)
        c, g = cadena(m)
        out[p] = dict(medidas=m, curva=g, cadena=c)
    print(json.dumps(out, ensure_ascii=False, indent=1))
