# -*- coding: utf-8 -*-
"""Conclusiones del curso (2:06). Cuadros 7–3623."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_ed_profe import *  # noqa: E402,F401,F403
from base_ed_profe import armar  # noqa: E402

globals().update(armar('ed_99_conclusiones', '99 CONCLUSIONES', 'Conclusiones del curso',
                     'ED - CURSO - CONCLUSIONES', 'enfoquediferencial - CURSO - CONCLUSIONES', 'ED99', 7, 3623))

ITEMS = [
    ('lt01', 'lt', 0.5, 6.5, PROFE),
    ('c01_igualdad', 'carton', 14.8, 28.0, cita(
        'El principio de igualdad es central para el desarrollo y protección de los derechos '
        'fundamentales, tanto individuales como colectivos.')),
    ('c02_oportunidades', 'carton', 29.2, 40.3, c_tit(
        'La igualdad de oportunidades',
        'Uno de sus imperativos es precisamente el de considerar los enfoques diferenciales.')),
    ('c03_obligacion', 'carton', 40.5, 48.6, c_tit(
        'Una obligación funcional',
        'No obedecen a la magnanimidad o bondad de los servidores públicos.')),
    ('c04_revictimizacion', 'carton', 49.5, 61.1, cita(
        'No considerarlos sí lleva a una indebida actuación y, muy posiblemente, a una '
        'revictimización.')),
    ('c05_dinamico', 'carton', 67.0, 80.9, c_tit(
        'Un campo dinámico y en expansión',
        'Atentos a nuevos grupos o colectivos que requieran especial protección constitucional.')),
    ('c06_prejuicios', 'carton', 83.6, 91.3, cita(
        'Muchas veces, la primera actuación es revisar nuestros propios prejuicios.')),
    ('c07_diversidad', 'carton', 91.6, 104.2, cita(
        'La apertura a la diversidad humana es condición básica para promover y defender los '
        'derechos fundamentales, de las víctimas y de los victimarios.')),
]
