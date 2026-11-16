# -*- coding: utf-8 -*-
r"""Presentación del curso «Derechos humanos aplicados a la función judicial» (16 nov 2026).

**Fuente.** `01. Video Presentación.mp4` (4:05,7), la toma cruda; ver `base_dh_profe.py`.
Empieza «Bienvenida y bienvenido al curso de Derechos Humanos Aplicados a la Función Judicial,
de la Dirección de Altos Estudios de la Fiscalía General de la Nación» y termina «El expediente
ya está sobre su escritorio».

**Profe.** Yefri Yoel Torrado Verjel. No dice su nombre en el video y ningún documento del
Drive dice quién graba; la ficha lista tres autores (Estanislao Escalante Barreto, Yefri Yoel
Torrado Verjel y Laura Juliana Galvez Depablos) y no es Estanislao, que es el profe de SRPA.
Lo confirmó Sebastián (16 nov), y pidió de cargo «coautor del curso y el nombre del curso».

**Dos cortes** (Scribe sobre WAV a 16 kHz, una voz):
- un arranque en falso: después de «…una herramienta que usted domina.» (44,92) dice «Aquí no
  encontrará un listado de trabajos. Un, dos, tres.» (48,06–53,32) y vuelve a empezar la
  frase en 54,10. Se corta de 45,50 a 53,80. JP lo cortó igual en la versión de Camtasia.
- una pausa de 3,6 s después de «…de forma permanente.» (205,10–208,72). El profe está quieto
  mirando a cámara; se deja en 1 s (corte de 205,70 a 208,25). JP la acortó también.

Después de cada corte va el plano cerrado hasta el final de la frase, sin gráficos encima
(53,80–57,70 y 208,25–216,85).

**Gráficos.** Los textos son sus palabras recortadas. Las listas van donde enumera: las cuatro
decisiones, lo que se hace en cada unidad (cuatro filas, sin título: la columna es de 520) y
las tres reglas prácticas. Las cinco unidades van en cartones con su nombre corto de la ficha
(«El fiscal como garante», «La caja de herramientas normativa», «Proteger con debida
diligencia», «Restringir con legitimidad», «Decidir como garante»).

Los tiempos están en segundos de la fuente; `cuadro` los pasa a la línea descontando los cortes.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_dh_profe import *  # noqa: E402,F401,F403
from base_dh_profe import CURSO, BIN_CURSO, CERRADO, cuadro_de, cita, c_tit, c_ante, c_suelta, lista  # noqa: E402

R = CURSO + '/PRESENTACION DEL CURSO'
BIN = BIN_CURSO + ['PRESENTACION DEL CURSO']
ORIGINAL = R + '/01 VIDEO/01. Video Presentación.mp4'
COMPUESTO = R + '/01 VIDEO/DH00_compuesto_v1.mp4'
TITULO = R + '/02 CARTONES/carton titulo dh presentacion del curso.mp4'
SUB = 'Presentación del curso'
NOMBRE_LINEA = 'DH - CURSO - PRESENTACION'
EXPORT = 'PRIO 2 - DERECHOS HUMANOS - PRESENTACION DEL CURSO-v%d'
PREFIJO = 'DH00'
TMP = 'D:/DAE/_tmp/dh_profe/dh00'

PROFE = ('Yefri Yoel Torrado Verjel', 'Coautor del curso Derechos humanos aplicados a la función judicial')

TRAMOS = [
    (0.0, 45.50, None),
    (53.80, 57.70, CERRADO),     # «Aquí no encontrará un listado de tratados para memorizar.»
    (57.70, 205.70, None),
    (208.25, 216.85, CERRADO),   # «Al final, más que aprobar un curso, … que la rigen.»
    (216.85, 245.667, None),
]
T0, T1 = 0.0, 245.667
cuadro = cuadro_de(TRAMOS)

ITEMS = ([('lt01', 'lt', 2.0, 10.0, PROFE)] if PROFE else []) + [
    ('m01_decisiones', 'mg_lista', 16.8, 27.8, lista(
        None,
        ('carpeta', 'Asignar una noticia criminal', 17.0),
        ('lupa_doc', 'Ordenar un acto de investigación', 19.1),
        ('persona', 'Atender a una víctima', 21.4),
        ('firma', 'Proyectar una solicitud', 23.5))),
    ('c02_decidio', 'carton', 28.2, 35.0, cita(
        'En cada una de esas decisiones, usted decidió sobre derechos humanos.')),
    ('c03_herramienta', 'carton', 35.3, 45.4, c_tit(
        'Una herramienta que usted domina',
        'Que esa dimensión de su trabajo deje de ser implícita.')),
    ('c04_expediente', 'carton', 57.9, 62.3, cita('Un expediente, una carpeta de investigación')),
    ('c05_noticia', 'carton', 62.4, 72.0, c_tit(
        'Una noticia criminal llega a un despacho',
        'Amenazas contra una lideresa social en un municipio del país.')),
    ('m02_cada_unidad', 'mg_lista', 87.2, 103.9, lista(
        None,
        ('escritorio', 'Vivirá una situación del caso', 88.8),
        ('bombilla', 'Reflexionará sobre lo que hizo', 91.6),
        ('libros', 'Estudiará los estándares', 95.5),
        ('doc_check', 'Los aplicará en un protocolo real', 99.3))),
    ('c06_u1', 'carton', 107.2, 117.2, c_ante(
        'Unidad 1', 'El fiscal como garante', 'Su función incide dos veces en los derechos humanos.')),
    ('c07_u1', 'carton', 117.3, 122.3, cita('Los garantiza y también puede restringirlos legítimamente.')),
    ('c08_u2', 'carton', 122.5, 133.0, c_ante(
        'Unidad 2', 'Caja de herramientas normativa',
        'Constitución, bloque de constitucionalidad y control de convencionalidad.')),
    ('c09_u3', 'carton', 133.2, 140.2, c_ante(
        'Unidad 3', 'Proteger con debida diligencia', 'Protege e investiga con enfoque diferencial.')),
    ('c10_u4', 'carton', 140.3, 153.4, c_ante(
        'Unidad 4', 'Restringir con legitimidad',
        'Presunción de inocencia, proporcionalidad y trato digno a las personas privadas de la libertad.')),
    ('c11_u5', 'carton', 153.5, 161.0, c_ante('Unidad 5', 'Decidir como garante', 'Integra todo en una decisión final.')),
    ('c12_virtual', 'carton', 161.2, 170.0, c_tit(
        'Virtual y de autoformación',
        '48 horas en total que usted podrá administrar a su ritmo.')),
    ('m03_reglas', 'mg_lista', 170.2, 195.0, lista(
        'Tres reglas prácticas',
        ('lista', 'Comience por la autoevaluación diagnóstica', 174.2),
        ('libreta', 'Lleve su bitácora', 183.0),
        ('dialogo', 'Aproveche la retroalimentación', 189.7))),
    ('c13_proposito', 'carton', 217.3, 231.5, c_tit(
        'Ese es el propósito',
        'Que cada actuación sea mejor y proteja en debida diligencia los derechos fundamentales, '
        'tanto de la víctima como de los indiciados.')),
    ('c14_garante', 'carton', 233.0, 241.7, c_tit(
        'La Fiscalía es garante de derechos',
        'Ese garante, en cada despacho, en cada territorio, es usted.')),
    ('c15_escritorio', 'carton', 241.9, 245.6, c_suelta('El expediente ya está sobre su escritorio.')),
]
