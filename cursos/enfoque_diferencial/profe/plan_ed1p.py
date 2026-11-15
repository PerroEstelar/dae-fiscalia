# -*- coding: utf-8 -*-
"""Presentación de la unidad 1 (47 s). Cuadros 54–1355."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_ed_profe import *  # noqa: E402,F401,F403
from base_ed_profe import armar  # noqa: E402

globals().update(armar('ed_u1_presentacion', 'UNIDAD 1/PRESENTACION', 'Unidad 1. Presentación',
                     'ED - U1 - PRESENTACION', 'enfoquediferencial - U1 - PRESENTACION', 'ED1P', 54, 1355))

ITEMS = [
    ('lt01', 'lt', 1.9, 7.9, PROFE),
    ('c01_principio', 'carton', 8.6, 18.4, c_tit(
        'La igualdad como principio de optimización',
        'Una comparación entre principios y reglas en materia jurídica.')),
    ('m01_unidad', 'mg_lista', 20.3, 37.0, lista(
        'En esta unidad',
        ('balanza', 'La igualdad de trato', 21.5),
        ('lista', 'Los tests de igualdad', 32.7))),
]
