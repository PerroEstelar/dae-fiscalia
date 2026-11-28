# -*- coding: utf-8 -*-
r"""Inicio de la unidad 3, «Gestión de servicios, planeación y seguimiento», de «Gerencia judicial» (27 nov 2026). **Entrega provisional** (ver `base_gj_profe`).

**Fuente.** `01 VIDEO/gj_u3i_fuente.mp4`, sacada de `00 FUENTES/VIDEO 3 … apertura y cierre.mp4` (cuadros 20101 a 25339 de esa
grabación; los tramos de abajo ya están en cuadros del _fuente). Entra medio segundo antes de «Bienvenidas,» y sale 0,8 s después de «tercera.».

**1 cortes**:
- 13:33.9 de la grabación, «…cambia ninguna decisión, sobra. [A propósito de la evaluación integradora, única al cierre de cada unidad.] Los casos se narran…»: salen los cuadros 4315 a 4500 de la fuente (6.20 s); energía en los bordes 49 y 40 dB bajo la voz; diferencia de imagen 6.0 (plano cerrado después).

Empieza en «Bienvenidas, bienvenidos a la unidad tres»: sale el rótulo leído «Unidad tres. Gestión de servicios, planeación y
seguimiento.» (el cartón de título ya lo dice).

El lower third entra 1,2 s después de la primera palabra y dura 8 s.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_gj_profe import *  # noqa: E402,F401,F403
from base_gj_profe import armar_unidad, PROFE, CERRADO  # noqa: E402

globals().update(armar_unidad(3, 'INICIO', [(230, 4315), (4501, 4643, CERRADO), (4643, 5186)]))

SUAVE = 3            # cuadros de mezcla en un corte sin cambio de plano

ITEMS = [
    ('lt01', 'lt', 9.35, 17.35, PROFE),
]
