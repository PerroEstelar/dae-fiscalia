# -*- coding: utf-8 -*-
r"""Inicio (bienvenida) de la unidad 4 de SRPA (17 nov 2026).

**Fuente.** `srpa_u4_inicio_v2_fuente.mp4` (Drive del curso → VIDEOS/UNIDADES,
«SRPA_unidad_4_inicio_v2.mp4», `1lDPp4niSdZZ1th82hPZfZOmxcn6S3x02`, subida el 17 nov): grabación
de Teams, 1280×720, 30 fps parejos (60.414 cuadros, 2.013,8 s), BT.601, AAC estéreo a −13,0 LUFS
con picos de +1,5 dBTP. Carlos Humberto Ramírez Romero, con el fondo aéreo, el saco y la corbata
de la presentación y el desarrollo de la unidad 3 (se comparó con cuadros de esas fuentes). No
dice su nombre.

**El archivo trae dos cosas**, igual que la unidad 3 en sus dos archivos «presentacion - a» y
«presentacion - b»:
- cuadros 0–3521 (0–117,4 s): la bienvenida de la unidad. Es esta pieza.
- cuadros 3522–60413: la clase («Sean ustedes bienvenidos, queridos discentes, a nuestra unidad
  número cuatro… En la lección número uno vamos a hablar…»). Es `plan_sr4d`.
En el cuadro 3522 hay un corte seco entre las dos tomas (el panel DAE/Fiscalía cambia de nivel
contra su mediana, 2,5 → 0,8, y la diferencia entre cuadros salta a 6,7). La primera subida del
mismo día, «SRPA_unidad4_inicio_.mp4» (`1wRxW_FCMNuuBMl--NuOG7KD8Ses0z8JB`, 3.522 cuadros), es
solo este tramo.

STT (Scribe, WAV a 16 kHz): 217 palabras, de 0,36 a 117,20 s. Una sola toma, sin repeticiones.
La última palabra termina en 117,20 y después hay 0,2 s de silencio (−68 dB) hasta el corte.

**Ventana 1143×643 desde (12, 30), ×1,68**: la de la presentación y el desarrollo de la unidad 3.
El borde izquierdo de la cabeza va de x 560 (mín.) a 588 (p50) de la fuente: queda desde x≈920 de
salida. El panel DAE/Fiscalía (x 35–497, y 42–142 de la fuente) entra entero. Con la caja de
cartones en x 86–750, la persona no la toca en este tramo (`caja_u4.py`).
**Columna de 560** y lower third con el nombre a 44 px (termina en x≈918) y el cargo a 560 de
ancho (2 renglones).

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
K_CORTE = 3522
globals().update(armar(
    'srpa_u4_inicio_v2_fuente.mp4', 'UNIDAD 4/BIENVENIDA', 4, 'SRPA - U4 - INICIO', 'srpa - U4 - INICIO',
    'SR4B', [(0.0, K_CORTE / 30.0, None)]))
# Sebastián (17 nov, con la pieza ya subida como BIENVENIDA): «cambia el nombre a inicio, siempre
# serán inicio y cierre». Se renombraron la entrega, el máster y la línea; la carpeta y el bin
# siguen siendo `UNIDAD 4/BIENVENIDA`, para no mover los medios de una línea ya armada.

ITEMS = [
    ('lt01', 'lt', 1.0, 9.0, CARLOS),
    ('m01_horas', 'mg_lista', 17.2, 27.2, lista(
        None,
        ('libros', '4 lecciones', 18.2),
        ('reloj', '8 horas de trabajo autónomo', 21.0),
        ('portatil', '2 horas de orientación virtual', 22.9))),
    ('c01_leccion1', 'carton', 27.4, 37.6, c_ante(
        'Lección 1', 'Desarrollo conceptual', 'Justicia restaurativa y justicia terapéutica.')),
    ('c02_leccion2', 'carton', 39.6, 46.5, c_ante(
        'Lección 2', 'Marco normativo', 'Las prácticas restaurativas.')),
    ('c03_leccion3', 'carton', 46.7, 60.5, c_ante(
        'Lección 3', 'Sistema Nacional de Coordinación de Responsabilidad Penal para Adolescentes',
        'Su importancia y su operatividad en Colombia.')),
    ('c04_leccion4', 'carton', 62.9, 73.3, c_ante(
        'Lección 4', 'Mecanismos procesales', 'Para la implementación de procesos y prácticas restaurativas.')),
    ('c05_acompanamiento', 'carton', 73.5, 86.0, c_tit(
        'Acompañamiento docente',
        'En la presentación de la unidad, en la retroalimentación de la evaluación y en la '
        'recapitulación de la unidad.')),
    ('c06_casos', 'carton', 87.0, 102.5, c_tit(
        'Metodología de análisis de casos',
        'Nos permitirá establecer cuál es la ruta de atención frente a cada uno de los tipos planteados, '
        'basados en principios restaurativos.')),
]
