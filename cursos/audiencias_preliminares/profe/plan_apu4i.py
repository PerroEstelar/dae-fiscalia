# -*- coding: utf-8 -*-
r"""Inicio de la unidad 4 de «Audiencias preliminares y medidas de aseguramiento» (20 nov 2026). **Entrega provisional.**

Fuente: `Unidad 4 - Introducción.mp4` (154.56 s). Es el «Video» de la introducción a la unidad (3.2 de la ficha).

**Tramo:** desde 2.33 s (0,45 s antes de «Bueno, un cordial», a 2.78 s; antes hay silencio digital) hasta el final del archivo (la última palabra termina a 154.52 s de 154.56: el archivo viene cortado pegado a ella). Sin cortes:
la lee de corrido. Termina «…esta cuarta y última unidad.».
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_ap_profe import *  # noqa: E402,F401,F403
from base_ap_profe import armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad(4, 'INICIO', [(2.33, 154.56)]))

ITEMS = rotulo(T0)  # noqa: F821
