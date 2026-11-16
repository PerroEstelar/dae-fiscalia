# -*- coding: utf-8 -*-
r"""Inicio de la unidad 3 de «Derechos humanos aplicados a la función judicial» (16 nov 2026).

**Pedido.** Sebastián: «ahora pasemos al inicio de la unidad 3 de DDHH, de pe a pa».

**Fuente.** `06. Video Inicio U3.mp4` del Drive de JP (`VIDEOS`), la toma cruda: 1620×1080,
30 fps parejos (7347 cuadros en 244,9 s), 16 Mb/s, BT.709, AAC estéreo. Mismo profe, fondo y
encuadre. Sin versión de Camtasia: los cortes salen del STT (Scribe, WAV a 16 kHz, 548 palabras),
de los cuadros y del RMS en ventanas de 50 ms.
- No hay arranques en falso ni frases repetidas.
- Una pausa de 3,4 s entre «…qué corresponde a otras entidades.» (205,42) y «Cerrará esta
  unidad…» (208,86), casi toda en silencio digital (205,60–207,95). Se corta de 205,70 a 207,90:
  queda una pausa de 1,2 s.
- Después del corte, el plano cerrado hasta la pausa entre «…que debe terminar» y «con la ruta
  de protección…» (214,54–215,40), sin gráficos.

**Unidad 3:** «Proteger con debida diligencia: investigación, víctimas y enfoques diferenciales»
(ficha).

**Textos.** Sus palabras recortadas, contrastadas con el guion de la ficha (video de bienvenida),
que él amplía bastante. Las cuatro fallas de la primera entrevista se cotejaron con el guion del
audiodrama (`herramientas/voz/textos/guion_dh.py`, U3): «seguir hablando al aire» es lo que dice
el entrevistador de la emisora. «Construidos a través de situaciones reales» no va literal: el
cartón dice «basados en situaciones reales».

**Gráficos.** Cartones (un antetítulo por cada lección) y cuatro listas de AE: el contexto nuevo,
las cuatro fallas de la primera versión, lo que hace bien la segunda y la versión reforzada del
estándar. Las de cuatro filas van sin título (columna de 520).

Los tiempos están en segundos de la fuente; `cuadro` los pasa a la línea descontando el corte.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_dh_profe import *  # noqa: E402,F401,F403
from base_dh_profe import CURSO, BIN_CURSO, CERRADO, cuadro_de, cita, c_tit, c_ante, lista  # noqa: E402

R = CURSO + '/UNIDAD 3 - INICIO PROFE'
BIN = BIN_CURSO + ['UNIDAD 3 - INICIO PROFE']
ORIGINAL = R + '/01 VIDEO/06. Video Inicio U3.mp4'
COMPUESTO = R + '/01 VIDEO/DH3I_compuesto_v1.mp4'
TITULO = R + '/02 CARTONES/carton titulo dh u3 inicio.mp4'
SUB = 'Unidad 3. Proteger con debida diligencia: investigación, víctimas y enfoques diferenciales'
NOMBRE_LINEA = 'DH - U3 - INICIO PROFE'
EXPORT = 'PRIO 2 - DERECHOS HUMANOS - UNIDAD 3 INICIO-v%d'
PREFIJO = 'DH3I'
TMP = 'D:/DAE/_tmp/dh_profe/dh3i'

PROFE = ('Yefri Yoel Torrado Verjel', 'Coautor del curso Derechos humanos aplicados a la función judicial')

TRAMOS = [
    (0.0, 205.70, None),
    (207.90, 214.95, CERRADO),   # «Cerrará esta unidad con su aporte… que debe terminar»
    (214.95, 244.9, None),
]
T0, T1 = 0.0, 244.9
cuadro = cuadro_de(TRAMOS)

ITEMS = [
    ('lt01', 'lt', 1.3, 9.0, PROFE),
    ('c01_amenazas', 'carton', 9.3, 20.2, c_ante(
        'Semana ocho', 'Nuevas amenazas contra Carmen Elisa Rojas',
        'Por llamadas y mensajes, con un componente de género.')),
    ('m01_contexto', 'mg_lista', 29.0, 44.0, lista(
        'El contexto',
        ('mundo', 'Un grupo armado en el municipio', 29.6),
        ('dialogo', 'Las amenazas no se detienen', 36.6),
        ('lupa_doc', 'La fuente de riesgo: una estructura', 39.3))),
    ('c02_pregunta', 'carton', 49.8, 58.6, c_ante(
        'La pregunta de esta unidad', '¿Qué significa, en concreto, proteger con debida diligencia?')),
    ('c03_deber', 'carton', 66.0, 77.4, c_tit(
        'Un deber jurídico propio del Estado',
        'No una simple formalidad ni una gestión que dependa de la insistencia de la víctima.')),
    ('m02_primera', 'mg_lista', 85.5, 104.6, lista(
        None,
        ('carpeta', 'Le pide contar todo otra vez', 85.6),
        ('dialogo', 'Le reprocha seguir hablando al aire', 91.5),
        ('persona', 'Pregunta si no será un exnovio despechado', 94.5),
        ('escritorio', 'La interrumpe para atender un mensaje', 97.9))),
    ('c04_segunda', 'carton', 105.9, 111.8, c_ante(
        'En la segunda', 'La misma diligencia, con método y con humanidad')),
    ('m03_segunda', 'mg_lista', 112.5, 123.9, lista(
        None,
        ('lupa_doc', 'Ya revisó el expediente', 113.3),
        ('carpeta', 'No le pide repetir lo que ya contó', 115.1),
        ('mano_corazon', 'Toma en serio el dato de género', 117.6),
        ('ruta', 'Le explica qué sigue', 119.8))),
    ('c05_relatos', 'carton', 124.0, 136.7, c_tit(
        'Relatos de violencia y de revictimización',
        'Ficticios, pero basados en situaciones reales. Si algún contenido le afecta, puede pausar y '
        'retomar.')),
    ('c06_clinica', 'carton', 137.0, 147.4, c_ante(
        'La clínica de errores', 'Una investigación que falló',
        'Inspirada en las lecciones del caso Bedoya Lima contra Colombia.')),
    ('c07_primera', 'carton', 157.0, 169.6, c_ante(
        'En la cartilla, tres lecciones', 'Primera: los componentes operativos de la debida diligencia')),
    ('m04_reforzada', 'mg_lista', 170.6, 180.35, lista(
        'Reforzada frente a la violencia contra',
        ('persona', 'Mujeres', 174.1),
        ('dialogo', 'Periodistas', 175.2),
        ('escudo', 'Personas defensoras de derechos humanos', 176.3))),
    ('c08_segunda', 'carton', 180.45, 189.6, c_ante(
        'Segunda', 'Los derechos de las víctimas',
        'Atención sin revictimizar, con enfoque diferencial e interseccional.')),
    ('c09_tercera', 'carton', 189.7, 205.5, c_ante(
        'Tercera', 'Las rutas y los mecanismos de protección',
        'Qué puede activar la Fiscalía y qué corresponde a otras entidades.')),
    ('c10_aporte', 'carton', 215.4, 227.6, c_ante(
        'Su aporte al plan de investigación', 'La ruta de protección de la lideresa',
        'Qué mecanismo activa, ante quién, con qué urgencia y qué seguimiento.')),
    ('c11_tratar', 'carton', 227.7, 231.5, cita('Proteger es la manera de tratar.')),
    ('c12_fallar', 'carton', 231.6, 244.6, c_tit(
        'Todos los actos en orden, y aun así fallar',
        'Si se le traslada a la víctima la carga de investigar o la obligación de repetir su historia.')),
]
