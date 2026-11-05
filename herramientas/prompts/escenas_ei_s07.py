# -*- coding: utf-8 -*-
r"""SITUACIÓN 07 · La fosa clandestina · 9 ranuras · 973 cuadros. Narra Pilar.

LO QUE SE OYE ENCIMA
    r01-r02  la Fiscalía investiga la desaparición de varias personas |
             después de un operativo militar en una zona rural
    r03      una fuente informa sobre la posible existencia de una fosa
    r04-r05  durante las actuaciones iniciales, | los investigadores
             identifican restos humanos y algunas prendas de vestir
    r06-r07  también se obtiene información sobre fotografías y videos |
             publicados en redes sociales durante los días del operativo
    r08      una de las publicaciones muestra a personas que podrían
             corresponder a las víctimas
    r09      el fiscal debe orientar la obtención y conservación

LO QUE NO SE DIBUJA
    Ningún resto humano, hueso ni cuerpo: la fosa es la carpa blanca, la
    cuadrícula de cuerda, la lona y las manos enguantadas. Ni el operativo:
    los camiones se van, lejos. La fuente, protegida, sin cara. Las personas
    de la publicación: figuras grises pequeñas, sin rostro. El acento es el
    saco mostaza hallado, en su bolsa de evidencia (r05, r09).
"""

R = {}

R[1] = (74, 'dia', (), None, False, 'caserio', '''
Wide shot of the small rural hamlet in the morning, the camera at standing
height on the unpaved road, perfectly level. The road runs between a few
one-storey houses of brick and planks with zinc roofs; every door is closed,
an empty hammock hangs on a porch, a lone dog lies in the road. Forested
hills rise behind under low cloud. Nobody anywhere.
''')

R[2] = (104, 'dia', (), None, False, 'montana', '''
Very wide shot from a hillside above the same hamlet, the camera high,
perfectly level. On the mountain road below, three plain olive-green military
trucks with canvas covers drive away in a line around a bend, tiny in the
frame, a little dust behind them, no people visible. Mist in the folds of the
hills. No flag, no marking.
''')

R[3] = (129, 'hero', ('fuente', 'investigadora'), None, False, 'cocina', '''
Medium shot of the rural kitchen at night, the camera at seated height,
perfectly level. In the left foreground, %(fuente)s sits with his back to the
camera, a dark shape against the small oil lamp on the table; his right index
finger points at a sheet of paper on the table with a simple hand-drawn map
of plain lines -a path, a stream, a cross- and no letters. Across the table,
%(investigadora)s leans in and listens, writing in her notebook. The wood
stove glows faintly behind her. Each person appears ONCE.
''')

R[4] = (103, 'dia', ('forenses', 'antropologa'), None, False, 'claro', '''
Wide shot of the forest clearing, the camera at standing height at its edge,
perfectly level. Under tall trees, the plain white canopy tent; the ground in
front of it is marked out with a grid of plain white string on small wooden
stakes. %(forenses)s are at work: two kneel at the string grid with small
trowels, one carries a plain grey equipment case toward the tent, caught
mid-stride. At the left, %(antropologa)s stands directing, hood down, pointing
at the grid. Only earth, string and a grey tarpaulin: no bones, no remains,
no body. Each person appears ONCE.
''')

R[5] = (76, 'dia', ('antropologa',), 'saco', False, 'claro', '''
Close shot at chest height, perfectly level: two hands in plain blue-grey
gloves hold up a clear plastic evidence bag with a folded matte
mustard-yellow knitted sweater inside, earth on its folds, and a small plain
white tag with no writing. Behind, out of focus, the white tent and the trees.
Exactly two hands. No face.
''')

R[6] = (89, 'dia', ('analista',), None, False, 'lab_digital', '''
Medium shot of %(analista)s in the small dark digital analysis office,
three-quarter view, the camera at his seated eye level, perfectly level. He
sits close to two computer screens that fill with grids of small plain grey
thumbnail rectangles, his hand on the mouse, his face lit by the cool light
of the screens. Nothing on the screens is readable. He appears ONCE.
''')

R[7] = (103, 'dia', ('analista',), None, False, 'lab_digital', '''
Close shot at desk height, perfectly level: a man's hand holds a plain mobile
phone; its screen shows a social media post made only of plain grey shapes: a
small grey photograph of a mountain road with a few tiny distant grey figures
on it, no face readable, and plain grey bars below. The glow of the screen on
his fingers; the dark office behind. Exactly one hand. No face.
''')

R[8] = (130, 'dia', ('analista', 'fiscal_s07'), None, False, 'lab_digital', '''
Medium shot of the digital analysis office, the camera at standing height,
perfectly level. %(analista)s sits at the desk in three-quarter back view;
behind him %(fiscal_s07)s leans in over his shoulder and points at the larger
screen, where one photograph is enlarged: a mountain road with a small group
of distant grey figures, no faces, nothing readable. Both are lit by the
screen. Each person appears ONCE.
''')

R[9] = (165, 'dia', ('fiscal_s07',), 'saco', False, 'evidencia', '''
Medium shot of %(fiscal_s07)s in the evidence storage room, three-quarter
view, the camera at standing height, perfectly level. At the plain steel
table he lowers the sealed clear evidence bag with the folded mustard knitted
sweater into a plain open cardboard box, beside a second sealed bag with a
plain grey phone inside. Tall metal shelves of sealed boxes and bags with
blank white tags behind him. Flat white light. He appears ONCE.
''')

NOMBRE = {1: 'el_caserio', 2: 'el_operativo', 3: 'la_fuente', 4: 'el_claro',
          5: 'la_prenda', 6: 'el_analista', 7: 'la_publicacion',
          8: 'las_personas', 9: 'la_conservacion'}

CON_PERSONA = set(R) - {1, 2}
SILUETAS = {3}
CARTONES = {2, 3, 5, 7, 8, 9}
CENITALES = set()
SOLO_MANOS = {5, 7}
SIN_CARA = set()
TOPE_SIN_GENTE = 3
TOTAL = 973
PIEZA = TOTAL + (182 + 119 + 48 + 119 + 182)

HOJAS = {6: ['analista'], 8: ['analista', 'fiscal_s07'], 9: ['fiscal_s07']}

ANCLAS = {1, 3, 4, 6, 9}

REF_PLACA = {
 1: (['EI_ANCLA_rural'], 'estilo', ''),
 3: (['EI_ANCLA_noche_int'], 'estilo', ''),
 4: (['EI_ANCLA_rural'], 'estilo', ''),
 6: (['EI_ANCLA_noche_int'], 'estilo', ''),
 9: (['EI_ANCLA_oficina'], 'estilo', ''),
 2: (['EI_S07_r01_el_caserio'], 'lugar', 'It is the SAME mountains, seen from higher up. '),
 5: (['EI_S07_r04_el_claro'], 'lugar', ''),
 7: (['EI_S07_r06_el_analista'], 'lugar', ''),
 8: (['EI_S07_r06_el_analista'], 'lugar', 'It is the SAME office and the SAME analyst. '),
}

REUSA = {}
DET = {}
BROLL = {}

MOV = {
 2: 'kling: los camiones se alejan por la carretera; la niebla',
 4: 'kling: el equipo forense trabaja; uno camina con la caja',
 6: 'kling: el analista desplaza la pantalla; la luz de las pantallas cambia',
 8: 'kling: el fiscal se inclina y señala la pantalla',
 9: 'kling: el fiscal baja la bolsa a la caja',
}

LOWER_THIRD = {}


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
    if len(CENITALES) > 3:
        fallos.append('%d cenitales' % len(CENITALES))
    if set(LOWER_THIRD) & CARTONES:
        fallos.append('rotulo y carton en la misma ranura')
    for (n, _), d in DET.items():
        if (d['entra'] < 60 and not d.get('abre')) or d['entra'] + d['cuadros'] > R[n][0]:
            fallos.append('detalle r%02d fuera de su ranura' % n)
    return fallos, tot, mejor
