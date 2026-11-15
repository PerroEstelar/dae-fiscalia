# -*- coding: utf-8 -*-
"""Presentación de la unidad 2 (44 s). Cuadros 14–1262."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_ed_profe import *  # noqa: E402,F401,F403
from base_ed_profe import armar  # noqa: E402

globals().update(armar('ed_u2_presentacion', 'UNIDAD 2/PRESENTACION', 'Unidad 2. Presentación',
                     'ED - U2 - PRESENTACION', 'enfoquediferencial - U2 - PRESENTACION', 'ED2P', 14, 1262))

ITEMS = [
    ('lt01', 'lt', 0.6, 6.6, PROFE),
    ('c02_sujetos', 'carton', 11.6, 24.4, c_tit(
        'Sujetos de especial protección constitucional',
        'Base fundacional de los enfoques diferenciales y de las acciones afirmativas.')),
    ('c03_interseccionalidad', 'carton', 30.5, 38.9, cita(
        'Escenarios en donde aparecerá con fuerza el imperativo de la interseccionalidad.')),
]
