# -*- coding: utf-8 -*-
r"""VIDEO 06 · El caso Francisco (U4 L5). Narra Pilar. 26 ranuras.
La narración es la del libreto DOCUMENTO 1 - CASO FRANCISCO, literal, un
bloque por paso. Los títulos de los ocho pasos van en pantalla (mg_da), con
su subtítulo del libreto, al empezar cada bloque.

LO QUE EL LIBRETO PIDE Y NO SE DIBUJA (reglas de la serie)
    - las luces rojas y azules de la captura: la policía llega a pie, de día
    - el sello «CAPTURA EN FLAGRANCIA»: ningún texto en la imagen; el paso 1
      lo dice en el gráfico
    - los recuerdos del ataque a su hogar: la casa vacía, la puerta abierta,
      nadie; ninguna violencia, ningún cuerpo
    - el mazo del juez: el juez firma
    - el logo de Corpoamazonia: la técnica de la autoridad ambiental, sin nada
      escrito
El tránsito de lo punitivo a lo restaurativo lo cargan la luz (de la celda a
la selva) y la gente (del policía a la mesa redonda), no un cambio de color.

LA PROGRESIÓN
    r01-r03   paso 1: Francisco y el árbol · la patrulla · la flagrancia
    r04-r07   paso 2: la celda · el código · la audiencia · su cara
    r08-r11   paso 3 (gráfico del rompecabezas): la fiscal · la casa vacía ·
              solo · las monedas del empresario
    r12-r14   paso 4 (las tres preguntas): la fiscal en la ventana · el
              acopio de madera · la ventana de la celda
    r15-r17   paso 5: las seis tablas · la caracterización · la carpeta
    r18-r19   paso 6: la defensora · el equipo
    r20-r22   paso 7 (la balanza): las pruebas sobre la mesa · el vivero ·
              Francisco y la técnica
    r23-r24   paso 8: la mesa redonda · el juez avala
    r25-r26   el árbol nuevo · el Amazonas

R[n] = (cuadros, registro, gente, acento, fuego, lugar, escena)
"""

R = {}

R[1] = (100, 'dia', ('francisco',), None, False, 'amazonia_tala', '''
Medium-wide shot in the dense Amazon rainforest, the camera at standing
height, perfectly level, four metres from %(francisco)s. He cuts into the
trunk of a tall tree with a small chainsaw, leaning his weight into it, pale
sawdust flying from the cut; beside him on the ground lie exactly six freshly
sawn wooden planks, stacked. Very tall trees and vines all around.
''')

R[2] = (100, 'dia', ('policias',), None, False, 'amazonia_tala', '''
Medium-wide shot on a narrow forest path, the camera at standing height,
perfectly level: %(policias)s walk along the path toward the sound, pushing
aside a broad leaf; one of them carries a plain notebook. Daylight between
the tall trees. Calm; nobody runs.
''')

R[3] = (100, 'dia', ('francisco', 'policias'), None, False, 'amazonia_tala', '''
Medium-wide shot at the small clearing, the camera at standing height,
perfectly level: %(francisco)s stands beside the tree, the chainsaw now on
the ground at his feet, his empty hands open and lowered; in front of him
%(policias)s: one writes in the plain notebook, the other looks at the six
stacked planks. Nobody touches anybody.
''')

R[4] = (100, 'hero', ('francisco',), None, False, 'celda', '''
Medium shot of the holding room, the camera at standing height outside the
plain metal bars, perfectly level: %(francisco)s sits on the plain concrete
bench, his forearms on his knees, his hands loosely together, his eyes on
the floor; the flat daylight of the small high window falls on the wall
behind him.
''')

R[5] = (100, 'dia', ('fiscal',), None, False, 'despacho', '''
Medium close shot of %(fiscal)s at her desk, the camera at her seated eye
level from the side, perfectly level: she holds a thick plain law book open
in both hands, bound in plain dark grey cloth, and reads one article, her
pencil held between two fingers against the page.
''')

R[6] = (100, 'dia', ('jueza_gar', 'fiscal', 'francisco', 'defensora'), None, False, 'sala', '''
Wide shot of a small hearing room, the camera at standing height at the
back, perfectly level: %(jueza_gar)s at her plain desk on the low platform;
%(fiscal)s stands at the prosecution table reading from a plain sheet;
%(francisco)s sits at the defence table beside %(defensora)s, very still.
''')

R[7] = (100, 'dia', ('francisco',), None, False, 'sala', '''
Close shot of %(francisco)s alone at the defence table in the hearing room,
the camera at his seated eye level, perfectly level: his head and shoulders
fill the frame, his tired face, his eyes lowered to his hands folded on the
table, his mouth closed, a straight line. Behind him, soft and grey, the
plain wall of the room. ONLY ONE person in the picture.
''')

R[8] = (100, 'dia', ('fiscal',), None, False, 'despacho', '''
Medium shot of %(fiscal)s at her desk, the camera at seated height across the
desk, perfectly level: three plain cards are laid out in a row on the desk in
front of her and she holds a fourth card in her hand, above the gap at the
end of the row, not putting it down, her eyes on it.
''')

R[9] = (100, 'contra_ext', (), None, False, 'amazonia_tala', '''
Medium-wide shot of a small wooden house on stilts at the edge of the
forest, the camera at standing height, perfectly level: the plank door hangs
open, a hammock still tied inside, a pot on the cold hearth, a child's plain
sandal on the step; nobody there. The forest is quiet around it. Nothing
broken, nothing burned: only empty.
''')

R[10] = (100, 'contra_ext', ('francisco',), None, False, 'ninguno', '''
Medium shot on the plank pier of an Amazon river town, the camera at standing
height behind %(francisco)s, perfectly level: he sits alone at the end of
the pier, seen from behind, his shoulders down, looking at the wide brown
river and the forest on the far bank. This is the Colombian Amazon: a plain
plank pier, a few wooden boats, never a European harbour.
''')

R[11] = (100, 'hero', ('francisco', 'empresario'), None, False, 'madera', '''
Medium shot at the timber landing, the camera at standing height, perfectly
level: %(empresario)s stands in the shadow under a tin roof and drops a few
coins into the open palm of %(francisco)s, who stands in the light in front
of him, looking down at the coins. Stacks of sawn planks behind them.
''')

R[12] = (100, 'contra_ext', ('fiscal',), None, False, 'despacho', '''
Medium shot of %(fiscal)s standing at the window of her office, the camera at
standing height behind her shoulder, perfectly level: she holds her closed
folder against her chest and looks out at the green line of the forest
beyond the town roofs, thinking.
''')

R[13] = (100, 'hero', ('empresario',), None, False, 'madera', '''
Wide shot of the timber landing at dusk, the camera at standing height,
perfectly level: a long wooden riverboat piled high with sawn planks is tied
at the bank; %(empresario)s, a dark figure seen from behind under the tin
roof, watches two men carry planks aboard. The light is grey, never orange.
''')

R[14] = (100, 'hero', ('francisco',), None, False, 'celda', '''
Medium shot of the holding room, the camera at standing height inside,
perfectly level: %(francisco)s stands below the small high window, seen from
behind, and looks up at the square of grey daylight; the plain metal bars at
the side of the frame.
''')

R[15] = (100, 'dia', (), None, False, 'ninguno', '''
Medium shot of a plain evidence storage room of the prosecution service, the
camera at standing height, perfectly level: exactly six sawn wooden planks
lie stacked on a plain metal shelf, tied with plain string, a plain blank
grey tag hanging from the string; beside them a closed plain cardboard
folder. Plain painted walls. Nobody in the frame. Nothing legible anywhere.
''')

R[16] = (100, 'dia', ('francisco', 'social'), None, False, 'mesa_restaurativa', '''
Medium shot at a plain table, the camera at seated height, perfectly level:
%(social)s listens to %(francisco)s and writes in a plain folder; he speaks,
one hand open on the table; a glass of water in front of each of them.
''')

R[17] = (100, 'dia', (), None, False, 'ninguno', '''
Close top-down shot of an open plain cardboard folder on a plain desk, the
camera looking straight down: inside it, a few plain certificates covered in
plain grey bars, each with a plain round stamp shape and a signature line; a
small plain photograph of an empty wooden house on stilts clipped to the
first page; a plain pen beside the folder. No hand in the frame. Nothing
legible anywhere.
''')

R[18] = (100, 'dia', ('defensora', 'francisco'), None, False, 'mesa_restaurativa', '''
Medium shot at a plain table, the camera at seated height, perfectly level:
%(defensora)s sits beside %(francisco)s and explains a plain document of one
page laid on the table between them, her finger on one line; he follows her
finger with his eyes and nods slowly. Nothing legible on the page.
''')

R[19] = (100, 'dia', ('fiscal', 'colegas', 'defensora', 'francisco'), None, False, 'mesa_restaurativa', '''
Wide shot of the round table, the camera at standing height, perfectly level:
around it sit %(fiscal)s, %(colegas)s of the restorative justice unit,
%(defensora)s and %(francisco)s; the fiscal speaks with one hand open over
the table; the others listen. Glasses of water, plain folders.
''')

R[20] = (100, 'dia', ('fiscal',), None, False, 'despacho', '''
Medium shot of %(fiscal)s at her desk, the camera at seated height across the
desk, perfectly level: three plain case folders lie open side by side in
front of her; she rests both hands flat on the desk between them and looks
from one to the next, deciding.
''')

R[21] = (100, 'dia', (), None, False, 'ninguno', '''
Wide shot of a plant nursery of the regional environmental authority at the
edge of an Amazon town, the camera at standing height, perfectly level: long
rows of young native tree seedlings in plain black bags under a plain
shade net, a plain water hose, the green wall of the forest behind. Nobody in
the frame. No sign, no logo, no lettering anywhere. This is the Colombian
Amazon.
''')

R[22] = (100, 'dia', ('francisco', 'corpo'), None, False, 'ninguno', '''
Medium shot in the plant nursery under the plain shade net, the camera at
standing height, perfectly level: %(corpo)s hands %(francisco)s a young
seedling in a plain black bag; he takes it in both hands and looks at it.
Rows of seedlings around them, the forest behind. No sign, no logo, no
lettering anywhere.
''')

R[23] = (100, 'dia', ('francisco', 'corpo', 'fiscal'), None, False, 'mesa_restaurativa', '''
Medium shot at the round table, the camera at seated height, perfectly
level: %(francisco)s and %(corpo)s shake hands across the table, both half
standing; %(fiscal)s, seated beside them, watches with a plain signed
document in front of her. A window onto the green forest.
''')

R[24] = (100, 'dia', ('juez',), None, False, 'sala', '''
Medium shot of %(juez)s at his plain desk on the low platform of the hearing
room, the camera at seated height, perfectly level: he signs a plain
document of one page with a plain pen, his other hand flat on the page,
palm down, fingers together, thumb visible. No gavel anywhere.
''')

R[25] = (100, 'contra_ext', ('francisco',), None, False, 'amazonia_tala', '''
Medium-wide shot at the small clearing in the forest, the camera at standing
height, perfectly level: %(francisco)s kneels beside the old cut stump and
presses the earth around a young tree he has just planted, with both hands;
around him the forest is green and tall.
''')

R[26] = (100, 'aire', (), None, False, 'selva_aire', '''
High aerial view over the Colombian Amazon rainforest, the camera far above
looking down at a steep angle, the horizon level near the top: an unbroken
canopy of tree crowns in muted grey-green, a wide brown river winding through
it, low white mist lying over the water.
''')

NOMBRE = {1: 'el_arbol', 2: 'la_patrulla', 3: 'la_flagrancia', 4: 'la_celda',
          5: 'el_codigo', 6: 'la_audiencia', 7: 'su_cara', 8: 'las_piezas',
          9: 'la_casa_vacia', 10: 'solo', 11: 'las_monedas',
          12: 'la_ventana', 13: 'el_acopio', 14: 'la_luz', 15: 'las_tablas',
          16: 'la_caracterizacion', 17: 'la_carpeta', 18: 'la_defensora',
          19: 'el_equipo', 20: 'la_decision', 21: 'el_vivero',
          22: 'la_planta', 23: 'el_acuerdo', 24: 'el_aval',
          25: 'el_arbol_nuevo', 26: 'el_amazonas'}

CORTE = {
 1: ('m01_noticia', 'Nuestra noticia'),
 2: ('m01_noticia', 'El origen'),
 3: ('m01_noticia', 'Se sorprende'),
 4: ('m02_norma', 'El encuadre'),
 5: ('m02_norma', 'La norma seleccionada'),
 6: ('m02_norma', 'Se surten'),
 7: ('m02_norma', 'La norma encaja'),
 8: ('m03_hipotesis', 'Al construir'),
 9: ('m03_hipotesis', 'Francisco no es'),   # 7 nov: la casa vacía tenía 51
 10: ('m03_hipotesis', 'Perdió a su familia'),
 11: ('m03_hipotesis', 'Actuó bajo'),
 12: ('m04_objeto', 'Los interrogantes'),
 13: ('m04_objeto', 'Quién es'),
 14: ('m04_objeto', 'y Qué mecanismo'),
 15: ('m05_utilidad', 'La evidencia'),
 16: ('m05_utilidad', 'El elemento'),
 17: ('m05_utilidad', 'Documentamos'),
 18: ('m06_legalidad', 'La obtención'),
 19: ('m06_legalidad', 'y se suma'),
 20: ('m07_suficiencia', 'Con las pruebas'),
 21: ('m07_suficiencia', 'La ley nos ofrece'),
 22: ('m07_suficiencia', 'El objetivo'),
 23: ('m08_viabilidad', 'La viabilidad'),
 24: ('m08_viabilidad', 'El juez'),
 25: ('m09_precedente', 'Los hechos'),
 26: ('m09_precedente', 'sanación'),
}

# 7 nov: en minúscula y la ropa en positivo (lección de ED y del V03 r17: un
# token en mayúscula con «nothing written» al lado se imprime en la ropa)
EXTRA_TOKENS = {
 'francisco': ('a thin indigenous man of about forty-five from the Colombian '
               'Amazon, short straight black hair, a tired kind face, in a worn '
               'plain grey-white shirt and plain dark trousers, rubber boots'),
 # 7 nov (r03): salieron con escudo en la manga y funda en el cinto
 'policias': ('two patrolmen of the Colombian National Police in the dark '
              'olive-green patrol uniform of completely plain fabric, the '
              'sleeves plain from shoulder to cuff, a matte lime yellow-green '
              'vest with two plain grey reflective bands, a plain belt with '
              'nothing hanging from it, plain dark green caps, empty hands'),
 'jueza_gar': ('the judge of guarantees, a Colombian woman of about sixty, '
               'short curly grey hair, no glasses, in a plain black blazer over '
               'a plain grey blouse'),
 'social': ('a social worker of the prosecution service, a Colombian woman of '
            'about fifty, short dark hair, plain glasses, in a plain light '
            'grey cardigan'),
}

REF = {
 5: ('DA_V02_r02_la_eleccion', 'lugar', 'It is the SAME prosecutor in her SAME office.'),
 8: ('DA_V02_r02_la_eleccion', 'lugar', 'It is the SAME prosecutor at her SAME desk.'),
 20: ('DA_V02_r02_la_eleccion', 'lugar', 'It is the SAME prosecutor at her SAME desk.'),
 12: ('DA_V02_r02_la_eleccion', 'lugar', 'It is the SAME prosecutor in her SAME office.'),
 6: ('DA_V03_r03_la_solicitud', 'gente', 'The judge is the SAME woman; the prosecutor is the one of the first reference.'),
 24: ('DA_V02_r19_el_juicio', 'lugar', 'It is the SAME hearing room and the SAME judge, closer.'),
 2: (3, 'gente', 'The two patrolmen are the SAME men.'),
 3: (1, 'lugar', 'It is the SAME clearing and the SAME man.'),
 4: (1, 'gente', 'It is the SAME man.'),
 7: (6, 'lugar', 'It is the SAME hearing room; the man is the one of the first reference, much closer.'),
 10: (1, 'gente', 'It is the SAME man.'),
 11: (1, 'gente', 'It is the SAME man.'),
 14: (4, 'lugar', 'It is the SAME holding room and the SAME man.'),
 16: (1, 'gente', 'It is the SAME man.'),
 18: (1, 'gente', 'It is the SAME man.'),
 19: (18, 'gente', 'The defence lawyer and the man are the SAME; the prosecutor is the one of the first reference.'),
 22: (21, 'lugar', 'It is the SAME nursery; the man is the SAME as in the first reference.'),
 23: (19, 'lugar', 'It is the SAME round table and the SAME people.'),
 25: (1, 'lugar', 'It is the SAME clearing and the SAME man, months later.'),
 13: (11, 'lugar', 'It is the SAME timber landing, at dusk.'),
}
REF2 = {7: ('DA_V06_r01_el_arbol', 'THE INDIGENOUS MAN'), 6: 'DA_V01_r30_la_fiscal', 19: 'DA_V01_r30_la_fiscal',
        22: ('DA_V06_r01_el_arbol', 'THE INDIGENOUS MAN'), 23: 'DA_V01_r30_la_fiscal'}

ANCLA_DE = {4: 'noche_int', 9: 'rural', 10: 'pueblo', 15: 'oficina',
            16: 'oficina', 17: 'oficina', 21: 'rural', 26: 'rural'}

CON_PERSONA = {1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 16, 18, 19, 20,
               22, 23, 24, 25}
AEREOS = {26}
CENITALES = {17}
SOLO_MANOS = set()
TOPE_SIN_GENTE = 3
TOTAL = 2600
PIEZA = TOTAL + (182 + 119 + 48 + 119 + 182)

GRIS = (20, 110)
SIN_TECHO = {4, 14}

# los ocho pasos del libreto, cada uno al abrir su bloque (el 3 con el
# rompecabezas, el 4 con sus tres preguntas, el 7 con la balanza)
GRAFICOS = {1: 'paso1', 4: 'paso2', 8: 'paso3', 12: 'paso4', 15: 'paso5',
            18: 'paso6', 20: 'paso7', 23: 'paso8'}

KLING = {}
KLING_PRESTADO = {}
KLING_FIJA = 'Tripod shot: the camera stays where it is.'
KLING_AIRE = 'The camera moves only forward, smoothly, at the same height.'
KLING_FIN = ('Every movement travels all the way and arrives; nothing stops '
             'halfway. Keep the picture exactly as drawn in the first frame: the '
             'same flat graphic illustration with broad flat tonal planes, the '
             'same muted grey palette, the same people with the same faces.')
KLING_NEG = ('photorealistic, photograph, 3D render, texture, film grain, noise, '
             'ink outlines, colour shift, saturated colours, morphing, distorted '
             'face, extra people, extra hands, new objects, text, letters, logo, '
             'flag, weapon')


def comprobar():
    fallos = []
    tot = sum(v[0] for v in R.values())
    if sorted(R) != list(range(1, len(NOMBRE) + 1)):
        fallos.append('faltan ranuras')
    if tot != TOTAL:
        fallos.append('los cuadros suman %d y la rejilla dice %d' % (tot, TOTAL))
    racha = mejor = 0
    for i in sorted(R):
        racha = 0 if i in CON_PERSONA else racha + 1
        mejor = max(mejor, racha)
    if mejor > TOPE_SIN_GENTE:
        fallos.append('%d ranuras seguidas sin gente' % mejor)
    return fallos, tot, mejor

# --- 7 nov: cuadros medidos (cortes de Scribe sobre la voz masterizada:
# cada ranura entra 3 cuadros antes de la primera palabra de su CORTE; la
# ultima termina con el master)
CUADROS = {1: 172, 2: 102, 3: 232, 4: 157, 5: 85, 6: 138, 7: 175, 8: 127, 9: 107, 10: 111, 11: 163, 12: 225, 13: 64, 14: 193, 15: 82, 16: 154, 17: 236, 18: 230, 19: 276, 20: 169, 21: 227, 22: 137, 23: 301, 24: 95, 25: 203, 26: 78}
for _n, _c in CUADROS.items():
    R[_n] = (_c,) + R[_n][1:]
TOTAL = 4239
PIEZA = TOTAL + (182 + 119 + 48 + 119 + 182)
