# -*- coding: utf-8 -*-
r"""Inicio de la unidad 4, «Articulación interinstitucional y territorial», de «Gerencia judicial» (27 nov 2026). **Entrega provisional** (ver `base_gj_profe`).

**Fuente.** `01 VIDEO/gj_u4i_fuente.mp4`, sacada de `00 FUENTES/VIDEO 3 … apertura y cierre.mp4` (cuadros 31032 a 35737 de esa
grabación; los tramos de abajo ya están en cuadros del _fuente). Entra medio segundo antes de «Bienvenidos» y sale 0,8 s después de «unidad.».

**1 cortes**:
- 18:35.8 de la grabación, «…de la actuación penal. [Frente a este actor, ¿qué relación tengo? ¿Jerarquía? ¿Dirección funcional? ¿Coordinación? ¿Influencia?] El eje es una…»: salen los cuadros 2442 a 2758 de la fuente (10.57 s); energía en los bordes 42 y 48 dB bajo la voz; diferencia de imagen 7.5 (plano cerrado después).



El lower third entra 1,2 s después de la primera palabra y dura 8 s.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_gj_profe import *  # noqa: E402,F401,F403
from base_gj_profe import armar_unidad, PROFE, CERRADO  # noqa: E402

globals().update(armar_unidad(4, 'INICIO', [(46, 2442), (2759, 2904, CERRADO), (2904, 4653)]))

SUAVE = 3            # cuadros de mezcla en un corte sin cambio de plano

ITEMS = [
    ('lt01', 'lt', 3.23, 11.23, PROFE),
]
