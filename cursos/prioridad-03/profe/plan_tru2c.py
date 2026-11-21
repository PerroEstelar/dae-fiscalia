# -*- coding: utf-8 -*-
r"""Cierre de la unidad 2, «Tráfico de migrantes y trata de personas» (17–18 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos
(ver `base_tr_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo compuesto.

**Fuente.** Drive del curso → VIDEOS, «UNIDAD 2/Cierre de la Unidad 2.webm» (`1z1dC9NXBTZeJizyKQGARJItuYRB95Jpb`):
1280×720, H.264 en WebM con cadencia variable, Opus mono; 446,6 s. STT (Scribe, WAV a 16 kHz): 948 palabras, de 2,88 a 444,10 s.

Entra de 2,38 a 444,90 s: medio segundo antes de la primera palabra y hasta 0,8 s después de la última
(o hasta el final del archivo). Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_tr_profe import *  # noqa: E402,F401,F403
from base_tr_profe import armar_curso, armar_unidad, PROFE_CIERRES  # noqa: E402,F401

globals().update(armar_unidad(2, 'CIERRE', '.webm', 2.38, 444.9))
XY, VENTANA = (0, 40), (1143, 643)
POR_TIEMPO = True       # cadencia variable: el video se corta por tiempo
FPS_FUENTE = 30

# v2 (21 nov 2026): con el rótulo de la presentadora, que Sebastián confirmó (PROFE_CIERRES en la base). La v1 iba
# sin rótulo; mismo compuesto.
VERSION = 2
ITEMS = [('lt01', 'lt', 3.9, 11.9, PROFE_CIERRES)] if PROFE_CIERRES else []
