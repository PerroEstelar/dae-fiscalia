# -*- coding: utf-8 -*-
r"""Inicio de la unidad 1 de «Audiencias preliminares y medidas de aseguramiento» (20 nov 2026). **Entrega provisional.**

Fuente: `Unidad 1 - Introducción.mp4` (195.71 s). Es el «Video» de la introducción a la unidad (3.2 de la ficha).

**Tramo:** desde 3.33 s (0,45 s antes de «Un cordial saludo.», a 3.78 s; antes hay silencio digital) hasta 192.34 s (0,7 s después de la última palabra; el archivo dura 195.71). Sin cortes:
la lee de corrido. Termina «…límites constitucionales del ejercicio punitivo.».
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_ap_profe import *  # noqa: E402,F401,F403
from base_ap_profe import armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad(1, 'INICIO', [(3.33, 192.34)]))

ITEMS = rotulo(T0)  # noqa: F821
