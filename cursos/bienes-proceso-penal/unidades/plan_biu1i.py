# -*- coding: utf-8 -*-
r"""Inicio de la unidad 1 de «Bienes en el proceso penal» (17 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos
(ver `base_bi_unidades`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo
compuesto.

**Fuente.** `bi_u1_inicio_fuente.mp4` (Drive del curso → VIDEOS UNIDADES, «Bienes -  Unidad  1 - Inicio.mp4»,
`1Jn35bOga4zLvl2DV0W8sDnye6Q4Rd6MS`, del 17 nov): 1920×1080, 30 fps parejos, 12.676 cuadros (422,5 s). Trae
pegada una intro en los cuadros 0–277 y un outro desde el cuadro 12.398. STT (Scribe, WAV a 16 kHz):
844 palabras, de 9,90 a 412,42 s, leído de corrido.

Entra del cuadro 282 al 12397: desde 0,50 s antes de la primera palabra hasta 0,81 s después
de la última. Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_bi_unidades import *  # noqa: E402,F401,F403
from base_bi_unidades import armar_unidad, PROFE  # noqa: E402

globals().update(armar_unidad(1, 'INICIO', 282, 12397))

ITEMS = [
    ('lt01', 'lt', 10.9, 18.9, PROFE),
]
