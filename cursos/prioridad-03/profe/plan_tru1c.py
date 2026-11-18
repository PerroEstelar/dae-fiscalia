# -*- coding: utf-8 -*-
r"""Cierre de la unidad 1, «Tráfico de migrantes y trata de personas» (17–18 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos
(ver `base_tr_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo compuesto.

**Fuente.** Drive del curso → VIDEOS, «UNIDAD 1/Cierre de la Unidad 1.webm» (`1pKLKkbHUblFgUx8YHxlD1DkctakxPQSB`):
1280×720, H.264 en WebM con cadencia variable, Opus mono; 453,7 s. STT (Scribe, WAV a 16 kHz): 973 palabras, de 3,06 a 450,50 s.

Entra de 2,56 a 451,30 s: medio segundo antes de la primera palabra y hasta 0,8 s después de la última
(o hasta el final del archivo). Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_tr_profe import *  # noqa: E402,F401,F403
from base_tr_profe import armar_curso, armar_unidad, PROFE_CIERRES  # noqa: E402,F401

globals().update(armar_unidad(1, 'CIERRE', '.webm', 2.56, 451.3))
XY, VENTANA = (0, 40), (1143, 643)
POR_TIEMPO = True       # cadencia variable: el video se corta por tiempo
FPS_FUENTE = 30

# El lower third espera el nombre de la presentadora (PROFE_CIERRES en la base).
ITEMS = [('lt01', 'lt', 4.1, 12.1, PROFE_CIERRES)] if PROFE_CIERRES else []
