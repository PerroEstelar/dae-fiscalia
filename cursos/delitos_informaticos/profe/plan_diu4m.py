# -*- coding: utf-8 -*-
r"""Video intermedio (síntesis) de la unidad 4 de «Delitos informáticos» (22 nov 2026). **Entrega provisional** (ver `base_di_profe`).

Fuente: `5. intermedio unidad 4.mov` (6:40,3), editada por el profe. Su cartón «Acompañamiento docente · Síntesis de la Unidad 4» va de 0 a 4,20 s; la primera palabra («Hola de nuevo»), en 4,52. Termina 0,7 s después de «…finalizando esta unidad» (399,04); no trae cartón final.

La placa «DAE | FISCALÍA» de arriba a la derecha se tapa en `01 VIDEO/DIU4M_fuente_limpia.mp4` (`limpia_logo_di.py`;
la placa está en 10,48–15,68 s). Adentro no se corta nada: sus rótulos y sus láminas quedan.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_di_profe import *  # noqa: E402,F401,F403
from base_di_profe import armar, armar_unidad  # noqa: E402,F401

globals().update(armar_unidad(4, 'INTERMEDIO', '5. intermedio unidad 4.mov', [(4.28, 399.74)]))

ITEMS = []
