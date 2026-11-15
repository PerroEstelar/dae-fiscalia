# -*- coding: utf-8 -*-
"""Presentación de la unidad 3 (52 s). Cuadros 38–1496."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_ed_profe import *  # noqa: E402,F401,F403
from base_ed_profe import armar  # noqa: E402

globals().update(armar('ed_u3_presentacion', 'UNIDAD 3/PRESENTACION', 'Unidad 3. Presentación',
                     'ED - U3 - PRESENTACION', 'enfoquediferencial - U3 - PRESENTACION', 'ED3P', 38, 1496))

ITEMS = [
    ('lt01', 'lt', 1.4, 7.4, PROFE),
    ('c01_derechos', 'carton', 13.5, 21.2, c_tit(
        'Derechos especiales',
        'De los que gozan algunas poblaciones específicas.')),
    ('m01_derechos', 'mg_lista', 22.4, 33.8, lista(
        'Los derechos de',
        ('mundo', 'Comunidades étnicamente diferenciadas', 23.7),
        ('familia', 'Niños, niñas y adolescentes', 27.4),
        ('personas', 'Las mujeres', 29.6))),
    ('c02_holistica', 'carton', 34.6, 44.6, c_tit(
        'Derechos y obligaciones',
        'Una visión holística de la igualdad como principio vivo y operativo.')),
]
