# -*- coding: utf-8 -*-
"""Entrevista «Técnicas especiales de investigación» (Delitos ambientales, Unidad 3,
11 nov 2026).

Fuente: Drive, carpeta del curso → `VIDEOS/VIDEOS UNIDADES`, archivo
`tecnicas_especiales_delitos_ambientales.mp4`. Es una grabación de Teams de 14:59,
1280×720 a 30 fps, con fondo virtual DAE/Fiscalía (el aéreo). Habla un solo
profe a cámara.

**Quién es.** La ficha del curso (Unidad 3) pide para esta sección una
«Entrevista al doctor Jairo Porras o CTI: Técnicas especiales de investigación:
interceptación de comunicaciones, búsquedas selectivas en bases de datos, análisis
link, agente encubierto, entregas controladas». El profe no dice su nombre en el
video. Sí dice que lleva 32 años en la Fiscalía y que fue 13 años fiscal
especializado ante la DEMA, y habla de fuentes no formales, interceptación, agente
encubierto y entrega controlada. **El nombre está por confirmar con Sebastián.**

**Dónde va.** En la Unidad 3, «Estrategias y técnicas de investigación en los
delitos ambientales». La ficha lo pone en la sección de las técnicas de policía
judicial (lección 3).

Formato: el de las introducciones de Delitos ambientales y el de los videos de
profes del curso SRPA. El profe va a la derecha, con la ventana 1143×643 desde
(12, 30) como en el fondo aéreo de la U3 de SRPA, y la caja de cartones a la
izquierda. El audio es el v2 de SRPA: ecualizado, comprimido y a −16 LUFS. El
cierre y el outro van a 1:1.

Los tiempos son segundos de la fuente (sin cortes). En la línea:
cuadro = 409 + round(t · 23,976). Los textos son verbatim, sin muletillas; se
corrigió «pseudónimo» a «seudónimo» y «nombe iuris» a «nomen iuris».
"""

CLIP0 = 409
FPS = 24000 / 1001
ANTE, TIT, CUE, SUELTA = 29, 46, 37, 54
GAP_TIT, GAP_CUE, GAP_ANTE = 28, 12, 16

CURSO = 'E:/DAE MASTER/CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE'
R = CURSO + '/UNIDAD 3/ENTREVISTA - Tecnicas especiales de investigacion'
BIN = ['CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE', 'UNIDAD 3', 'ENTREVISTA - Tecnicas especiales de investigacion']
ORIGINAL = R + '/01 VIDEO/tecnicas_especiales_delitos_ambientales.mp4'
COMPUESTO = R + '/01 VIDEO/TE_compuesto_v1.mp4'
TITULO = R + '/02 CARTONES/carton titulo entrevista tecnicas especiales.mp4'
SUB = 'Entrevista: técnicas especiales de investigación'
NOMBRE_LINEA = 'MA - U3 - ENTREVISTA TECNICAS ESPECIALES'
EXPORT = 'delitosambientales - U3 - ENTREVISTA TECNICAS ESPECIALES-v%d'
XY, VENTANA = (12, 30), (1143, 643)

PROFE = ('Jairo Porras',
         '32 años en la Fiscalía General de la Nación, 13 como fiscal especializado de la DEMA')


def cuadro(t):
    return CLIP0 + int(round(t * FPS))


def cita(t):
    return [(t, 'bold', TIT, 0)] if len(t) <= 78 else [(t, 'med', CUE, 0)]


def c_tit(titulo, cuerpo):
    return [(titulo, 'bold', TIT, 0), (cuerpo, 'med', CUE, GAP_TIT)]


def c_suelta(t):
    return [(t, 'bold', SUELTA, 0)]


def act(icono, ante, titulo, cuerpo=None):
    return {'icono': icono, 'ante': ante, 'titulo': titulo, 'cuerpo': cuerpo}


def lista(titulo, *filas):
    return {'titulo': titulo, 'filas': list(filas)}


ITEMS = [
    ('lt01', 'lt', 3.2, 13.5, PROFE),
    ('c01_amazonia', 'carton', 22.8, 40.4, cita(
        'Varias técnicas de investigación para generar una buena dinámica investigativa, sobre todo '
        'en la Amazonía colombiana.')),
    ('c02_macrocasos', 'carton', 41.0, 56.8, cita(
        'En principio eran situaciones irregulares de explotación ilícita de yacimiento minero, que '
        'posteriormente se convirtieron en macrocasos.')),
    ('m01_macrocasos', 'mg_lista', 57.2, 72.0, lista(
        'Macrocasos',
        ('personas', 'Muchas personas involucradas', 60.3),
        ('edificio', 'Autoridades: gobernaciones y alcaldes', 67.8),
        ('persona', 'Miembros de la Fuerza Pública', 70.5))),
    ('c03_identidad', 'carton', 87.2, 95.6, cita(
        'Guardar la identidad de las personas que nos daban información.')),
    ('m02_fuente', 'mg_act', 131.0, 161.0, act(
        'carpeta', 'Técnica de investigación', 'Fuente no formal',
        'Debe estar registrada en un cardex, con la identidad de la persona, para que la información '
        'sea fidedigna.')),
    ('c04_seudonimo', 'carton', 161.3, 177.4, cita(
        'Se reserva la información, se guarda en el cardex y se le recibe el testimonio a la persona '
        'bajo un seudónimo.')),
    ('c05_precaria', 'carton', 178.0, 196.0, cita(
        'Es relevante en aquellos casos donde es muy precaria la recepción de la información y el '
        'acceso a los sitios de los hechos.')),
    ('c06_no_prueba', 'carton', 223.0, 237.4, c_tit(
        'Las fuentes no formales no son prueba per se',
        'Son información legalmente aportada al proceso con la cual vamos a buscar la prueba.')),
    ('c07_motivo', 'carton', 240.0, 259.4, cita(
        'Verificar que ese número telefónico esté siendo usado por un actor criminal: entonces tengo '
        'el motivo fundado para interceptar.')),
    ('m03_tecnicas', 'mg_lista', 259.8, 292.4, lista(
        'Técnicas especiales de investigación',
        ('senal', 'Interceptación de comunicaciones', 261.6),
        ('lupa_persona', 'Agente encubierto', 273.0),
        ('ruta', 'Entrega controlada', 287.0))),
    ('c08_testigos', 'carton', 292.8, 303.0, cita(
        'En la Amazonía colombiana o en la Orinoquía son pocos los testigos que quedan.')),
    ('c09_prueba', 'carton', 320.0, 341.8, cita(
        'Lo que convertimos en prueba es lo que otorgan los contactos o las líneas telefónicas, no lo '
        'que nos señala la fuente no formal.')),
    ('m04_escalar', 'mg_lista', 349.0, 386.0, lista(
        'Escalar la investigación',
        ('mazo', 'Judicializaciones primarias', 356.8),
        ('apreton', 'Negociar u otorgar principios de oportunidad', 366.9),
        ('persona', 'Testigos en juicio contra los principales actores', 381.7))),
    ('c10_fuertes', 'carton', 388.0, 407.0, cita(
        'Llegar no a los más débiles de la cadena, sino a los más fuertes: los que se quedan con el '
        'dinero, los que mueven la parte financiera.')),
    ('c11_ganancia', 'carton', 407.2, 432.0, c_tit(
        'Detrás de un delito ambiental siempre hay una ganancia económica',
        'El músculo financiero hace que las actividades extractivas en los frentes mineros sean mucho '
        'más dinámicas.')),
    ('m05_gobernador', 'mg_act', 458.8, 480.6, act(
        'mazo', 'Corte Suprema de Justicia', 'Un gobernador del Putumayo',
        'La primera persona de más alto rango condenada por explotación ilícita de yacimiento minero.')),
    ('c12_art332', 'carton', 481.0, 500.0, c_tit(
        'Explotación ilícita de yacimiento minero',
        'Así lo contempla el artículo 332. No está bien decir minería ilegal o minería criminal.')),
    ('c13_legal', 'carton', 500.2, 532.8, cita(
        'La minería en Colombia es legal: está amparada por la Constitución y por la ley, '
        'principalmente por la Ley 685 de 2001.')),
    ('m06_requisitos', 'mg_lista', 533.2, 546.0, lista(
        'Dos requisitos',
        ('firma', 'Título minero', 536.8),
        ('brote', 'Licenciamiento ambiental', 540.4))),
    ('c14_legal', 'carton', 580.0, 592.4, cita(
        'La minería, como actividad amparada por la Constitución y la ley, siempre es legal.')),
    ('m07_delitos', 'mg_lista', 598.0, 650.0, lista(
        None,
        ('mineria', 'Explotación ilícita de yacimiento minero', 603.0),
        ('mapa', 'Invasión de áreas de especial importancia ecológica', 620.9),
        ('tala', 'Daño a los recursos naturales', 633.8),
        ('bidon', 'Contaminación ambiental', 647.8))),
    ('c15_mercurio', 'carton', 650.4, 668.8, cita(
        'No solo por el uso de metales pesados como el mercurio, sino también por la forma como se '
        'ejecuta la explotación.')),
    ('m08_peritos', 'mg_lista', 669.2, 718.8, lista(
        'Los peritos',
        ('mapa', 'Zona de reserva forestal', 682.7),
        ('grupos', 'Comunidades indígenas o comunidades negras', 685.2),
        ('matraz', 'En cercanías de una fuente hídrica', 710.1))),
    ('c16_peritacion', 'carton', 719.2, 727.6, cita('La peritación en los delitos ambientales es fundamental.')),
    ('m09_perito', 'mg_lista', 727.8, 750.0, lista(
        None,
        ('lupa_doc', 'Qué clase de daño', 729.2),
        ('brote', 'Cuál es el recurso natural afectado', 734.1),
        ('infografia', 'En qué cantidad', 736.5),
        ('excavadora', 'La modalidad de la explotación', 740.7))),
    ('c17_nomen', 'carton', 750.2, 763.6, cita(
        'Determinar en concreto el nomen iuris, el nombre del delito que se está ejecutando.')),
    ('c18_fuentes', 'carton', 770.0, 792.0, c_tit(
        'Siempre inicien indagando',
        'En fuentes no formales y en fuentes abiertas: en redes sociales, la venta de oro o el '
        'comercio de minerales en determinado lugar.')),
    ('c19_grupos', 'carton', 820.0, 847.2, cita(
        'Llegar a los grupos más fuertes: grupos criminales armados que dominan el territorio y las '
        'actividades económicas de la explotación.')),
    ('lt02', 'lt', 848.0, 857.0, PROFE),
    ('c20_pais', 'carton', 872.0, 897.0, cita(
        'Un país tan maltratado por la explotación ilícita de yacimiento minero necesita funcionarios '
        'comprometidos e ilustrados.')),
]
