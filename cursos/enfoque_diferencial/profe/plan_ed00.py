# -*- coding: utf-8 -*-
"""Presentación general del curso (1:52). Cuadros 28–3266: sin el silencio del arranque ni el final, cuando el profe se acerca a la cámara para cortar."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_ed_profe import *  # noqa: E402,F401,F403
from base_ed_profe import armar  # noqa: E402

globals().update(armar('ed_00_presentacion_general', '00 PRESENTACION DEL CURSO', 'Presentación del curso',
                     'ED - CURSO - PRESENTACION', 'enfoquediferencial - CURSO - PRESENTACION', 'ED00', 28, 3266))

ITEMS = [
    ('c01_lentes', 'carton', 1.4, 8.3, c_ante('Enfoques diferenciales', 'El símil de los lentes')),
    ('c02_lentes', 'carton', 25.1, 39.2, c_tit(
        'Poblaciones diversas',
        'Es necesario usar unas lentes que nos permitan ver más allá de los prejuicios y falsas '
        'concepciones.')),
    ('m01_hablaremos', 'mg_lista', 48.0, 56.8, lista(
        'Hablaremos de',
        ('personas', 'Mujeres', 50.2),
        ('grupos', 'Identidades diversas', 50.9),
        ('mundo', 'Poblaciones étnicamente diferenciadas', 52.6))),
    # la enumeración va a dos ítems por segundo: tres listas de tres, cada última fila 4 s o más
    ('m02_hablaremos', 'mg_lista', 56.9, 63.7, lista(
        None,
        ('casa_lote', 'Comunidades campesinas', 57.0),
        ('mano_corazon', 'Personas con capacidades diferentes', 57.4),
        ('familia', 'Niños, niñas y adolescentes', 59.6))),
    ('m03_hablaremos', 'mg_lista', 63.8, 70.6, lista(
        None,
        ('reloj', 'Adultos mayores', 63.9),
        ('escudo', 'Defensores y defensoras de derechos humanos', 64.2),
        ('apreton', 'Firmantes de acuerdos de paz', 66.3))),
    ('c04_colectivo', 'carton', 70.8, 82.2, c_tit(
        'Un proyecto colectivo',
        'En su elaboración han intervenido muchos profesionales de la Universidad Nacional.')),
    ('lt01', 'lt', 86.6, 94.4, PROFE),
    ('c05_trayectoria', 'carton', 94.6, 105.8, c_tit(
        'Cuarenta años en la Universidad Nacional',
        'Animando la reflexión en derechos humanos, justicia transicional y enfoques diferenciales.')),
]
