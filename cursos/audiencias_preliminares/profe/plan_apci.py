# -*- coding: utf-8 -*-
r"""Inicio del curso «Audiencias preliminares y medidas de aseguramiento» (23 nov 2026). **Entrega provisional.**

Fuente: `Apertura de curso.mp4` (334.81 s), que llegó el 23 nov a la carpeta «Videos Curso Virtual FGN-UNAL» del
profe. Es el «Video de presentación» del curso (2.1 de la ficha), el que faltaba el 20 nov.

**Tramo:** desde 5.55 s (0,45 s antes de «Un cordial saludo…», a 6.00 s; antes hay silencio digital) hasta 331.74 s
(0,7 s después de la última palabra; el archivo dura 334.81). Sin cortes: lo lee de corrido; un «mmm» con una pausa de
1,3 s en 2:19 se queda. Termina «…así que muy bienvenidos al curso.».
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_ap_profe import *  # noqa: E402,F401,F403
from base_ap_profe import armar_curso, rotulo  # noqa: E402,F401

globals().update(armar_curso('INICIO', 'Inicio del curso', [(5.55, 331.74)]))

ITEMS = rotulo(T0)  # noqa: F821
