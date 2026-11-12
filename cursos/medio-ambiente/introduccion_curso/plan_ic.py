# -*- coding: utf-8 -*-
"""Introducción al curso «Investigación y judicialización de delitos contra el
medio ambiente y los recursos naturales» (Delitos ambientales, 12 nov 2026).

Fuente: Drive, carpeta del curso → `VIDEOS`, archivo `ambiental_inicio_curso.mp4`.
Es una grabación de Teams de 3:47,6, 1280×720 a 30 fps, con el fondo virtual
DAE/Fiscalía (el aéreo, con el logo arriba a la izquierda). Habla la docente de
las introducciones de unidad.

**Quién es.** Ella dice «Mi nombre es Diana Carolina Flórez Bayona». El lower
third dice «Diana Carolina Florez Vallona», como el de la U1 que confirmó
Sebastián el 10 nov (en los clips suena «Bayona»). Debajo, lo que ella dice de sí
misma: doctora en Derecho, magíster en Administración Pública y especialista en
Derecho Constitucional.

**Formato.** El de los videos de profes (SRPA, entrevista TE) con lo de las
introducciones de esta docente:
- intro FGN, cartón de título «Introducción al curso» (el de las introducciones,
  `titulo_dema` sobre u1v2), el clip, cartón de cierre y outro FGN, todo a 1:1
  (ni la marca APRENDE CON LA DAE ni el outro se recortan);
- la ventana 1143×643 desde (0, 30): ella queda a la derecha (la cabeza empieza
  en x≈857) y la caja de cartones (x 62–790) queda libre; el logo del fondo
  virtual entra entero (x 59–832, y 20–188);
- lower third de la U1 (`cartones_srpa.lower_third`), cartones de caja
  (`cartones_ma`, rejilla B) y listas de After Effects (`mg_srpa`, en
  `MA_intros_mg.aep`);
- audio v2 de los profes (ecualizado, comprimido, −16 LUFS), con el limitador
  después del export (`ic_limita`).

Los tiempos son segundos de la fuente (sin cortes). En la línea:
cuadro = 409 + round(t · 23,976). Textos verbatim de la transcripción (Scribe), sin
muletillas. Se corrigió «afecciones» por «afectaciones» (U2) y el nombre del curso
va como en el cartón de título (ella dice «delitos con el medio ambiente»).
"""

CLIP0 = 409
FPS = 24000 / 1001
ANTE, TIT, CUE, SUELTA = 29, 46, 37, 54
GAP_TIT, GAP_CUE, GAP_ANTE = 28, 12, 16

CURSO = 'E:/DAE MASTER/CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE'
R = CURSO + '/INTRODUCCION AL CURSO'
BIN = ['CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE', 'INTRODUCCION AL CURSO']
ORIGINAL = R + '/01 VIDEO/ambiental_inicio_curso.mp4'
COMPUESTO = R + '/01 VIDEO/IC_compuesto_v1.mp4'
TITULO = R + '/02 CARTONES/carton titulo ambientales introduccion al curso.mp4'
TITULO_BASE = CURSO + '/UNIDAD 1/02 CARTONES/carton titulo ambientales u1v2.mp4'
SUB = 'Introducción al curso'
NOMBRE_LINEA = 'MA - CURSO - INTRODUCCION'
EXPORT = 'delitosambientales - CURSO - INTRODUCCION-v%d'
PREFIJO = 'IC'
TMP = 'D:/DAE/_tmp/ma/ic'
XY, VENTANA = (0, 30), (1143, 643)
AUDIO_META = 'I=-16:TP=-3:LRA=7'

NOMBRE_CURSO = ('Investigación y judicialización de delitos contra el medio ambiente y los '
                'recursos naturales')
PROFE = ('Diana Carolina Florez Vallona',
         'Doctora en Derecho, magíster en Administración Pública y especialista en Derecho '
         'Constitucional')


def cuadro(t):
    return CLIP0 + int(round(t * FPS))


def c_tit(titulo, cuerpo):
    return [(titulo, 'bold', TIT, 0), (cuerpo, 'med', CUE, GAP_TIT)]


def c_ante(ante, titulo, cuerpo=None):
    ls = [(ante, 'med', ANTE, 0), (titulo, 'bold', TIT, GAP_ANTE)]
    if cuerpo:
        ls.append((cuerpo, 'med', CUE, GAP_CUE + 8))
    return ls


def c_unidad(n, titulo, cuerpo=None):
    return c_ante('Unidad %d' % n, titulo, cuerpo)


def c_suelta(t):
    return [(t, 'bold', SUELTA, 0)]


def lista(titulo, *filas):
    return {'titulo': titulo, 'filas': list(filas)}


ITEMS = [
    ('lt01', 'lt', 0.6, 10.4, PROFE),
    ('c01_bienvenida', 'carton', 21.0, 31.8, c_ante('Bienvenida al curso', NOMBRE_CURSO)),
    ('m01_experiencia', 'mg_lista', 34.6, 52.2, lista(
        'Con la experiencia',
        ('mazo', 'Fiscal especializada en el sistema penal oral acusatorio', 37.94),
        ('mundo', 'Asesora legal en proyectos de cooperación internacional', 40.28),
        ('libro_ley', 'Formulación de políticas públicas en política criminal y justicia '
                      'transicional', 45.02))),
    ('c02_proposito', 'carton', 78.2, 96.9, c_tit(
        'Tiene como propósito',
        'Fortalecer los conocimientos y las herramientas para comprender y abordar desafíos que '
        'plantea la investigación y judicialización de las conductas que afectan el medio ambiente '
        'y los recursos naturales en Colombia.')),
    ('c03_cinco', 'carton', 97.6, 103.1, c_suelta('Cinco unidades')),
    ('c04_u1', 'carton', 103.3, 113.8, c_unidad(
        1, 'Los desafíos del derecho penal ambiental', 'Y su relación con la Constitución Ecológica.')),
    ('c05_u2', 'carton', 114.0, 122.2, c_unidad(
        2, 'Aplicación del derecho penal ambiental y afectación de los recursos naturales en '
           'Colombia')),
    ('m02_u2', 'mg_lista', 122.4, 135.0, lista(
        'Con especial atención a',
        ('mineria', 'La extracción ilícita de minerales', 124.22),
        ('tala', 'La deforestación', 127.38),
        ('grupos', 'Las afectaciones ambientales asociadas a grupos armados organizados', 129.16))),
    ('c06_u3', 'carton', 135.4, 141.4, c_unidad(
        3, 'Estrategias y técnicas de investigación en los delitos ambientales')),
    ('m03_u3', 'mg_lista', 141.5, 155.0, lista(
        None,
        ('binoculares', 'La dirección de la investigación', 141.7),
        ('lupa_doc', 'Hechos jurídicamente relevantes', 145.76),
        ('huella', 'Procedimientos de policía judicial', 148.36),
        ('red', 'La investigación en contexto', 151.16),
        ('matraz', 'La prueba pericial', 153.36))),
    ('c07_u4', 'carton', 158.9, 168.6, c_unidad(
        4, 'La justicia restaurativa',
        'Y su aplicación en los delitos contra el medio ambiente y los recursos naturales.')),
    ('c08_u5', 'carton', 168.8, 182.8, c_unidad(
        5, 'Las terminaciones anticipadas del proceso penal',
        'Y sus particularidades en el contexto de la criminalidad ambiental.')),
    ('m04_recorrido', 'mg_lista', 186.4, 206.2, lista(
        'Que este recorrido les permita',
        ('libros', 'Profundizar en sus conocimientos', 188.9),
        ('bombilla', 'Reflexionar sobre los retos que enfrenta la investigación de los delitos '
                     'ambientales', 191.54),
        ('engranaje', 'Fortalecer sus capacidades para abordar estos fenómenos', 197.94))),
    ('c09_invito', 'carton', 206.4, 221.7, c_tit(
        'Les invito',
        'A participar activamente en todas las actividades propuestas, aprovechar los recursos de '
        'aprendizaje y relacionar todos los contenidos con los desafíos que se encuentran en el '
        'ejercicio de sus funciones.')),
    ('c10_bienvenidos', 'carton', 221.9, 227.4, [
        ('Les deseo muchísimos éxitos en este proceso', 'med', ANTE, 0),
        ('Bienvenidos y bienvenidas', 'bold', SUELTA, GAP_ANTE)]),
]
