# -*- coding: utf-8 -*-
"""Plan de las introducciones de unidad U2–U5 de Delitos contra el medio ambiente.

Molde: `MA - U1 - INTRODUCCION` tal como la dejó Sebastián (10 nov 2026):
    V1  intro FGN 0–194 · (hueco tapado por el cartón de título en V2) ·
        clip de la unidad desde el 409 · cartón de título de cierre (zoom 1,16,
        pan 145) · outro FGN (mismo clip, zoom 1,16, pan 145)
    V2  cartón de título 194–409 + cartones de caja (rejilla B, cartones_v3)
    V3  libre en la U1 → aquí MOTION GRAPHICS (After Effects, por aftr)
    V4/V5  lower third «Diana Carolina Florez Vallona» 413–569 (Text+ y Text)
    A1  audio del intro, del clip y del outro. Sin música, sin marca de agua.

Todos los cuadros son de LÍNEA (el clip empieza en el 409). Los textos salen de la
transcripción palabra por palabra de cada clip (Scribe, `03 VOCES/stt`), con la
puntuación y las mayúsculas corregidas; nada que ella no diga.

Tipos:
    carton   cartón de caja de cartones_v3 (Pillow): [(texto, peso, tamaño, gap)]
    mg_lista After Effects: título + filas ícono/rótulo que entran con su palabra
    mg_act   After Effects: tarjeta de actividad con ícono animado
"""

CLIP0 = 409
FPS = 24000 / 1001

ANTE, TIT, CUE, SUELTA = 29, 46, 37, 54
GAP_TIT, GAP_CUE, GAP_ANTE = 28, 12, 16


def c_unidad(n, titulo, cuerpo=None):
    ls = [('Unidad %d' % n, 'med', ANTE, 0), (titulo, 'bold', TIT, GAP_ANTE)]
    if cuerpo:
        ls.append((cuerpo, 'med', CUE, GAP_CUE + 8))
    return ls


def c_tit(titulo, cuerpo):
    return [(titulo, 'bold', TIT, 0), (cuerpo, 'med', CUE, GAP_TIT)]


def c_leccion(n, titulo, cuerpo=None):
    ls = [('Lección %d' % n, 'med', ANTE, 0), (titulo, 'bold', TIT, GAP_ANTE)]
    if cuerpo:
        ls.append((cuerpo, 'med', CUE, GAP_CUE + 8))
    return ls


def c_suelta(t):
    return [(t, 'bold', SUELTA, 0)]


def act(n, icono, titulo, cuerpo):
    return {'icono': icono, 'ante': 'Actividad %d' % n, 'titulo': titulo, 'cuerpo': cuerpo}


UNIDADES = {
 2: {
  'clip_cuadros': 7553,
  'titulo': 'Aplicación del derecho penal ambiental y afectación de los recursos naturales en Colombia',
  'items': [
   ('c01_unidad', 'carton', 818, 200, c_unidad(2,
       'Aplicación del derecho penal ambiental y afectación de los recursos naturales en Colombia')),
   ('c03_competencia', 'carton', 1521, 300, c_tit('La competencia',
       'Comprender la estructura de los delitos contra el medio ambiente en Colombia.')),
   ('m01_macrocriminalidad', 'mg_lista', 1990, 400, {
       'titulo': 'Macrocriminalidad ambiental',
       'filas': [('mineria', 'Extracción ilícita de minerales', 2111),
                 ('tala', 'Deforestación', 2166),
                 ('grupos', 'Grupos armados organizados', 2214)]}),
   ('c05_cinco_lecciones', 'carton', 2800, 171, c_suelta('Cinco lecciones')),
   ('c06_leccion1', 'carton', 2995, 300, c_leccion(1,
       'Régimen jurídico de los recursos naturales renovables en Colombia',
       'Su regulación y protección.')),
   ('c07_leccion2', 'carton', 3410, 300, c_leccion(2,
       'Estructura y análisis de los tipos penales',
       'Que protegen el medio ambiente y los recursos naturales en Colombia.')),
   ('c08_leccion3', 'carton', 3785, 300, c_leccion(3,
       'Extracción ilícita de minerales',
       'Desde la perspectiva del derecho penal y de la investigación.')),
   ('c09_leccion4', 'carton', 4182, 290, c_leccion(4,
       'La deforestación',
       'Su abordaje dentro de la investigación penal.')),
   ('c10_leccion5', 'carton', 4500, 300, c_leccion(5,
       'Fenómeno de afectación ambiental por grupos armados organizados en Colombia')),
   ('c11_actividades', 'carton', 4935, 200, c_suelta('Actividades y recursos')),
   ('m02_act1', 'mg_act', 5215, 300, act(1, 'tactil', 'Recurso interactivo',
       'Sobre la extracción ilícita de minerales.')),
   ('m03_act2', 'mg_act', 5565, 251, act(2, 'mapa', 'Análisis cartográfico',
       'La dimensión territorial de la deforestación.')),
   ('m04_act3', 'mg_act', 5840, 300, act(3, 'libro_ley', 'Fundamentación conceptual y jurídica',
       'De los tipos penales.')),
   ('m05_act4', 'mg_act', 6180, 255, act(4, 'video', 'Video integrador de repaso',
       'Para recuperar los principales elementos estudiados.')),
   ('m06_act5', 'mg_act', 6460, 300, act(5, 'lista', 'Actividad evaluativa',
       'De consolidación de los conceptos.')),
   ('c12_invito', 'carton', 7430, 286, c_tit('Los invito',
       'A recorrer cada una de las lecciones, desarrollar las actividades propuestas y '
       'relacionar los contenidos jurídicos con las situaciones concretas.')),
   ('c13_bienvenidos', 'carton', 7740, 210, [
       ('Bienvenidos a la unidad 2', 'med', ANTE, 0),
       ('Aplicación del derecho penal ambiental y afectación de los recursos naturales en Colombia',
        'bold', TIT, GAP_ANTE)]),
  ]},
 3: {
  'clip_cuadros': 7194,
  'titulo': 'Estrategias y técnicas de investigación en los delitos ambientales',
  'items': [
   ('c01_unidad', 'carton', 740, 260, c_unidad(3,
       'Estrategias y técnicas de investigación en los delitos ambientales')),
   ('c02_esta_unidad', 'carton', 1030, 330, c_tit('En esta unidad',
       'Las herramientas y estrategias necesarias para desarrollar adecuadamente una '
       'investigación penal en materia ambiental.')),
   ('c03_competencia', 'carton', 1500, 228, c_tit('La competencia',
       'Implementar estrategias de investigación y judicialización para delitos contra el '
       'medio ambiente.')),
   ('m01_integrando', 'mg_lista', 1752, 234, {
       'titulo': 'Integrando',
       'filas': [('huella', 'Procedimientos de policía judicial', 1782),
                 ('binoculares', 'Técnicas especiales de investigación', 1844),
                 ('red', 'Análisis de contexto de criminalidad organizada', 1910)]}),
   ('c04_hechos', 'carton', 2010, 300, c_tit('Manejo probatorio y pericial',
       'Para la correcta construcción de unos hechos jurídicamente relevantes.')),
   ('c06_cinco_lecciones', 'carton', 2590, 101, c_suelta('Cinco lecciones')),
   ('c07_leccion1', 'carton', 2715, 300, c_leccion(1,
       'Dirección de la investigación y estrategia de judicialización en delitos ambientales')),
   ('c08_leccion2', 'carton', 3337, 300, c_leccion(2,
       'Construcción de los hechos jurídicamente relevantes',
       'En delitos contra el medio ambiente.')),
   ('c09_leccion3', 'carton', 3834, 300, c_leccion(3,
       'Procedimientos de policía judicial',
       'Aplicados a la investigación de delitos medioambientales.')),
   ('c10_leccion4', 'carton', 4259, 300, c_leccion(4,
       'Articulación con investigaciones en contexto',
       'Crimen organizado y finanzas.')),
   ('c11_leccion5', 'carton', 4800, 300, c_leccion(5,
       'La prueba pericial',
       'En materia procesal penal frente a los delitos ambientales.')),
   ('c12_actividades', 'carton', 5225, 200, c_suelta('Actividades')),
   ('m02_act1', 'mg_act', 5541, 300, act(1, 'ruta', 'Recorrido por experiencias institucionales',
       'De investigación en delitos ambientales.')),
   ('m03_act2', 'mg_act', 5882, 300, act(2, 'lupa_doc', 'Análisis crítico',
       'Sobre la actuación investigativa y el uso de las técnicas de policía judicial.')),
   ('m04_act3', 'mg_act', 6306, 300, act(3, 'portatil', 'Material virtual',
       'Fundamentación conceptual y jurídica de las técnicas de investigación, la priorización '
       'y la prueba pericial.')),
   ('m05_act4', 'mg_act', 6818, 244, act(4, 'video', 'Video integrador de repaso',
       'Para recuperar los principales contenidos abordados.')),
   ('m06_act5', 'mg_act', 7086, 270, act(5, 'lista', 'Actividad evaluativa',
       'De consolidación de conceptos.')),
   ('c13_bienvenidos', 'carton', 7380, 210, [
       ('Bienvenidos a la unidad 3', 'med', ANTE, 0),
       ('Estrategias y técnicas de investigación en los delitos ambientales', 'bold', TIT,
        GAP_ANTE)]),
  ]},
 4: {
  'clip_cuadros': 8256,
  'titulo': 'La justicia restaurativa en el marco del proceso penal colombiano y su aplicación a '
            'los delitos contra el medio ambiente y los recursos naturales',
  'items': [
   ('c01_unidad', 'carton', 700, 201, c_unidad(4,
       'La justicia restaurativa en el marco del proceso penal colombiano',
       'Y su aplicación a los delitos contra el medio ambiente y los recursos naturales.')),
   ('c02_esta_unidad', 'carton', 925, 300, c_tit('En esta unidad',
       'Los principales enfoques, principios y mecanismos de la justicia restaurativa en el '
       'proceso penal colombiano.')),
   ('m01_participacion', 'mg_lista', 1250, 358, {
       'titulo': 'La participación',
       'filas': [('personas', 'De las víctimas', 1324),
                 ('grupos', 'De las comunidades', 1346),
                 ('dialogo', 'De los demás involucrados', 1387)]}),
   ('c03_competencia', 'carton', 1632, 300, c_tit('La competencia',
       'Identificar los enfoques, los principios y mecanismos de la justicia restaurativa en el '
       'proceso penal colombiano frente a los delitos ambientales.')),
   ('m02_reparacion', 'mg_lista', 1990, 400, {
       'titulo': 'Soluciones orientadas a',
       'filas': [('manos_brote', 'La reparación', 2225),
                 ('brote', 'La restauración', 2265),
                 ('balanza_hoja', 'La compensación efectiva del daño ecológico', 2300)]}),
   ('c05_cinco_lecciones', 'carton', 2965, 102, c_suelta('Cinco lecciones')),
   ('c06_leccion1', 'carton', 3091, 300, c_leccion(1,
       'Justicia restaurativa en el marco del proceso penal colombiano',
       'En los delitos contra el medio ambiente y los recursos naturales.')),
   ('c07_leccion2', 'carton', 3616, 300, c_leccion(2,
       'Participación de las víctimas, comunidades y demás actores',
       'En los procesos restaurativos ambientales.')),
   ('c08_leccion3', 'carton', 4150, 300, c_leccion(3,
       'Mecanismos de reparación, restauración y compensación',
       'En los delitos contra el medio ambiente y los recursos naturales.')),
   ('c09_leccion4', 'carton', 4762, 300, c_leccion(4,
       'Criterios para la aplicación de justicia restaurativa',
       'En la investigación y judicialización de delitos ambientales.')),
   ('c10_leccion5', 'carton', 5361, 300, c_leccion(5,
       'Análisis de casos y experiencias',
       'De justicia restaurativa en materia ambiental.')),
   ('c11_actividades', 'carton', 5967, 200, c_suelta('Actividades')),
   ('m03_act1', 'mg_act', 6288, 300, act(1, 'ruta', 'Recorrido por experiencias',
       'De justicia restaurativa, ambiental y jurisprudencial.')),
   ('m04_act2', 'mg_act', 6736, 300, act(2, 'lupa_doc', 'Análisis crítico',
       'Sobre el daño ambiental, los enfoques biocéntricos y las respuestas restaurativas.')),
   ('m05_act3', 'mg_act', 7251, 300, act(3, 'portatil', 'Material virtual',
       'Fundamentación conceptual y jurídica de la justicia restaurativa y los mecanismos de '
       'reparación.')),
   ('m06_act4', 'mg_act', 7738, 225, act(4, 'video', 'Video integrador de repaso',
       'Para recuperar los principales contenidos abordados.')),
   ('m07_act5', 'mg_act', 7988, 290, act(5, 'lista', 'Actividad evaluativa',
       'De consolidación de conceptos.')),
   ('c12_bienvenidos', 'carton', 8314, 300, [
       ('Bienvenidos a la unidad 4', 'med', ANTE, 0),
       ('La justicia restaurativa en el marco del proceso penal colombiano', 'bold', TIT,
        GAP_ANTE)]),
  ]},
 5: {
  'clip_cuadros': 7569,
  'titulo': 'Mecanismos de terminación anticipada, negociación y reparación integral en el '
            'proceso penal ambiental',
  'items': [
   ('c01_unidad', 'carton', 740, 221, c_unidad(5,
       'Mecanismos de terminación anticipada, negociación y reparación integral en el proceso '
       'penal ambiental')),
   ('c02_esta_unidad', 'carton', 985, 313, c_tit('En esta unidad',
       'Los principales mecanismos de terminación anticipada del proceso penal colombiano y su '
       'aplicación en la judicialización de los delitos ambientales.')),
   ('m01_mecanismos', 'mg_lista', 1322, 430, {
       'titulo': 'Estudiaremos',
       'filas': [('senal', 'El principio de oportunidad', 1381),
                 ('apreton', 'Los preacuerdos y negociaciones', 1418),
                 ('firma', 'El allanamiento a cargos', 1483)]}),
   ('c03_competencia', 'carton', 1780, 300, c_tit('La competencia',
       'Comprender los mecanismos de terminación anticipada del proceso penal colombiano en la '
       'judicialización de delitos ambientales.')),
   ('m02_reparacion', 'mg_lista', 2140, 240, {
       'titulo': 'Condicionando su procedencia',
       'filas': [('manos_brote', 'A la efectiva reparación integral del daño ecológico causado', 2224)]}),
   ('c05_cuatro_lecciones', 'carton', 2905, 116, c_suelta('Cuatro lecciones')),
   ('c06_leccion1', 'carton', 3045, 300, c_leccion(1,
       'Principio de oportunidad',
       'En los delitos contra el medio ambiente y los recursos naturales.')),
   ('c07_leccion2', 'carton', 3500, 300, c_leccion(2,
       'Preacuerdos y negociaciones',
       'Entre la Fiscalía y el imputado en materia ambiental.')),
   ('c08_leccion3', 'carton', 4102, 300, c_leccion(3,
       'Allanamiento a cargos y aceptación de responsabilidad',
       'En delitos ambientales.')),
   ('c09_leccion4', 'carton', 4647, 300, c_leccion(4,
       'Reparación integral del daño ambiental',
       'Como criterio para la aplicación de terminaciones anticipadas.')),
   ('c10_actividades', 'carton', 5231, 200, c_suelta('Actividades')),
   ('m03_act1', 'mg_act', 5611, 300, act(1, 'tactil', 'Recurso interactivo',
       'Sobre los fundamentos y finalidades de las terminaciones anticipadas.')),
   ('m04_act2', 'mg_act', 5982, 300, act(2, 'libro_ley', 'Análisis normativo',
       'De los mecanismos de terminación anticipada establecidos en la Ley 906.')),
   ('m05_act3', 'mg_act', 6333, 300, act(3, 'infografia', 'Infografía interactiva',
       'Sobre la fundamentación conceptual y jurídica de los preacuerdos y las negociaciones.')),
   ('m06_act4', 'mg_act', 6786, 300, act(4, 'ruta', 'Recorrido interactivo',
       'Por la ruta del allanamiento a cargos y su aplicación ambiental.')),
   ('m07_act5', 'mg_act', 7118, 206, act(5, 'video', 'Video integrador de repaso',
       'Para recuperar los principales contenidos abordados.')),
   ('m08_act6', 'mg_act', 7348, 292, act(6, 'lista', 'Actividad evaluativa',
       'De consolidación de conceptos.')),
   ('c11_bienvenidos', 'carton', 7664, 270, [
       ('Bienvenidos a la unidad 5', 'med', ANTE, 0),
       ('Mecanismos de terminación anticipada, negociación y reparación integral en el proceso '
        'penal ambiental', 'bold', TIT, GAP_ANTE)]),
  ]},
}


def revisar():
    for u, d in UNIDADES.items():
        fin = CLIP0 + d['clip_cuadros']
        prev = None
        tot = 0
        for clave, tipo, ini, dur, _ in d['items']:
            assert ini + dur <= fin, (u, clave, ini + dur, fin)
            if prev:
                hueco = ini - prev
                assert hueco >= 10, (u, clave, 'pisa al anterior', hueco)
            prev = ini + dur
            tot += dur
        print('U%d: %d items, %d cuadros de %d (%.0f %%), fin del clip %d'
              % (u, len(d['items']), tot, d['clip_cuadros'], 100 * tot / d['clip_cuadros'], fin))


if __name__ == '__main__':
    revisar()
