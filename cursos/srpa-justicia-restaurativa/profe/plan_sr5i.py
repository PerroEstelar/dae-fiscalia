# -*- coding: utf-8 -*-
r"""Inicio (bienvenida) de la unidad 5 de SRPA (17 nov 2026).

**Fuente.** `srpa_u5_inicio_fuente.mp4` (Drive del curso → VIDEOS/UNIDADES,
«SRPA_inicio_unidad5.mp4», `1ccSM6ImbU5of5m-GQTbxPSLfleMmKWV8`, subida el 17 nov): grabación de
Teams, 1280×720, 30 fps parejos (61.786 cuadros, 2.059,5 s), BT.601, AAC estéreo a −15,8 LUFS con
picos de +0,8 dBTP. Carlos Humberto Ramírez Romero, con el fondo aéreo, el saco y la corbata de
las unidades 3 y 4 (se comparó con un cuadro de la fuente de la unidad 4). No dice su nombre.

**El archivo trae dos cosas**, igual que el de la unidad 4:
- cuadros 0–3423 (0–114,1 s): la bienvenida de la unidad. Es esta pieza.
- cuadros 3424–61785: la clase («Queridos discentes, bienvenidos a la unidad número cinco. En
  esta unidad, la lección número uno nos permitirá conocer…»). Es `plan_sr5d`.
En el cuadro 3424 hay un corte seco entre las dos tomas (un pico aislado de la diferencia entre
cuadros, 7,1, con la cabeza en otro sitio). En esta fuente el panel DAE/Fiscalía no cambia de
nivel entre tomas, así que los cortes se buscaron solo por ese pico (`saltos_u5.py`).

STT (Scribe, WAV a 16 kHz): 4.875 palabras en todo el archivo; la bienvenida va de 0,82 a
113,60 s. Una sola toma, sin repeticiones. Después de «Bienvenidos.» hay medio segundo de
silencio hasta el corte.

**Ventana 1143×643 desde (12, 30), ×1,68**: la de las unidades 3 y 4. El borde izquierdo de la
cabeza va de x 564 (mín.) a 612 (p50) de la fuente. Con la caja de cartones en x 86–750 de
salida, la persona no la toca en este tramo (`caja_u5.py`).
**Columna de 560** y lower third con el nombre a 44 px y el cargo a 560 de ancho (2 renglones),
como en la unidad 4.

**Textos.** Sus palabras, sin muletillas. Las cifras, en dígitos.

Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_sr_profe import *  # noqa: E402,F401,F403
from base_sr_profe import armar, columna, CARLOS, c_tit, c_ante, lista  # noqa: E402

XY, VENTANA = (12, 30), (1143, 643)
MAXW = columna(560)
LT = (44, 560)
K_CORTE = 3424
globals().update(armar(
    'srpa_u5_inicio_fuente.mp4', 'UNIDAD 5/INICIO', 5, 'SRPA - U5 - INICIO', 'srpa - U5 - INICIO',
    'SR5I', [(0.0, K_CORTE / 30.0, None)]))

ITEMS = [
    ('lt01', 'lt', 1.0, 9.0, CARLOS),
    ('c01_tres', 'carton', 11.4, 17.4, c_ante('Unidad 5', '3 lecciones')),
    ('c02_leccion1', 'carton', 17.8, 33.4, c_ante(
        'Lección 1', 'Medidas restrictivas de derechos',
        'En el marco de la indagación y la investigación: las medidas de aseguramiento y su '
        'aplicabilidad en el sistema.')),
    ('c03_leccion2', 'carton', 33.6, 43.2, c_ante(
        'Lección 2', 'Requisitos habilitantes', 'De las medidas restrictivas de derechos.')),
    ('m01_controles', 'mg_lista', 45.8, 61.2, lista(
        None,
        ('doc_check', 'Controles generales', 46.9),
        ('candado', 'Medidas restrictivas en la investigación', 49.2),
        ('lupa_doc', 'Actos de investigación de la Fiscalía', 54.8))),
    ('c04_leccion3', 'carton', 61.5, 75.2, c_ante(
        'Lección 3', 'Los adolescentes privados de la libertad',
        'La sanción a imponer y los criterios relevantes para determinarla.')),
    ('c05_enfoque', 'carton', 84.9, 97.5, c_tit(
        'Enfoque pedagógico',
        'La metodología reflexiva y conceptual de la Dirección de Altos Estudios de la Fiscalía.')),
    ('m02_horas', 'mg_lista', 99.8, 107.2, lista(
        None,
        ('reloj', '6 horas de trabajo autónomo', 100.9),
        ('portatil', '2 horas de orientación virtual', 102.6))),
]
