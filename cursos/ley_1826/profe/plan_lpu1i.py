# -*- coding: utf-8 -*-
r"""Inicio de la unidad 1, «Finalidad, ámbito de aplicación y procedencia», de «Ley 1826 de 2017: procedimiento penal
especial abreviado y acusador privado» (19 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos (ver
`base_lp_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo compuesto.

**Fuente.** Drive «VIDEOS CURSO PPA» (`1glwsHbdJS1ltwziPilxhj4od6Ky4o-Cf`), «Copia de entrada unidad 1-18/11/2026,
18:26.mp4» (`1V6EKTtRNWik_5O9wD7FA7w_cBUw77-Ok`, 159.482.226 bytes): 1920×1080, 30 fps parejos, 9.548 cuadros
(5:18,3), audio mono. El profe se recorta y va sobre el fondo de la Fiscalía (`recorta_cuadro.py`, ver la base): la
`ORIGINAL` del plan es el recortado. STT (Scribe): 708 palabras; la voz va de 11,00 a 316,35 s (medida en el audio).

Entra del cuadro 315 (10,50 s: medio segundo antes de la primera palabra) al 9515 (317,17 s: 0,8 s después de la
última).

En la carpeta hay otro archivo con los mismos bytes («Copia de entrada unidad 1.mp4»,
`1g3bOsK7IMwHPa6-ut_vQdZdOIsuJpWli`): no se usa. Sin cortes: una sola toma leída de corrido.

El lower third entra 1,2 s después de la primera palabra y dura 8 s. Los tiempos de `ITEMS` están en segundos de la
fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_lp_profe import *  # noqa: E402,F401,F403
from base_lp_profe import armar_unidad, PROFE  # noqa: E402

globals().update(armar_unidad(1, 'INICIO', [(315, 9515)]))

ITEMS = [
    ('lt01', 'lt', 12.2, 20.2, PROFE),
]
