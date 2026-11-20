# -*- coding: utf-8 -*-
r"""Cierre de la unidad 3 de «Audiencias preliminares y medidas de aseguramiento» (20 nov 2026). **Entrega provisional.**

Fuente: `Unidad 3 - Recapitulación.mp4` (660.52 s). Es el «Video» de la actividad de acompañamiento dirigido (3.8 de la ficha: «una síntesis de los principales temas abordados en la unidad»).

**Tramo:** desde 2.67 s (0,45 s antes de «Muchas felicitaciones. Has», a 3.12 s; antes hay silencio digital) hasta 659.66 s (0,7 s después de la última palabra; el archivo dura 660.52). Sin cortes:
la lee de corrido. Termina «…han culminado la unidad tercera.».
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_ap_profe import *  # noqa: E402,F401,F403
from base_ap_profe import armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad(3, 'CIERRE', [(2.67, 659.66)]))

ITEMS = rotulo(T0)  # noqa: F821
