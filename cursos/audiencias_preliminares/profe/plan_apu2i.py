# -*- coding: utf-8 -*-
r"""Inicio de la unidad 2 de «Audiencias preliminares y medidas de aseguramiento» (20 nov 2026). **Entrega provisional.**

Fuente: `Unidad 2 - Introducción.mp4` (145.28 s). Es el «Video» de la introducción a la unidad (3.2 de la ficha).

**Tramo:** desde 1.57 s (0,45 s antes de «Un cordial saludo.», a 2.02 s; antes hay silencio digital) hasta el final del archivo (la última palabra termina a 145.24 s de 145.28: el archivo viene cortado pegado a ella). Sin cortes:
la lee de corrido. Termina «…legalización de captura en flagrancia.».
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_ap_profe import *  # noqa: E402,F401,F403
from base_ap_profe import armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad(2, 'INICIO', [(1.57, 145.28)]))

ITEMS = rotulo(T0)  # noqa: F821
