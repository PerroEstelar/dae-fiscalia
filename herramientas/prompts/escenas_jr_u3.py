# -*- coding: utf-8 -*-
r"""UNIDAD 3 «Prosigue la situación reflexiva» · 32 ranuras · pieza 6571.

LO QUE SE OYE ENCIMA (resumen; el cruce completo en cruce_jr.json)
    r01-02  Juana agradece; piensa en su primo    r03-04  el vaso; el perdon?
    r05-06  Van Gogh; el pie de foto              r07     Rubiano, la revista
    r08-16  la historia del jardin                r17-18  es una broma?
    r19-22  exigir el perdon a la fuerza; encontrarse; no tiene que
    r23     «Lea esto», el celular, Hillman       r24-31  la cita de Hillman
    r32     Juana termina de leer; silencio

LA OFICINA AL MEDIODIA, Y TRES RECUERDOS
    La misma oficina de la U2, al mediodia: la luz entra mas alta y mas
    plana por la misma ventana de la izquierda. Juana en la misma silla;
    sobre la mesa, ahora, el vaso de agua. La camara sigue siendo «usted».
    Lo recordado va en `hero` y `contraluz`: el hombre cansado (Van Gogh),
    la calle con jardines y el jardin de la historia de Rubiano.

EL JARDIN: LO QUE SE DIBUJA Y LO QUE NO
    La madre y el nino juegan (r08); el hombre esta en la reja, de
    espaldas (r09); el cuarto sin jardin de su infancia (r10); la mano de
    la madre en el hombro del nino (r12); el jardin desde la puerta (r14);
    la reja abierta y la madre sola (r16). El hombre NUNCA toca al nino en
    imagen, y el nino no se dibuja llevado por nadie: la r16 es la madre
    sola en la reja abierta, mirando la calle.

PLACAS: 22 · REUSOS: r04<-r03, r06<-r05, r11<-r08, r13<-r09, r15<-r12,
r19<-r01, r20<-r18, r26<-r24, r28<-r25, r30<-r05.
"""

MEDIODIA = ('Midday: the light from the window on the left comes in higher '
            'and flatter than in the morning, a short bright plane on the '
            'desk and soft shadows.')

R = {}

R[1] = (228, 'dia', ('juana', 'fiscal'), None, False, 'oficina', '''
Medium shot across the plain grey desk, the camera at seated eye level on
the prosecutor's side, perfectly level, as if we were the prosecutor. In
the lower foreground, out of focus, the prosecutor's own two hands in
plain light grey shirt cuffs, resting on the desk either side of a plain
grey notebook.

%(juana)s sits in the visitor chair on the far side, her handbag on her
lap, her hands on it, her head a little lowered: her eyes are down on her
own hands, not on the camera; her mouth closed; her brows level. She is
thinking about someone who is not in the room. On the desk a plain glass
of water, full, and a plain white cup. ''' + MEDIODIA + '''
''')

R[2] = (212, 'dia', ('juana',), None, False, 'oficina', '''
Close shot of %(juana)s's two hands on the plain grey handbag in her lap,
the camera at desk height looking slightly down across the desk edge,
perfectly level. One hand lies over the other; the upper hand's fingers
have closed on the strap of the bag and the knuckles stand out a little.
The grey coat and the ends of the mustard scarf hang into the frame from
above. No face in frame; exactly two hands. ''' + MEDIODIA + '''
''')

R[3] = (123, 'dia', ('juana', 'fiscal'), None, False, 'oficina', '''
Medium shot across the desk, the camera at seated eye level on the
prosecutor's side, perfectly level, as if we were the prosecutor; the
prosecutor's hands out of focus at the bottom edge.

%(juana)s sits forward in the visitor chair holding the plain glass of
water in her right hand, raised halfway between the desk and her mouth,
stopped there; her left hand on the handbag. Her eyes on the camera, her
mouth a little open on the first word of a question, her brows up a
little. The water in the glass is still. ''' + MEDIODIA + '''
''')

R[4] = (242, 'dia', ('juana', 'fiscal'), None, False, 'oficina', '''
(reusa r03: Juana con el vaso, mas cerca)
''')

R[5] = (97, 'hero', (), False, False, 'recuerdo', '''
Medium shot of an old man seated on a plain wooden chair in a bare room,
the camera at the height of the seat, perfectly level, to one side so that
he is seen in three-quarter view.

He sits bent forward with his elbows on his knees and his face hidden in
both hands, his fingers in his thin grey hair, his bare feet flat on the
floor; a plain shirt and plain trousers, worn. One weak light from a small
window high on the far wall is the only light, laying a pale plane on the
floor beside the chair; everything else falls away into near-black. A
drawing of exhaustion, not of grief: his back is simply too tired to
straighten. His face is not visible.
''')

R[6] = (150, 'hero', (), False, False, 'recuerdo', '''
(reusa r05: el hombre cansado, mas cerca)
''')

R[7] = (227, 'contraluz', (), False, False, 'jardin', '''
Wide shot of a quiet residential street of single-storey houses in a
Colombian town, late in the afternoon, the camera at standing height in
the middle of the empty street, perfectly level, looking along it toward
the low sun hidden behind the far houses: the sky at the end of the street
is the only bright thing, and the houses and their small front gardens
nearer the camera sit in shadow. Low painted garden walls with simple
metal gates, patches of plain lawn, plain rendered facades. Nobody in the
street.

What the camera asserts: a street from a story, remembered more than seen.
''')

R[8] = (222, 'contraluz', (), False, False, 'jardin', '''
Wide shot of a small front garden in front of a single-storey house, seen
from the street over the low garden wall, the camera at standing height,
perfectly level. The low sun is behind the house, so the sky above the
roof is the only bright thing and the garden and the figures read as dark
planes with light along their edges.

On the plain lawn a woman crouches with her arms open and a small boy of
about five runs toward her, mid-stride, a plain ball on the grass behind
him; both are dark shapes against the light, their faces not drawn. At the
far right of the frame, by the open metal gate, a man stands with his back
to the camera, still, hands at his sides, a tall dark shape. He is three
metres from the child and touches nobody.
''')

R[9] = (151, 'contraluz', (), False, False, 'jardin', '''
Medium shot in the same front garden, the camera at chest height just
behind the man's shoulder, perfectly level, the bright sky over the house
the only light in the picture.

In the left foreground, large and out of focus, the back of the man's head
and shoulder, a dark shape. Facing him across two metres of lawn, the
mother, standing now, upright, her arms at her sides, her face a dark plane
against the light with no feature drawn; the small boy stands half behind
her leg, one of his hands holding her hand, his face hidden against her.
The man's hands are not in the frame. Nobody touches the child but the
mother.
''')

R[10] = (151, 'hero', (), False, False, 'recuerdo', '''
Medium shot of a small bare room, the camera low at the height of a child's
eyes, perfectly level, looking at a single plain window in a plain wall.

Through the window: not a garden, only the flat grey wall of the next
building, a metre away. The window's weak grey light is the only light in
the picture and lays a small square on the bare floor; everything else
falls away into near-black. A plain small chair against the wall. Nobody
in the room.

What the camera asserts: where there was no garden.
''')

R[11] = (233, 'contraluz', (), False, False, 'jardin', '''
(reusa r08: el jardin, otro encuadre)
''')

R[12] = (207, 'contraluz', (), False, False, 'jardin', '''
Close shot of a woman's hand resting on a small boy's shoulder, the camera
at the child's shoulder height, perfectly level, the bright sky behind
them the only light; the hand and the shoulder read as dark planes with
light along their edges. The boy's plain T-shirt, the sleeve of the
mother's plain blouse. The fingers of the hand have closed a little on the
shoulder. Exactly one hand in the frame; no face.
''')

R[13] = (131, 'contraluz', (), False, False, 'jardin', '''
(reusa r09: la madre frente al hombre, otro encuadre)
''')

R[14] = (172, 'contraluz', (), False, False, 'jardin', '''
Wide shot of the same front garden seen from the open front door of the
house, the camera at standing height in the doorway, perfectly level,
looking out over the lawn to the street. The sky over the far houses is
the only bright thing; the lawn, the low wall and the figures on it are
dark planes with edges of light.

Three figures stand on the lawn, small: the mother on the left with the
boy beside her holding her hand, and the man on the right by the open
gate, two metres from them, all three still, all three dark shapes with no
feature drawn. The plain ball on the grass between them.
''')

R[15] = (172, 'contraluz', (), False, False, 'jardin', '''
(reusa r12: la mano de la madre, otro encuadre)
''')

R[16] = (120, 'contraluz', (), False, False, 'jardin', '''
Wide shot of the same front garden from the street, the camera at standing
height, perfectly level, the sky over the house the only bright thing.

The garden is EMPTY except for one figure: the mother stands at the open
metal gate with her back to the camera, one hand on the gate, facing down
the street, completely still, a dark shape against the pale lawn. The
plain ball lies on the grass. Nobody else in the picture: no man, no
child, no shadow of either.
''')

R[17] = (102, 'dia', ('juana', 'fiscal'), None, False, 'oficina', '''
Medium shot across the desk, the camera at seated eye level on the
prosecutor's side, perfectly level, as if we were the prosecutor; the
prosecutor's hands out of focus at the bottom edge.

%(juana)s has just laughed: her head a little back, her eyes narrowed with
it, a real but small smile with the mouth closed, one hand lifted off the
handbag with the palm half open. The glass of water on the desk. ''' + MEDIODIA + '''
''')

R[18] = (127, 'dia', ('fiscal', 'juana'), None, False, 'oficina', '''
Over-the-shoulder shot across the desk, the camera at seated eye level just
behind and above the prosecutor's right shoulder, perfectly level, wide
enough to take in the whole desk and the window.

In the left foreground, large and out of focus, %(fiscal)s from BEHIND:
the back of a head of short dark hair, the shoulder of a plain charcoal
grey jacket, nothing of the face. Beyond, in focus, %(juana)s in the
visitor chair with her head tilted and one eyebrow higher than the other,
her mouth closed in a line that is not quite a smile: she does not believe
what she has just been told. The glass of water, the cup, the notebook on
the desk. ''' + MEDIODIA + '''
''')

R[19] = (270, 'dia', ('juana', 'fiscal'), None, False, 'oficina', '''
(reusa r01: Juana escucha, otro encuadre)
''')

R[20] = (291, 'dia', ('fiscal', 'juana'), None, False, 'oficina', '''
(reusa r18: sobre el hombro, abierto)
''')

R[21] = (136, 'dia', ('juana',), None, False, 'oficina', '''
Close shot of %(juana)s's face and shoulders in three-quarter view across
the desk, the camera at seated eye level, perfectly level, as if we were
the prosecutor, the window soft behind her. She is listening: her mouth
closed, the corners level, her eyes on the camera and steady, her brows
level. The scarf at her neck. ''' + MEDIODIA + ''' One side of the face in
light, the other in soft shadow built from flat tonal planes.
''')

R[22] = (264, 'dia', ('juana',), None, False, 'oficina', '''
Close shot of the plain glass of water standing on the plain grey desk,
half full, the camera at desk height, perfectly level, the glass in the
left third of the frame. Beyond it, out of focus, %(juana)s's hands on the
handbag in her lap and the grey of her coat; no face in frame. ''' + MEDIODIA + '''
The light makes one bright edge on the rim of the glass and a soft oval on
the desk under it.
''')

R[23] = (258, 'dia', ('fiscal', 'juana'), None, False, 'oficina', '''
Medium shot across the desk, the camera at seated eye level on the
prosecutor's side, perfectly level, as if we were the prosecutor.

In the right foreground, large and sharp, %(fiscal)s's right hand holds a
plain dark grey mobile phone out across the desk toward Juana, screen
toward her; the screen shows only plain flat grey bars, no character. On
the far side, %(juana)s leans forward and her eyes are on the screen, her
right hand already lifted off the handbag and open, a hand's width from
the phone, not yet touching it. Her mouth closed. The glass and the cup on
the desk. ''' + MEDIODIA + '''
''')

R[24] = (202, 'dia', ('juana',), None, False, 'oficina', '''
Medium shot across the desk, the camera at seated eye level on the
prosecutor's side, perfectly level, as if we were the prosecutor.

%(juana)s sits back a little in the visitor chair holding the plain dark
grey phone in both hands at chest height, reading: her eyes down on the
screen, her mouth closed, her brows level, her face lit a little from
below by the pale screen as well as from the window. The screen, turned
away from the camera, shows nothing but its edge. The handbag on her lap
under her forearms. ''' + MEDIODIA + '''
''')

R[25] = (177, 'dia', ('juana',), None, False, 'oficina', '''
Close shot of %(juana)s's eyes and brows as she reads, three-quarter view,
the camera at eye level, perfectly level: the eyes lowered toward a screen
below the frame, moving along a line, the lids half down, the brows level
and still; a pale even light from below on the lower half of the face and
the daylight from the left on the rest. The top of the phone's edge just
visible at the bottom of the frame. No other hand, no other face.
''')

R[26] = (123, 'dia', ('juana',), None, False, 'oficina', '''
(reusa r24: Juana lee, otro encuadre)
''')

R[27] = (193, 'dia', ('juana',), None, False, 'oficina', '''
Close shot of the plain dark grey phone held in %(juana)s's two hands, seen
from over her shoulder, the camera just behind and above, perfectly level;
the screen fills the middle of the frame and carries only plain flat grey
bars in the shape of a paragraph of text, with no readable character
anywhere; her thumb rests on the edge of the screen. Her hands, the cuffs
of the grey coat, the end of the mustard scarf hanging into the frame. No
face.
''')

R[28] = (223, 'dia', ('juana',), None, False, 'oficina', '''
(reusa r25: los ojos de Juana, otro encuadre)
''')

R[29] = (231, 'dia', (), False, False, 'oficina', '''
Medium shot of the office window from inside, the camera at seated height,
perfectly level, square to the window: plain metal frame, plain glass,
and through it the flat roofs and brick facades of the city under a grey
midday sky, soft. On the sill, a plain grey folder and nothing else. The
light comes through the glass and lays a bright plane on the wall beside
the frame. Nobody in frame.
''')

R[30] = (188, 'hero', (), False, False, 'recuerdo', '''
(reusa r05: el hombre cansado, abierto)
''')

R[31] = (156, 'dia', ('juana',), None, False, 'oficina', '''
Medium shot across the desk, the camera at seated eye level on the
prosecutor's side, perfectly level, as if we were the prosecutor.

%(juana)s has lowered the phone to her lap, still holding it in both hands,
and raised her eyes to the camera: her mouth closed, her brows level, her
eyes steady on us, her face quiet. Nothing is decided in it. The glass and
the cup on the desk. ''' + MEDIODIA + '''
''')

R[32] = (142, 'dia', ('fiscal', 'juana'), None, False, 'oficina', '''
Wide shot of the whole office from the far corner behind the prosecutor's
chair, the camera at standing height, perfectly level.

In the near foreground, %(fiscal)s seated at the desk seen from BEHIND and
above: the back of the head, the charcoal shoulders, the hands on the desk.
Across the desk, %(juana)s in the visitor chair, the phone in her lap,
looking down at it, still. The window on the left with the midday light,
the filing shelf, the door closed. Neither moves; nobody speaks. The room
is quiet and the light is the only thing that fills it.
''')

NOMBRE = {1: 'juana_piensa', 2: 'las_manos_de_juana', 3: 'el_vaso',
          4: 'el_vaso_b', 5: 'cansado', 6: 'cansado_b', 7: 'la_calle',
          8: 'el_jardin', 9: 'en_la_reja', 10: 'sin_jardin', 11: 'el_jardin_b',
          12: 'la_mano_de_la_madre', 13: 'en_la_reja_b', 14: 'desde_la_puerta',
          15: 'la_mano_de_la_madre_b', 16: 'la_reja_abierta', 17: 'juana_rie',
          18: 'sobre_el_hombro', 19: 'juana_piensa_b', 20: 'sobre_el_hombro_b',
          21: 'juana_escucha', 22: 'el_vaso_en_la_mesa', 23: 'el_celular',
          24: 'juana_lee', 25: 'los_ojos', 26: 'juana_lee_b', 27: 'el_texto',
          28: 'los_ojos_b', 29: 'la_ventana', 30: 'cansado_c',
          31: 'baja_el_celular', 32: 'el_silencio'}

REUSA = {
 4: (3, dict(encuadre=0.76, empuje=0.04, centro=[0.5, 0.45])),
 6: (5, dict(encuadre=0.76, empuje=0.05, centro=[0.5, 0.45])),
 11: (8, dict(encuadre=0.78, empuje=0.03, centro=[0.4, 0.5])),
 13: (9, dict(encuadre=0.76, empuje=0.04, centro=[0.55, 0.45])),
 15: (12, dict(encuadre=1.0, empuje=0.0, centro=[0.5, 0.5])),
 19: (1, dict(encuadre=0.78, empuje=0.04, centro=[0.5, 0.45])),
 20: (18, dict(encuadre=1.0, empuje=0.0, centro=[0.5, 0.5])),
 26: (24, dict(encuadre=0.76, empuje=0.04, centro=[0.5, 0.45])),
 28: (25, dict(encuadre=1.0, empuje=0.0, centro=[0.5, 0.5])),
 30: (5, dict(encuadre=1.0, empuje=0.0, centro=[0.5, 0.5])),
}

CON_PERSONA = {1, 2, 3, 4, 5, 6, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19,
               20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32}
SILUETAS = set()
CARTONES = {1, 4, 6, 7, 9, 12, 16, 19, 20, 21, 22, 24, 25, 27, 29, 31, 32}
CENITALES = set()
SOLO_MANOS = {2, 12, 15, 22, 27}
SIN_CARA = {5, 6, 8, 9, 11, 13, 14, 16, 30}
TOPE_SIN_GENTE = 3
PIEZA = 6571
TOTAL = PIEZA - (182 + 119 + 48 + 119 + 182)

HOJAS = {1: ['juana'], 2: ['juana'], 3: ['juana'], 17: ['juana'], 18: ['juana'],
         21: ['juana'], 22: ['juana'], 23: ['juana'], 24: ['juana'],
         25: ['juana'], 27: ['juana'], 31: ['juana'], 32: ['juana']}

DET = {
 (19, 'el_vaso_baja'): dict(cuadros=72, entra=120, registro='dia',
     personas=('juana',),
     escena='Close shot of a woman\'s right hand setting a plain glass of '
            'water down on a plain grey desk, the cuff of a grey coat at the '
            'wrist, midday light from the left making one bright edge on the '
            'glass.',
     gesto='The hand lowers the glass the last two centimetres onto the '
           'desk, lets go of it and draws back out of the frame. The glass '
           'stays where it was set. Nothing else moves.'),
 (23, 'el_pulgar'): dict(cuadros=72, entra=130, registro='dia',
     personas=('juana',),
     escena='Close shot of a woman\'s hand taking a plain dark grey phone from '
            'another hand across a desk; the receiving hand\'s thumb on the '
            'edge of the screen, which shows only plain flat grey bars; the '
            'giving hand in a plain light grey shirt cuff. Exactly two hands.',
     gesto='The receiving hand closes on the phone and draws it toward the '
           'camera a few centimetres; the giving hand opens and lets go. '
           'Nothing else moves.'),
 (32, 'la_luz_en_la_mesa'): dict(cuadros=72, entra=50, registro='dia',
     personas=(),
     escena='Close shot of the plain grey desk top: the notebook closed, the '
            'white cup, the glass with a little water left, the bright plane '
            'of midday light across them. No hand, no face.',
     gesto='Nothing in the frame moves except the light, which dims very '
           'slightly as a cloud passes and holds.'),
}

BROLL = {}

MOV = {
 3: 'kling: el vaso baja hasta la mesa y la mano se queda sobre el (cara quieta)',
 8: 'kling: el nino termina la carrera hacia la madre; el hombre quieto',
 16: 'kling: la madre baja la mano de la reja; la luz baja',
 24: 'kling: los ojos recorren una linea; el pulgar sube (cara quieta)',
 29: 'luz: pasa una nube (sin modelo)',
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
