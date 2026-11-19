# -*- coding: utf-8 -*-
r"""Cierre del curso de «Ley 1826 de 2017: procedimiento penal especial abreviado y acusador privado» (19 nov 2026).
**Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos (ver
`base_lp_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo compuesto.

**Fuente.** Drive «VIDEOS CURSO PPA» (`1glwsHbdJS1ltwziPilxhj4od6Ky4o-Cf`), «Copia de cierre del curso-18/11/2026,
21:37.mp4» (`1pJBEjAlp0x-nw5Q_ivJW5GuvwMMd1Kf5`, 254.576.116 bytes): 1920×1080, 30 fps parejos, 14.495 cuadros
(8:03,2), audio mono. El profe se recorta y va sobre el fondo de la Fiscalía (`recorta_cuadro.py`, ver la base): la
`ORIGINAL` del plan es el recortado. STT (Scribe): 981 palabras; la voz va de 5,04 a 479,93 s (medida en el audio).

Entra del cuadro 136 (4,53 s: medio segundo antes de la primera palabra) al 14422 (480,73 s: 0,8 s después de la
última).

**Qué se deja.** «…el descubrimiento recíproco de la, de la defensa» (3:22): el primer «de la» va pegado a
«recíproco», sin un valle donde cortar. Dos pausas de más de 2 s (4:11,3 a 4:13,5 y 7:15,6 a 7:18,4), las dos
entre un bloque y el siguiente («En la unidad tres…», «Estimadas y estimados participantes…»).

El lower third entra 1,2 s después de la primera palabra y dura 8 s. Los tiempos de `ITEMS` están en segundos de la
fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_lp_profe import *  # noqa: E402,F401,F403
from base_lp_profe import armar_curso, PROFE  # noqa: E402

globals().update(armar_curso('CIERRE', [(136, 14422)]))

ITEMS = [
    ('lt01', 'lt', 6.3, 14.3, PROFE),
]
