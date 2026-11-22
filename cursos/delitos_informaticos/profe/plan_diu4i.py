# -*- coding: utf-8 -*-
r"""Inicio de la unidad 4 de «Delitos informáticos» (22 nov 2026). **Entrega provisional** (ver `base_di_profe`).

Fuente: `4. Bienvenida Unidad 4.mov` (5:55,7), editada por el profe. Su cartón «Unidad 4 · Evidencia digital · La pregunta de la unidad: ¿cómo lo pruebo?» va de 0 a 5,00 s; la primera palabra, en 5,86. Al final, su cartón «¡Bienvenido a la Unidad 4!» desde 350,60: termina 0,7 s después de «…Bienvenido a la unidad número cuatro» (349,62). `4. Bienvenida Unidad 4 (1).mov` es el mismo archivo.

La placa «DAE | FISCALÍA» de arriba a la derecha se tapa en `01 VIDEO/DIU4I_fuente_limpia.mp4` (`limpia_logo_di.py`;
la placa está en 22,28–30,04 y 345,44–350,60 s). Adentro no se corta nada: sus rótulos y sus láminas quedan.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_di_profe import *  # noqa: E402,F401,F403
from base_di_profe import armar, armar_unidad  # noqa: E402,F401

globals().update(armar_unidad(4, 'INICIO', '4. Bienvenida Unidad 4.mov', [(5.36, 350.32)]))

ITEMS = []
