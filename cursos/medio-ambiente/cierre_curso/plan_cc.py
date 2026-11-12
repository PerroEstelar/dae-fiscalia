# -*- coding: utf-8 -*-
"""Cierre del curso «Investigación y judicialización de delitos contra el medio
ambiente y los recursos naturales» (Delitos ambientales, 12 nov 2026).

Fuente: Drive, carpeta del curso → `VIDEOS`, archivo `ambiental_cierre_curso.mp4`.
Es una grabación de Teams de 2:52,6, 1280×720 a 30 fps, con el mismo fondo
virtual y la misma docente que la introducción al curso (`plan_ic.py`): «Soy
Diana Carolina Flórez Bayona». El lower third dice «Diana Carolina Florez
Vallona», como la U1 y la introducción.

**Formato.** El de la introducción al curso, con las mismas herramientas
(`ic_pieza`, `ic_linea`, `ic_mp4`, `ic_revision`, con `DAE_PLAN=plan_cc`):
- intro FGN, cartón de título «Cierre del curso» (`titulo_dema` sobre u1v2), el
  clip, cartón de cierre y outro, todo a 1:1;
- la ventana 1143×643 desde (0, 30);
- lower third, cartones de caja (`cartones_ma`) y listas de AE (`mg_srpa`, en
  `MA_intros_mg.aep`, comps `CC_*`);
- audio v2 de los profes (−16 LUFS);
- entrega en MP4 (receta del 23 oct, `ic_mp4`).

Tiempos en segundos de la fuente; en la línea cuadro = 409 + round(t · 23,976).
Textos verbatim de Scribe (WAV 16 kHz).
- Se corrigió «contribuyen» por «contribuyan».
- Los rótulos de las listas son sus palabras recortadas para caber en la caja
  (cima ≥ 250, medido antes de armar).
- Densidad: se dejaron fuera tres frases para no pasar del ~70 %:
  - «Esto considerando las particularidades…»;
  - «No basta con identificar…»;
  - el agradecimiento.
"""

CLIP0 = 409
FPS = 24000 / 1001
ANTE, TIT, CUE, SUELTA = 29, 46, 37, 54
GAP_TIT, GAP_CUE, GAP_ANTE = 28, 12, 16

CURSO = 'E:/DAE MASTER/CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE'
R = CURSO + '/CIERRE DEL CURSO'
BIN = ['CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE', 'CIERRE DEL CURSO']
ORIGINAL = R + '/01 VIDEO/ambiental_cierre_curso.mp4'
COMPUESTO = R + '/01 VIDEO/CC_compuesto_v1.mp4'
TITULO = R + '/02 CARTONES/carton titulo ambientales cierre del curso.mp4'
TITULO_BASE = CURSO + '/UNIDAD 1/02 CARTONES/carton titulo ambientales u1v2.mp4'
SUB = 'Cierre del curso'
NOMBRE_LINEA = 'MA - CURSO - CIERRE'
EXPORT = 'delitosambientales - CURSO - CIERRE-v%d'
PREFIJO = 'CC'
TMP = 'D:/DAE/_tmp/ma/cc'
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


def c_cuerpo(t):
    # una frase larga sola, en mediana: con título encima se salía de la caja (cima < 250)
    return [(t, 'med', CUE, 0)]


def c_suelta(t):
    return [(t, 'bold', SUELTA, 0)]


def lista(titulo, *filas):
    return {'titulo': titulo, 'filas': list(filas)}


ITEMS = [
    ('lt01', 'lt', 0.8, 8.8, PROFE),
    # con el nombre del curso debajo quedaba a 20 car/s; el nombre ya está en los cartones de título
    ('c01_final', 'carton', 8.8, 16.6, [(
        'Quiero felicitarlos por haber llegado al final de este curso', 'bold', TIT, 0)]),
    ('c02_perspectivas', 'carton', 22.0, 33.4, c_tit(
        'Diferentes perspectivas jurídicas, investigativas y procesales',
        'Para comprender los desafíos que representa la criminalidad ambiental en Colombia.')),
    ('m01_unidades', 'mg_lista', 36.4, 54.4, lista(
        'En las cinco unidades',
        ('libro_ley', 'Fundamentos constitucionales y penales', 38.14),
        ('lupa_doc', 'Conductas que afectan los recursos naturales', 42.98),
        ('binoculares', 'Estrategias y herramientas de investigación', 48.02))),
    ('m02_tambien', 'mg_lista', 54.6, 65.2, lista(
        'También analizamos',
        ('manos_brote', 'La justicia restaurativa', 57.5),
        ('apreton', 'Los mecanismos de terminación anticipada del proceso penal', 61.34))),
    ('c03_integral', 'carton', 80.6, 88.8, [(
        'La investigación de los delitos ambientales exige una mirada integral.', 'bold', TIT, 0)]),
    ('m03_necesario', 'mg_lista', 95.0, 114.4, lista(
        'También es necesario',
        ('mapa', 'Comprender las dinámicas territoriales, económicas y sociales', 96.18),
        ('lupa_persona', 'Identificar a los posibles responsables', 104.08),
        ('grupos', 'Valorar las afectaciones', 108.12))),
    ('c04_servidores', 'carton', 114.6, 125.0, c_tit(
        'Como servidores y servidoras de la Fiscalía General de la Nación',
        'Tienen una responsabilidad fundamental en la investigación y judicialización de estas '
        'conductas.')),
    ('m04_esperamos', 'mg_lista', 128.6, 143.0, lista(
        'Esperamos que les puedan',
        ('persona', 'Aportar a su ejercicio profesional', 130.62),
        ('lupa_doc', 'Enriquecer sus análisis', 133.58),
        ('edificio', 'Contribuir al fortalecimiento institucional', 135.66))),
    ('c05_proteccion', 'carton', 143.4, 153.2, c_tit(
        'La protección del medio ambiente',
        'Es un desafío que requiere conocimiento, compromiso y una actuación articulada.')),
    ('c06_exitos', 'carton', 160.8, 167.8, c_cuerpo(
        'Les deseo muchos éxitos en el desarrollo de sus funciones y en los retos profesionales que '
        'tienen por delante.')),
    ('c07_gracias', 'carton', 168.1, 172.4, [
        ('Muchas gracias', 'bold', SUELTA, 0),
        ('Hasta una próxima oportunidad', 'med', ANTE, GAP_ANTE)]),
]
