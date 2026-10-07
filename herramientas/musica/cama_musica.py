#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arma la cama de música de una pieza, con el ducking ya horneado.

POR QUÉ HORNEADO Y NO AUTOMATIZADO EN RESOLVE
    La API de Resolve de este build no deja escribir niveles ni keyframes de
    audio. Entonces el archivo sale con la envolvente ya aplicada y entra a la
    línea con la ganancia en cero. Si hay que cambiar el balance, se vuelve a
    correr esto, no se toca el fader.

LOS NIVELES DE LA SERIE
    voz           −19 LUFS
    música        −32 LUFS bajo la narración      (6 dB de ducking)
    música        −29 LUFS bajo el bloque de preguntas (3 dB de ducking)
    música        −26 LUFS en los huecos
    Se normaliza a −26 y se agacha donde hay voz, con rampas de 1 s.

    POR QUÉ EL BLOQUE DE PREGUNTAS TAMBIÉN SE AGACHA
    Antes las preguntas entraban como «hueco», a −26, porque el bloque se había
    pensado sin voz. Con voz encima eso deja un escalón de 5,6 dB justo en el
    cuadro donde cambia de narrador: la voz no se mueve pero pierde ese aire de
    golpe, y se oye como si el segundo locutor hablara más bajo. Medidas las dos
    pistas por ventanas, narrador y preguntas quedan dentro de 1 LU en los cinco
    casos: el escalón era la cama, no la voz. Con 3 dB el bloque sigue
    levantando sobre la narración sin comerse al locutor.
"""
import json, os, subprocess, sys
import numpy as np

SR = 48000
RAMPA = 1.0          # segundos de subida y bajada del ducking
ENTRADA = 1.5        # fade in
SALIDA = 2.5         # fade out
DUCK_DB = -6.0       # narración
DUCK_PREGUNTAS = -3.0


def _decodificar(ruta, dur):
    cmd = ["ffmpeg", "-v", "error", "-i", ruta, "-t", f"{dur:.3f}",
           "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"]
    crudo = subprocess.run(cmd, capture_output=True, check=True).stdout
    a = np.frombuffer(crudo, dtype=np.float32).reshape(-1, 2).copy()
    n = int(round(dur * SR))
    if len(a) < n:                      # la pista es más corta: se repite con cruce
        cruce = int(1.5 * SR)
        salida = np.zeros((n, 2), dtype=np.float32)
        pos = 0
        while pos < n:
            tramo = a if pos == 0 else a[cruce:]
            fin = min(pos + len(tramo), n)
            trozo = tramo[: fin - pos].copy()
            if pos > 0:
                k = min(cruce, len(trozo))
                f = np.linspace(0, 1, k, dtype=np.float32)[:, None]
                salida[pos:pos + k] = salida[pos:pos + k] * (1 - f) + trozo[:k] * f
                salida[pos + k:fin] = trozo[k:]
            else:
                salida[pos:fin] = trozo
            pos = fin - (cruce if fin < n else 0)
        a = salida
    return a[:n]


def _envolvente(dur, tramos_voz):
    """1.0 en los huecos y el ducking que pida cada tramo, con rampas lineales.

    Un tramo es (a, b) —y usa DUCK_DB— o (a, b, db) para pedir otra
    profundidad; así la narración baja 6 dB y el bloque de preguntas 3.
    """
    n = int(round(dur * SR))
    g = np.ones(n, dtype=np.float32)
    r = int(RAMPA * SR)
    for tramo in tramos_voz:
        a, b = tramo[0], tramo[1]
        duck = float(10 ** ((tramo[2] if len(tramo) > 2 else DUCK_DB) / 20))
        ia, ib = int(a * SR), int(b * SR)
        i0, i1 = max(0, ia - r), min(n, ib + r)
        if ia > i0:
            g[i0:ia] = np.minimum(g[i0:ia], np.linspace(1.0, duck, ia - i0, dtype=np.float32))
        g[max(0, ia):min(n, ib)] = np.minimum(g[max(0, ia):min(n, ib)], duck)
        if i1 > ib:
            g[ib:i1] = np.minimum(g[ib:i1], np.linspace(duck, 1.0, i1 - ib, dtype=np.float32))
    ne, ns = int(ENTRADA * SR), int(SALIDA * SR)
    g[:ne] *= np.linspace(0, 1, ne, dtype=np.float32)
    g[-ns:] *= np.linspace(1, 0, ns, dtype=np.float32)
    return g[:, None]


def _lufs(ruta):
    out = subprocess.run(["ffmpeg", "-nostats", "-i", ruta, "-af", "ebur128=peak=true",
                          "-f", "null", "-"], capture_output=True, text=True).stderr
    for i, l in enumerate(out.splitlines()):
        if "Integrated loudness" in l:
            for s in out.splitlines()[i:i + 3]:
                if s.strip().startswith("I:"):
                    return float(s.split()[1])
    return None


def cama(pista, salida, dur, tramos_voz, objetivo=-26.0):
    a = _decodificar(pista, dur)

    tmp = salida + ".plano.wav"
    _escribir(tmp, a)
    actual = _lufs(tmp)
    a *= float(10 ** ((objetivo - actual) / 20))        # al nivel de hueco
    os.remove(tmp)

    a *= _envolvente(dur, tramos_voz)
    pico = float(np.abs(a).max())
    if pico > 0.89:                                      # techo a −1 dBTP con aire
        a *= 0.89 / pico
    _escribir(salida, a)
    print(f"{os.path.basename(salida)}  {dur:.1f}s  hueco {objetivo} LUFS  "
          f"bajo voz {objetivo + DUCK_DB} LUFS  medido {_lufs(salida):.1f} LUFS integrado")


def _escribir(ruta, a):
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR),
                          "-ac", "2", "-i", "-", "-c:a", "pcm_s24le", ruta],
                         stdin=subprocess.PIPE)
    p.stdin.write(np.clip(a, -1, 1).astype(np.float32).tobytes())
    p.stdin.close()
    p.wait()


if __name__ == "__main__":
    spec = json.load(open(sys.argv[1], encoding="utf-8"))
    for c in spec:
        cama(c["pista"], c["salida"], c["dur"], [tuple(t) for t in c["voz"]],
             c.get("objetivo", -26.0))
