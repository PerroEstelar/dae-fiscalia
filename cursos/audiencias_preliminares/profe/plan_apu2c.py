# -*- coding: utf-8 -*-
r"""Cierre de la unidad 2 de «Audiencias preliminares y medidas de aseguramiento» (20 nov 2026). **Entrega provisional.**

Fuente: `Unidad 2 - Recapitulación.mp4` (555.29 s). Es el «Video» de la actividad de acompañamiento dirigido (3.8 de la ficha: «una síntesis de los principales temas abordados en la unidad»).

**Tramo:** desde 1.45 s (0,45 s antes de «Un cordial saludo,», a 1.90 s; antes hay silencio digital) hasta el final del archivo (la última palabra termina a 555.26 s de 555.29: el archivo viene cortado pegado a ella). Sin cortes:
la lee de corrido. Termina «…con el proceso de formación.».
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_ap_profe import *  # noqa: E402,F401,F403
from base_ap_profe import armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad(2, 'CIERRE', [(1.45, 555.28)]))

ITEMS = rotulo(T0)  # noqa: F821
