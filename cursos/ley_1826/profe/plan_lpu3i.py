# -*- coding: utf-8 -*-
r"""Inicio de la unidad 3, «Acusador privado, conversión y reversión», de «Ley 1826 de 2017: procedimiento penal
especial abreviado y acusador privado» (19 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos (ver
`base_lp_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo compuesto.

**Fuente.** Drive «VIDEOS CURSO PPA» (`1glwsHbdJS1ltwziPilxhj4od6Ky4o-Cf`), «Copia de bienvenida unidad
3-18/11/2026, 20:32.mp4» (`1uDUhtYz2m-mHxdS6IoWWwk7_nGu7DH54`, 179.765.779 bytes): 1920×1080, 30 fps parejos, 11.075
cuadros (6:09,2), audio mono. El profe se recorta y va sobre el fondo de la Fiscalía (`recorta_cuadro.py`, ver la
base): la `ORIGINAL` del plan es el recortado. STT (Scribe): 810 palabras; la voz va de 6,85 a 367,39 s (medida en
el audio).

Entra del cuadro 190 (6,33 s: medio segundo antes de la primera palabra) al 11046 (368,20 s: 0,8 s después de la
última).

Sin cortes: una sola toma leída de corrido. Una pausa de 2,2 s (0:58,2 a 1:00,3) antes de «En la lección
uno…»: se deja.

El lower third entra 1,2 s después de la primera palabra y dura 8 s. Los tiempos de `ITEMS` están en segundos de la
fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_lp_profe import *  # noqa: E402,F401,F403
from base_lp_profe import armar_unidad, PROFE  # noqa: E402

globals().update(armar_unidad(3, 'INICIO', [(190, 11046)]))

ITEMS = [
    ('lt01', 'lt', 8.1, 16.1, PROFE),
]
