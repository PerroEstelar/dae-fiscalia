#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La camara horneada de la serie: encuadre, empuje, deriva y pulso de mano.

POR QUE NO LO HACE zoompan
    `zoompan` redondea el recorte a pixel entero de la fuente. Sobre la placa
    subida x2 un pixel de fuente son 0,44 px de salida, asi que todo movimiento
    mas lento que 0,44 px por cuadro se queda quieto varios cuadros y despues
    salta. Para vencer ese escalon hubo que meterle al pulso una banda de 2 a
    3,6 Hz, y medido eso da 4,1 cambios de direccion por segundo: una camara en
    mano de verdad hace uno. Se veia entrecortado porque lo estaba.

    Aqui el recorte lo hace PIL con `resize(box=...)`, que acepta coordenadas
    con decimales y filtra en Lanczos. No hay escalon. El pulso puede entonces
    ser lento y la imagen igual cambia en cada cuadro, porque un desplazamiento
    de 0,09 px si se ve cuando el remuestreo es real.

EL PULSO
    No es una pila de senos sino ruido filtrado: ruido blanco pasado por tres
    filtros de dos polos, a 0,12, 0,45 y 1,2 Hz, con pesos 0,60, 0,30 y 0,10.
    Eso da un espectro que cae como el de una mano de verdad -mucha energia
    abajo, cola corta arriba- y, a diferencia de una suma de senos, no se
    repite nunca: no hay periodo que el ojo pueda agarrar.

    Encima va una envolvente lenta, de 17 a 28 s de periodo, que abre y cierra
    la amplitud: tramos mas calmados y tramos mas vivos.

    El eje vertical tiene su propio ruido y pesa 0,72 del horizontal, como en
    una camara en mano.

    La senal se normaliza por su excursion REAL en la ranura, no por la suma
    teorica de los pesos: con componentes lentas una ranura corta no alcanza a
    recorrer su maximo.
"""
import math
import os
import random
import subprocess
import sys

from PIL import Image

Image.MAX_IMAGE_PIXELS = None

SALIDA_AN, SALIDA_AL = 1920, 1080
FPS_N = 23.976023976
FPS = "24000/1001"
PESO_VERTICAL = 0.72
MARGEN = 1.002
# (corte en Hz, peso). Dos bandas y tres polos cada una.
#
# El numero que importa no es la amplitud sino los CAMBIOS DE DIRECCION por
# segundo: es lo que el ojo lee como entrecortado. Una camara en mano de verdad
# hace alrededor de uno. Medido sobre ranuras de 2,1 / 7,3 / 10,1 s:
#
#   3 bandas, 2 polos (0.12/0.45/1.20)   3,3 a 5,5 por segundo   entrecortado
#   2 bandas, 2 polos                    2,4 a 3,6
#   2 bandas, 3 polos  <- esta           0,4 a 1,0               en mano
#   2 bandas, 4 polos                    0,3 a 0,5  pero se mueve 0,05 px por
#                                        cuadro y vuelve a quedarse quieta
#
# Una banda rapida con poco peso igual manda en la derivada: a 1,2 Hz cada
# unidad de amplitud mueve diez veces mas por cuadro que a 0,12 Hz. Por eso la
# banda de arriba se quita entera y no se baja de peso.
BANDAS = ((0.12, 0.70), (0.40, 0.30))
POLOS = 3
PRE = 400                      # cuadros de arranque que se tiran, para que el
                               # filtro llegue asentado al primer cuadro util


def _filtro(x, corte, fps, polos=POLOS):
    a = math.exp(-2 * math.pi * corte / fps)
    y = [0.0] * polos
    out = []
    for v in x:
        e = v
        for j in range(polos):
            y[j] = a * y[j] + (1 - a) * e
            e = y[j]
        out.append(e)
    return out


def pulso(n, r):
    """Ruido rosado por bandas, normalizado a excursion 1."""
    N = n + PRE
    s = [0.0] * N
    for corte, peso in BANDAS:
        blanco = [r.gauss(0.0, 1.0) for _ in range(N)]
        y = _filtro(blanco, corte, FPS_N)
        # cada banda se normaliza sola: si no, la mas lenta se come el resto
        p = max(abs(v) for v in y) or 1.0
        for i in range(N):
            s[i] += peso * y[i] / p
    return s[PRE:]


def _envolvente(n, r):
    f = r.uniform(1 / 28.0, 1 / 17.0)
    p = r.uniform(0, 2 * math.pi)
    return [0.65 + 0.35 * math.sin(2 * math.pi * f * (i / FPS_N) + p)
            for i in range(n)]


def señal(n, r, vibra):
    env = _envolvente(n, r)
    sx = [a * b for a, b in zip(pulso(n, r), env)]
    sy = [a * b for a, b in zip(pulso(n, r), env)]
    pico = max(max(map(abs, sx)), max(map(abs, sy))) or 1.0
    k = vibra / pico
    return ([v * k for v in sx], [v * k * PESO_VERTICAL for v in sy])


def render(t, ffmpeg="ffmpeg"):
    src, n, salida = t["fuente"], int(t["frames"]), t["salida"]
    enc = float(t.get("encuadre", 0.88))
    emp = float(t.get("empuje", 0.0))
    dx, dy = t.get("deriva", [0.0, 0.0])
    cx, cy = t.get("centro", [0.5, 0.5])
    vib = float(t.get("vibra", 5.0))
    sem = t.get("semilla")
    if sem is None:
        import hashlib
        sem = int(hashlib.md5(os.path.basename(salida).encode()).hexdigest()[:8], 16)
    r = random.Random(int(sem))

    im = Image.open(src).convert("RGB")
    AN, AL = im.size
    piso = SALIDA_AN / float(AN) * MARGEN
    for w in (enc, enc * (1 - emp)):
        if w > 1.0 or w < piso:
            raise ValueError("ventana fuera de riel: %.3f (riel %.3f-1.0) en %s"
                             % (w, piso, os.path.basename(salida)))

    # el pulso se pide en px de SALIDA; aqui se pasa a px de fuente
    sx, sy = señal(n, r, vib)

    os.makedirs(os.path.dirname(salida), exist_ok=True)
    p = subprocess.Popen(
        [ffmpeg, "-loglevel", "error", "-y", "-f", "rawvideo",
         "-pix_fmt", "rgb24", "-s", "%dx%d" % (SALIDA_AN, SALIDA_AL),
         "-r", FPS, "-i", "-", "-an", "-c:v", "libx264", "-preset", "fast",
         "-crf", "14", "-pix_fmt", "yuv420p", "-g", "600", "-keyint_min", "600",
         "-sc_threshold", "0", "-r", FPS, salida], stdin=subprocess.PIPE)

    for i in range(n):
        f = i / float(max(n - 1, 1))
        w = enc * (1 - emp * f)
        cw, ch = AN * w, AL * w
        esc = cw / SALIDA_AN                 # px de salida -> px de fuente
        x = cx * AN - cw / 2 + dx * cw * f + sx[i] * esc
        y = cy * AL - ch / 2 + dy * ch * f + sy[i] * esc
        x = max(0.0, min(AN - cw, x))
        y = max(0.0, min(AL - ch, y))
        cuadro = im.resize((SALIDA_AN, SALIDA_AL), Image.LANCZOS,
                           box=(x, y, x + cw, y + ch))
        p.stdin.write(cuadro.tobytes())
    p.stdin.close()
    p.wait()
    return p.returncode == 0


if __name__ == "__main__":
    import json
    trabajos = json.load(open(sys.argv[1], encoding="utf-8"))
    ff = os.environ.get("FFMPEG", "ffmpeg")
    for t in trabajos:
        if t.get("modo") != "camara":
            continue
        ok = render(t, ff)
        print("%-36s %s" % (os.path.basename(t["salida"]), "OK" if ok else "FALLO"))
