# -*- coding: utf-8 -*-
r"""Cierre de la unidad 1, «Finalidad, ámbito de aplicación y procedencia», de «Ley 1826 de 2017: procedimiento penal
especial abreviado y acusador privado» (19 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos (ver
`base_lp_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo compuesto.

**Fuente.** Drive «VIDEOS CURSO PPA» (`1glwsHbdJS1ltwziPilxhj4od6Ky4o-Cf`), «Copia de cierre unidad 1-18/11/2026,
19:10.mp4» (`1vU78NqLh_kdvKoIe1rGgzPB8-tlX9eNB`, 148.382.074 bytes): 1920×1080, 30 fps parejos, 8.831 cuadros
(4:54,4), audio mono. El profe se recorta y va sobre el fondo de la Fiscalía (`recorta_cuadro.py`, ver la base): la
`ORIGINAL` del plan es el recortado. STT (Scribe): 664 palabras; la voz va de 8,77 a 292,92 s (medida en el audio).

Entra del cuadro 248 (8,27 s: medio segundo antes de la primera palabra) al 8812 (293,73 s: 0,8 s después de la
última).

Sin cortes: una sola toma leída de corrido.

El lower third entra 1,2 s después de la primera palabra y dura 8 s. Los tiempos de `ITEMS` están en segundos de la
fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_lp_profe import *  # noqa: E402,F401,F403
from base_lp_profe import armar_unidad, PROFE  # noqa: E402

globals().update(armar_unidad(1, 'CIERRE', [(248, 8812)]))

ITEMS = [
    ('lt01', 'lt', 10.0, 18.0, PROFE),
]
