# -*- coding: utf-8 -*-
r"""Videos de profe **a cámara** de «Justicia restaurativa en la práctica del fiscal» (25 nov 2026). **Entrega provisional.**

Sebastián (24 nov): «continuemos con el video de cierre de justicia restaurativa, profe mirando a cámara, gráfica
provisional; el material está en …\CURSO - JUSTICIA RESTAURATIVA\CIERRE DEL CURSO; edita, compón y de pe a pa». El 25
pidió seguir con «los videos de profe a cámara» y dejar los enlaces.

**El material.** Dos grabaciones nuevas de Víctor Hugo Ospina Vargas solo, mirando a cámara, ya puesto por el editor de la
grabación sobre el fondo de la Fiscalía (edificio y panel de logos DAE–FGN arriba a la izquierda, x 190–890, y 80–235):
1920×1080, 30 cuadros, H.264 Constrained Baseline, **sin etiqueta de color**. Se midió el rojo y el azul del logo
decodificando en BT.601 y en BT.709 contra el fondo original (`FONDO 4 V2.png`): BT.601 queda más cerca (rojo a 30 de
distancia contra 45; azul 15,6 contra 16,6), como las demás fuentes de este editor. No lleva `MATRIZ_FUENTE`.
- «VIDEO 2 CIERRE DE TODO EL CURSO … TOMA 1.mp4» es el **cierre del curso** (13:50).
- «VIDEO JUSTICIA RESTAURATIVA TOMA 2.mp4» **no es otra toma del cierre: es la bienvenida al curso** (12:24).

**Cortes.** El profesor se equivoca y retoma él mismo («no, me equivoqué», «voy a retomar», «retomo», «una pausa, por
favor»). Cada corte cambia de plano (entero ↔ cerrado), como en Ley 1826: a cámara fija, el salto de la persona se ve
como un cambio de plano. El plano cerrado (`CERRADO`) deja entero el panel de logos.

**Lower third.** El de la serie (blanco con sombra), abajo a la izquierda, angosto para no tocar el saco: nombre en dos
renglones y cargo a 470 px. Nombre y cargo, de la ficha (ver `base_jr_profe`).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_jr_profe import *  # noqa: E402,F401,F403
from base_jr_profe import RAIZ, BIN_CURSO, MASTERS, CLIP0, FPS, FQ  # noqa: E402

CERRADO = (110, 30, 1728, 972)
LT = (44, 470)
LT_TOP = 800
VICTOR_CAM = ('Víctor Hugo\nOspina Vargas',
              'Coautor del curso. Profesor de pregrado y posgrado de la Universidad Nacional de Colombia')


def armar_camara(fuente, carpeta, sub, linea, export, prefijo, tramos):
    """`tramos`, lo que entra, en cuadros de la fuente: [(k0, k1)] o [(k0, k1, ventana)], k1 exclusivo. Entre dos
    tramos que no se tocan hay un corte."""
    r = RAIZ + '/' + carpeta
    tr = [(t[0] / FQ, t[1] / FQ, t[2] if len(t) > 2 else None) for t in tramos]

    def cuadro(t):
        """Segundos de la fuente → cuadro de la línea, descontando los cortes."""
        acum = 0.0
        for a, b, _w in tr:
            if a - 1e-6 <= t <= b + 1e-6:
                return CLIP0 + int(round((acum + t - a) * FPS))
            acum += b - a
        raise ValueError('%.2f cae fuera de los tramos' % t)

    return dict(
        R=r, BIN=BIN_CURSO + [carpeta.replace('/', ' - ') + ' - PROFE A CAMARA'],
        ORIGINAL=r + '/01 VIDEO/' + fuente, COMPUESTO=r + '/01 VIDEO/%s_compuesto_v1.mp4' % prefijo,
        TITULO=r + '/02 CARTONES/carton titulo %s.mp4' % prefijo.lower(), SUB=sub, NOMBRE_LINEA=linea,
        EXPORT=export + '-v%d', PREFIJO=prefijo, TMP='D:/DAE/_tmp/jr_p/' + prefijo.lower(),
        TRAMOS=tr, T0=tr[0][0], T1=tr[-1][1], cuadro=cuadro, MASTER_DIR=MASTERS + '/' + carpeta)
