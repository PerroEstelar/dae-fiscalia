# -*- coding: utf-8 -*-
r"""Cierre de la unidad 4 de «Delitos informáticos» (22 nov 2026). **Entrega provisional** (ver `base_di_profe`).

Fuente: `6. cierre unidad 4.mov` (5:51,5), editada por el profe. Su cartón «Finalización · Cierre de la Unidad 4» va de 0 a 5,00 s y el profe empieza a hablar en el mismo corte («Llegamos al cierre…»): entra en el cuadro 125. Al final, el mismo cartón desde 346,44: termina un cuadro antes, 0,2 s después de «…Felicitaciones por llegar hasta aquí» (346,20; el audio de su cartón es silencio digital).

La placa «DAE | FISCALÍA» de arriba a la derecha se tapa en `01 VIDEO/DIU4C_fuente_limpia.mp4` (`limpia_logo_di.py`;
la placa está en 5,00–12,20 y 328,40–333,72 s). Adentro no se corta nada: sus rótulos y sus láminas quedan.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_di_profe import *  # noqa: E402,F401,F403
from base_di_profe import armar, armar_unidad  # noqa: E402,F401

globals().update(armar_unidad(4, 'CIERRE', '6. cierre unidad 4.mov', [(5.00, 346.40)]))

ITEMS = []
