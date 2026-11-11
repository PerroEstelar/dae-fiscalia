# -*- coding: utf-8 -*-
"""Plan del conversatorio «Articulación DEMA y DECOC» (Unidad 1, 11 nov 2026).

Fuente: `Video articulacion DEMA y DECOC.mp4` (Drive, carpeta VIDEOS UNIDADES):
grabación de Teams de 19:20, 1280×720 a 30 fps. Son dos mosaicos de 640×360
lado a lado (y 180–540), con franjas negras arriba y abajo y los rótulos de
Teams abajo. La Unidad 1 lo anuncia como «un conversatorio institucional con
la DEMA».

    izquierda  Ana María Díaz González       (speaker_0 en Scribe)
    derecha    Camilo Andrés González López  (speaker_1)

Montaje: el mismo esqueleto de las introducciones MA (intro FGN 0–194, cartón
de título 194–409, clip desde el 409, cartón de cierre y outro con zoom 1,16 y
pan 145). El clip es una composición propia: fondo azul institucional #002048
plano, sin degradé (es el «noche» medido en el intro FGN), y la franja de los
dos mosaicos a 1,5× (1920×540) en y=140. Así se van los rótulos de Teams y
abajo queda una banda de 400 px (y 680–1080) para los gráficos.

Todo gráfico va en esa banda, debajo de quien habla:
    izquierda  barra x=86,   texto x=170
    derecha    barra x=1046, texto x=1130
ancho máximo 720 y bloque anclado arriba en y=725.

Los textos son verbatim de la transcripción (Scribe con diarización,
`03 VOCES/stt/DEMA_DECOC_stt.json`): sin muletillas, nada que no digan. Los
tiempos son segundos del clip. En la línea, cuadro = 409 + t·23,976.

Tipos:
    lt        lower third: nombre y dirección, con barrido como el de la U1
    carton    cartón de caja de cartones_v3, [(texto, peso, px, gap)]
    mg_act    After Effects: ícono, antetítulo, título y cuerpo opcional
    mg_lista  After Effects: título y filas de ícono y rótulo, cada fila con
              su palabra
"""

CLIP0 = 409
FPS = 24000 / 1001
ANTE, TIT, CUE, SUELTA = 29, 46, 37, 54
GAP_TIT, GAP_CUE, GAP_ANTE = 28, 12, 16

FONDO = (0x00, 0x20, 0x48)
TILES_Y = 140
BANDA_TOP = 725
LADO = {'L': {'bar_x': 86, 'text_x': 170}, 'R': {'bar_x': 1046, 'text_x': 1130}}
MAXW = 720

ANA = ('Ana María Díaz González',
       'Dirección Especializada para los Delitos contra los Recursos Naturales y el Medio Ambiente (DEMA)')
CAMILO = ('Camilo Andrés González López',
          'Dirección Especializada contra las Organizaciones Criminales (DECOC)')


def cuadro(t):
    return CLIP0 + int(round(t * FPS))


def cita(t):
    """Una frase: negrita 46 si es corta, mediana 37 si es larga."""
    return [(t, 'bold', TIT, 0)] if len(t) <= 78 else [(t, 'med', CUE, 0)]


def tit_cue(titulo, cuerpo):
    return [(titulo, 'bold', TIT, 0), (cuerpo, 'med', CUE, GAP_TIT)]


def ante_tit(ante, titulo):
    return [(ante, 'med', ANTE, 0), (titulo, 'bold', TIT, GAP_ANTE)]


def act(icono, ante, titulo, cuerpo=None):
    return {'icono': icono, 'ante': ante, 'titulo': titulo, 'cuerpo': cuerpo}


ITEMS = [
    # clave, tipo, lado, t0, t1, contenido
    ('lt01_ana', 'lt', 'L', 3.0, 10.5, ANA),
    ('c01_dos_mundos', 'carton', 'L', 26.8, 37.6, cita(
        'Los delitos ambientales y el crimen organizado se investigaban como desde dos mundos '
        'que no se tocaban.')),
    ('lt02_camilo', 'lt', 'R', 39.0, 46.5, CAMILO),
    ('c02_macro', 'carton', 'L', 138.6, 146.0, cita(
        'Estábamos frente a una macrocriminalidad ambiental.')),
    ('c03_periferica', 'carton', 'L', 152.0, 162.0, cita(
        'Esto dejó de ser una conducta periférica para convertirse en el eje principal o '
        'estructural de las finanzas criminales.')),
    ('c04_corazon', 'carton', 'R', 171.8, 180.0, cita(
        'La afectación ambiental no es un daño colateral, es precisamente el corazón de su '
        'modelo de negocio.')),
    ('c05_rentas', 'carton', 'R', 184.6, 201.0, tit_cue(
        'Rentas tan altas o superiores a las del narcotráfico',
        'Históricamente tenían una menor persecución penal y una liquidez casi inmediata.')),
    ('c06_gravedad', 'carton', 'R', 211.2, 226.0, cita(
        'Perseguir el delito ambiental con un rigor tan fuerte que lográramos golpear el centro '
        'de gravedad financiero y logístico de esas estructuras criminales.')),
    ('c07_industrial', 'carton', 'L', 260.2, 268.0, cita(
        'Esto es una operación industrial perfectamente articulada.')),
    ('m01_frente1', 'mg_act', 'L', 272.4, 298.6, act(
        'mineria', 'Primer frente', 'La explotación ilícita de yacimientos mineros')),
    ('c08_mercurio', 'carton', 'L', 298.9, 307.0, cita(
        'Vertimiento indiscriminado de mercurio y de cianuro en esas grandes cuencas.')),
    ('c09_musculo', 'carton', 'L', 335.0, 347.0, cita(
        '¿Quién tiene el músculo financiero y quién tiene el control armado para meter diez '
        'retroexcavadoras en plena selva?')),
    ('c10_venia', 'carton', 'R', 350.0, 360.0, cita(
        'Ningún particular entra con maquinaria pesada a una zona de control de un grupo '
        'armado organizado sin la venia de sus comandantes.')),
    ('m02_organizacion', 'mg_lista', 'R', 368.6, 384.0, {
        'titulo': 'La organización',
        'filas': [('excavadora', 'Impone el cobro por máquina', 371.6),
                  ('bidon', 'Monopoliza el ingreso de miles de galones de combustible', 373.7),
                  ('oro', 'Regula la compraventa del oro', 377.7)]}),
    ('m03_frente2', 'mg_act', 'L', 412.3, 426.0, act(
        'tala', 'Segundo frente',
        'La deforestación y la invasión de áreas de especial importancia ecológica')),
    ('c11_motosierra', 'carton', 'L', 433.6, 447.8, cita(
        'Detrás de la motosierra o de los autores inmediatos, es una estrategia criminal.')),
    ('m04_talan', 'mg_lista', 'L', 448.0, 462.4, {
        'titulo': 'Talan para',
        'filas': [('ruta', 'Abrir corredores de movilidad', 449.7),
                  ('brote', 'Establecer cultivos de coca', 451.9),
                  ('vaca', 'La ganadería de forma extensiva', 459.7)]}),
    ('c12_baldios', 'carton', 'L', 462.6, 470.0, cita(
        'Apropiación ilícita de baldíos de la nación y lavado de activos.')),
    ('m05_frente3', 'mg_act', 'R', 481.0, 494.0, act(
        'casa_lote', 'Tercer frente',
        'El loteo y la urbanización ilegal en zonas de reserva o humedales periurbanos')),
    ('c13_fraccionan', 'carton', 'L', 526.0, 534.0, cita(
        'Fraccionan el terreno ilegalmente y lo venden a población vulnerable.')),
    ('c14_renta', 'carton', 'R', 571.5, 583.0, cita(
        'Destruyen el ecosistema, estafan, urbanizan ilegalmente, crean una renta fija '
        'permanente.')),
    ('m06_frente4', 'mg_act', 'R', 584.3, 596.5, act(
        'madera_fauna', 'Y a eso súmale',
        'Las redes estructurales de tráfico de madera fina, de fauna silvestre')),
    ('lt03_ana', 'lt', 'L', 597.6, 604.6, ANA),
    ('c15_aquiles', 'carton', 'L', 605.2, 613.0, cita(
        '¿Cuál es ese talón de Aquiles de la investigación tradicional?')),
    ('c16_fotografia', 'carton', 'R', 616.8, 624.6, cita(
        'Nos quedábamos en la fotografía del día del operativo.')),
    ('lt04_camilo', 'lt', 'R', 626.0, 633.0, CAMILO),
    ('c17_eslabon', 'carton', 'R', 637.6, 655.0, tit_cue(
        'Judicializábamos al eslabón reemplazable, fungible',
        'Los determinadores, los cabecillas, los financiadores, los testaferros seguían '
        'intactos.')),
    ('c18_cadena', 'carton', 'L', 678.8, 693.0, ante_tit(
        'Cambiamos la lógica',
        'La investigación estructural con enfoque de cadena de mando')),
    ('m07_eje1', 'mg_act', 'L', 701.8, 711.0, act(
        'lupa_doc', 'Primer eje',
        'La articulación de la prueba técnica y científica con la prueba del contexto criminal')),
    ('c19_prueba_reina', 'carton', 'L', 711.2, 716.2, cita(
        'En los delitos ambientales la prueba reina es técnica.')),
    ('m08_necesitamos', 'mg_lista', 'L', 716.4, 734.0, {
        'titulo': 'Necesitamos',
        'filas': [('brote', 'Caracterizaciones de tipo ambiental', 716.3),
                  ('matraz', 'Pruebas químicas de contaminación con mercurio', 720.0),
                  ('satelite', 'Análisis geomáticos e imágenes satelitales multitemporales', 723.9)]}),
    ('c20_orden', 'carton', 'L', 796.0, 813.5, [
        ('Interceptaciones telefónicas, agentes encubiertos, fuentes humanas, inteligencia '
         'militar y policial', 'med', CUE, 0),
        ('Probar quién dio la orden y qué estructura se benefició.', 'bold', TIT, GAP_TIT)]),
    ('m09_eje2', 'mg_act', 'R', 820.5, 832.0, act(
        'libro_ley', 'Segundo eje', 'La articulación dogmática y la imputación estratégica')),
    ('c21_concurso', 'carton', 'R', 844.2, 857.0, cita(
        'Los asociamos sistemáticamente en concurso con concierto para delinquir agravado, '
        'lavado de activos.')),
    ('m10_eje3', 'mg_act', 'L', 873.5, 888.0, act(
        'finanzas', 'Tercer eje', 'Una investigación financiera paralela')),
    ('c21b_origen', 'carton', 'L', 888.2, 895.5, cita(
        'Se estudia el origen de los recursos y el destino de los mismos.')),
    ('c22_colchon', 'carton', 'R', 913.4, 919.0, cita(
        'Ese dinero no se queda debajo del colchón.')),
    ('c23_uiaf', 'carton', 'R', 925.2, 935.0, cita(
        'Nos articulamos tempranamente con la UIAF, la DIAN, los colegas de lavado de activos, '
        'de extinción de dominio.')),
    ('c24_patrimonio', 'carton', 'R', 946.2, 956.0, cita(
        'Si no les quitamos ese patrimonio, realmente no desmantelamos las organizaciones '
        'criminales.')),
    ('c25_despachos', 'carton', 'L', 976.6, 983.0, cita(
        'Antes podíamos tener dos despachos investigando el mismo territorio sin saberlo.')),
    ('c26_teoria', 'carton', 'L', 1001.8, 1010.0, cita(
        'Unificamos el recaudo probatorio y construimos una teoría del caso mucho más sólida.')),
    ('c27_perito', 'carton', 'R', 1021.6, 1028.8, cita(
        'El fiscal de crimen organizado necesita la rigurosidad científica del perito '
        'ambiental.')),
    ('c28_arquitectura', 'carton', 'R', 1029.0, 1037.5, cita(
        'El fiscal ambiental necesita la arquitectura investigativa del crimen organizado.')),
    ('c29_diaco', 'carton', 'R', 1056.8, 1067.0, ante_tit(
        'DIACO',
        'Dirección de Apoyo a la Investigación y Análisis contra la Criminalidad Organizada')),
    ('c30_solitario', 'carton', 'L', 1093.4, 1100.0, cita(
        'La invitación para no investigar en solitario.')),
    ('c31_bolsillos', 'carton', 'L', 1115.4, 1128.0, cita(
        '¿Cuál estructura criminal controla ese territorio y a los bolsillos de quién estaría '
        'posiblemente llegando ese dinero?')),
    ('c32_proteccion', 'carton', 'R', 1130.0, 1145.0, cita(
        'La protección penal de nuestros recursos naturales es hoy por hoy una de las '
        'herramientas más poderosas para defender la vida, la seguridad territorial y el '
        'Estado de derecho en Colombia.')),
]


def revisar():
    """Sin solapes del mismo lado, en orden, y con tiempo para leer."""
    ultimo = {'L': -1, 'R': -1}
    for clave, tipo, lado, t0, t1, _c in ITEMS:
        assert t1 > t0, clave
        assert t0 >= ultimo[lado], 'solape en %s' % clave
        ultimo[lado] = t1
    n = sum(1 for i in ITEMS if i[1] != 'lt')
    cubre = sum(i[4] - i[3] for i in ITEMS)
    print('%d items (%d gráficos), %.0f s en pantalla' % (len(ITEMS), n, cubre))


if __name__ == '__main__':
    revisar()
