# -*- coding: utf-8 -*-
r"""UNIDAD 4 · Caso de análisis 2 · 9 ranuras · pieza 2386. Narra Pilar.

LO QUE SE OYE ENCIMA (cruce_lp.json)
    r01  lesiones personales culposas en accidente de tránsito,
    r02  las partes comparecen voluntariamente y piden la mediación penal
    r03  el fiscal de conocimiento remite el conflicto a un mediador del
         distrito judicial con el formato FGN-MP02-F-132
    r04  (sigue el formato, deletreado)
    r05  en la sesión, el indiciado acepta que conducía con exceso de velocidad,
    r06  arrepentimiento; ofrece 10 millones de pesos como indemnización total
    r07  tras varias sesiones no hay acuerdo: formato FGN-MP02-F-133
    r08  en el juicio oral el fiscal pretende introducir el audio de la sesión
    r09  el defensor se opone: regla de exclusión

QUIÉN LLEVA CARA
    El fiscal lleva al juicio el audio de la mediación (decide mal): sin cara.
    El indiciado se presume inocente: de espaldas. El lesionado y el mediador
    sí llevan cara; la defensora también. El accidente no se dibuja con
    heridos: el después en la calle, sin nadie.
"""

R = {}

R[1] = (122, 'dia', (), None, False, 'cruce', '''
Wide shot of an ordinary street crossing in a Colombian city on an overcast
morning after a minor traffic accident, the camera at standing height on the
pavement, perfectly level. In the middle of the crossing, a small plain car
stands at an angle with its front bumper dented, and a plain motorcycle helmet
lies on the asphalt beside it; three plain grey traffic cones set around. Nobody in the frame. No injured person, no blood.
''')

R[2] = (185, 'dia', ('lesionado', 'conductor', 'fiscal_sin_cara'), None, False, 'despacho', '''
Over-the-shoulder shot from BEHIND the visitor chairs, the camera at seated
height, perfectly level. In the right foreground, %(conductor)s sits with his
back fully to the camera: we see only the back of his head, his ears and his
shoulders, filling the right third of the frame; his face is entirely hidden
by his own head, not his eye, not his nose, not his cheek. Beside him, in the
left visitor chair, %(lesionado)s in three-quarter view, calm, his forearm in
the sling, his eyes on the desk in front of them. Across the desk, the
prosecutor is OUT OF FRAME to the left: only his hand in a plain charcoal
sleeve rests flat on an open case folder at the left edge of the desk. The
office window and the shelving behind. Daylight from the window.
''')

R[3] = (239, 'dia', ('fiscal_sin_cara',), None, False, 'despacho', '''
Close shot at desk height: a man's hands in a plain charcoal jacket sleeve
slide a one-page institutional form, its boxes drawn only as plain grey bars
and empty rectangles, into a plain grey folder, next to a plain rubber stamp.
Only hands and sleeves; no face. Daylight from one side.
''')

R[4] = (150, 'dia', ('mediador',), None, False, 'mediacion', '''
Medium shot of %(mediador)s standing in the doorway of a small mediation room,
three-quarter view, the camera at his eye level, perfectly level, holding a
plain grey folder he has just received, opening it with one hand, reading
the first page. Behind him, the round table and three chairs. Soft window
light. He is ALONE in the frame and appears ONCE.
''')

R[5] = (166, 'dia', ('mediador', 'lesionado', 'conductor'), None, False, 'mediacion', '''
Medium-wide shot of a mediation session at the round table, the camera at
seated height, perfectly level. Mid-action: %(conductor)s, seen in
three-quarter back view, leans forward with both hands open on the table,
speaking; across from him %(lesionado)s listens, his forearm in the sling;
between them %(mediador)s listens with his hands flat on the table. Soft
window light.
''')

R[6] = (183, 'dia', ('conductor', 'lesionado'), None, False, 'mediacion', '''
Close shot at table height over the shoulder of %(conductor)s, seen from
behind: his two hands clasped tight on the table, head bowed; across the
table, in focus, %(lesionado)s looks at him, still, his good hand resting on
the table beside a glass of water. Soft window light.
''')

R[7] = (299, 'dia', (), None, False, 'mediacion', '''
Overhead shot looking straight down at the round mediation table after the
last session, nobody in the frame: one form with plain grey boxes lies in the
middle with three plain signature scribbles at the bottom, three plain pens
laid down beside it, three half-empty glasses of water, three chairs pushed
back from the table. Soft daylight from one side throws the shadows of the
glasses across the table.
''')

R[8] = (270, 'dia', ('fiscal_sin_cara', 'juez'), None, False, 'sala', '''
Medium-wide shot of an oral trial in a Colombian hearing room, the camera
behind %(fiscal_sin_cara)s at the prosecution table, perfectly level. In the
foreground, his back and shoulder; mid-action, he holds up a small plain
digital voice recorder in one raised hand toward the judge. At the centre,
behind the plain desk, %(juez)s looks at the recorder. Daylight from high
windows.
''')

R[9] = (122, 'dia', ('defensora',), None, False, 'sala', '''
Medium-close shot of %(defensora)s rising from the defence table, from the
chest up, three-quarter view, the camera at her eye level, perfectly level.
Mid-action: her right hand is raised, palm open, in objection, her mouth
half open mid-word. Behind her, soft and out of focus, the hearing room. She
is ALONE in the frame and appears ONCE.
''')

NOMBRE = {1: 'el_cruce', 2: 'las_partes', 3: 'la_remision', 4: 'el_mediador',
          5: 'la_sesion', 6: 'el_arrepentimiento', 7: 'sin_acuerdo',
          8: 'el_audio', 9: 'la_oposicion'}

CON_PERSONA = {2, 3, 4, 5, 6, 8, 9}
SILUETAS = set()
CARTONES = {1, 3, 5, 6, 7, 8, 9}
CENITALES = {7}
SOLO_MANOS = {3}
SIN_CARA = set()
TOPE_SIN_GENTE = 3
PIEZA = 2386
TOTAL = PIEZA - (182 + 119 + 48 + 119 + 182)

HOJAS = {4: ['mediador'], 5: ['mediador']}

ANCLA = 'LP_U4C2_r05_la_sesion'
REF_PLACA = {
 5: (['LP_U4C1_r01_la_noticia'], 'estilo', ''),
 1: ([ANCLA], 'estilo', ''),
 2: (['LP_U4C2_r02_las_partes'], 'lugar', 'It is the SAME office and the SAME two men as in that plate; only the camera has moved behind the visitor chairs. '),
 3: (['LP_U4C1_r01_la_noticia'], 'lugar', ''),
 4: ([ANCLA], 'lugar', ''),
 6: ([ANCLA], 'lugar', ''),
 7: ([ANCLA], 'lugar', ''),
 8: (['LP_U4C1_r05_la_recusacion'], 'lugar', ''),
 9: (['LP_U4C1_r05_la_recusacion'], 'lugar', ''),
}

REUSA = {}

DET = {}

BROLL = {}

MOV = {
 5: 'kling: el conductor habla con las manos abiertas; los otros escuchan',
 8: 'kling: el fiscal levanta la grabadora hacia el juez',
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
    return fallos, tot, mejor
