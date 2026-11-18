# -*- coding: utf-8 -*-
r"""Introducción de la unidad 1, «Tráfico de migrantes y trata de personas» (17–18 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos
(ver `base_tr_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo compuesto.

**Fuente.** Drive del curso → VIDEOS, «UNIDAD 1/Introducción a la Unidad 1.mp4» (`1nAIK96kjlR-_R-FvzAmTJO_8UoEGBQ2Z`):
1920×1080 a 25 fps con el avatar vertical entre barras negras (columnas 656–1263); 397,7 s. STT (Scribe, WAV a 16 kHz): 1026 palabras, de 0,86 a 396,74 s.

Entra de 0,36 a 397,54 s: medio segundo antes de la primera palabra y hasta 0,8 s después de la última
(o hasta el final del archivo). Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_tr_profe import *  # noqa: E402,F401,F403
from base_tr_profe import armar_curso, armar_unidad, vertical, PROFE  # noqa: E402,F401

globals().update(armar_unidad(1, 'INICIO', '.mp4', 0.36, 397.54))
FPS_FUENTE = 25
FPS_COMPUESTO = '25'
PREFILTRO = vertical(120, x=656, lado=608)      # recorte cuadrado desde y=120

ITEMS = [
    ('lt01', 'lt', 1.9, 9.9, PROFE),
]
