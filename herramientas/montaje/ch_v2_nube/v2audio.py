# -*- coding: utf-8 -*-
"""Audio de la V2 (casos del profe Carlos Humberto). Trabaja en tiempo de
muestra a 48 kHz sobre los stems de la linea (voz = A4/A5, fondo = el resto).

Operaciones, todas en tiempo de la V1 salvo `poner`, que va en tiempo V2:
  limpiar(voz, a, b)          silencia la voz vieja entre a y b (fundidos 15 ms)
  insertar(x, T, D, fuente)   mete D segundos en T; fondo: repite fuente..fuente+D
                              con fundido de igual potencia en las dos juntas;
                              voz: silencio
  poner(x, toma, t, g)        pone la toma nueva (recortada a su habla) en t
"""
import json
import subprocess

import numpy as np
import soundfile as sf

SR = 48000
U = '/mnt/user-data/uploads/DAE/_tmp/ch/'


def leer(p):
    y, sr = sf.read(p, dtype='float32', always_2d=True)
    assert sr == SR, (p, sr)
    if y.shape[1] == 1:
        y = np.repeat(y, 2, 1)
    return y


def leer_mp3(p):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-f', 'f32le', '-ac', '2', '-ar', str(SR), '-'],
                       capture_output=True, check=True)
    return np.frombuffer(r.stdout, np.float32).reshape(-1, 2).copy()


def s(t):
    return int(round(t * SR))


def env_db(y, hop=0.01):
    m = y.mean(1)
    h = int(SR * hop)
    n = len(m) // h
    r = np.sqrt((m[:n * h].reshape(n, h) ** 2).mean(1) + 1e-12)
    return 20 * np.log10(r)


def habla(y, umbral=-45.0):
    """(inicio, fin) en s de lo que suena por encima del umbral (dBFS, 10 ms)."""
    e = env_db(y)
    act = np.where(e > umbral)[0]
    return act[0] * 0.01, (act[-1] + 1) * 0.01


def rms_activo(y, rel=-30.0):
    e = env_db(y)
    m = e > e.max() + rel
    if not m.any():
        return -120.0
    h = int(SR * 0.01)
    mm = y.mean(1)[:len(e) * h].reshape(len(e), h)[m]
    return 10 * np.log10((mm ** 2).mean() + 1e-12)


def rampa(n, sube=True):
    r = np.sin(np.linspace(0, np.pi / 2, n)) ** 2 if n > 0 else np.zeros(0)
    return (r if sube else r[::-1]).astype(np.float32)[:, None]


def limpiar(voz, a, b, f=0.015):
    i, j, k = s(a), s(b), s(f)
    voz[i:j] = 0
    voz[max(0, i - k):i] *= rampa(min(k, i), False)
    voz[j:j + k] *= rampa(k, True)[:len(voz[j:j + k])]


def insertar(x, T, D, fuente=None, xf=0.6):
    """Inserta D s en T. fuente=None -> silencio. Si no, el hueco suena con
    x[fuente:fuente+D], con fundidos de igual potencia de xf s centrados en las
    dos juntas (si fuente+D == T la segunda junta es continua)."""
    i, n = s(T), s(D)
    if fuente is None:
        return np.concatenate([x[:i], np.zeros((n, 2), np.float32), x[i:]])
    a = s(fuente)
    k = s(xf) // 2
    y = np.concatenate([x[:i], x[a:a + n], x[i:]]).copy()
    up = np.sqrt(np.linspace(0, 1, 2 * k, dtype=np.float32))[:, None]
    dn = up[::-1]
    y[i - k:i + k] = x[i - k:i + k] * dn + x[a - k:a + k] * up
    y[i + n - k:i + n + k] = x[a + n - k:a + n + k] * dn + x[i - k:i + k] * up
    return y


def toma(path, pre=0.03, post=0.12):
    y = leer_mp3(path)
    a, b = habla(y, -50)
    y = y[max(0, s(a - pre)):s(b + post)].copy()
    k = s(0.004)
    y[:k] *= rampa(k)
    k = s(0.06)
    y[-k:] *= rampa(k, False)
    return y, a, b


def poner(x, clip, t, g_db=0.0):
    i = s(t)
    g = 10 ** (g_db / 20)
    if i + len(clip) > len(x):
        x = np.concatenate([x, np.zeros((i + len(clip) - len(x), 2), np.float32)])
    x[i:i + len(clip)] += clip * g
    return x


def lufs(y):
    p = '/tmp/claude-0/-home-claude/3ed68810-2da1-5d00-9607-4b64ae51b22f/scratchpad/ch/_lufs.wav'
    sf.write(p, y, SR, subtype='FLOAT')
    r = subprocess.run(['ffmpeg', '-nostats', '-i', p, '-af', 'ebur128=peak=true', '-f', 'null', '-'],
                       capture_output=True, text=True).stderr
    t = r[r.find('Summary'):]
    i = float(t.split('I:')[1].split('LUFS')[0])
    pk = float(t.split('Peak:')[1].split('dBFS')[0])
    return i, pk


def limitar(y, techo_db=-1.0, ataque=0.002, suelta=0.08):
    """Limitador con mirada adelante (4x sobremuestreo para picos verdaderos)."""
    from scipy.signal import resample_poly
    up = resample_poly(y, 4, 1, axis=0)
    pk = np.abs(up).max(1).reshape(-1, 4).max(1)[:len(y)]
    techo = 10 ** (techo_db / 20)
    need = np.minimum(1.0, techo / np.maximum(pk, 1e-9))
    la = int(SR * ataque)
    # minimo deslizante hacia adelante (mirada adelante)
    from scipy.ndimage import minimum_filter1d
    g = minimum_filter1d(need, size=2 * la + 1, origin=0)
    g = np.convolve(g, np.ones(la + 1) / (la + 1), mode='same')
    # suelta exponencial
    a = np.exp(-1.0 / (SR * suelta))
    out = np.empty_like(g)
    cur = 1.0
    for idx in range(len(g)):
        v = g[idx]
        cur = v if v < cur else v + (cur - v) * a
        out[idx] = cur
    return y * out[:, None].astype(np.float32)
