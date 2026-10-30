# -*- coding: utf-8 -*-
r"""UNIDAD 4 «Culminamos la situación con diversas reflexiones» · 35 ranuras
· pieza 6984.

LO QUE SE OYE ENCIMA (resumen; el cruce completo en cruce_jr.json)
    r01-02  el agua terminada; otro cafe?       r03-05  para que la JR?
    r06-07  el cafe, el libro de Thiebaut        r08-13  primer fragmento
    r14-16  mas practico; otro fragmento         r17-23  segundo fragmento
    r24-26  muy fuerte; la voluntariedad         r27-28  el camino, los
                                                        mediadores
    r29-33  la Divina Comedia, Dante y Virgilio  r34-35  se rien; se levanta

LA OFICINA AL CAER LA TARDE
    La misma oficina, la tercera vez, con la luz baja de la tarde entrando
    casi horizontal por la ventana de la izquierda: planos largos de luz y
    sombra, y en varias placas la ventana es lo unico claro (`contraluz`).
    Sobre la mesa: el vaso vacio, el libro de tapa gris, la taza, el termo.
    La camara sigue siendo «usted»; del fiscal se ven las manos (el cafe,
    el libro, la pagina) y, sobre el hombro, la espalda.

LO QUE SE RECUERDA O SE PIENSA, EN OTRO REGISTRO
    La silla vacia del que no vino (r10, r21); dos personas, una junto al
    doliente (r11); un hombre volviendo a colgar una puerta (r17, r18); el
    camino con dos figuras (r27); las tres sillas de una mediacion (r28);
    la bajada a oscuras (r30) y la subida hacia la luz con el guia adelante
    (r32, r33). Sin horrores dibujados: la oscuridad y la profundidad
    bastan.

PLACAS: 24 · REUSOS: r04<-r03, r05<-r01, r09<-r03, r13<-r08, r15<-r14,
r16<-r07, r18<-r17, r19<-r01, r21<-r10, r24<-r03, r33<-r32.
"""

TARDE = ('Late afternoon: the light from the window on the left comes in '
         'low and almost horizontal, laying long planes of light and shadow '
         'across the desk and the wall; the brightest value is still a light '
         'grey, not white.')

R = {}

R[1] = (222, 'dia', ('juana', 'fiscal'), None, False, 'oficina', '''
Medium shot across the plain grey desk, the camera at seated eye level on
the prosecutor's side, perfectly level, as if we were the prosecutor. In
the lower foreground, out of focus, the prosecutor's own two hands in
plain light grey shirt cuffs resting on the desk.

%(juana)s sits in the visitor chair on the far side, her handbag on her
lap, her hands on it, her eyes down and a little to one side, on nothing;
her mouth closed, her brows level. In front of her on the desk the plain
glass, now EMPTY, and beside it the white cup; on the prosecutor's side of
the desk a plain grey hardcover book, closed, with no lettering on it.
''' + TARDE + '''
''')

R[2] = (155, 'dia', ('juana',), None, False, 'oficina', '''
Close shot of the empty plain glass on the plain grey desk, the camera at
desk height, perfectly level, the glass in the left third of the frame
with one bright edge of low light on its rim and a long shadow behind it.
Beyond it, in focus, %(juana)s's right hand raised a little above the
handbag with the palm turned out toward the camera, the small gesture of
«no, thank you»; her other hand on the bag; no face in frame. The cuff of
the grey coat. ''' + TARDE + '''
''')

R[3] = (146, 'dia', ('juana',), None, False, 'oficina', '''
Close shot of %(juana)s's face and shoulders in three-quarter view across
the desk, the camera at seated eye level, perfectly level, as if we were
the prosecutor, the window soft behind her on the left. She is about to
ask something and has not yet: her mouth closed, her brows a little drawn,
her eyes on the camera, steady. The low light from the left on one side of
her face and the scarf; the other side in soft shadow built from flat
tonal planes.
''')

R[4] = (104, 'dia', ('juana',), None, False, 'oficina', '''
(reusa r03: Juana de cerca, otro encuadre)
''')

R[5] = (108, 'dia', ('juana', 'fiscal'), None, False, 'oficina', '''
(reusa r01: Juana del otro lado, otro encuadre)
''')

R[6] = (159, 'dia', ('fiscal',), False, False, 'oficina', '''
High three-quarter shot of the prosecutor's side of the desk, the camera at
the height of the prosecutor's own eyes looking down at the hands,
perfectly level.

%(fiscal)s's two hands: the left holds the plain white cup steady on the
desk, the right pours from a plain grey thermos flask into it, the thin
stream of coffee caught mid-pour. Beside the cup, the plain grey hardcover
book, closed, no lettering. A plain grey pen, the plain grey notebook.
Exactly two hands, both in plain light grey shirt cuffs; no face.
''' + TARDE + '''
''')

R[7] = (158, 'dia', ('fiscal',), False, False, 'oficina', '''
High three-quarter shot of the desk from the prosecutor's eyes, the camera
looking down at the hands, perfectly level.

%(fiscal)s's two hands open the plain grey hardcover book on the desk: the
left hand holds the cover open, the right hand holds a page half turned.
The pages carry only plain flat grey bars, no readable character anywhere;
the cover is plain grey with no title. The white cup with coffee beside
the book, steam faintly rising. Exactly two hands; no face. ''' + TARDE + '''
''')

R[8] = (280, 'dia', ('fiscal', 'juana'), None, False, 'oficina', '''
Medium shot across the desk, the camera at seated eye level on the
prosecutor's side, perfectly level, as if we were the prosecutor.

In the lower foreground, sharp, %(fiscal)s's two hands hold the open book
up a little off the desk, its pages of plain flat grey bars toward the
camera's side, tilted so that we read over them. Beyond the book,
%(juana)s in the visitor chair listens: her hands on her handbag, her head
a little inclined, her eyes on the book, her mouth closed. The empty glass
and the cup on the desk. ''' + TARDE + '''
''')

R[9] = (103, 'dia', ('juana',), None, False, 'oficina', '''
(reusa r03: Juana de cerca, segundo encuadre)
''')

R[10] = (255, 'contraluz', (), False, False, 'oficina', '''
Medium shot of a plain corridor in a public building at the end of the
day, the camera at seated height, perfectly level, looking along the wall
toward a window at the far end: the window is the only bright thing in
the picture, and the corridor nearer the camera is in shadow.

Against the wall, a row of three plain metal chairs; the nearest one, in
the foreground, is EMPTY and turned a little toward the camera, its seat
catching a thin edge of light. The other two also empty. Nobody in the
corridor, no bag, no coat, nothing left on any chair.

What the camera asserts: the chair of the one who could not come.
''')

R[11] = (252, 'contraluz', (), False, False, 'recuerdo', '''
Medium shot of two people seated side by side on a plain bench against a
plain wall, the camera at seated height to one side, perfectly level. A
single window high on the left is the only light, and the two figures read
as dark planes with light along their edges, their faces not drawn.

The one on the right sits bent forward with the forearms on the knees and
the head lowered. The one on the left sits upright, turned a little toward
the first, with one hand resting flat on the other's back between the
shoulder blades, and stays there. Nobody speaks. Nothing else in the
room.
''')

R[12] = (170, 'dia', ('fiscal',), False, False, 'oficina', '''
Close shot of the open book on the plain grey desk, the camera at desk
height looking slightly down, perfectly level: the two pages of plain flat
grey bars fill the frame, and %(fiscal)s's right index finger rests on one
line of the left page, the plain light grey shirt cuff at the wrist. The
low light from the left lays a bright plane across the page and a soft
shadow of the finger beside it. Exactly one hand; no face; no readable
character anywhere.
''')

R[13] = (144, 'dia', ('fiscal', 'juana'), None, False, 'oficina', '''
(reusa r08: leyendo, otro encuadre)
''')

R[14] = (147, 'dia', ('juana', 'fiscal'), None, False, 'oficina', '''
Medium shot across the desk, the camera at seated eye level on the
prosecutor's side, perfectly level, as if we were the prosecutor; the
prosecutor's hands and the edge of the book out of focus at the bottom.

%(juana)s has sat back in the visitor chair and raised her right hand with
the palm toward the camera at shoulder height, fingers together: «wait,
enough». Her head a little back, her brows up, her mouth closed. The left
hand still on the handbag. ''' + TARDE + '''
''')

R[15] = (114, 'dia', ('juana', 'fiscal'), None, False, 'oficina', '''
(reusa r14: la mano alzada, mas cerca)
''')

R[16] = (144, 'dia', ('fiscal',), False, False, 'oficina', '''
(reusa r07: las manos abren el libro, otro encuadre)
''')

R[17] = (251, 'contraluz', (), False, False, 'barrio', '''
Medium-wide shot of a plain house doorway on a Colombian street in the
early morning, the camera at standing height on the pavement, perfectly
level. The sky in the open doorway and over the street is the only bright
thing; the facade and the figure read as dark planes with edges of light.

A man stands in the doorway with his back to the camera, holding a plain
wooden door upright with both hands by its edge, its top hinge a hand's
width from the hinge plate on the frame, mid-lift: he is hanging the door
back on its hinges. A plain toolbox open on the step beside his feet. His
face is not visible. Nobody else in the street.

What the camera asserts: a thing being put back where it was.
''')

R[18] = (255, 'contraluz', (), False, False, 'barrio', '''
(reusa r17: la puerta, mas cerca)
''')

R[19] = (157, 'dia', ('juana', 'fiscal'), None, False, 'oficina', '''
(reusa r01: Juana del otro lado, abierto)
''')

R[20] = (180, 'contraluz', (), False, False, 'oficina', '''
Medium shot of the office window from inside, the camera at seated height,
perfectly level, square to the window, the glass the only bright thing in
the picture: through it the flat roofs and the far mountains under a pale
late sky, soft. On the sill, the empty plain glass, catching one edge of
light. The wall around the window and the sill in shadow. Nobody in
frame.
''')

R[21] = (295, 'contraluz', (), False, False, 'oficina', '''
(reusa r10: la silla vacia, mas cerca)
''')

R[22] = (145, 'contraluz', ('juana',), None, False, 'oficina', '''
Medium-close shot of %(juana)s in the visitor chair, in PROFILE, facing the
window on the left, the camera at seated eye level across the desk,
perfectly level. The window is the only bright thing in the picture: her
profile reads as a dark plane with the light along the edge of the brow,
the nose and the lips, the ends of the scarf lit on one side; her eyes
open, on the window; her mouth closed. The desk and the room nearer the
camera in shadow.
''')

R[23] = (230, 'dia', ('fiscal',), False, False, 'oficina', '''
High three-quarter shot of the desk from the prosecutor's eyes, the camera
looking down at the hands, perfectly level.

%(fiscal)s's two hands close the plain grey hardcover book: the right hand
brings the cover down, the last few centimetres from the pages, the left
hand flat on the desk beside it. The cover plain grey with no lettering.
The white cup, the empty glass beyond, the long low light across the desk.
Exactly two hands; no face.
''')

R[24] = (131, 'dia', ('juana',), None, False, 'oficina', '''
(reusa r03: Juana de cerca, tercer encuadre)
''')

R[25] = (156, 'dia', ('juana', 'fiscal'), None, False, 'oficina', '''
Medium shot across the desk, the camera at seated eye level on the
prosecutor's side, perfectly level, as if we were the prosecutor.

%(juana)s leans forward with both forearms on the edge of the desk, her
hands clasped, her shoulders up a little: her eyes on the camera, her
brows drawn, her mouth closed hard. The handbag has slipped to her feet.
The empty glass by her hands. ''' + TARDE + '''
''')

R[26] = (262, 'dia', ('fiscal', 'juana'), None, False, 'oficina', '''
Over-the-shoulder shot across the desk, the camera at seated eye level just
behind and above the prosecutor's left shoulder, perfectly level.

In the right foreground, large and out of focus, %(fiscal)s from BEHIND:
the back of a head of short dark hair, the shoulder of a plain charcoal
grey jacket, nothing of the face. Beyond, in focus, %(juana)s sitting
forward, listening, her hands clasped on the desk edge, her eyes on the
prosecutor. The book closed on the desk, the cup, the empty glass.
''' + TARDE + '''
''')

R[27] = (155, 'hero', (), False, True, 'recuerdo', '''
Wide shot of a narrow path across open ground at dusk, the camera at
standing height on the path, perfectly level. One weak pale light low on
the far horizon is the only light; the ground falls away into near-black
on both sides of the path, which is a faint lighter line.

On the path, walking away from the camera toward that light, two figures
as solid dark SILHOUETTES, one a step ahead of the other, the one ahead
with an arm reaching back so that the two are joined hand to hand. Nothing
else in the picture.
''')

R[28] = (220, 'dia', (), False, False, 'oficina', '''
Medium shot of a plain room with a plain grey floor and plain walls, the
camera at seated height, perfectly level. Three plain chairs stand in the
middle of the room arranged in a loose triangle, facing one another, each
a little apart from the others, all EMPTY; a small plain table with a plain
jug of water and three plain glasses to one side. Low afternoon light from
a window on the right lays long shadows of the chairs across the floor.
Nobody in the room.
''')

R[29] = (165, 'dia', ('juana', 'fiscal'), None, False, 'oficina', '''
Medium shot across the desk, the camera at seated eye level on the
prosecutor's side, perfectly level, as if we were the prosecutor.

%(juana)s has sat back again; one hand has gone to the scarf at her neck
and holds it; a small closed-mouth smile, the first easy one, her eyes on
the camera with the brows a little up: remembering school. The other hand
on the handbag, back on her lap. ''' + TARDE + '''
''')

R[30] = (259, 'hero', (), False, True, 'recuerdo', '''
Wide shot looking down a wide stone stair that descends into darkness,
the camera at standing height at the top of the stair, perfectly level.
One weak pale light far below, at the bottom, is the only light, and the
walls of the stair fall away into near-black on both sides; nothing is
drawn in that dark, no figure, no face, no shape.

Halfway down, two figures as solid dark SILHOUETTES against the weak light
below: one a step ahead, turned back with an arm raised toward the other,
the other a step behind. Nothing else in the picture.
''')

R[31] = (150, 'dia', ('juana',), None, False, 'oficina', '''
Close shot of %(juana)s's face and shoulders in three-quarter view across
the desk, the camera at seated eye level, perfectly level, as if we were
the prosecutor. Her head tilted to one side, one eyebrow higher than the
other, her mouth a little open: she does not see what this has to do with
anything. The low light from the left on the scarf and one side of the
face.
''')

R[32] = (189, 'contraluz', (), False, True, 'recuerdo', '''
Wide shot looking up a narrow rock stair that climbs toward an opening of
pale daylight above, the camera at standing height at the bottom of the
stair, perfectly level. The opening at the top is the only bright thing
in the picture; everything nearer the camera is deep shadow.

On the stair, climbing toward the light, two figures as solid dark
SILHOUETTES: the one ahead has stopped a few steps up and turned back,
reaching a hand down to the one behind, who reaches up; the two hands are
about to meet in the light. Nothing else in the picture.
''')

R[33] = (189, 'contraluz', (), False, True, 'recuerdo', '''
(reusa r32: la subida, mas cerca)
''')

R[34] = (109, 'dia', ('juana', 'fiscal'), None, False, 'oficina', '''
Medium shot across the desk, the camera at seated eye level on the
prosecutor's side, perfectly level, as if we were the prosecutor.

%(juana)s laughs: her head back a little, her eyes narrowed with it, an
open smile showing a line of teeth, one hand flat on her chest over the
scarf. The handbag on her lap. The book closed on the desk, the cup, the
empty glass. ''' + TARDE + '''
''')

R[35] = (175, 'dia', ('juana', 'fiscal'), None, False, 'oficina', '''
Medium-wide shot across the desk, the camera at seated eye level on the
prosecutor's side, perfectly level, as if we were the prosecutor.

%(juana)s is standing up from the visitor chair: her weight already on her
feet, her knees still a little bent, one hand on the chair's armrest and
the other holding the handbag's handles, her body half turned toward the
door on the right, her face still toward the camera with a small
closed-mouth smile. The chair pushed back behind her. On the desk the
closed book, the cup, the empty glass. ''' + TARDE + '''
''')

NOMBRE = {1: 'el_vaso_vacio', 2: 'no_gracias', 3: 'juana_cerca', 4: 'juana_cerca_b',
          5: 'el_vaso_vacio_b', 6: 'el_cafe', 7: 'el_libro', 8: 'leyendo',
          9: 'juana_cerca_c', 10: 'la_silla_vacia', 11: 'junto_al_doliente',
          12: 'la_pagina', 13: 'leyendo_b', 14: 'mas_practico',
          15: 'mas_practico_b', 16: 'el_libro_b', 17: 'la_puerta',
          18: 'la_puerta_b', 19: 'el_vaso_vacio_c', 20: 'la_ventana',
          21: 'la_silla_vacia_b', 22: 'juana_contraluz', 23: 'cierra_el_libro',
          24: 'juana_cerca_d', 25: 'juana_adelante', 26: 'sobre_el_hombro',
          27: 'el_camino', 28: 'tres_sillas', 29: 'juana_sonrie',
          30: 'la_bajada', 31: 'juana_confundida', 32: 'la_subida',
          33: 'la_subida_b', 34: 'juana_rie', 35: 'se_levanta'}

REUSA = {
 4: (3, dict(encuadre=1.0, empuje=0.0, centro=[0.5, 0.5])),
 5: (1, dict(encuadre=0.78, empuje=0.04, centro=[0.5, 0.45])),
 9: (3, dict(encuadre=0.76, empuje=0.04, centro=[0.5, 0.45])),
 13: (8, dict(encuadre=0.76, empuje=0.03, centro=[0.55, 0.42])),
 15: (14, dict(encuadre=0.76, empuje=0.04, centro=[0.5, 0.45])),
 16: (7, dict(encuadre=0.76, empuje=0.04, centro=[0.5, 0.5])),
 18: (17, dict(encuadre=0.76, empuje=0.05, centro=[0.5, 0.45])),
 19: (1, dict(encuadre=1.0, empuje=0.0, centro=[0.5, 0.5])),
 21: (10, dict(encuadre=0.76, empuje=0.05, centro=[0.4, 0.55])),
 24: (3, dict(encuadre=0.78, empuje=0.03, centro=[0.55, 0.45])),
 33: (32, dict(encuadre=0.76, empuje=0.05, centro=[0.5, 0.4])),
}

CON_PERSONA = {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19,
               22, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 35}
SILUETAS = {27, 30, 32, 33}
CARTONES = {1, 3, 7, 8, 10, 12, 13, 17, 19, 20, 22, 23, 26, 27, 28, 30, 32, 35}
CENITALES = set()
SOLO_MANOS = {2, 6, 7, 12, 16, 23}
SIN_CARA = {11, 17, 18}
TOPE_SIN_GENTE = 3
PIEZA = 6984
TOTAL = PIEZA - (182 + 119 + 48 + 119 + 182)

HOJAS = {1: ['juana'], 2: ['juana'], 3: ['juana'], 8: ['juana'], 14: ['juana'],
         22: ['juana'], 25: ['juana'], 26: ['juana'], 29: ['juana'],
         31: ['juana'], 34: ['juana'], 35: ['juana']}

DET = {
 (8, 'la_pagina_que_pasa'): dict(cuadros=72, entra=150, registro='dia',
     personas=('fiscal',),
     escena='Close shot of two hands in plain light grey shirt cuffs holding '
            'an open plain grey hardcover book, the right hand holding the '
            'corner of the right page lifted a little; pages of plain flat '
            'grey bars; low afternoon light from the left.',
     gesto='The right hand turns the page over to the left and lays it flat, '
           'and both hands hold the book still. Nothing else moves.'),
 (26, 'las_manos_de_juana'): dict(cuadros=72, entra=130, registro='dia',
     personas=('juana',),
     escena='Close shot of a woman\'s two hands clasped on the edge of a plain '
            'grey desk, the cuffs of a grey coat at the wrists, low afternoon '
            'light from the left; beside them an empty plain glass.',
     gesto='The clasped hands tighten a little, the thumbs cross, and hold. '
           'Nothing else moves.'),
 (20, 'la_luz_baja'): dict(cuadros=72, entra=60, registro='contraluz',
     personas=(),
     escena='Close shot of the empty plain glass on the window sill against '
            'the pale late sky, one bright edge of light on its rim.',
     gesto='Nothing in the frame moves except the light, which dims slowly '
           'and evenly as the sun goes lower.'),
}

BROLL = {}

MOV = {
 6: 'kling: el cafe termina de caer y el termo se endereza; la taza quieta',
 17: 'kling: la puerta sube los ultimos centimetros y entra en la bisagra',
 20: 'luz: baja la tarde (sin modelo)',
 32: 'kling: la mano de abajo sube y la de arriba la toma; las figuras quietas',
 35: 'kling: Juana termina de levantarse y se queda de pie (cara quieta)',
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
    for n, (m, _c) in REUSA.items():
        if m in REUSA or m not in R:
            fallos.append('r%02d reusa r%02d, que no es placa madre' % (n, m))
    return fallos, tot, mejor
