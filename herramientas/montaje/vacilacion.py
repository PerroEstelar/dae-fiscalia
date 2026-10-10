#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Busca la vacilacion del principio en los loops de Kling.

Cuando la placa tiene una mano a punto de alcanzar algo, el modelo se congela
en el gesto y despues la mano va y viene. El defecto es LOCAL —una mano, un
brazo— y en un promedio de todo el cuadro desaparece: el loop conocido del
Caso 08, que vacila, mide igual que uno limpio si se promedia entero.

Asi que se mide por bloques. El cuadro se parte en una rejilla de 8x6 y de cada
bloque se saca su distancia al cuadro 0. El bloque que mas se mueve en los
primeros cuadros es el que tiene el gesto; si SU curva sube, hace pico y se
deshace, eso es la vacilacion. Despues se mira hasta donde llega y se sugiere
entrar por ahi.

    vacilacion.py clip.mp4 [clip2.mp4 ...]
    vacilacion.py --lista rutas.txt
    vacilacion.py --curva clip.mp4      # la curva cuadro a cuadro del bloque

No necesita numpy.
"""

import os
import subprocess
import sys

FFMPEG = os.environ.get("FFMPEG", "ffmpeg")
AN, AL = 128, 72
BX, BY = 8, 6                  # rejilla de bloques
BW, BH = AN // BX, AL // BY    # 16 x 12
TAM = AN * AL

VENTANA = 45      # la vacilacion esta al principio: solo ahi se busca el pico
SUAVE = 5         # ventana del promedio movil, mata el ruido de bloque oscuro
MIN_PICO = 12.0   # por debajo de esto el bloque no tiene gesto, solo ruido
CAIDA = 0.25      # cuanto del pico tiene que deshacerse
REGRESO = 0.85    # si vuelve a esta fraccion del pico es un ciclo, no una vacilacion


def cuadros_gris(ruta):
    cmd = [FFMPEG, "-v", "error", "-i", ruta,
           "-vf", "scale=%d:%d,format=gray" % (AN, AL),
           "-f", "rawvideo", "-pix_fmt", "gray", "-"]
    p = subprocess.run(cmd, capture_output=True)
    if p.returncode:
        raise RuntimeError(p.stderr[:200].decode("utf-8", "replace"))
    b = p.stdout
    return [b[i:i + TAM] for i in range(0, len(b) - TAM + 1, TAM)]


def indices_bloque(bx, by):
    out = []
    for y in range(by * BH, (by + 1) * BH):
        base = y * AN
        out.extend(range(base + bx * BW, base + (bx + 1) * BW))
    return out


IDX = [[indices_bloque(bx, by) for by in range(BY)] for bx in range(BX)]


def dist_bloque(f, f0, idx):
    s = 0
    for i in idx:
        d = f[i] - f0[i]
        s += d if d >= 0 else -d
    return s / float(len(idx))


def medir(ruta):
    fs = cuadros_gris(ruta)
    n = len(fs)
    if n < 20:
        return None
    f0 = fs[0]
    fin = min(VENTANA, n)
    # el bloque del gesto: el que mas se aleja del cuadro 0 en la ventana
    mejor, mpico = None, -1.0
    for bx in range(BX):
        for by in range(BY):
            idx = IDX[bx][by]
            p = max(dist_bloque(fs[i], f0, idx) for i in range(1, fin))
            if p > mpico:
                mejor, mpico = (bx, by), p
    idx = IDX[mejor[0]][mejor[1]]
    curva = [dist_bloque(f, f0, idx) for f in fs]
    return {"ruta": ruta, "n": n, "bloque": mejor, "curva": curva}


def suavizar(c, k=SUAVE):
    n, m = len(c), k // 2
    return [sum(c[max(0, i - m):min(n, i + m + 1)]) /
            float(len(c[max(0, i - m):min(n, i + m + 1)])) for i in range(n)]


def veredicto(m):
    """La firma del defecto, medida sobre el loop conocido del Caso 08:
    sube rapido en los primeros cuadros, hace pico, se deshace una parte y
    se queda abajo. Lo ultimo es lo que la separa de un loop ciclico, que
    tambien sube y baja pero VUELVE a subir al mismo sitio."""
    c = suavizar(m["curva"])
    n = m["n"]
    fin = min(VENTANA, n)
    p = max(range(1, fin), key=lambda i: c[i])
    pico = c[p]
    cola = c[p:min(p + 45, n)]
    valle = min(cola)
    v = cola.index(valle) + p
    deshecho = (pico - valle) / pico if pico else 0.0

    despues = c[v:min(v + 70, n)]
    vuelve = max(despues) >= pico * REGRESO if despues else False

    vacila = (p >= 5 and pico >= MIN_PICO and deshecho >= CAIDA and not vuelve)
    ini = min(v + 15, max(n - 40, 0)) if vacila else 0
    nota = "limpio"
    if not vacila and p >= 5 and pico >= MIN_PICO and deshecho >= CAIDA and vuelve:
        nota = "ciclico"
    return vacila, ini, pico, deshecho, p, v, nota


def main(rutas):
    print("%-34s %5s %6s %6s %7s %5s %5s  %s" % (
        "clip", "n", "bloque", "pico", "deshace", "pico@", "valle", "veredicto"))
    print("-" * 112)
    pendientes = []
    for r in rutas:
        try:
            m = medir(r)
        except Exception as ex:
            print("%-34s  FALLO %s" % (os.path.basename(r), ex))
            continue
        if m is None:
            print("%-34s  muy corto" % os.path.basename(r))
            continue
        vac, ini, pico, desh, p, v, nota = veredicto(m)
        print("%-34s %5d  %d,%d  %6.1f %6.0f%% %5d %5d  %s" % (
            os.path.basename(r), m["n"], m["bloque"][0], m["bloque"][1],
            pico, desh * 100, p, v,
            ("VACILA -> inicio %d" % ini) if vac else nota))
        print("      curva/10: %s" % " ".join(
            "%.0f" % m["curva"][i] for i in range(0, m["n"], 10)))
        if vac:
            pendientes.append((r, ini))
    print()
    print("--- %d de %d vacilan" % (len(pendientes), len(rutas)))
    for r, ini in pendientes:
        print('   %-34s inicio %d' % (os.path.basename(r), ini))


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--curva":
        m = medir(a[1])
        print("bloque", m["bloque"], "n", m["n"])
        for i in range(0, min(160, m["n"])):
            print("%4d %6.2f %s" % (i, m["curva"][i], "#" * int(m["curva"][i])))
        sys.exit(0)
    if a and a[0] == "--lista":
        rutas = [x.strip() for x in open(a[1], encoding="utf-8") if x.strip()]
    else:
        rutas = a
    main(rutas)
