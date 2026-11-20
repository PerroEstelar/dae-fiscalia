# -*- coding: utf-8 -*-
r"""Inicio de la unidad 3 de «Audiencias preliminares y medidas de aseguramiento» (20 nov 2026). **Entrega provisional.**

Fuente: `Unidad 3 - Introducción.mp4` (216.38 s). Es el «Video» de la introducción a la unidad (3.2 de la ficha).

**Tramo:** desde 2.75 s (0,45 s antes de «Un cordial saludo.», a 3.20 s; antes hay silencio digital) hasta 214.20 s (0,7 s después de la última palabra; el archivo dura 216.38). Sin cortes:
la lee de corrido. Termina «…a la tercera unidad. Comencemos.».
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_ap_profe import *  # noqa: E402,F401,F403
from base_ap_profe import armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad(3, 'INICIO', [(2.75, 214.20)]))

ITEMS = rotulo(T0)  # noqa: F821
