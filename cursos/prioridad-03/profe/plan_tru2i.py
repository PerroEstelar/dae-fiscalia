# -*- coding: utf-8 -*-
r"""Introducción de la unidad 2, «Tráfico de migrantes y trata de personas» (17–18 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos
(ver `base_tr_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo compuesto.

**Fuente.** Drive del curso → VIDEOS, «UNIDAD 2/Introducción a la Unidad 2.mp4» (`1zf_awWI_VRDlUrBHNtsns9vYulaNkb-M`):
1080×1920 a 25 fps (avatar vertical); 399,0 s. STT (Scribe, WAV a 16 kHz): 1014 palabras, de 0,86 a 398,18 s.

Entra de 0,36 a 398,98 s: medio segundo antes de la primera palabra y hasta 0,8 s después de la última
(o hasta el final del archivo). Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_tr_profe import *  # noqa: E402,F401,F403
from base_tr_profe import armar_curso, armar_unidad, vertical, PROFE  # noqa: E402,F401

globals().update(armar_unidad(2, 'INICIO', '.mp4', 0.36, 398.98))
FPS_FUENTE = 25
FPS_COMPUESTO = '25'
PREFILTRO = vertical(230)      # recorte cuadrado desde y=230

ITEMS = [
    ('lt01', 'lt', 1.9, 9.9, PROFE),
]
