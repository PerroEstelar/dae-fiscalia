# -*- coding: utf-8 -*-
r"""Cierre de la unidad 2, «Procedimiento: investigación, traslado, audiencia concentrada y juicio», de «Ley 1826 de
2017: procedimiento penal especial abreviado y acusador privado» (19 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos (ver
`base_lp_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo compuesto.

**Fuente.** Drive «VIDEOS CURSO PPA» (`1glwsHbdJS1ltwziPilxhj4od6Ky4o-Cf`), «Copia de Cierre unidad 2-18/11/2026,
19:59.mp4» (`19zNCrnk7_yuUlE_C5javMZ7ZRSIXsh30`, 135.208.899 bytes): 1920×1080, 30 fps parejos, 9.344 cuadros
(5:11,5), audio mono. El profe se recorta y va sobre el fondo de la Fiscalía (`recorta_cuadro.py`, ver la base): la
`ORIGINAL` del plan es el recortado. STT (Scribe): 675 palabras; la voz va de 5,74 a 309,06 s (medida en el audio).

Entra del cuadro 157 (5,23 s: medio segundo antes de la primera palabra) al 9296 (309,87 s: 0,8 s después de la
última).

Sin cortes: una sola toma leída de corrido. **Termina sin despedida**: la última frase es «Los invito a
revisar y consultar la retroalimentación detallada de cada una de las actividades propuestas y desarrolladas».

El lower third entra 1,2 s después de la primera palabra y dura 8 s. Los tiempos de `ITEMS` están en segundos de la
fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_lp_profe import *  # noqa: E402,F401,F403
from base_lp_profe import armar_unidad, PROFE  # noqa: E402

globals().update(armar_unidad(2, 'CIERRE', [(157, 9296)]))

ITEMS = [
    ('lt01', 'lt', 6.9, 14.9, PROFE),
]
