#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Encuentra la costura menos audible para repetir una pista.

En vez de elegir el punto de corte a oido, compara por correlacion normalizada
la ventana previa a cada candidato de SALIDA contra la previa a cada candidato
de RETORNO. La pareja con mayor correlacion cae en compas y con el mismo
timbre.

DOS MODOS
    vuelta completa   salir del final y volver al principio. Sirve cuando la
                      pista ya es una cama.
    costura interna   salir del cuerpo y volver al cuerpo. Es lo que hay que
                      usar cuando la pista es una pieza compuesta: asi la
                      cabeza y la cola conservan la entrada y el final reales
                      y solo se repite el tramo parejo del medio.

Como saber cual es cual: mirar el RMS por segundo. Si sube al empezar y cae al
terminar, es una pieza compuesta y la vuelta completa nunca va a sonar bien.
"""
import subprocess, sys
import numpy as np

SR = 48000
VENT = 1.5
PASO = 0.125


def carga(ruta):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", ruta, "-ac", "1",
                          "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.float32)


def _norm(x):
    x = x - x.mean()
    s = np.linalg.norm(x)
    return x / s if s else x


def perfil(a):
    """RMS por segundo, en dB. Para ver si la pista es cama o pieza."""
    r = np.sqrt(np.convolve(a.astype(np.float64) ** 2,
                            np.ones(SR) / SR, "same"))[::SR]
    return 20 * np.log10(r + 1e-9)


def buscar(a, sal_desde, sal_hasta, ret_desde, ret_hasta, bucle_min=25.0):
    L, p = int(VENT * SR), int(PASO * SR)
    W = {i: _norm(a[i - L:i])
         for i in range(max(L, int(ret_desde * SR)), int(ret_hasta * SR), p)}
    mejor = (-2.0, 0.0, 0.0)
    for s in range(max(L, int(sal_desde * SR)), int(sal_hasta * SR), p):
        ws = _norm(a[s - L:s])
        for r, wr in W.items():
            if (s - r) / SR < bucle_min:
                continue
            c = float(ws @ wr)
            if c > mejor[0]:
                mejor = (c, s / SR, r / SR)
    return mejor


if __name__ == "__main__":
    a = carga(sys.argv[1])
    dur = len(a) / SR
    pf = perfil(a)
    print("pista %.1f s" % dur)
    print("RMS dB:", " ".join("%.0f" % x for x in pf[::6]))
    compuesta = pf[:3].mean() < pf[len(pf) // 2] - 4 and pf[-3:].mean() < pf[len(pf) // 2] - 4
    print("parece", "una pieza compuesta" if compuesta else "una cama")
    if compuesta:
        c, s, r = buscar(a, dur * .35, dur * .92, dur * .18, dur * .62)
        print("costura interna: corta %.2f s, retoma %.2f s, correlacion %.3f" % (s, r, c))
        print("   cabeza %.1f s | bucle %.1f s | cola %.1f s" % (r, s - r, dur - s))
    else:
        c, s, r = buscar(a, dur * .55, dur, VENT, dur * .45, bucle_min=0)
        print("vuelta completa: corta %.2f s, retoma %.2f s, correlacion %.3f" % (s, r, c))
