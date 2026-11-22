# -*- coding: utf-8 -*-
r"""Inicio de la unidad 3 de «Delitos informáticos» (22 nov 2026). **Entrega provisional** (ver `base_di_profe`).

Fuente: `1. bienvenida unidad 3.mov` (5:57,6), editada por el profe. Su cartón «Unidad 3 · Investigación y judicialización · La pregunta de la unidad: ¿cómo lo investigo?» va de 0 a 2,08 s; la primera palabra («Bienvenido a la unidad tres»), en 2,56. Termina en «…Bienvenidos a la unidad número tres» (354,76) con 0,7 s de aire; no trae cartón final.

La placa «DAE | FISCALÍA» de arriba a la derecha se tapa en `01 VIDEO/DIU3I_fuente_limpia.mp4` (`limpia_logo_di.py`;
la placa está en 2,16–10,36, 12,48–17,80 y 352,20–357,56 s). Adentro no se corta nada: sus rótulos y sus láminas quedan.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_di_profe import *  # noqa: E402,F401,F403
from base_di_profe import armar, armar_unidad  # noqa: E402,F401

globals().update(armar_unidad(3, 'INICIO', '1. bienvenida unidad 3.mov', [(2.16, 355.46)]))

ITEMS = []
