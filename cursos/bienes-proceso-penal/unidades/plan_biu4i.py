# -*- coding: utf-8 -*-
r"""Inicio de la unidad 4 de «Bienes en el proceso penal» (17 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos
(ver `base_bi_unidades`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo
compuesto.

**Fuente.** `bi_u4_inicio_fuente.mp4` (Drive del curso → VIDEOS UNIDADES, «Bienes -  Unidad  4 - inicio.mp4»,
`1475aYsyLMY6M_DxAOVg5TijIHaHGsIWv`, del 17 nov): 1920×1080, 30 fps parejos, 9.715 cuadros (323,8 s). Trae
pegada una intro en los cuadros 0–277 y un outro desde el cuadro 9.437. STT (Scribe, WAV a 16 kHz):
692 palabras, de 9,96 a 314,10 s, leído de corrido.

Entra del cuadro 284 al 9437: desde 0,49 s antes de la primera palabra hasta 0,47 s después
de la última. Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_bi_unidades import *  # noqa: E402,F401,F403
from base_bi_unidades import armar_unidad, PROFE  # noqa: E402

globals().update(armar_unidad(4, 'INICIO', 284, 9437))

ITEMS = [
    ('lt01', 'lt', 11.0, 19.0, PROFE),
]
