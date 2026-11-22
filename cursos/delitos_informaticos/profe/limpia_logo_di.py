# -*- coding: utf-8 -*-
r"""Delitos informáticos · quita el logo DAE | FISCALÍA que el profe puso arriba a la derecha (22 nov 2026).

El profe entregó sus videos ya editados (DaVinci, 1280×720 a 25, BT.709): cartón propio al empezar (y en dos, al
terminar), sus rótulos, sus láminas y, junto con los rótulos de sección, una placa pequeña «DAE | FISCALÍA» arriba a
la derecha (en x 998–1270, y 17–88, según el rótulo). Sebastián: «lo que no puede ir es ese logo que él le puso en la esquina superior
derecha».

Detrás de la placa está el fondo virtual de la videollamada, que es una foto quieta (el cielo del campus). Entonces no
se difumina: se pone encima el MISMO fondo, sacado de la propia grabación.

1. Medida (cada 10 cuadros): la mediana de una franja de cielo a la izquierda de la placa dice cómo es el fondo; un
   cuadro es «del profe» si esa franja se le parece (en las láminas no). La placa limpia es la mediana, sobre los
   cuadros del profe, del rectángulo de la placa con un margen.
2. Cuadro a cuadro: hay logo si, en un cuadro del profe, el rectángulo de la placa se aparta de la placa limpia. Esos
   tramos se ensanchan 4 cuadros a cada lado (la placa entra y sale con un fundido).
3. Se reescribe la fuente con la placa limpia encima solo en esos cuadros, con 8 píxeles de borde suave, trabajando
   en YUV 4:2:0 (sin pasar por RGB: el color no se toca). x264 CRF 14, el audio copiado.

    python limpia_logo_di.py <fuente> <salida.mp4> <informe.json> [medir]
"""
import glob
import json
import os
import subprocess
import sys

import numpy as np

FB = glob.glob(os.path.expanduser('~') + r'\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg*\*\bin')[0]
FF, FP = FB + r'\ffmpeg.exe', FB + r'\ffprobe.exe'
W, H = 1280, 720
# La placa no está siempre en el mismo sitio: x 998–1226, y 40–88 en unos rótulos; x 1016–1266, y 31–83 y x 1024–1270,
# y 17–67 en otros (medido en la primera pasada, que se quedaba corta). El rectángulo los cubre a todos.
LOGO = (984, 1278, 8, 100)          # x0, x1, y0, y1 de la placa (pares, para el croma)
PARCHE = (968, 1280, 0, 116)        # lo que se reemplaza: la placa y hasta 16 px alrededor (el cuadro corta arriba
                                    # y a la derecha)
BORDE = 8                           # píxeles de borde suave dentro del margen
REF = (880, 972, 6, 30)             # franja de cielo para saber si el cuadro es del profe
UMBRAL_REF = 6.0                    # diferencia media (Y) para decir «es el fondo»
UMBRAL_LOGO = 4.0                   # diferencia media (Y) en la placa para decir «hay logo»
ANCHO = 4                           # cuadros que se ensancha cada tramo


def lector(src):
    p = subprocess.Popen([FF, '-v', 'error', '-i', src, '-map', '0:v:0', '-f', 'rawvideo', '-pix_fmt', 'yuv420p',
                          '-'], stdout=subprocess.PIPE, bufsize=1 << 24)
    n = W * H * 3 // 2
    while True:
        b = p.stdout.read(n)
        if len(b) < n:
            break
        yield b
    p.wait()


def planos(b):
    a = np.frombuffer(b, np.uint8)
    y = a[:W * H].reshape(H, W)
    u = a[W * H:W * H * 5 // 4].reshape(H // 2, W // 2)
    v = a[W * H * 5 // 4:].reshape(H // 2, W // 2)
    return y, u, v


def recorte(pl, r, sub=1):
    x0, x1, y0, y1 = [c // sub for c in r]
    return pl[y0:y1, x0:x1]


def medir(src):
    refs, parches = [], []
    for i, b in enumerate(lector(src)):
        if i % 10:
            continue
        y, u, v = planos(b)
        refs.append(recorte(y, REF).astype(np.float32))
        parches.append((recorte(y, PARCHE).copy(), recorte(u, PARCHE, 2).copy(), recorte(v, PARCHE, 2).copy()))
    ref = np.median(np.stack(refs), axis=0)
    es = [float(np.abs(r - ref).mean()) < UMBRAL_REF for r in refs]
    sel = [p for p, e in zip(parches, es) if e]
    limpia = tuple(np.median(np.stack([p[k] for p in sel]), axis=0).astype(np.uint8) for k in range(3))
    return ref, limpia, sum(es), len(es)


def marcas(src, ref, limpia):
    lx0, lx1, ly0, ly1 = [a - b for a, b in zip(LOGO, (PARCHE[0], PARCHE[0], PARCHE[2], PARCHE[2]))]
    ly = limpia[0][ly0:ly1, lx0:lx1].astype(np.float32)
    perfil, logo = [], []
    for b in lector(src):
        y, _, _ = planos(b)
        dr = float(np.abs(recorte(y, REF).astype(np.float32) - ref).mean())
        dl = float(np.abs(recorte(y, LOGO).astype(np.float32) - ly).mean())
        perfil.append(dr < UMBRAL_REF)
        logo.append(dr < UMBRAL_REF and dl > UMBRAL_LOGO)
    n = len(logo)
    ancho = [False] * n
    for i, s in enumerate(logo):
        if s:
            for j in range(max(0, i - ANCHO), min(n, i + ANCHO + 1)):
                ancho[j] = True
    # solo se parchea sobre cuadros del profe (en un fundido hacia una lámina, no)
    ancho = [a and p for a, p in zip(ancho, perfil)]
    return ancho, perfil


def mascara():
    x0, x1, y0, y1 = PARCHE
    lx0, lx1, ly0, ly1 = LOGO
    h, w = y1 - y0, x1 - x0
    yy, xx = np.mgrid[0:h, 0:w]
    # distancia hacia afuera desde el rectángulo de la placa, en píxeles
    dx = np.maximum(np.maximum((lx0 - x0) - xx, xx - (lx1 - x0 - 1)), 0)
    dy = np.maximum(np.maximum((ly0 - y0) - yy, yy - (ly1 - y0 - 1)), 0)
    d = np.maximum(dx, dy).astype(np.float32)
    m = np.clip(1.0 - (d - (16 - BORDE)) / BORDE, 0.0, 1.0)   # 1 hasta 8 px fuera de la placa, baja a 0 en 16
    return m, m[::2, ::2]


def tramos(flags, fps=25.0):
    out, a = [], None
    for i, f in enumerate(flags + [False]):
        if f and a is None:
            a = i
        if not f and a is not None:
            out.append((round(a / fps, 2), round(i / fps, 2)))
            a = None
    return out


def aplicar(src, dst, flags, limpia):
    my, mc = mascara()
    x0, x1, y0, y1 = PARCHE
    enc = subprocess.Popen([FF, '-y', '-v', 'error', '-f', 'rawvideo', '-pix_fmt', 'yuv420p', '-s', '%dx%d' % (W, H),
                            '-r', '25', '-i', '-', '-i', src, '-map', '0:v', '-map', '1:a:0', '-c:v', 'libx264',
                            '-preset', 'medium', '-crf', '14', '-pix_fmt', 'yuv420p', '-colorspace', 'bt709',
                            '-color_primaries', 'bt709', '-color_trc', 'bt709', '-color_range', 'tv',
                            '-c:a', 'copy', '-movflags', '+faststart', dst + '.parcial.mp4'],
                           stdin=subprocess.PIPE)
    ly, lu, lv = [p.astype(np.float32) for p in limpia]
    for i, b in enumerate(lector(src)):
        if i < len(flags) and flags[i]:
            a = np.frombuffer(b, np.uint8).copy()
            y = a[:W * H].reshape(H, W)
            u = a[W * H:W * H * 5 // 4].reshape(H // 2, W // 2)
            v = a[W * H * 5 // 4:].reshape(H // 2, W // 2)
            ry = y[y0:y1, x0:x1].astype(np.float32)
            y[y0:y1, x0:x1] = np.clip(ry * (1 - my) + ly * my + 0.5, 0, 255).astype(np.uint8)
            for pl, lim in ((u, lu), (v, lv)):
                rc = pl[y0 // 2:y1 // 2, x0 // 2:x1 // 2].astype(np.float32)
                pl[y0 // 2:y1 // 2, x0 // 2:x1 // 2] = np.clip(rc * (1 - mc) + lim * mc + 0.5, 0, 255).astype(np.uint8)
            b = a.tobytes()
        enc.stdin.write(b)
    enc.stdin.close()
    enc.wait()
    assert enc.returncode == 0
    os.replace(dst + '.parcial.mp4', dst)


if __name__ == '__main__':
    src, dst, inf = sys.argv[1:4]
    ref, limpia, nprofe, nmuestras = medir(src)
    flags, perfil = marcas(src, ref, limpia)
    rep = {'fuente': src, 'cuadros': len(flags), 'muestras_del_profe': '%d/%d' % (nprofe, nmuestras),
           'cuadros_parcheados': sum(flags), 'tramos_s': tramos(flags)}
    json.dump(rep, open(inf, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(json.dumps(rep, ensure_ascii=False))
    if len(sys.argv) > 4 and sys.argv[4] == 'medir':
        sys.exit(0)
    aplicar(src, dst, flags, limpia)
    print('LISTO', dst)
