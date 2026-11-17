# -*- coding: utf-8 -*-
r"""Inicio de la unidad 4 de «Terminaciones anticipadas» (17 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos
(ver «Unidades» en `base_ta_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el
mismo compuesto.

**Fuente.** `ta_u4_inicio_fuente.mp4` (Drive del curso → VIDEOS › VIDEOS UNIDADES,
«Terminaciones Anticipadas Inicio U4 Juan Peña.mp4», `1vgGm-htgbmrtefXO99s5UPNPeS8dMQwe`, del 17 nov): 1920×1080, 30 fps
parejos, 14.300 cuadros (476,7 s). STT (Scribe, WAV a 16 kHz): 1.098 palabras, de 4,46 a 471,14 s, leído
de corrido y en una sola toma.

Entra del cuadro 119 (medio segundo antes de la primera palabra) al 14158 (0,8 s después de la
última). Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_ta_profe import *  # noqa: E402,F401,F403
from base_ta_profe import armar_unidad, PROFE, XY_UNIDADES, VENTANA_UNIDADES  # noqa: E402

XY, VENTANA = XY_UNIDADES, VENTANA_UNIDADES
MATRIZ_FUENTE = 'bt709'
globals().update(armar_unidad(4, 'INICIO', 119, 14158))

ITEMS = [
    ('lt01', 'lt', 5.5, 13.5, PROFE),
]
