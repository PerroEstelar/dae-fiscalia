# -*- coding: utf-8 -*-
"""Caso 4 (sin linea en Resolve): piezas de video sobre la V1 entregada.
Puerta: la V1 toca la fuente a 0,5 cuadro por cuadro desde su cuadro 0 (medido:
V1 830 = src 36, V1 848 = src 45); aqui igual, 164 cuadros = 82 de fuente.
Cocina: V1 1961 = src 14 a 1:1 con un grado lineal (lift) que se ajusto por
canal; se usan los cuadros de la V1 sin carton (1950-2008) y se sigue con la
fuente graduada. Patio: clip P3TYc (Arley solo) nuevo, estirado 1,19x."""
import sys, json, subprocess
sys.path.insert(0, '/tmp/claude-0/-home-claude/3ed68810-2da1-5d00-9607-4b64ae51b22f/scratchpad/ch')
import numpy as np, v2graf as G
S = '/mnt/user-data/uploads/DAE/_tmp/ch/seg/'
O = '/tmp/claude-0/-home-claude/3ed68810-2da1-5d00-9607-4b64ae51b22f/scratchpad/ch/out/c4/'
FPS = 24000 / 1001
V1 = lambda nm, b, k, n=1: G.leer(S + nm + '.mp4', n=n, desde=k - b)


def fuente(p, n=None):
    cmd = ['ffmpeg', '-v', 'error', '-i', p, '-vf', 'scale=1920:1080:flags=lanczos']
    if n:
        cmd += ['-frames:v', str(n)]
    r = subprocess.run(cmd + ['-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True, check=True).stdout
    return np.frombuffer(r, np.uint8).reshape(-1, 1080, 1920, 3)


def retime(frames, n):
    idx = np.round(np.linspace(0, len(frames) - 1, n)).astype(int)
    return [frames[i] for i in idx]


def fundido(frames, entra=0, sale=0):
    out = []
    n = len(frames)
    for i, f in enumerate(frames):
        k = 1.0
        if entra and i < entra:
            k = G.ease((i + 1) / entra)
        if sale and i >= n - sale:
            k = min(k, G.ease((n - i) / sale))
        out.append((f.astype(np.float32) * k + 0.5).astype(np.uint8) if k < 1 else f)
    return out


EST_PUERTA = dict(G.CARTON, x=250, barra=(176, 514, 189, 644))
piezas = []

import os
if not os.path.exists(O + 'CH_U1_C04_puerta_f759.mp4') or os.path.getsize(O + 'CH_U1_C04_puerta_f759.mp4') < 6_000_000:
    # ---------------------------------------------------------------- puerta (V2 759 -> 923)
    D1 = 72
    src = fuente(S + 'c4src_s7ZN5e3l8e.mp4')
    puerta = [G.con_marca(src[i // 2]) for i in range(92 + D1)]
    n = len(puerta)
    # carton A sigue encendido desde el cuadro 0 (viene de la V1); texto fuera hasta idx 100
    A = list(G.carton_cuadros(puerta, ['Se presentaron dos encuentros', 'en la residencia de Arley'], est=EST_PUERTA,
                              velo_desde=0, velo_hasta=n, velo_in=1, velo_out=10,
                              txt_desde=0, txt_hasta=100, txt_in=1, txt_out=9, con_velo=True))
    # carton B sobre lo mismo, sin velo propio (ya esta): texto 103 -> 158
    B = list(G.carton_cuadros(A, ['En los que sostuvieron', 'relaciones sexuales'], est=EST_PUERTA,
                              txt_desde=103, txt_hasta=158, txt_in=11, txt_out=9, con_velo=False))
    G.mp4(B, O + 'CH_U1_C04_puerta_f759.mp4')
    piezas.append(dict(archivo='CH_U1_C04_puerta_f759.mp4', en=759, cuadros=n, pista=1))
    del src, puerta, A, B

# ---------------------------------------------------------------- cocina + patio (V2 2022 -> 2287)
D2 = 146
coc_v1 = list(V1('c4_v1_f1900', 1900, 1950, 59))               # 1950..2008 tal cual
K = fuente(S + 'c4src_5jPOs8iKxe.mp4')[62:121].copy()
GAIN = np.array([0.927, 0.905, 0.871], np.float32)
OFF = np.array([36.8, 39.6, 37.4], np.float32)
grad = lambda f: np.clip(f.astype(np.float32) * GAIN + OFF + 0.5, 0, 255).astype(np.uint8)
coc_src = [G.con_marca(grad(f)) for f in K]              # sigue desde donde iba la V1 (2009 = src 62)
del K
# junta de 4 cuadros
for i in range(4):
    k = (i + 1) / 5.0
    coc_v1[-4 + i] = (coc_v1[-4 + i].astype(np.float32) * (1 - k) + coc_src[i].astype(np.float32) * k + 0.5).astype(np.uint8)
cocina = coc_v1 + coc_src[4:]                                   # 59 + 55 = 114
cocina = fundido(cocina, sale=14)
nc = len(cocina)
cocina = list(G.carton_cuadros(cocina, ['Arley vivía con su núcleo familiar'],
                               velo_desde=57, velo_hasta=nc - 8, velo_in=14, velo_out=10,
                               txt_desde=66, txt_hasta=nc - 10, txt_in=11, txt_out=9))
G.mp4(cocina, O + '_cocina.mp4', crf=4)
del cocina, coc_v1, coc_src
P = fuente(S + 'c4src_P3TYcEG42C.mp4')
npat = 265 - nc
patio = [G.con_marca(f) for f in retime(P, npat)]
del P
patio = fundido(patio, entra=12, sale=16)
patio = list(G.carton_cuadros(patio, ['No registraba antecedentes', 'de conductas violentas ni de otro tipo',
                                      'de infracciones a la ley penal'],
                              velo_desde=12, velo_hasta=npat - 14, velo_in=12, velo_out=10,
                              txt_desde=18, txt_hasta=npat - 16, txt_in=11, txt_out=9))
G.mp4(patio, O + '_patio.mp4', crf=4)
del patio
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', O + '_cocina.mp4', '-i', O + '_patio.mp4', '-filter_complex', '[0:v][1:v]concat=n=2:v=1:a=0[v]', '-map', '[v]',
                '-c:v', 'libx264', '-crf', '8', '-preset', 'slow', '-tune', 'animation', '-pix_fmt', 'yuv420p', O + 'CH_U1_C04_cocina_patio_f2022.mp4'], check=True)
piezas.append(dict(archivo='CH_U1_C04_cocina_patio_f2022.mp4', en=2022, cuadros=nc + npat, pista=1))
json.dump(dict(piezas=piezas, D1=D1, D2=D2, nc=nc, npat=npat), open(O + 'piezas.json', 'w'), indent=1)
print(piezas, nc, npat)
from PIL import Image
def uno(p, k): return G.leer(O + p, n=1, desde=k)[0]
sel = [uno('CH_U1_C04_puerta_f759.mp4', k) for k in (0, 60, 101, 108, 140, 160)] + \
      [uno('CH_U1_C04_cocina_patio_f2022.mp4', k) for k in (50, 60, 90, 110, nc + 8, nc + 40, nc + 120, nc + 148)]
o = Image.new('RGB', (640 * 4, 360 * 4))
for i, f in enumerate(sel): o.paste(Image.fromarray(f).resize((640, 360)), ((i % 4) * 640, (i // 4) * 360))
o.save(O + 'chk.jpg')
