# -*- coding: utf-8 -*-
"""Presentación de la unidad 4 (43 s). Cuadros 51–1210."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_ed_profe import *  # noqa: E402,F401,F403
from base_ed_profe import armar  # noqa: E402

globals().update(armar('ed_u4_presentacion', 'UNIDAD 4/PRESENTACION', 'Unidad 4. Presentación',
                     'ED - U4 - PRESENTACION', 'enfoquediferencial - U4 - PRESENTACION', 'ED4P', 51, 1210))

ITEMS = [
    ('lt01', 'lt', 1.8, 7.8, PROFE),
    ('m01_indigenas', 'mg_lista', 11.9, 20.3, lista(
        'Pueblos indígenas',
        ('balanza', 'Jurisdicción especial', 12.9),
        ('persona', 'Fuero personal', 14.3),
        ('mundo', 'Enfoque diferencial étnico', 16.2))),
    ('c01_competencias', 'carton', 20.6, 31.0, cita(
        'Herramientas para actuar donde las competencias de la Fiscalía colindan con las de las '
        'autoridades tradicionales indígenas.')),
    ('c02_conflictos', 'carton', 31.4, 37.0, cita(
        'Criterios para orientar posibles conflictos de competencias.')),
]
