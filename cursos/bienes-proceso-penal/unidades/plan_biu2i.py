# -*- coding: utf-8 -*-
r"""Inicio de la unidad 2 de «Bienes en el proceso penal» (17 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos
(ver `base_bi_unidades`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo
compuesto.

**Fuente.** `bi_u2_inicio_fuente.mp4` (Drive del curso → VIDEOS UNIDADES, «Bienes -  Unidad  2 - Inicio.mp4»,
`1b6OgEPvDrYNyNbkGakJgI_hXhp-gWsnE`, del 17 nov): 1920×1080, 30 fps parejos, 13.759 cuadros (458,6 s). Trae
pegada una intro en los cuadros 0–277 y un outro desde el cuadro 13.481. STT (Scribe, WAV a 16 kHz):
946 palabras, de 13,70 a 446,58 s, leído de corrido.

Entra del cuadro 396 al 13421: desde 0,50 s antes de la primera palabra hasta 0,79 s después
de la última. Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_bi_unidades import *  # noqa: E402,F401,F403
from base_bi_unidades import armar_unidad, PROFE  # noqa: E402

globals().update(armar_unidad(2, 'INICIO', 396, 13421))

ITEMS = [
    ('lt01', 'lt', 14.7, 22.7, PROFE),
]
