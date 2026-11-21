# -*- coding: utf-8 -*-
r"""Inicio de la unidad 3 de «Derecho de petición y acción de tutela» (20 nov 2026). **Entrega provisional** (ver `base_dp_profe`).

Fuente: `VIDEO4 - PRESENTACION UNIDAD 3- TOMA 1.mp4`.

Va entera, sin cortes adentro: de «Llega a su dependencia una comunicación…» a «…a quienes deben atenderlas» (sale
«Listo»). Empieza en 5,30 y no en 5,05: entre 0,5 y 5,4 s hay un ruido que sube hasta −21 dB antes de la primera
palabra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_dp_profe import *  # noqa: E402,F401,F403
from base_dp_profe import armar, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad(3, 'INICIO', 'VIDEO4 - PRESENTACION UNIDAD 3- TOMA 1.mp4', [(5.30, 459.20)]))

ITEMS = rotulo(T0 + 1.5)  # noqa: F821
