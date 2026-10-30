# -*- coding: utf-8 -*-
r"""CASO 2 (de lesividad alta) «Fase 1 — La historia» · 29 ranuras ·
pieza 6268.

LO QUE SE OYE ENCIMA (resumen; el cruce completo en cruce_jr.json)
    r01-02  nota metodologica          r03-07  los hechos
    r08-09  flagrancia, no se conocian r10-13  perfil de la victima
    r14-15  delito imputado            r16-19  perfil de los procesados
    r20-22  condiciones restaurativas  r23-26  la acusacion y la pena
    r27-29  el acuerdo y la solicitud

SIETE ESCENAS, VEINTIDOS PLACAS, SIETE REUSOS
    A  la cuadra de la tienda, de noche (hero): r03, r04, r05, r06
    B  el hospital: r07 (el corredor de cirugia), r10 (Camilo en la cama)
    C  el despacho: r01 el expediente, r13 el dictamen (cenital), r20 el
       acuerdo (cenital), r25 las dos carpetas; r02 la ventanilla
    D  el corredor de detencion: r08 (siluetas), r19 (la reja)
    E  la sala: r14 vacia (contraluz), r23 la audiencia
    F  la casa de Camilo: r11 la mesa, r12 la venda, r28 la ventana
    J  los oficios de los procesados sin ellos: r17 el bus, r18 el puesto
    y la cuadra de dia (r09) y la mesa del acuerdo privado (r27).
    Reusos: r15<-r01, r16<-r08, r21<-r14, r22<-r11, r24<-r23, r26<-r14,
    r29<-r02.

LO QUE NO SE DIBUJA
    Ni la rina, ni el arma, ni la herida, ni la sangre, ni nadie en el
    suelo. La r05 es el anden vacio bajo la lampara; la r06 son dos
    siluetas quietas en la esquina. Los procesados: siluetas y espaldas,
    siempre. Nadie firma nada: el acuerdo esta sobre la mesa.

QUIEN LLEVA CARA
    Camilo (r10, r11, r22, r28). Nadie mas.
"""

R = {}

R[1] = (157, 'dia', ('fiscal2',), False, False, 'oficina', '''
Medium-close shot of a thick plain grey case file lying open on a plain
grey institutional desk, the camera low at desk height on the far side of
the desk, perfectly level, looking across the open file toward the person
reading it.

%(fiscal2)s: two hands in the sleeves of a plain charcoal grey jacket hold
the file open, one flat on the left page, the other holding the corner of the
right page lifted a few centimetres, mid-turn. The pages carry only plain
flat grey bars where text would be, and one small rectangle of darker grey
where a photograph would be. Daylight from a window on the left across the
desk. Behind the hands, out of focus, the plain grey of the jacket; no face
in frame.
''')

R[2] = (156, 'dia', ('defensor2',), False, False, 'oficina', '''
Medium shot of a plain public-office reception window seen from the public
side: a counter, a glass partition with a small opening at the bottom, the
camera at standing height, perfectly level, slightly to one side.

%(defensor2)s stands at the window seen from BEHIND, her back to the
camera, her face not visible; with her right hand she slides a thin plain
grey folder under the opening in the glass, her left hand holding a larger
folder against her side. On the other side of the glass a clerk's hand in
a plain grey sleeve takes the folder. The folder carries only a plain flat
grey bar where a label would be. Daylight from a high window.
''')

R[3] = (210, 'hero', ('amiga',), False, False, 'barrio', '''
Wide shot of a corner shop on a residential street in Bogota at night, the
camera at standing height across the street, perfectly level.

The shop's roll-down metal shutter is half open and the only light in the
picture comes from inside the shop, spilling in a long plane across the
pavement; the rest of the street falls away into near-black, with the
brick facades and a concrete utility pole just readable in the dark. On
the pavement in front of the shop, in that light, five or six people stand
in two loose groups a few metres apart, all seen from a distance, their
faces not readable: ordinary people in plain dark clothes, standing. Nobody
is touching anybody; nobody is on the ground; nothing is in anyone's hand.
It is the moment before.

What the camera asserts: one lit doorway on a dark street, and too many
people in front of it.
''')

R[4] = (249, 'hero', ('camilo', 'amiga'), None, False, 'barrio', '''
Medium shot at the lit doorway of the same corner shop at night, the camera
at standing height on the pavement, perfectly level, the doorway and the
shop interior the only bright thing in the picture.

%(camilo)s stands in the foreground with his BACK to the camera, close to
the doorway, in profile-from-behind: his right arm (no bandage yet, the
sleeve plain) held out a little to the side at waist height with the palm
open and back, the gesture of someone telling the people behind him to
stay back; his face is not visible. Beside him on the right, %(amiga)s,
also from behind, half a step behind his shoulder. Through the doorway,
inside the shop behind the counter, two small figures -an older man and
an older woman in plain grey, the owners- stand still, far and small, their
faces not readable. Nobody is touching anybody. Nothing is in anyone's
hand.
''')

R[5] = (205, 'hero', (), False, False, 'barrio', '''
Wide shot of the same street at night, a few metres further along from the
shop, the camera low at knee height on the pavement, perfectly level,
looking along the pavement.

The only light is one street lamp on a concrete pole, throwing a weak cone
onto the raised concrete pavement and the kerb; the brick facades with
their window grilles sit in the dark on the left, the road on the right is
black. Under the lamp the pavement is EMPTY: no person, no object, no mark,
no stain, nothing on the ground. Far back, out of focus, the faint spill
of the shop's light at the corner.

What the camera asserts: this is the spot, a few metres on, and there is
nothing to see on it.
''')

R[6] = (138, 'hero', ('procesados',), False, True, 'barrio', '''
Wide shot of the same street corner at night, the camera at standing height
across the street, perfectly level.

Two figures stand at the corner under the street lamp, side by side, a
metre apart, completely still, facing along the street away from the
camera: solid dark SILHOUETTES against the weak light of the lamp on the
wall behind them, one slight and one heavy-set, with no face, no feature
and nothing in their hands. The rest of the street is near-black. Nobody
else in the picture, nothing on the ground.
''')

R[7] = (223, 'contraluz', (), False, False, 'hospital', '''
Wide shot of a hospital corridor at night, the camera at standing height,
perfectly level, looking down the corridor toward a pair of swing doors
with small windows: the light behind those doors is the only bright thing
in the picture, and everything nearer sits in shadow.

In the corridor, against the wall, an EMPTY wheeled stretcher with a plain
light grey sheet, pushed aside at an angle. A plain metal bench on the
other wall, empty. Nobody in the corridor. The floor carries a long plane
of light from the doors.
''')

R[8] = (152, 'contraluz', ('procesados',), False, True, 'celda', '''
Wide shot down a plain institutional detention corridor, the camera at
standing height, perfectly level, looking through a long barred metal gate
in the foreground toward a high small window at the far end: that window
is the only light, and everything nearer reads as shadow and edge.

Far down the corridor, beyond the gate, two figures sit side by side on a
bench bolted to the wall, a metre apart, completely still: solid dark
SILHOUETTES against the light of the window, one slight and one heavy-set,
no face, no feature, their hands in their laps. Nobody else. No uniform,
no lettering, no number anywhere.
''')

R[9] = (152, 'dia', (), False, False, 'barrio', '''
Wide shot of the same street corner in Bogota by day, the camera at
standing height across the street, perfectly level.

The corner shop with its shutter rolled up, the brick facades, the window
grilles, the concrete pole with its bundle of cables, a small motorcycle
parked on the pavement, a plain hatchback at the kerb. Ordinary grey
daylight from one side. Nobody in the street at this moment; a plain grey
plastic chair stands empty beside the shop door.

What the camera asserts: an ordinary corner where people who did not know
each other happened to be on the same night.
''')

R[10] = (150, 'dia', ('camilo',), None, False, 'hospital', '''
Medium shot in a hospital room, the camera at the height of someone seated
by the bed, perfectly level.

%(camilo)s sits up in a plain hospital bed against two pillows, the sheet
to his waist, in his mustard sweater, his right forearm in its plain light
grey bandage resting on the sheet, his left hand flat beside it. His face
in three-quarter view, turned toward the window on the left, his eyes open
and steady on something outside, his mouth closed. No drama: a man who has
been told he will live and is thinking about it. Daylight from the window
on him and on the sheet; a plain metal bedside table with a plain glass of
water; a plain wall.
''')

R[11] = (249, 'dia', ('camilo',), None, False, 'barrio', '''
Medium shot inside a small plain kitchen-living room of a house in a Bogota
neighbourhood, the camera at seated height at the end of the table,
perfectly level.

%(camilo)s sits at a plain grey table by a window with a metal grille, his
bandaged right forearm resting on the table, his left hand around a plain
white cup. On the table in front of him a single plain sheet of paper with
flat grey bars. On the floor beside his chair, a closed plain grey toolbox
that has not been opened in weeks. His face in three-quarter view, eyes on
the paper, mouth closed, brow level. Daylight through the grille lays a
pattern of light across the table.

What the camera asserts: he works for himself, and the toolbox is closed.
''')

R[12] = (260, 'dia', ('camilo',), None, False, 'barrio', '''
Close shot across the same plain grey table, the camera at table height,
perfectly level.

In the foreground, filling the lower half of the frame, %(camilo)s's right
forearm rests on the table, wrapped from wrist to elbow in a plain light
grey bandage, the sleeve of his mustard sweater pushed up above it; the
hand lies open and relaxed, palm down. Beyond it, out of focus, the edge of
the plain white cup and the sheet of paper with grey bars. No face in
frame; exactly ONE arm in the frame. Daylight from the window on the left
across the bandage.
''')

R[13] = (147, 'dia', (), False, False, 'oficina', '''
Top-down shot, the camera directly above a plain grey desk, looking straight
down.

A single plain sheet of a medical report lies flat and square on the desk:
a printed form reduced to plain flat grey bars, with one short bar in a box
near the bottom where a number would be. A hand in the sleeve of a plain
light grey coat rests flat on the lower corner of the sheet, holding it
flat; a plain grey pen lies beside it. Nothing else on the desk. Daylight
from the upper left.
''')

R[14] = (172, 'contraluz', (), False, False, 'sala', '''
Wide shot of an empty Colombian hearing room, the camera at standing height
at the back of the room, perfectly level, looking toward the high plain
windows at the far end: those windows are the only bright thing in the
picture, and the room nearer the camera sits in shadow.

Plain institutional tables and chairs in two rows, a plain raised table at
the far end under the windows, plain wooden public benches in the
foreground, all empty. The light from the windows lays long planes across
the floor and the table tops. Nobody in the room.
''')

R[15] = (172, 'dia', ('fiscal2',), False, False, 'oficina', '''
(reusa r01: el expediente, otro encuadre)
''')

R[16] = (116, 'contraluz', ('procesados',), False, True, 'celda', '''
(reusa r08: el corredor de detencion, otro encuadre)
''')

R[17] = (242, 'contraluz', (), False, False, 'ciudad', '''
Wide shot of a bus depot at first light: a single plain grey city bus
parked side-on in an open concrete yard, its windows dark, its doors
closed, the camera at standing height across the yard, perfectly level.
Behind the bus, a plain rendered wall and a sky going from dark to grey;
the light comes from behind the bus, which reads mostly as silhouette and
edge, with the pale sky in its windows. Nobody in the yard. NO lettering,
NO number, NO logo, NO route sign anywhere on the bus.
''')

R[18] = (157, 'dia', (), False, False, 'ciudad', '''
Medium shot of a small street-market stall on a Bogota pavement by day: a
plain metal frame with a plain grey tarpaulin roof, a plain table with a
few plain cardboard boxes closed on it and under it, a plain plastic
chair empty beside it, the camera at standing height, perfectly level.
The stall is shut: a plain grey cloth is thrown over the table. Ordinary
grey daylight. Nobody at the stall; a passer-by far down the pavement,
small, from behind. No lettering, no sign, no logo anywhere.
''')

R[19] = (285, 'contraluz', (), False, False, 'celda', '''
Close shot of the long barred metal gate of a detention corridor, the
camera at the height of the lock, perfectly level, square to the bars.

The bars fill the frame, plain painted metal; the plain heavy lock and its
bolt in the centre, closed. Through the bars, out of focus, the corridor
beyond and the small high window at its end, the only light in the picture.
Nobody in frame, no hand, no uniform, no lettering, no number.
''')

R[20] = (180, 'dia', ('fiscal2',), False, False, 'oficina', '''
Top-down shot, the camera directly above a plain grey desk, looking straight
down.

A two-page document lies flat on the desk: the two sheets side by side,
each reduced to plain flat grey bars, with, near the bottom of the second
sheet, three short horizontal lines where signatures would go, each with a
small plain flat grey mark on it. Two hands in the sleeves of a plain
charcoal grey jacket rest on the desk at the bottom edge of the frame, one
flat beside the document, the other holding a plain grey pen pointing at
one line of the first sheet, not writing. Nothing else on the desk.
Daylight from the upper left.
''')

R[21] = (179, 'contraluz', (), False, False, 'sala', '''
(reusa r14: la sala vacia, otro encuadre)
''')

R[22] = (234, 'dia', ('camilo',), None, False, 'barrio', '''
(reusa r11: Camilo en la mesa de su casa, otro encuadre)
''')

R[23] = (177, 'dia', ('defensor2', 'procesados', 'fiscal2'), False, False,
         'sala', '''
Medium-wide shot inside the hearing room during a hearing, the camera at
seated height behind the public benches, perfectly level, looking over the
back of the room toward the tables.

In the foreground, the backs of two heads on the public bench, out of
focus. Beyond them, at the table on the left, %(defensor2)s seen from
BEHIND, seated, her hands on an open folder; beside her, seated, the two
accused -TWO MEN, both with SHORT hair, one slight and one heavy-set- as
plain dark SILHOUETTES from behind, still, no face visible, no long hair
anywhere. At the table on the right, %(fiscal2)s: only
the back of a charcoal grey jacket and two hands on a file. At the far end,
the plain raised table, its occupant out of frame above the top edge of the
picture. High plain windows; daylight from the left. Everyone is still;
nobody stands; no gesture.
''')

R[24] = (177, 'dia', ('defensor2', 'procesados', 'fiscal2'), False, False,
         'sala', '''
(reusa r23: la audiencia, otro encuadre)
''')

R[25] = (298, 'dia', ('fiscal2',), False, False, 'oficina', '''
Medium-close shot of two plain grey case folders on a plain grey desk, the
camera low at desk height on the far side, perfectly level.

The folder on the LEFT is CLOSED, and a hand in the sleeve of a plain
charcoal grey jacket rests flat on its cover, holding it shut. The folder
on the RIGHT is OPEN, its pages carrying only plain flat grey bars, and the
other hand holds its right-hand page flat at the margin. Exactly TWO hands
in the frame, one on each folder. No face. Daylight from a window on the
left across the desk; a plain white cup out of focus at the edge.

What the camera asserts: one charge closed, one kept open.
''')

R[26] = (97, 'contraluz', (), False, False, 'sala', '''
(reusa r14: la sala vacia, tercer encuadre)
''')

R[27] = (211, 'dia', (), False, False, 'barrio', '''
Medium shot of a plain grey table in a plain room, seen from a low
three-quarter angle at seated height, perfectly level.

On the table, in the centre, a two-page document lies flat, its sheets
reduced to plain flat grey bars, with three short signature lines near the
bottom of the second sheet, each carrying a small plain grey mark. Two
plain grey pens lie beside it. Three plain chairs stand around the table,
all empty, one pushed back a little as if someone just got up. Afternoon
daylight from a window on the right lays a plane of light across the
table. Nobody in the room.

What the camera asserts: three people sat here, and the table is what is
left of it.
''')

R[28] = (211, 'contraluz', ('camilo',), None, False, 'barrio', '''
Medium shot of %(camilo)s standing at the window of his house, seen from
inside the room, the camera at standing height behind and to one side of
him, perfectly level. The window with its metal grille is the only bright
thing in the picture: the daylight outside, the brick facade across the
street soft in it. He stands with his back three-quarter to the camera,
his bandaged right forearm held against his chest with his left hand, his
head turned to the window, his face seen only as an edge against the light.
The room nearer the camera is in shadow: the plain table, the closed
toolbox on the floor.
''')

R[29] = (262, 'dia', ('defensor2',), False, False, 'oficina', '''
(reusa r02: la ventanilla, otro encuadre)
''')

NOMBRE = {1: 'el_expediente', 2: 'la_ventanilla', 3: 'la_tienda',
          4: 'camilo_y_la_amiga', 5: 'el_anden', 6: 'las_siluetas',
          7: 'cirugia', 8: 'el_corredor', 9: 'la_cuadra_de_dia',
          10: 'la_cama', 11: 'en_casa', 12: 'la_venda', 13: 'el_dictamen',
          14: 'la_sala_vacia', 15: 'el_expediente_b', 16: 'el_corredor_b',
          17: 'el_bus', 18: 'el_puesto', 19: 'la_reja', 20: 'el_acuerdo',
          21: 'la_sala_vacia_b', 22: 'en_casa_b', 23: 'la_audiencia',
          24: 'la_audiencia_b', 25: 'dos_carpetas', 26: 'la_sala_vacia_c',
          27: 'la_mesa_del_acuerdo', 28: 'la_ventana', 29: 'la_ventanilla_b'}

# ranura -> (madre, camara). La madre va al 0,88 sin empuje; el reuso cambia
# encuadre, empuje y centro para que la misma placa lea como otro plano.
REUSA = {
 15: (1, dict(encuadre=0.78, empuje=0.04, centro=[0.45, 0.55])),
 16: (8, dict(encuadre=0.76, empuje=0.0, centro=[0.55, 0.5])),
 21: (14, dict(encuadre=0.76, empuje=0.05, centro=[0.5, 0.45])),
 22: (11, dict(encuadre=0.76, empuje=0.04, centro=[0.42, 0.5])),
 24: (23, dict(encuadre=0.76, empuje=0.04, centro=[0.4, 0.5])),
 26: (14, dict(encuadre=1.0, empuje=0.0, centro=[0.5, 0.5])),
 29: (2, dict(encuadre=0.76, empuje=0.05, centro=[0.55, 0.5])),
}

CON_PERSONA = {1, 2, 3, 4, 6, 8, 10, 11, 12, 13, 15, 16, 20, 22, 23, 24, 25, 28, 29}
SILUETAS = {6, 8, 16}
CARTONES = {1, 3, 8, 10, 12, 13, 14, 17, 18, 19, 20, 22, 23, 25, 26, 27, 29}
CENITALES = {13, 20}
SOLO_MANOS = {1, 12, 13, 15, 20, 25}
SIN_CARA = {2, 4, 23, 24, 29}
TOPE_SIN_GENTE = 3
PIEZA = 6268
TOTAL = PIEZA - (182 + 119 + 48 + 119 + 182)

HOJAS = {4: ['camilo'], 10: ['camilo'], 11: ['camilo'], 12: ['camilo'],
         28: ['camilo']}

DET = {
 (11, 'la_taza'): dict(cuadros=72, entra=100, registro='dia',
     personas=('camilo',),
     escena='Close shot of a man\'s left hand around a plain white cup on a '
            'plain grey table, the cuff of a matte mustard sweater at the '
            'wrist, daylight through a window grille laying a pattern of '
            'light on the table.',
     gesto='The fingers tighten a little around the cup and the hand turns '
           'the cup a quarter turn on the table without lifting it. The cup '
           'never leaves the table. Nothing else moves.'),
 (19, 'el_cerrojo'): dict(cuadros=72, entra=120, registro='contraluz',
     personas=(),
     escena='Extreme close shot of the plain heavy lock and bolt of a barred '
            'metal gate, the bars out of focus around it, the weak light of '
            'a distant window behind.',
     gesto='Nothing in the frame moves except the light: it dims very '
           'slightly and holds, as a cloud passes the window far away.'),
 (25, 'la_carpeta'): dict(cuadros=72, entra=140, registro='dia',
     personas=('fiscal2',),
     escena='Close shot of a hand in a plain charcoal grey sleeve resting '
            'flat on the cover of a closed plain grey folder on a desk, '
            'daylight from the left.',
     gesto='The hand presses down on the cover once, lightly, and stays '
           'there. The folder does not open. Nothing else moves.'),
}

BROLL = {
 'la_cuadra_lluvia': ('hero', 'Wide shot of the same Bogota street corner at '
                      'night after rain, the street lamp reflected in the '
                      'wet pavement, nobody in the street.'),
}

MOV = {
 3: 'kling: dos de las figuras lejanas se mueven un paso; la luz de la tienda parpadea una vez',
 5: 'luz: la lampara de la calle baja y sube apenas (sin modelo)',
 7: 'kling: la puerta de vaiven se abre a medias y vuelve; nadie pasa',
 10: 'kling: Camilo respira; la cortina del fondo se mueve; la cara quieta',
 17: 'luz: amanece (sube el cielo, sin modelo)',
 28: 'kling: baja la mano izquierda un poco; la luz de afuera',
}

LOWER_THIRD = {10: 'Camilo Andrés Ferreira Buitrago'}


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
