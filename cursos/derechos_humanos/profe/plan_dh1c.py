# -*- coding: utf-8 -*-
r"""Cierre de la unidad 1 de «Derechos humanos aplicados a la función judicial» (16 nov 2026).

**Pedido.** Sebastián: «por ahora hagamos cierre de la unidad 1, mismo profesor, mismo curso».
Mandó el enlace de la versión de Camtasia (`DDHH_funcion_cierre_unidad1.mp4`, 1280×720, 2:27,8).

**Fuente.** `3. Video Cierre U1.mp4` del mismo Drive (`VIDEOS`), la toma cruda: 1620×1080, 30 fps
parejos (4476 cuadros en 149,2 s), 16 Mb/s, BT.709, AAC estéreo. Es la misma toma que la de
Camtasia: alineadas las dos transcripciones (Scribe, WAV a 16 kHz), las 318 palabras caen en el
mismo sitio y JP solo le quitó 1,4 s de la cola. No hay arranques en falso ni pausas largas
(la más larga, 2,3 s antes de «Su valoración inicial…»), así que va entera.

**Ventana, columna y lower third:** las de `base_dh_profe.py`. El fondo, el encuadre y el profe
son los de la presentación.

**Unidad 1:** «El fiscal como garante: fundamentos de los derechos humanos y doble incidencia de
la función fiscal» (ficha del curso). El cartón de título lleva «Unidad 1. <nombre>», como los
de SRPA.

**Gráficos.** Sus palabras recortadas. Un cartón con antetítulo por cada parte del repaso
(«Primero», «Segundo», «Tercero»), una lista con las tres dimensiones de la dignidad y otra con
lo que implica garantizar. «Idoneidad, necesidad y proporcionalidad» va en cartón y no en lista:
la tercera fila no alcanzaba sus 4 s antes de «Tercero».

Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_dh_profe import *  # noqa: E402,F401,F403
from base_dh_profe import CURSO, BIN_CURSO, cuadro_de, cita, c_tit, c_ante, lista  # noqa: E402

R = CURSO + '/UNIDAD 1 - CIERRE PROFE'
BIN = BIN_CURSO + ['UNIDAD 1 - CIERRE PROFE']
ORIGINAL = R + '/01 VIDEO/3. Video Cierre U1.mp4'
COMPUESTO = R + '/01 VIDEO/DH1C_compuesto_v1.mp4'
TITULO = R + '/02 CARTONES/carton titulo dh u1 cierre.mp4'
SUB = ('Unidad 1. El fiscal como garante: fundamentos de los derechos humanos y doble incidencia '
       'de la función fiscal')
NOMBRE_LINEA = 'DH - U1 - CIERRE PROFE'
EXPORT = 'PRIO 2 - DERECHOS HUMANOS - UNIDAD 1 CIERRE-v%d'
PREFIJO = 'DH1C'
TMP = 'D:/DAE/_tmp/dh_profe/dh1c'

PROFE = ('Yefri Yoel Torrado Verjel', 'Coautor del curso Derechos humanos aplicados a la función judicial')

TRAMOS = [(0.0, 149.2, None)]
T0, T1 = 0.0, 149.2
cuadro = cuadro_de(TRAMOS)

ITEMS = [
    ('lt01', 'lt', 0.8, 8.4, PROFE),
    ('c01_primero', 'carton', 21.7, 27.9, c_ante('Primero', 'El fundamento de la dignidad humana')),
    ('m01_dimensiones', 'mg_lista', 28.0, 35.0, lista(
        'Tres dimensiones',
        ('ruta', 'Vivir como se quiere', 28.4),
        ('casa_lote', 'Vivir bien', 29.6),
        ('mano_corazon', 'Vivir sin humillaciones', 30.4))),
    ('c02_derechos', 'carton', 35.1, 41.1, cita('No se pierden ni se renuncian y dependen unos de otros.')),
    ('c03_voz', 'carton', 41.3, 47.0, cita('Proteger su vida es también proteger su voz.')),
    ('c04_segundo', 'carton', 54.1, 61.9, c_ante(
        'Segundo', 'Los deberes', 'El Estado se obligó a respetar los derechos y a garantizarlos.')),
    ('m02_garantizar', 'mg_lista', 62.0, 69.4, lista(
        'Lo que implica',
        ('escudo', 'Prevenir', 62.1),
        ('lupa_doc', 'Investigar', 62.9),
        ('mazo', 'Sancionar', 63.9),
        ('curita', 'Reparar', 65.2))),
    ('c05_responsabilidad', 'carton', 72.0, 85.6, c_ante(
        'Caso Bedoya Lima contra Colombia', 'Lo que usted hace y lo que deja de hacer',
        'Puede comprometer la responsabilidad internacional del Estado.')),
    ('c06_doble', 'carton', 86.1, 98.9, c_tit(
        'La doble incidencia de su función',
        'Protege los derechos de las víctimas y, a la vez, puede restringir los de las personas '
        'investigadas.')),
    ('c07_siempre', 'carton', 99.0, 104.2, cita('Siempre con idoneidad, necesidad y proporcionalidad.')),
    ('c08_tercero', 'carton', 104.3, 113.6, c_ante(
        'Tercero', 'Las personas no llegan iguales',
        'El enfoque diferencial ajusta la atención a sus condiciones.')),
    ('c09_potencia', 'carton', 116.2, 126.8, c_tit(
        'Lectura interseccional', 'Cuando esas condiciones confluyen, el riesgo no se suma: se potencia.')),
    ('c10_proxima', 'carton', 132.6, 142.6, c_ante(
        'En la próxima unidad', 'La defensa cuestionará el fundamento normativo',
        'Responder con fuentes, no con opiniones.')),
    ('c11_cuestionario', 'carton', 143.0, 149.1, c_tit(
        'Resuelva el cuestionario de esta unidad', 'Nos vemos en la unidad 2.')),
]
