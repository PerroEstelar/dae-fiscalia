# -*- coding: utf-8 -*-
"""Introducción al curso «Bienes en el proceso penal» (Curso 5, 14 nov 2026).

**Pedido.** Sebastián pidió el inicio y el cierre del curso como videos de profe a
cámara. Llevan:
- intro y outro;
- cartones de entrada y de salida con el nombre del curso;
- lower thirds con el nombre y el recorrido del profe;
- cartones de apoyo;
- gráficos de After Effects.

**Fuente.** Drive, curso → `VIDEOS UNIDADES/bienes_iniciocurso.mp4`.
- Es una grabación de Teams de 6:21, 1280×720 a 30 fps, con el fondo virtual del
  edificio, el mismo de los videos de SRPA.
- Audio: AAC 44,1 kHz dual-mono, −17,1 LUFS, pico +0,1 dBTP.

**Profe.** «Mi nombre es Sergio Andrés López Zamora». Es el autor del curso según
la ficha («1.5 Autor») y el libro del curso.
- Su recorrido, dicho por él: abogado, especialista en Derecho Penal y Procesal
  Penal y en Casación Penal, magíster en Derecho Penal y Procesal Penal y en
  Derechos Humanos, doctor en Derecho Público.
- Su trayectoria combina el litigio penal, la docencia universitaria y la
  investigación jurídica.

**Unidades** (de la ficha y de lo que él dice):
1. Función del bien.
2. Medidas cautelares con fines de reparación.
3. Medidas cautelares con fines de comiso y administración de bienes.
4. Medidas cautelares con fines de extinción del derecho de dominio.

**Formato.** Es el de las introducciones de curso de Delitos ambientales, con las
mismas herramientas: `ic_pieza`, `ic_linea`, `ic_revision` y `mp4_entrega`, con
`DAE_PLAN=plan_bi`.
- **Cartón de título:** se rehace con el nombre de este curso
  (`CURSO_LINEAS`, `titulo_srpa.rendir_fijo`) sobre el mismo fondo, la misma barra y
  la misma marca.
- **AE:** las comps van en su propio proyecto, `00 MOTION GRAPHICS/BIENES_intros_mg.aep`.
- **Ventana:** 1143×643 desde (0, 40), ×1,68. Es la estándar, la misma del cierre.
  - El profe está centrado y muy cerca de la cámara. Se midió sobre 152 cuadros,
    con el fondo calculado como la mediana:
    - la cabeza empieza en y≈270, con el borde izquierdo en x 392–434 (p2),
      406–456 (p10) y 442–482 (p50);
    - el mentón llega a y≈630 y los hombros abren desde y≈560.
  - La primera prueba (960×540, ×2) dejaba la caja libre, pero cortaba la cara
    por la boca. Se descartó.
  - Con ×1,68 entra el mentón con aire, pero la cabeza queda desde x≈660 de
    salida (p2) en las filas de la caja, y la cara llega hasta y≈990.
  - Por eso la columna de cartones y listas se angosta: `MAXW` = 500, con el
    texto hasta x≈670. El estándar es 615, hasta x 785.
  - El lower third lleva el nombre a 42 px y el cargo a 540 de ancho
    (`LT`). El estándar es 48 y 900. Así «Zamora» no pisa la mandíbula. Se
    simuló sobre seis cuadros.
  - El panel DAE/Fiscalía del fondo entra entero.
  - Este fondo no trae filete blanco.

Los tiempos están en segundos de la fuente. En la línea, cuadro = 409 + round(t · 23,976).
Los textos salen de Scribe (WAV a 16 kHz, 817 palabras, una voz), sin muletillas.
Los rótulos de las listas son sus palabras recortadas para caber en la caja: se
midieron antes de armar (cima ≥ 250) con las mismas fuentes y el mismo `maquetar`.
Con la columna angosta (`MAXW` 500, rótulos de 416 px) cada fila entra en dos renglones
como mucho, y las listas de cuatro filas van sin título:
- m01 lleva los títulos abreviados («Especialista en Penal, Procesal y Casación»).
- m02, m07 y m08 van sin título; m07 con «Analizar su relación con el delito».
- c10 va entera en mediana, sin título (con título se salía de la caja).
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'herramientas',
                                'cartones'))
import balanceo as B  # noqa: E402

CLIP0 = 409
FPS = 24000 / 1001
ANTE, TIT, CUE, SUELTA = 29, 46, 37, 54
GAP_TIT, GAP_CUE, GAP_ANTE = 28, 12, 16

CURSO = 'E:/DAE MASTER/CURSO 5 - Bienes en el proceso penal'
R = CURSO + '/INTRODUCCION AL CURSO'
BIN = ['C5 BIENES EN EL PROCESO PENAL', 'INTRODUCCION AL CURSO']
ORIGINAL = R + '/01 VIDEO/bienes_iniciocurso.mp4'
COMPUESTO = R + '/01 VIDEO/BI_compuesto_v1.mp4'
TITULO = R + '/02 CARTONES/carton titulo bienes introduccion al curso.mp4'
TITULO_BASE = None
CURSO_LINEAS = ['Bienes en el proceso penal']
SUB = 'Introducción al curso'
NOMBRE_LINEA = 'BIENES - CURSO - INTRODUCCION'
EXPORT = 'bienes - CURSO - INTRODUCCION-v%d'
PREFIJO = 'BI'
TMP = 'D:/DAE/_tmp/bienes/bi'
XY, VENTANA = (0, 40), (1143, 643)
MAXW = 500                 # columna de cartones y listas (estándar 615): la cara está centrada
LT = (42, 540)             # lower third: px del nombre y ancho del cargo (estándar 48 y 900)
AUDIO_META = 'I=-16:TP=-3:LRA=7'
AEP = CURSO + '/00 MOTION GRAPHICS/BIENES_intros_mg.aep'
ICONOS = CURSO + '/00 MOTION GRAPHICS/iconos'

ANCHO = MAXW                # ancho de la columna de texto de los cartones (cartones_ma.MAXW)
NOMBRE_CURSO = 'Bienes en el proceso penal'
PROFE = ('Sergio Andrés López Zamora',
         'Abogado, doctor en Derecho Público, magíster en Derecho Penal y Procesal Penal y en '
         'Derechos Humanos')


def cuadro(t):
    return CLIP0 + int(round(t * FPS))


def _p(texto, peso, px, gap):
    # renglones equilibrados (herramientas/cartones/balanceo.py): sin palabras solas abajo
    return B.piezas(texto, peso, px, gap, ANCHO)


def cita(t):
    return _p(t, 'bold', TIT, 0) if len(t) <= 78 else _p(t, 'med', CUE, 0)


def c_tit(titulo, cuerpo):
    return _p(titulo, 'bold', TIT, 0) + _p(cuerpo, 'med', CUE, GAP_TIT)


def c_ante(ante, titulo, cuerpo=None):
    ls = _p(ante, 'med', ANTE, 0) + _p(titulo, 'bold', TIT, GAP_ANTE)
    if cuerpo:
        ls += _p(cuerpo, 'med', CUE, GAP_CUE + 8)
    return ls


def c_suelta(t):
    return _p(t, 'bold', SUELTA, 0)


def lista(titulo, *filas):
    return {'titulo': titulo, 'filas': list(filas)}


def act(icono, ante, titulo, cuerpo=None):
    return {'icono': icono, 'ante': ante, 'titulo': titulo, 'cuerpo': cuerpo}


ITEMS = [
    ('lt01', 'lt', 0.6, 8.6, PROFE),
    ('m01_recorrido', 'mg_lista', 18.5, 39.1, lista(
        None,
        ('birrete', 'Especialista en Penal, Procesal y Casación', 21.2),
        ('libros', 'Magíster en Penal y Derechos Humanos', 25.7),
        ('birrete', 'Doctor en Derecho Público', 29.6),
        ('mazo', 'Litigio, docencia e investigación', 31.8))),
    ('c01_funciones', 'carton', 44.4, 52.7, cita(
        'En el desarrollo de una investigación penal, los bienes pueden desempeñar diferentes '
        'funciones, tanto jurídicas como probatorias.')),
    ('c01b_ejemplos', 'carton', 53.0, 62.3, cita(
        'Un vehículo, un inmueble, una suma de dinero, una cuenta bancaria o incluso un activo digital.')),
    ('c02_no_significa', 'carton', 73.7, 85.4, cita(
        'Identificar un bien relacionado con una investigación no significa que automáticamente pueda '
        'ser incautado, embargado, secuestrado o sometido a extinción de dominio.')),
    ('m02_exige', 'mg_lista', 85.8, 99.5, lista(
        None,
        ('ojo', 'Reconocer su finalidad', 88.4),
        ('libro_ley', 'Establecer su fundamento', 90.4),
        ('lupa_doc', 'Construir su soporte probatorio', 93.3),
        ('escudo', 'Garantizar los derechos', 95.8))),
    ('c03_proposito', 'carton', 99.8, 111.3, cita(
        'Herramientas para adoptar decisiones patrimoniales jurídicamente fundamentadas, eficaces '
        'y respetuosas del debido proceso.')),
    ('c04_u1', 'carton', 125.4, 131.8, c_ante('Unidad 1', 'Función del bien')),
    ('m03_u1', 'mg_lista', 132.0, 149.6, lista(
        None,
        ('lista', 'Sus diferentes funciones', 132.1),
        ('balanza', 'Los estándares probatorios', 133.6),
        ('lupa_doc', 'Trazabilidad y análisis financiero', 139.0),
        ('escudo', 'Víctimas y terceros de buena fe', 143.7))),
    ('c05_pregunta', 'carton', 149.9, 161.2, cita(
        '¿Qué función cumple un determinado bien dentro de la actuación penal y cuál es el '
        'tratamiento jurídico que le corresponde?')),
    ('c06_u2', 'carton', 161.5, 173.4, c_ante(
        'Unidad 2', 'Medidas cautelares con fines de reparación')),
    ('m04_u2', 'mg_lista', 173.6, 187.7, lista(
        None,
        ('lista', 'Requisitos de procedencia', 173.8),
        ('lupa_doc', 'Presupuestos probatorios', 176.6),
        ('candado', 'El embargo y el secuestro', 178.4),
        ('escudo', 'Garantías en su solicitud y ejecución', 182.1))),
    ('c07_u3', 'carton', 200.0, 212.2, c_ante(
        'Unidad 3', 'Medidas cautelares con fines de comiso y administración de bienes')),
    ('m05_u3', 'mg_lista', 212.4, 221.7, lista(
        None,
        ('mano_corazon', 'La incautación', 212.4),
        ('edificio', 'La ocupación', 214.1),
        ('candado', 'La suspensión del poder dispositivo', 215.2),
        ('doc_check', 'Entrega y puesta a disposición', 218.5))),
    ('c08_basta', 'carton', 233.4, 246.0, cita(
        'No basta con afectar jurídicamente un bien: resulta necesario garantizar su adecuada '
        'conservación, administración y destinación.')),
    ('c09_u4', 'carton', 246.2, 251.6, c_ante(
        'Unidad 4', 'Medidas cautelares con fines de extinción del derecho de dominio')),
    ('m06_u4', 'mg_lista', 251.8, 274.0, lista(
        None,
        ('libro_ley', 'Su naturaleza autónoma', 251.8),
        ('lista', 'Las causales', 257.0),
        ('candado', 'Las medidas cautelares', 265.9),
        ('apreton', 'Terminación anticipada', 269.1))),
    ('m07_herramientas', 'mg_lista', 289.5, 309.4, lista(
        None,
        ('ojo', 'Identificar su función jurídica', 294.7),
        ('ruta', 'Determinar su origen y trazabilidad', 297.6),
        ('lupa_doc', 'Analizar su relación con el delito', 300.1),
        ('balanza', 'Sustentar las medidas', 302.9))),
    ('m08_metodologia', 'mg_lista', 323.2, 337.8, lista(
        None,
        ('libros', 'Lecturas y audiovisuales', 329.8),
        ('libro_ley', 'Análisis normativo', 331.3),
        ('engranaje', 'Ejercicios de aplicación', 334.4),
        ('doc_check', 'Actividades evaluativas', 336.1))),
    ('c10_gestion', 'carton', 351.8, 367.7, cita(
        'La adecuada gestión de los bienes fortalece la eficacia de la investigación, protege los '
        'derechos de las víctimas y mantiene las actuaciones dentro de los límites constitucionales '
        'y legales.')),
    ('lt02', 'lt', 368.2, 376.6, PROFE),
]
