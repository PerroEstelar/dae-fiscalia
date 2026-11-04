# -*- coding: utf-8 -*-
r"""ED C5: los golpes de aire en la voz del funcionario (Sebastian, marcador
1051 de su linea: «mucho golpeo de aire en el micrófono»).

Medido por bloque en el master (fraccion de la energia bajo 80 Hz, en los
tramos con voz): Pilar 0,02-0,07 % en el p95; Julian e05 70 % en el p95 y
92 % en el p99 (golpes de aire: bajo 80 Hz no hay voz), e11 4,3 %. Solo los
dos bloques de Julian pasan por un paso alto de 100 Hz de cuatro polos (dos
`highpass` de ffmpeg en cascada: -24 dB en 50 Hz, -42 en 30 Hz; la
fundamental de su voz esta por encima de 100 Hz). Se empalma con fundidos de
20 ms en los silencios entre bloques; el resto del master queda identico y
mide lo mismo. El nivel del habla (banda 200-4000 Hz) se conserva: si el paso
alto le quita algo, se le devuelve con ganancia.

    python aire_c5.py      escribe ED_C5_NARRADOR_v3.wav (el master lo tiene
                           abierto Resolve: entra con `cirugia_ed C5 v=2 cambiar`)

SEGUNDA PASADA (v3). Con el paso alto solo, medido en envolvente de 20 ms: los
golpes de e05 bajaron de -7 dBFS (¡8 dB por ENCIMA del habla!) a -24, todavia
8,5 dB bajo el habla; en Pilar quedan 32 dB bajo. Lo que queda son los golpes
de aire: ahi, y solo ahi, se pasa a un paso alto de 200 Hz (cuatro polos). El
detector: tramos de 10 ms con energia bajo 60 Hz por encima de -40 dBFS (en la
voz de Julian, normal, eso no pasa nunca: maximo -41 en e11; en e05 hay un
golpe de -6 dBFS entre «real...» y «o es», 1,15-1,42 s del bloque), ensanchados
30 ms y con rampas de 10 ms. Un primer intento con «graves a menos de 10 dB del
habla» marcaba 1,4 s de e05: la voz de un hombre tiene graves y se la comia.
Fuera de esos tramos queda el paso alto de 100 Hz, que no toca el cuerpo de la
voz.
"""
import glob
import json
import os
import subprocess
import sys

import numpy as np

H = r'D:\DAE\_repo\herramientas'
sys.path.insert(0, os.path.join(H, 'voz', 'textos'))
import rutas_ed as R          # noqa: E402

FF = (glob.glob(r'C:\Users\call_\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg*'
                r'\*\bin\ffmpeg.exe') or ['ffmpeg'])[0]
SR = 48000
V = R.voces('C5')
MASTER = os.path.join(V, 'ED_C5_NARRADOR.wav')
MASTER_V2 = MASTER[:-4] + '_v3.wav'
BLOQUES = ('e05_el_apodo', 'e11_o_su_amante')
MARGEN = 0.20
FUNDE = 0.020


def lee(p, af=None):
    a = [FF, '-v', 'error', '-i', p]
    if af:
        a += ['-af', af]
    a += ['-ac', '2', '-ar', str(SR), '-f', 'f32le', '-']
    o = subprocess.run(a, capture_output=True, check=True).stdout
    return np.frombuffer(o, np.float32).reshape(-1, 2).copy()


def bandas(seg):
    m = seg.mean(axis=1)
    n, h = 4096, 1024
    fr = np.lib.stride_tricks.sliding_window_view(m, n)[::h] * np.hanning(n)
    S = np.abs(np.fft.rfft(fr, axis=1)) ** 2
    f = np.fft.rfftfreq(n, 1.0 / SR)
    tot = S.sum(axis=1) + 1e-12
    e = 10 * np.log10(tot)
    v = e > e.max() - 40
    lo = S[:, f < 80].sum(axis=1) / tot
    habla = S[:, (f >= 200) & (f < 4000)].sum(axis=1)
    return (float(np.percentile(lo[v], 95)) * 100, float(np.percentile(lo[v], 99)) * 100,
            10 * np.log10(habla[v].mean() + 1e-12))


def main():
    rej = json.load(open(os.path.join(V, 'ED_C5_rejilla.json'), encoding='utf-8'))
    tr = {t['bloque']: t for t in rej['tramos']}
    x = lee(MASTER)
    y = lee(MASTER, 'highpass=f=100:poles=2,highpass=f=100:poles=2')
    y2 = lee(MASTER, 'highpass=f=200:poles=2,highpass=f=200:poles=2')
    gr = lee(MASTER, 'lowpass=f=60:poles=2,lowpass=f=60:poles=2').mean(axis=1)
    assert len(x) == len(y) == len(y2) == len(gr), (len(x), len(y))
    h10 = int(0.010 * SR)

    def env(v, a0, a1):
        n = (a1 - a0) // h10
        return 20 * np.log10(np.sqrt((v[a0:a0 + n * h10].reshape(n, h10) ** 2).mean(axis=1)) + 1e-9)
    out = x.copy()
    f = int(FUNDE * SR)
    rampa = np.linspace(0, 1, f, dtype=np.float32)[:, None]
    for b in BLOQUES:
        a0 = int((tr[b]['entra'] - MARGEN) * SR)
        a1 = int((tr[b]['sale'] + MARGEN) * SR)
        antes = bandas(x[a0:a1])
        # los golpes: energia bajo 60 Hz por encima de -40 dBFS
        eg = env(gr, a0, a1)
        golpe = eg > -40
        k = 3                                              # 30 ms a cada lado
        golpe = np.convolve(golpe.astype(float), np.ones(2 * k + 1), 'same') > 0
        m = np.repeat(golpe.astype(np.float32), h10)
        m = np.concatenate([m, np.zeros(a1 - a0 - len(m), np.float32)])
        m = np.convolve(m, np.ones(h10, np.float32) / h10, 'same')[:, None]   # rampas de 10 ms
        seg = y[a0:a1] * (1 - m) + y2[a0:a1] * m
        print('%-16s golpes: %d tramos de 10 ms (%.0f ms)' % (b, int(golpe.sum()), golpe.sum() * 10),
              flush=True)
        desp = bandas(seg)
        g = 10 ** ((antes[2] - desp[2]) / 20.0)
        seg *= g
        fun = np.ones((a1 - a0, 1), np.float32)
        fun[:f] = rampa
        fun[-f:] = rampa[::-1]
        out[a0:a1] = x[a0:a1] * (1 - fun) + seg * fun
        fin = bandas(out[a0:a1])
        print('%-16s <80 Hz p95 %.2f%% -> %.2f%%  p99 %.2f%% -> %.2f%%  habla %.2f -> %.2f dB'
              ' (ganancia %+.2f dB)' % (b, antes[0], fin[0], antes[1], fin[1], antes[2], fin[2],
                                        20 * np.log10(g)), flush=True)
    assert len(out) == len(x)
    pk = float(np.abs(out).max())
    tmp = MASTER[:-4] + '__nuevo.wav'
    p = subprocess.run([FF, '-y', '-v', 'error', '-f', 'f32le', '-ar', str(SR), '-ac', '2',
                        '-i', '-', '-c:a', 'pcm_s24le', tmp], input=out.astype(np.float32).tobytes())
    assert p.returncode == 0
    os.replace(tmp, MASTER_V2)
    n2 = len(lee(MASTER_V2))
    d = np.abs(lee(MASTER_V2) - x)
    fuera = np.ones(len(x), bool)
    for b in BLOQUES:
        fuera[int((tr[b]['entra'] - MARGEN) * SR):int((tr[b]['sale'] + MARGEN) * SR)] = False
    print('pico %.3f | muestras %d = %d | diferencia fuera de los bloques %.6f'
          % (pk, len(x), n2, float(d[fuera].max())), flush=True)


if __name__ == '__main__':
    main()
