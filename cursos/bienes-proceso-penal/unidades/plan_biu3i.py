# -*- coding: utf-8 -*-
r"""Inicio de la unidad 3 de «Bienes en el proceso penal» (17 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos
(ver `base_bi_unidades`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo
compuesto.

**Fuente.** `bi_u3_inicio_fuente.mp4` (Drive del curso → VIDEOS UNIDADES, «Bienes -  Unidad  3 - inicio.mp4»,
`1KV_2nptVn_KVIlT5bHD6QgQ9HPGU_r8x`, del 17 nov): 1920×1080, 30 fps parejos, 10.336 cuadros (344,5 s). Trae
pegada una intro en los cuadros 0–277 y un outro desde el cuadro 10.058. STT (Scribe, WAV a 16 kHz):
692 palabras, de 9,92 a 335,04 s, leído de corrido.

Entra del cuadro 283 al 10058: desde 0,49 s antes de la primera palabra hasta 0,23 s después
de la última. Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_bi_unidades import *  # noqa: E402,F401,F403
from base_bi_unidades import armar_unidad, PROFE  # noqa: E402

globals().update(armar_unidad(3, 'INICIO', 283, 10058))

ITEMS = [
    ('lt01', 'lt', 10.9, 18.9, PROFE),
]
