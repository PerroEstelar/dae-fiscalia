# -*- coding: utf-8 -*-
r"""Cierre del curso «Derechos humanos aplicados a la función judicial» (16 nov 2026).

**Pedido.** Sebastián: «ahora lo mismo pero con el cierre en general de todo el curso, de pe a
pa». No estaba hecho: el archivo lo subió JP el mismo día y no había plan, carpeta ni entrega.

**Fuente.** `12. Video Cierre del Curso.mp4` del Drive de JP (`VIDEOS`), la toma cruda:
1620×1080, 30 fps parejos (2297 cuadros en 76,6 s), BT.709, AAC estéreo. Mismo profe, fondo y
encuadre. STT (Scribe, WAV a 16 kHz, 171 palabras), cuadros y RMS en ventanas de 50 ms. No hay
arranques en falso, frases repetidas ni pausas largas, así que va entera.

**Textos.** Sus palabras recortadas. El cierre retoma el caso que atraviesa el curso (el
expediente de Carmen Elisa Rojas) y se despide; no hay unidad en el subtítulo: va «Cierre del
curso», como en los cierres de los otros cursos.

**Gráficos.** Cartones y una lista de AE: a qué invita la DAE (continuar profundizando, llevar
los aprendizajes a la práctica, conectarlos con sus desafíos; la última fila queda
5,5 s). Quedan sin gráfico «Esperamos que este espacio haya contribuido…» y el agradecimiento de
la Dirección de Altos Estudios: el profe respira entre cartones. El último cartón se queda hasta
«Gracias y hasta pronto».

Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_dh_profe import *  # noqa: E402,F401,F403
from base_dh_profe import CURSO, BIN_CURSO, cuadro_de, cita, c_tit, c_ante, lista  # noqa: E402

R = CURSO + '/CIERRE DEL CURSO'
BIN = BIN_CURSO + ['CIERRE DEL CURSO']
ORIGINAL = R + '/01 VIDEO/12. Video Cierre del Curso.mp4'
COMPUESTO = R + '/01 VIDEO/DHCC_compuesto_v1.mp4'
TITULO = R + '/02 CARTONES/carton titulo dh cierre del curso.mp4'
SUB = 'Cierre del curso'
NOMBRE_LINEA = 'DH - CURSO - CIERRE'
EXPORT = 'PRIO 2 - DERECHOS HUMANOS - CIERRE DEL CURSO-v%d'
PREFIJO = 'DHCC'
TMP = 'D:/DAE/_tmp/dh_profe/dhcc'

PROFE = ('Yefri Yoel Torrado Verjel', 'Coautor del curso Derechos humanos aplicados a la función judicial')

TRAMOS = [(0.0, 76.5, None)]
T0, T1 = 0.0, 76.5
cuadro = cuadro_de(TRAMOS)

ITEMS = [
    ('lt01', 'lt', 1.0, 9.0, PROFE),
    ('c01_expediente', 'carton', 11.0, 20.5, c_ante(
        'Desde el día cero', 'El expediente de Carmen Elisa Rojas',
        'Usted acaba de sustentar la decisión que lo cierra.')),
    ('c02_ficcion', 'carton', 21.0, 29.2, c_tit(
        'Ficción construida sobre situaciones reales', 'Las decisiones que usted tomó en el camino, no.')),
    ('m01_invitamos', 'mg_lista', 39.0, 51.9, lista(
        'Le invitamos a',
        ('libros', 'Continuar profundizando', 39.84),
        ('ruta', 'Llevar los aprendizajes a la práctica', 44.16),
        ('mundo', 'Conectarlos con sus desafíos', 46.42))),
    ('c03_cartillas', 'carton', 52.5, 60.0, c_tit(
        'Las cartillas y el glosario', 'Seguirán a su disposición cuando un caso lo exija.')),
    ('c04_termina', 'carton', 67.1, 76.4, c_tit(
        'El expediente del curso termina aquí',
        'Los suyos siguen en su despacho. Hoy tiene un garante mejor preparado.')),
]
