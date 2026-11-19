# -*- coding: utf-8 -*-
r"""Cierre de la unidad 4, «Terminación anticipada y mecanismos restaurativos», de «Ley 1826 de 2017: procedimiento
penal especial abreviado y acusador privado» (19 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos (ver
`base_lp_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo compuesto.

**Fuente.** Drive «VIDEOS CURSO PPA» (`1glwsHbdJS1ltwziPilxhj4od6Ky4o-Cf`), «Copia de cierre unidad 4-18/11/2026,
20:59.mp4» (`1MGCX6Enax5Yq9bQCxoAsp_n410Xg7i1J`, 190.054.937 bytes): 1920×1080, 30 fps parejos, 11.176 cuadros
(6:12,5), audio mono. El profe se recorta y va sobre el fondo de la Fiscalía (`recorta_cuadro.py`, ver la base): la
`ORIGINAL` del plan es el recortado. STT (Scribe): 789 palabras; la voz va de 8,81 a 370,29 s (medida en el audio).

Entra del cuadro 249 (8,30 s: medio segundo antes de la primera palabra) al 11133 (371,10 s: 0,8 s después de la
última).

Sin cortes: una sola toma leída de corrido. Una pausa de 2,1 s (2:14,5 a 2:16,6) antes de «Delimitamos
también…»: se deja.

El lower third entra 1,2 s después de la primera palabra y dura 8 s. Los tiempos de `ITEMS` están en segundos de la
fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_lp_profe import *  # noqa: E402,F401,F403
from base_lp_profe import armar_unidad, PROFE  # noqa: E402

globals().update(armar_unidad(4, 'CIERRE', [(249, 11133)]))

ITEMS = [
    ('lt01', 'lt', 10.0, 18.0, PROFE),
]
