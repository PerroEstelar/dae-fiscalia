# -*- coding: utf-8 -*-
r"""Vuelve a hornear las 57 ranuras y los 5 respiros SIN EMPUJE DE CAMARA.

POR QUE
    27 de octubre, Sebastian: «note unos efectos extranos en las transiciones
    como un zoom in de camara (...) eso no me gusta, quitalo». Medido en el
    capitulo 1: entre el cuadro 790 y el 940 de la misma ranura la ventana y
    el plato crecen a ojo. `plan_camara_df.SIN_EMPUJE` deja el encuadre fijo.

    Se conserva el pulso de mano, que es sub-pixel: sin el, la placa se lee
    como un JPEG pegado.

EL RESPIRO AHORA ENCUADRA IGUAL QUE SU RANURA
    Antes el respiro era la placa entera escalada a 1920x1080 y la ranura r01
    iba recortada al 88 %%, asi que el «bookend» volvia a la misma imagen con
    OTRO encuadre, 12 %% mas abierto. Ahora pasa por el mismo horneado, con
    empuje cero: vuelve exactamente al plano con el que abrio.

NADA SE BORRA
    Los mp4 anteriores se mueven a `_descartes` con el motivo en el nombre.
"""
import os
import shutil
import subprocess
import sys
import time

sys.path.insert(0, "D:/DAE/_repo/herramientas/montaje")
sys.path.insert(0, "D:/DAE/_repo/herramientas/prompts")
import camara
import plan_camara_df as PC
from armar_df import NOMBRE

MOTIVO = "con_empuje_de_camara"
LARGO_RESPIRO = 48


def cuadros(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                        "-count_frames", "-show_entries", "stream=nb_read_frames",
                        "-of", "default=nw=1:nk=1", p],
                       capture_output=True, text=True).stdout.split()
    return int(r[0]) if r else -1


def aparta(p):
    if not os.path.exists(p):
        return
    des = os.path.join(os.path.dirname(p), "_descartes")
    os.makedirs(des, exist_ok=True)
    base, ext = os.path.splitext(os.path.basename(p))
    d = os.path.join(des, "%s_%s%s" % (base, MOTIVO, ext))
    k = 1
    while os.path.exists(d):
        d = os.path.join(des, "%s_%s_%d%s" % (base, MOTIVO, k, ext))
        k += 1
    shutil.move(p, d)


for cap in [int(a) for a in sys.argv[1:]] or [1, 2, 3, 4, 5]:
    E = __import__("escenas_df_c%d" % cap)
    NOM = {n: "DF_C%d_r%02d_%s.png" % (cap, n, NOMBRE[cap][n]) for n in E.R}
    LARGOS = {n: E.R[n][0] for n in E.R}
    print("=== capitulo %d" % cap, flush=True)
    for t in PC.trabajos(cap, NOM, LARGOS):
        aparta(t["salida"])
        t0 = time.time()
        camara.render(t)
        n = cuadros(t["salida"])
        ok = n == t["frames"]
        print("%-52s %4d/%4d %s  %.0f s"
              % (os.path.basename(t["salida"]), n, t["frames"],
                 "OK" if ok else "FALLA", time.time() - t0), flush=True)
        assert ok
    # el respiro, con el mismo encuadre que la r01
    sal = os.path.join(PC.RAIZ, PC.CAPS[cap], "10 TIMELINE SEBASTIAN", "RESPIRO")
    os.makedirs(sal, exist_ok=True)
    d = os.path.join(sal, "DF_C%d_respiro_v%d.mp4" % (cap, LARGO_RESPIRO))
    aparta(d)
    camara.render({"modo": "camara",
                   "fuente": os.path.join(PC.RAIZ, PC.CAPS[cap], "01 PLANOS",
                                          "_grade", NOM[1]),
                   "salida": d, "frames": LARGO_RESPIRO,
                   "encuadre": 0.88, "empuje": 0.0, "deriva": [0.0, 0.0],
                   "vibra": 5.0})
    n = cuadros(d)
    print("%-52s %4d/%4d %s" % (os.path.basename(d), n, LARGO_RESPIRO,
                                "OK" if n == LARGO_RESPIRO else "FALLA"), flush=True)
    assert n == LARGO_RESPIRO
print("LISTO", flush=True)
