# -*- coding: utf-8 -*-
r"""Cierre de la unidad 4 de «Audiencias preliminares y medidas de aseguramiento» (20 nov 2026). **Entrega provisional.**

Fuente: `Unidad 4 - Recapitulación.mp4` (616.32 s). Es el «Video» de la actividad de acompañamiento dirigido (3.8 de la ficha: «una síntesis de los principales temas abordados en la unidad»).

**Tramo:** desde 3.01 s (0,45 s antes de «Muchas felicitaciones. Han», a 3.46 s; antes hay silencio digital) hasta 615.95 s (0,7 s después de la última palabra; el archivo dura 616.32). Sin cortes:
la lee de corrido. Termina «…cursos puestos a su disposición.».
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_ap_profe import *  # noqa: E402,F401,F403
from base_ap_profe import armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad(4, 'CIERRE', [(3.01, 615.95)]))

ITEMS = rotulo(T0)  # noqa: F821
