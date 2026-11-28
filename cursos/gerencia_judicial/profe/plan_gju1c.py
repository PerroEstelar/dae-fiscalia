# -*- coding: utf-8 -*-
r"""Cierre de la unidad 1, «Contexto estratégico y política criminal», de «Gerencia judicial» (27 nov 2026). **Entrega provisional** (ver `base_gj_profe`).

**Fuente.** `01 VIDEO/gj_u1c_fuente.mp4`, sacada de `00 FUENTES/VIDEO 3 … apertura y cierre.mp4` (cuadros 5324 a 9998 de esa
grabación; los tramos de abajo ya están en cuadros del _fuente). Entra medio segundo antes de «Llegamos» y sale 0,8 s después de «gracias.».

**Sin cortes.**

Empieza en «Llegamos al final de la unidad primera»: sale el rótulo leído «Cierre de la unidad primera.». Se deja «se exige en los
acuerdos— en algunos acuerdos» (no hay silencio donde cortar).

El lower third entra 1,2 s después de la primera palabra y dura 8 s.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_gj_profe import *  # noqa: E402,F401,F403
from base_gj_profe import armar_unidad, PROFE, CERRADO  # noqa: E402

globals().update(armar_unidad(1, 'CIERRE', [(105, 4623)]))

SUAVE = 3            # cuadros de mezcla en un corte sin cambio de plano

ITEMS = [
    ('lt01', 'lt', 5.19, 13.19, PROFE),
]
