# -*- coding: utf-8 -*-
"""Voz y fondo de la V2, caso por caso.

Orden: (1) la voz de la V1 se centra -en las seis V1 la narracion sale 7,7 dB
cargada a la izquierda: el mp3 mono va en A4 (estereo: solo canal izquierdo)
y en A5 (mono: centro)-; (2) se silencian los tramos viejos; (3) se abren los
huecos de tiempo (insertos) en voz y fondo; (4) entran las tomas nuevas, al
nivel del tramo que reemplazan; (5) se normaliza el par a -18 LUFS (misma
ganancia a voz y fondo, para que la linea quede editable).
Los tiempos de `limpiar` y de `nivel` son de la V1; `t` de cada toma, de la V2.
"""
import json
import sys

import numpy as np
import soundfile as sf

sys.path.insert(0, '/tmp/claude-0/-home-claude/3ed68810-2da1-5d00-9607-4b64ae51b22f/scratchpad/ch')
import v2audio as A     # noqa: E402

U = A.U
TTS = U + 'tts/CH_U1_%s.mp3'
OUT = '/tmp/claude-0/-home-claude/3ed68810-2da1-5d00-9607-4b64ae51b22f/scratchpad/ch/out/'
OBJ = -18.0
FPS = 24000 / 1001

PLAN = {
 1: dict(limpiar=[(76.72, 82.40)],
         tomas=[('C01_r1_b', 76.80, (76.80, 82.08))]),
 4: dict(limpiar=[(27.70, 35.45), (82.30, 86.70)],
         # insertos: puerta +72 cuadros en el 851 (corte a negro); cocina/patio +146 en el 2069 (rotulo final)
         insertos=[(851 / FPS, 72 / FPS, (851 - 72) / FPS), (2069 / FPS, 146 / FPS, (2069 - 146) / FPS)],
         tomas=[('C04_r1_b', 27.78, (27.78, 35.20)), ('C04_r2_a', 82.38 + 72 / FPS, (82.38, 86.48))]),
 5: dict(limpiar=[(40.62, 59.70)],
         tomas=[('C05_r1_b', 40.55, (40.70, 50.56)), ('C05_r2_b', 51.70, (51.50, 59.50))]),
 2: dict(limpiar=[(37.60, 41.35), (80.95, 90.45)],
         # inserto en el cuadro 2088 (87,09 s, cena, antes del carton «Vincular»): 116 cuadros
         insertos=[(2088 / FPS, 116 / FPS, (2088 - 116) / FPS)],
         tomas=[('C02_r1_b', 37.95, (38.06, 40.90)), ('C02_r2_c', 81.10, (81.10, 89.98))]),
 3: dict(limpiar=[(33.40, 36.10), (64.08, 69.62), (69.80, 80.45), (81.92, 94.60)],
         # inserto: en el cuadro 2233 (93.135 s, entra el rotulo final) 474 cuadros
         # (19.770 s); el fondo repite la musica de los 19.77 s anteriores
         insertos=[(2233 / FPS, 474 / FPS, (2233 - 474) / FPS)],
         tomas=[('C03_r1_a', 33.54, (33.54, 35.72)), ('C03_r2_a', 64.20, (64.20, 67.82)),
                ('C03_r3_b', 69.92, (69.92, 79.96)), ('C03_r4_b', 82.04, (82.04, 94.12)),
                ('C03_i1_a', 95.68, (69.92, 94.12))]),
 6: dict(limpiar=[(16.12, 22.95), (37.74, 46.50)],
         tomas=[('C06_r1_a', 16.20, (16.20, 22.64)), ('C06_r2_b', 37.90, (37.82, 46.06))]),
}


def centrar(v):
    m = (v[:, 0] + v[:, 1]) * 0.5412
    return np.stack([m, m], 1).astype(np.float32)


def caso(n, p, voz=None, fondo=None):
    if voz is None:
        voz = A.leer(U + 'stems/CH_U1_C%02d_voz.flac' % n)
        fondo = A.leer(U + 'stems/CH_U1_C%02d_fondo.flac' % n)
    voz = centrar(voz)
    v1 = voz.copy()
    for a, b in p.get('limpiar', []):
        A.limpiar(voz, a, b)
    # insertos de tiempo: (T en V1, D, fuente del fondo en V1); de atras hacia adelante
    for T, D, F in sorted(p.get('insertos', []), reverse=True):
        voz = A.insertar(voz, T, D, None)
        fondo = A.insertar(fondo, T, D, F)
    reg = []
    for t, at, (oa, ob) in p['tomas']:
        clip, sa, sb = A.toma(TTS % t)
        clip = centrar(clip * np.float32(1 / 0.5412 / 2))   # mono puro, mismo nivel
        g = A.rms_activo(v1[A.s(oa):A.s(ob)]) - A.rms_activo(clip)
        voz = A.poner(voz, clip, at - 0.03, g)
        reg.append(dict(toma=t, t=at, dur=round(float(sb - sa), 2), fin=round(float(at + sb - sa), 2),
                        gan_db=round(float(g), 2)))
    L = max(len(voz), len(fondo))
    voz = np.pad(voz, ((0, L - len(voz)), (0, 0)))
    fondo = np.pad(fondo, ((0, L - len(fondo)), (0, 0)))
    i0, _ = A.lufs(voz + fondo)
    g = OBJ - i0
    voz *= np.float32(10 ** (g / 20))
    fondo *= np.float32(10 ** (g / 20))
    mezcla = A.limitar(voz + fondo, -1.0)
    i1, pk1 = A.lufs(mezcla)
    sf.write(OUT + 'CH_U1_C%02d_voz_v2.flac' % n, voz, 48000, subtype='PCM_24')
    sf.write(OUT + 'CH_U1_C%02d_fondo_v2.flac' % n, fondo, 48000, subtype='PCM_24')
    sf.write(OUT + 'CH_U1_C%02d_mezcla_v2.flac' % n, mezcla, 48000, subtype='PCM_24')
    info = dict(tomas=reg, largo_s=round(L / 48000, 3), ganancia_norm_db=round(float(g), 2),
                lufs=i1, pico=pk1)
    print(n, info, flush=True)
    return info


if __name__ == '__main__':
    casos = [int(x) for x in sys.argv[1:]] or sorted(PLAN)
    try:
        info = json.load(open(OUT + 'audio_v2.json'))
    except Exception:
        info = {}
    for n in casos:
        if n == 4:
            v = A.leer(OUT + 'CH_U1_C04_voz_v1sep.flac')
            f = A.leer(OUT + 'CH_U1_C04_fondo_v1sep.flac')
            info['4'] = caso(4, PLAN[4], v, f)
        else:
            info[str(n)] = caso(n, PLAN[n])
    json.dump(info, open(OUT + 'audio_v2.json', 'w'), indent=1, ensure_ascii=False)
