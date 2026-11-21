# -*- coding: utf-8 -*-
r"""Cierre de la unidad 1 de «Derecho de petición y acción de tutela» (20 nov 2026). **Entrega provisional** (ver `base_dp_profe`).

Fuente: `VIDEO6 - CIERRE UNIDAD 1- TOMA 1.mp4`.

El «Video de cierre» de la unidad 1 (27 min).
- Empieza en «Llegamos al cierre de la primera unidad» (4,50: antes hay una respiración).
- Sale de 1058,58 a 1080,21: el primer intento de «Orientar sobre funciones y cumplir el traslado…» y «Perdón,
  paremos ahí un segundo. Por favor».
- Sale de 1170,02 a 1230,49: el primer intento de «La tercera lección reunió reglas jurisprudenciales…», hasta «Pensemos
  en la víctima. ¿Qué solicita ella? Paremos un segundo ahí, por favor».
- Termina en «…tramitar, responder y comunicar» (sale «Listo»).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_dp_profe import *  # noqa: E402,F401,F403
from base_dp_profe import armar, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad(1, 'CIERRE', 'VIDEO6 - CIERRE UNIDAD 1- TOMA 1.mp4',
                             [(4.50, 1058.58), (1080.21, 1170.02), (1230.49, 1710.33)]))

ITEMS = rotulo(T0 + 1.5)  # noqa: F821
