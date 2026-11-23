# -*- coding: utf-8 -*-
r"""Cierre del curso «Audiencias preliminares y medidas de aseguramiento» (23 nov 2026). **Entrega provisional.**

Fuente: `Cierre de curso.mp4` (359.77 s), que llegó el 23 nov a la carpeta «Videos Curso Virtual FGN-UNAL» del
profe. La ficha (4.1) da el cierre del curso como un mensaje escrito; el profe lo grabó.

**Tramo:** desde 3.13 s (0,45 s antes de «Un cordial saludo…», a 3.58 s; antes hay silencio digital) hasta 356.28 s
(0,7 s después de la última palabra; el archivo dura 359.77). Sin cortes: lo lee de corrido. El tropiezo en el nombre
del curso («Audiencias preliminares… d-- y medidas de aseguramiento», con 1,6 s de pausa en 0:13) se queda en el
video y sale del subtítulo. Termina «Muchos éxitos en su labor institucional.».
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_ap_profe import *  # noqa: E402,F401,F403
from base_ap_profe import armar_curso, rotulo  # noqa: E402,F401

globals().update(armar_curso('CIERRE', 'Cierre del curso', [(3.13, 356.28)]))

ITEMS = rotulo(T0)  # noqa: F821
