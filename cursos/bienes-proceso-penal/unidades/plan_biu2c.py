# -*- coding: utf-8 -*-
r"""Cierre de la unidad 2 de «Bienes en el proceso penal» (17 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos
(ver `base_bi_unidades`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo
compuesto.

**Fuente.** `bi_u2_cierre_fuente.mp4` (Drive del curso → VIDEOS UNIDADES, «Bienes -  Unidad  2 - cierre.mp4»,
`1go98QpFXz_3xG9oBBmkQSDAdYHnwA52q`, del 17 nov): 1920×1080, 30 fps parejos, 41.257 cuadros (1375,2 s). Trae
pegada una intro en los cuadros 0–277 y un outro desde el cuadro 40.979. STT (Scribe, WAV a 16 kHz):
2.801 palabras, de 9,78 a 1365,96 s, leído de corrido.

Entra del cuadro 280 al 40979: desde 0,45 s antes de la primera palabra hasta 0,01 s después
de la última. Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_bi_unidades import *  # noqa: E402,F401,F403
from base_bi_unidades import armar_unidad, PROFE  # noqa: E402

globals().update(armar_unidad(2, 'CIERRE', 280, 40979))

ITEMS = [
    ('lt01', 'lt', 10.8, 18.8, PROFE),
]
