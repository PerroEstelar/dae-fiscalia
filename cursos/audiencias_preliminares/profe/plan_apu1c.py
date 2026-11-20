# -*- coding: utf-8 -*-
r"""Cierre de la unidad 1 de «Audiencias preliminares y medidas de aseguramiento» (20 nov 2026). **Entrega provisional.**

Fuente: `Unidad 1 - Recapitulación.mp4` (421.59 s). Es el «Video» de la actividad de acompañamiento dirigido (3.8 de la ficha: «una síntesis de los principales temas abordados en la unidad»).

**Tramo:** desde 3.29 s (0,45 s antes de «Bueno, muchas felicitaciones.», a 3.74 s; antes hay silencio digital) hasta 420.24 s (0,7 s después de la última palabra; el archivo dura 421.59). Sin cortes:
la lee de corrido. Termina «…continuar con las siguientes unidades.».
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_ap_profe import *  # noqa: E402,F401,F403
from base_ap_profe import armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad(1, 'CIERRE', [(3.29, 420.24)]))

ITEMS = rotulo(T0)  # noqa: F821
