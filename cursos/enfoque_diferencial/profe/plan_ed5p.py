# -*- coding: utf-8 -*-
"""Presentación de la unidad 5 (46 s). Cuadros 35–1168."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_ed_profe import *  # noqa: E402,F401,F403
from base_ed_profe import armar  # noqa: E402

globals().update(armar('ed_u5_presentacion', 'UNIDAD 5/PRESENTACION', 'Unidad 5. Presentación',
                     'ED - U5 - PRESENTACION', 'enfoquediferencial - U5 - PRESENTACION', 'ED5P', 35, 1168))

ITEMS = [
    ('lt01', 'lt', 1.3, 7.3, PROFE),
    ('c01_practicas', 'carton', 8.4, 18.6, c_tit(
        'Buenas prácticas y lineamientos',
        'Violencias fundadas en la orientación sexual o en la identidad de género.')),
    ('m01_violencias', 'mg_lista', 21.6, 30.8, lista(
        'Una comprensión amplia de',
        ('escudo', 'Las violencias sexuales', 23.8),
        ('persona', 'El feminicidio', 25.5),
        ('casa_lote', 'La violencia intrafamiliar', 26.8))),
    ('c02_protocolos', 'carton', 31.0, 35.6, cita(
        'Los protocolos y guías metodológicas de la Fiscalía.')),
]
