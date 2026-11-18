# -*- coding: utf-8 -*-
r"""Cierre de la unidad 3, «Tráfico de migrantes y trata de personas» (17–18 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos
(ver `base_tr_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo compuesto.

**Fuente.** Drive del curso → VIDEOS, «UNIDAD 3/Cierre de la Unidad 3.webm» (`18XZyGAk7tsVIaxuHm2rpS1_5qbqJxhIa`):
1280×720, H.264 en WebM con cadencia variable, Opus mono; 449,6 s. STT (Scribe, WAV a 16 kHz): 952 palabras, de 3,34 a 446,84 s.

Entra de 2,84 a 447,64 s: medio segundo antes de la primera palabra y hasta 0,8 s después de la última
(o hasta el final del archivo). Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_tr_profe import *  # noqa: E402,F401,F403
from base_tr_profe import armar_curso, armar_unidad, PROFE_CIERRES  # noqa: E402,F401

globals().update(armar_unidad(3, 'CIERRE', '.webm', 2.84, 447.64))
XY, VENTANA = (0, 40), (1143, 643)
POR_TIEMPO = True       # cadencia variable: el video se corta por tiempo
FPS_FUENTE = 30

# El lower third espera el nombre de la presentadora (PROFE_CIERRES en la base).
ITEMS = [('lt01', 'lt', 4.3, 12.3, PROFE_CIERRES)] if PROFE_CIERRES else []
