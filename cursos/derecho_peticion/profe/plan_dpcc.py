# -*- coding: utf-8 -*-
r"""Cierre del curso de «Derecho de petición y acción de tutela» (21 nov 2026). **Entrega provisional** (ver `base_dp_profe`).

Fuente: `Derecho de petición - Cierre.mp4` (14:23,4), en `E:\DAE MASTER\CURSO DERECHOS DE PETICION\`, la misma cámara y
el mismo fondo que las demás (H.264 Constrained Baseline a 30, AAC estéreo 48 kHz). Una sola toma. Bordes en RMS de
10 ms (`D:\DAE\_tmp\dp_p\cc\bordes.json`).

Qué sale:
- 0–6,16: antes de «Al cerrar este curso le propongo una pregunta» (de 6,32 a 7,0 hay respiración: el borde va a la
  mitad del silencio de antes).
- 456,16–469,63: el primer «La precisión protege a quien solicita la atención y la propia entidad.» y «Voy a retomar
  desde la precisión». Sigue la segunda lectura de la misma frase.
- 792,81–802,78: «El paso a siguientes—», «retomo en esa frase el paso siguiente» y la pausa. Sigue «El paso
  siguiente no consiste en recordar…».
- Termina en «…Este compromiso continúa con usted» (858,27; el borde a 0,7 s).

Quedan las pausas de lectura (la más larga, 2,1 s en «…orientarla, | no convertirse…») y los tropiezos sueltos sin
disculpa («Esta per— perspectiva», «no son un, un obstáculo»); salen del subtítulo.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_dp_profe import *  # noqa: E402,F401,F403
from base_dp_profe import armar, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar('CURSO/CIERRE', 'Cierre del curso', 'DP - CURSO - CIERRE', 'derechodepeticion - CURSO - CIERRE', 'DPCC',
                       'Derecho de petición - Cierre.mp4', [(6.16, 456.16), (469.63, 792.81), (802.78, 858.97)]))

ITEMS = rotulo(T0 + 1.5)  # noqa: F821
