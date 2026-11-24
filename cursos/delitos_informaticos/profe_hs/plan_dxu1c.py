# -*- coding: utf-8 -*-
r"""Cierre de la unidad 1 de «Delitos informáticos», Humberto Suárez Gómez (24 nov 2026). **Entrega provisional** (ver
`base_hs_profe`).

Fuente: `Cierre Unidad 1.mov`.

De «Llegamos al cierre de la primera unidad…» a «…Nos vemos allá».

**Un corte:** sale «a--» en «pasamos a-- de comprender a tipificar» (152,72–153,22; bordes en el bache después de
«pasamos», −42 dB, y en el silencio antes de «de», −49 dB).

**v2 (24 nov 2026):** en la v1 el corte empezaba en 152,60 y se llevaba también el «-mos» de «pasamos»: quedaba «pasa
de comprender» (lo dijo Scribe sobre la entrega). Las sílabas van pegadas y el STT de la fuente marcaba el final de
«pasamos» tarde: el borde sale de la energía en ventanas de 5 ms.

**Sin rótulo (24 nov 2026):** el nombre del profe no está confirmado (ver `base_hs_profe`). La v3 va sin rótulo y
con «24NOV» en el nombre del archivo.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_hs_profe import *  # noqa: E402,F401,F403
from base_hs_profe import armar_curso, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad('dxu1c', 1, 'CIERRE', 'Cierre Unidad 1.mov',
                              [(2.29, 152.72), (153.22, 157.04)]))

VERSION = 3
COMPUESTO = R + '/01 VIDEO/DXU1C_compuesto_v2.mp4'  # noqa: F821
NOMBRE_LINEA = 'DI HS - U1 - CIERRE v3'

ITEMS = rotulo(T0 + 1.5)  # noqa: F821   # vacío: sin rótulo
