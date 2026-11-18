# -*- coding: utf-8 -*-
r"""Cierre de la unidad 1 de «Bienes en el proceso penal» (17 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos
(ver `base_bi_unidades`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo
compuesto.

**Fuente.** `bi_u1_cierre_fuente.mp4` (Drive del curso → VIDEOS UNIDADES, «Bienes -  Unidad  1 - cierre.mp4»,
`1NMN3Gn9REzjRHWjIdWQNHXD6IyvJQ2q0`, del 17 nov): 1920×1080, 30 fps parejos, 47.649 cuadros (1588,3 s). Trae
pegada una intro en los cuadros 0–277 y un outro desde el cuadro 47.371. STT (Scribe, WAV a 16 kHz):
3.246 palabras, de 9,86 a 1578,54 s, leído de corrido.

Entra del cuadro 281 al 47371: desde 0,49 s antes de la primera palabra hasta 0,49 s después
de la última. Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_bi_unidades import *  # noqa: E402,F401,F403
from base_bi_unidades import armar_unidad, PROFE  # noqa: E402

globals().update(armar_unidad(1, 'CIERRE', 281, 47371))

ITEMS = [
    ('lt01', 'lt', 10.9, 18.9, PROFE),
]
