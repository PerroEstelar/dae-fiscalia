# -*- coding: utf-8 -*-
r"""Cierre de la unidad 2 de «Terminaciones anticipadas» (17 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos
(ver «Unidades» en `base_ta_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el
mismo compuesto.

**Fuente.** `ta_u2_cierre_fuente.mp4` (Drive del curso → VIDEOS › VIDEOS UNIDADES,
«Terminaciones Anticipadas Cierre U2 Juan-Peña.mp4», `12kgRw06veA86JXAo2HdXoyKNqSi5QYUh`, del 17 nov): 1920×1080, 30 fps
parejos, 11.014 cuadros (367,1 s). STT (Scribe, WAV a 16 kHz): 892 palabras, de 2,28 a 359,70 s, leído
de corrido y en una sola toma.

Entra del cuadro 53 (medio segundo antes de la primera palabra) al 10815 (0,8 s después de la
última). Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_ta_profe import *  # noqa: E402,F401,F403
from base_ta_profe import armar_unidad, PROFE, XY_UNIDADES, VENTANA_UNIDADES  # noqa: E402

XY, VENTANA = XY_UNIDADES, VENTANA_UNIDADES
MATRIZ_FUENTE = 'bt709'
globals().update(armar_unidad(2, 'CIERRE', 53, 10815))

ITEMS = [
    ('lt01', 'lt', 3.3, 11.3, PROFE),
]
