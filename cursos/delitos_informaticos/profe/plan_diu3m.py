# -*- coding: utf-8 -*-
r"""Video intermedio (síntesis) de la unidad 3 de «Delitos informáticos» (22 nov 2026). **Entrega provisional** (ver `base_di_profe`).

Fuente: `2. Intermedia unidad 3.mov` (5:24,1), editada por el profe. Su cartón «Acompañamiento docente · Síntesis de la Unidad 3» va de 0 a 5,08 s; la primera palabra («Buenas de nuevo»), en 6,96: entra medio segundo antes. Termina con el archivo (la última palabra, «…dentro de esta unidad», en 323,88).

La placa «DAE | FISCALÍA» de arriba a la derecha se tapa en `01 VIDEO/DIU3M_fuente_limpia.mp4` (`limpia_logo_di.py`;
la placa está en 18,64–23,96 s). Adentro no se corta nada: sus rótulos y sus láminas quedan.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_di_profe import *  # noqa: E402,F401,F403
from base_di_profe import armar, armar_unidad  # noqa: E402,F401

globals().update(armar_unidad(3, 'INTERMEDIO', '2. Intermedia unidad 3.mov', [(6.46, 324.00)]))

ITEMS = []
