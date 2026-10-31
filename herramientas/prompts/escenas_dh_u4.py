# -*- coding: utf-8 -*-
r"""UNIDAD 4 «La medida de aseguramiento» · 40 ranuras · pieza 8529.

LO QUE SE OYE ENCIMA (cruce_dh.json)
    r01-02  voz en off: semana diez, la captura, la legalizacion
    r03     el juez organiza la audiencia
    r04-23  Quintero: la solicitud y las tres cargas (r07-12 inferencia y los
            cuatro hechos; r13-16 los fines; r17-23 el tipo de medida y el
            costo)
    r24-27  la abogada Salgado
    r28-37  el juez resuelve, en orden
    r38     voz en off: «la suya»
    r39-40  «La otra silla», sin dialogo: el texto va en carton

CUATRO ESCENAS
    A  la emisora al amanecer, vacia (r01: la captura NO se dibuja)
    B  la sala de audiencias de la U2, con todos (r02, ANCLA de la sala con
       la U2 r08 como referencia): el juez (r03, r13, r28, r34), Quintero de
       pie con Sandra (r04, r06, r21, r31), sobre el hombro de Quintero (r07),
       los cuatro elementos de conocimiento en la mesa (r08-r11, y juntos en
       cenital r12: la convergencia), la apoderada (r14), Sandra (r15), la
       mesa de la defensa (r16, r24, r25), Acosta de espaldas (r26, r22),
       el catalogo (r19), la sala que se vacia (r38)
    C  Carmen Elisa al aire (r23: «la libertad de expresión de la víctima»)
       = la placa aprobada de la U2 r13, copiada, no se vuelve a pedir
    D  el epilogo: el corredor y la reja (r39), el pabellon en siluetas
       (r40). Sin rostros, sin hacinamiento espectacularizado.

LO QUE NO SE DIBUJA
    La captura, el panfleto legible, el arma (va en una caja de evidencia
    sellada), la cara de Acosta (presuncion de inocencia: el curso lo dice
    en el epilogo). Los «rotulos» del documento (tabla de tres columnas,
    «1 · 2 · 3» en verde) van como cartones de la serie, no en la placa.
"""

R = {}

R[1] = (195, 'contraluz', (), False, False, 'emisora', '''
Wide shot of the corner house of the community radio station at dawn, the
camera across the empty street at standing height, perfectly level. The
sky behind the antenna is the only bright thing; the facade, the closed
wooden door and the dark blank lamp box above it stand in soft shadow.
Nobody in the street. A thin mist over the far roofs.

What the camera asserts: the place where it happened, after it happened.
''')

R[2] = (245, 'dia', ('juez', 'quintero', 'sandra', 'salgado', 'acosta', 'apoderada'), False, False, 'sala', '''
Wide shot of the hearing room during the hearing, the camera at the back of
the room behind the public benches, at standing height, perfectly level,
the whole room in frame. At the centre, behind his plain desk on the low
platform, %(juez)s listens, his hands joined on the desk. At the
prosecution table on the left, %(quintero)s sits upright with her case file,
and beside her %(sandra)s with her dark notebook. At the defence table on the
right, %(salgado)s sits with her slim black folder, and beside her
%(acosta)s, seated still, seen from behind. At a third small table near the
front, %(apoderada)s takes notes. Everyone is small in the frame. Daylight
from the high plain windows on the left falls in long shapes across the
floor; the public benches in the foreground are empty.
''')

R[3] = (232, 'dia', ('juez',), False, False, 'sala', '''
Medium shot of %(juez)s at his plain desk on the low platform, from the
waist up, in three-quarter view, the camera at the height of the parties'
tables, perfectly level. Mid-action: he looks toward the defence table,
checking that the defence lawyer is there, his reading glasses in one hand,
the other hand open on the case file; his mouth just open, speaking. The
plain painted wall behind him, daylight from the high window on the left.

His state: orderly, procedural, attentive.
''')

R[4] = (156, 'dia', ('quintero', 'sandra'), False, False, 'sala', '''
Medium shot of %(quintero)s standing at the prosecution table, from the
waist up, in three-quarter view, the camera at seated height from the side
of the room, perfectly level. Mid-action: she has just risen to speak and
addresses the bench, one hand resting on her closed case file, a plain
microphone on a short stand in front of her. Seated beside her, a little
behind, %(sandra)s looks up at her, her dark notebook open. Daylight from the
high windows.

Her state: formal, composed, ready.
''')

R[5] = (155, 'dia', ('quintero', 'sandra'), False, False, 'sala', '''
(reusa r04: Quintero, mas cerca)
''')

R[6] = (163, 'dia', ('quintero',), False, False, 'sala', '''
CLOSE-UP of %(quintero)s ALONE in the frame, standing at the prosecution
table, face and shoulders filling the frame, nobody else in the picture, in three-quarter view, the camera at standing height, perfectly
level. Mid-action: she speaks with quiet urgency, her reading glasses in her
hand at chest height, her eyes on the bench. Behind her, out of focus, the
plain wall and a high window.

Her state: urgent, without raising her voice.
''')

R[7] = (244, 'dia', ('quintero', 'juez'), False, False, 'sala', '''
Over-the-shoulder shot from behind %(quintero)s standing at the prosecution
table, at standing height, perfectly level: in the left foreground, out of
focus, her shoulder in the charcoal blazer and the back of her head; across
the room, sharp, %(juez)s at his desk on the low platform listens with his
hands joined, his glasses on. Daylight from the high windows.
''')

R[8] = (249, 'dia', ('quintero',), False, False, 'sala', '''
Close shot at table height of the prosecution table, the camera low and
level. Mid-action: a woman's hand, the cuff of a plain charcoal grey blazer
at the wrist, lays a thin plain grey report folder flat on the table, first
of a row; the folder has nothing written on it. A plain microphone on its
short stand at the edge of the frame. Daylight from the left. No face in
frame.
''')

R[9] = (163, 'dia', ('quintero',), False, False, 'sala', '''
Close shot at table height of the prosecution table, the camera low and
level. On the table, next to a thin grey report folder, a small sealed plain
cardboard evidence box, closed with plain tape, a blank plain tag tied to
it with string; nothing written on the tag, nothing visible inside.
Mid-action: a woman's fingertips, the cuff of a plain charcoal grey blazer
at the wrist, rest on the tag. Daylight from the left. No face in frame.
''')

R[10] = (204, 'dia', ('quintero',), False, False, 'sala', '''
Close shot at table height of the prosecution table, the camera low and
level. Two clear plastic bags lie side by side, each holding a single sheet
of paper folded in three, their visible sides blank grey with no mark and no
letter: the two sheets are the same size and folded the same way.
Mid-action: a woman's forefinger, the cuff of a plain charcoal grey blazer
at the wrist, rests on the table between the two bags. Daylight from the
left. No face in frame.
''')

R[11] = (220, 'dia', ('quintero',), False, False, 'sala', '''
Close shot at table height of the prosecution table, the camera low and
level. A mobile phone sealed inside a clear plastic evidence bag lies on top
of a thin plain report; the phone's screen is dark. Mid-action: a woman's
hand, the cuff of a plain charcoal grey blazer at the wrist, straightens the
report under it by a centimetre; the bag never leaves the report. Daylight
from the left. No face in frame.
''')

R[12] = (252, 'dia', ('quintero',), False, False, 'sala', '''
Overhead shot, looking straight down, of the prosecution table: FOUR items
in one row across the table, evenly spaced -a thin plain grey report folder,
a small sealed cardboard evidence box with a blank tag, two clear bags each
holding a folded blank sheet, and a phone sealed in a clear evidence bag on
a thin report-. At the bottom edge of the frame, a woman's two hands in plain
charcoal grey sleeves rest flat on the table edge. Daylight falls across the
table from the left, each item casting a small soft shadow.
''')

R[13] = (275, 'dia', ('juez',), False, False, 'sala', '''
CLOSE-UP of %(juez)s ALONE in the frame, at his desk, face and shoulders
filling the frame, no tables of the parties and nobody else in the picture,
frontal, the camera at
the height of the parties' tables, perfectly level. Mid-action: he listens
without moving, his hands joined in front of his mouth, his eyes over the top
of his reading glasses on the speaker. Daylight from the high window on the
left side of his face.

His state: weighing every word.
''')

R[14] = (153, 'dia', ('apoderada',), False, False, 'sala', '''
Medium shot of %(apoderada)s ALONE in the frame, seated at the small third
table near the front of the hearing room, from the waist up, nobody else in
the picture, in three-quarter view, the camera at
seated height, perfectly level. Mid-action: she listens and writes a short
line in her plain grey notepad, her pen moving, her eyes lifting toward the
prosecution table. A plain microphone on its stand. Daylight from the high
windows.

Her state: alert; she is there for the victim.
''')

R[15] = (204, 'dia', ('sandra',), False, False, 'sala', '''
Medium close-up of %(sandra)s ALONE in the frame, seated at the prosecution
table, from the chest up, nobody else in the picture, in three-quarter view, the camera at seated height, perfectly
level. Mid-action: she holds her dark notebook closed on the table and looks
across the room toward the defence table, steady and silent. Daylight from
the high windows.

Her state: quiet, watchful.
''')

R[16] = (140, 'dia', ('salgado', 'acosta'), False, False, 'sala', '''
Medium shot of the defence table, the camera at seated height behind and to
one side of %(acosta)s, perfectly level: in the foreground, out of focus,
his shoulder in a plain dark grey zip jacket and the back of his head of
short black hair, his face turned away and never visible; beside him, sharp,
%(salgado)s looks up from her slim black folder toward the prosecution table
and makes a short note. Daylight from the high windows.
''')

R[17] = (175, 'dia', ('quintero', 'sandra'), False, False, 'sala', '''
(reusa r04: Quintero de pie, otro encuadre)
''')

R[18] = (175, 'dia', ('quintero', 'juez'), False, False, 'sala', '''
(reusa r07: sobre el hombro, mas cerca del juez)
''')

R[19] = (154, 'dia', ('quintero',), False, False, 'sala', '''
Close shot of a thick open book lying flat on the prosecution table, the
camera close and level with the table, looking along the pages. The right
page shows a short list drawn ONLY as plain flat grey bars of different
lengths: no numerals, no digits, no letters, no bullets, nothing legible
anywhere on either page.
Mid-action: a woman's forefinger, the cuff of a plain charcoal grey blazer
at the wrist, runs down the list and stops under one item. Daylight from the
left lays the shadow of the raised page edge across the paper. No face in
frame.
''')

R[20] = (154, 'dia', ('juez', 'quintero', 'sandra', 'salgado', 'acosta', 'apoderada'), False, False, 'sala', '''
(reusa r02: la sala, mas cerca del centro)
''')

R[21] = (297, 'dia', ('quintero',), False, False, 'sala', '''
Medium shot of %(quintero)s standing at the prosecution table, from the
waist up, seen in profile from the side of the room where the public benches
are, the camera at seated height, perfectly level. Mid-action: she explains,
one hand held out flat and the other turning over, a measured gesture
weighing one thing against another; her case file closed on the table.
Daylight from the high windows behind her.

Her state: methodical; she has examined every option.
''')

R[22] = (264, 'dia', ('quintero', 'acosta'), False, False, 'sala', '''
Over-the-shoulder shot from DIRECTLY BEHIND %(acosta)s seated at the
defence table, at seated height, perfectly level, the camera exactly behind
his head: in the right foreground, out of focus, the back of his head of
short black hair, his nape and the collar of his plain dark grey zip jacket,
slightly lowered. We see ONLY the back of his head: no cheek, no ear in
profile, no nose, no eye, no part of his face. Across the room, sharp,
%(quintero)s standing at the prosecution table pauses and looks toward him,
her hand flat on her case file. Daylight from the high windows.

Her state: she knows the cost of what she is asking.
''')

R[23] = (213, 'dia', ('carmen',), None, False, 'cabina', '''
(copia de la U2 r13: Carmen Elisa al aire; COPIA)
''')

R[24] = (215, 'dia', ('salgado', 'acosta'), False, False, 'sala', '''
Medium shot of %(salgado)s standing at the defence table, from the waist up,
in three-quarter view, the camera at seated height, perfectly level.
Mid-action: she addresses the bench, serene, one hand resting on her open
slim black folder, the other open in a small precise gesture; a plain
microphone on its stand. Seated beside her, out of focus, %(acosta)s, seen
from behind, his face turned away. Daylight from the high windows.

Her state: serene and technical.
''')

R[25] = (267, 'dia', ('salgado',), False, False, 'sala', '''
CLOSE-UP of %(salgado)s ALONE in the frame, standing at the defence table,
face and shoulders filling the frame, nobody else in the picture,
in three-quarter view, the camera at standing height, perfectly level.
Mid-action: she speaks calmly toward the bench, her chin level, one eyebrow
slightly raised. The plain wall behind her, out of focus.

Her state: precise, unhurried, sure of her ground.
''')

R[26] = (112, 'dia', ('acosta',), False, False, 'sala', '''
Medium-close shot from directly behind %(acosta)s seated at the defence
table, at seated height, perfectly level: his back in a plain dark grey zip
jacket, the back of his head of short black hair slightly lowered, his two
hands joined on the table in front of him, visible past his side. His face is
NOT visible at all. Beyond him, out of focus, the low platform and the
judge's desk. Daylight from the high windows.

What the camera asserts: a person who is presumed innocent.
''')

R[27] = (285, 'dia', ('salgado', 'acosta'), False, False, 'sala', '''
(reusa r24: Salgado, mas cerca)
''')

R[28] = (182, 'dia', ('juez',), False, False, 'sala', '''
Medium close-up of %(juez)s ALONE in the frame, at his desk on the low
platform, from the chest up, no tables of the parties and nobody else in the
picture, frontal, the camera at the height of the parties' tables,
perfectly level. Mid-action: he has taken off his reading glasses and,
holding them in one hand, delivers his ruling, his other hand flat on the
open case file, his eyes moving across the room. Daylight from the high
window on the left.

His state: deliberate, in order, one requirement at a time.
''')

R[29] = (168, 'dia', ('quintero',), False, False, 'sala', '''
(reusa r12: los cuatro elementos)
''')

R[30] = (163, 'dia', ('juez',), False, False, 'sala', '''
(reusa r28: el juez, mas cerca)
''')

R[31] = (162, 'dia', ('quintero', 'sandra'), False, False, 'sala', '''
Medium two-shot of %(quintero)s and %(sandra)s seated side by side at the
prosecution table, from the waist up, in three-quarter view, the camera at
seated height, perfectly level. Mid-action: both listen to the ruling,
still, Quintero with her hands folded on her closed case file, Sandra with
her pen resting on her notebook. Daylight from the high windows.
''')

R[32] = (111, 'dia', ('apoderada',), False, False, 'sala', '''
(reusa r14: la apoderada, mas cerca)
''')

R[33] = (273, 'dia', ('quintero',), False, False, 'sala', '''
(reusa r11: el telefono sellado, empuje lento)
''')

R[34] = (159, 'dia', ('juez',), False, False, 'sala', '''
Medium shot of %(juez)s at his desk on the low platform, from the waist up,
in three-quarter view, the camera at the height of the parties' tables,
perfectly level. Mid-action: he writes in the open case file with a plain
dark pen, his reading glasses on, his other hand holding the page flat.
Daylight from the high window falls across the desk.
''')

R[35] = (158, 'dia', ('salgado', 'acosta'), False, False, 'sala', '''
(reusa r16: la mesa de la defensa)
''')

R[36] = (183, 'dia', ('juez',), False, False, 'sala', '''
(reusa r03: el juez, otro encuadre)
''')

R[37] = (192, 'dia', ('juez', 'quintero', 'sandra', 'salgado', 'acosta', 'apoderada'), False, False, 'sala', '''
(reusa r02: la sala entera, empuje lento)
''')

R[38] = (222, 'contraluz', ('colegas',), False, False, 'sala', '''
Wide shot of the hearing room just after the hearing, the camera low at the
side of the prosecution table, perfectly level. In the foreground, on the
empty prosecution table, a closed case file and the plain microphone on its
short stand. At the far end of the room the double door stands open onto a
bright corridor, the only bright thing in the frame; %(colegas)s leave
through it as small dark figures. The platform and the judge's desk are
empty. The room around falls into soft shadow.
''')

R[39] = (173, 'contraluz', ('presos',), False, True, 'pabellon', '''
Wide shot down a long plain institutional prison corridor, the camera at
standing height, perfectly level. At the far end, a heavy barred gate and,
beyond it, a high small barred window: the only light. Halfway down the
corridor, %(presos)s: a single figure walks away from us toward the gate,
a dark silhouette with no face, carrying a rolled thin mattress under one
arm. The painted masonry walls fall into shadow.
''')

R[40] = (172, 'hero', ('presos',), False, True, 'pabellon', '''
Wide shot of a crowded communal cell block seen through an open barred gate,
the camera at standing height in the corridor, perfectly level. Low-key: one
weak light from a high small barred window deep in the frame. Thin mattresses
lie on the floor along both walls, clothes hang on lines; at the far wall,
%(presos)s wait in a short queue in front of a single wall telephone, all of
them dark silhouettes with no faces. Nobody looks at the camera. Calm, quiet,
crowded without spectacle.
''')

NOMBRE = {1: 'la_emisora_al_amanecer', 2: 'la_audiencia', 3: 'el_juez_constata',
          4: 'quintero_solicita', 5: 'quintero_b', 6: 'la_urgencia',
          7: 'sobre_el_hombro', 8: 'hecho_uno', 9: 'hecho_dos', 10: 'hecho_tres',
          11: 'hecho_cuatro', 12: 'convergen', 13: 'el_juez_escucha',
          14: 'la_apoderada', 15: 'sandra', 16: 'la_defensa', 17: 'quintero_c',
          18: 'sobre_el_hombro_b', 19: 'el_catalogo', 20: 'la_audiencia_b',
          21: 'quintero_explica', 22: 'el_costo', 23: 'carmen_al_aire',
          24: 'salgado_habla', 25: 'salgado_cerca', 26: 'acosta_de_espaldas',
          27: 'salgado_b', 28: 'el_juez_resuelve', 29: 'convergen_b',
          30: 'el_juez_b', 31: 'la_fiscalia_escucha', 32: 'la_apoderada_b',
          33: 'hecho_cuatro_b', 34: 'el_juez_escribe', 35: 'la_defensa_b',
          36: 'el_juez_c', 37: 'impongo', 38: 'la_sala_se_vacia',
          39: 'el_corredor', 40: 'el_pabellon'}

REUSA = {
 5: (4, dict(encuadre=0.72, empuje=0.03, centro=[0.45, 0.4])),
 17: (4, dict(encuadre=0.82, empuje=0.04, centro=[0.55, 0.45])),
 18: (7, dict(encuadre=0.72, empuje=0.04, centro=[0.6, 0.42])),
 20: (2, dict(encuadre=0.7, empuje=0.03, centro=[0.5, 0.45])),
 27: (24, dict(encuadre=0.7, empuje=0.03, centro=[0.48, 0.38])),
 29: (12, dict(encuadre=0.8, empuje=0.05, centro=[0.5, 0.5])),
 30: (28, dict(encuadre=0.72, empuje=0.03, centro=[0.5, 0.38])),
 32: (14, dict(encuadre=0.72, empuje=0.03, centro=[0.5, 0.4])),
 33: (11, dict(encuadre=1.0, empuje=0.08, centro=[0.5, 0.5])),
 35: (16, dict(encuadre=0.78, empuje=0.03, centro=[0.55, 0.45])),
 36: (3, dict(encuadre=0.76, empuje=0.04, centro=[0.5, 0.4])),
 37: (2, dict(encuadre=1.0, empuje=0.06, centro=[0.5, 0.5])),
}

# placa copiada de otra unidad: no se vuelve a pedir (Windows copia la
# candidata elegida a _candidatas con el nombre de esta ranura, letra a)
COPIA = {23: 'DH_U2_r13_carmen_al_aire', 34: 'DH_U2_r22_el_juez_valora'}

CON_PERSONA = set(range(2, 41))
SILUETAS = {39, 40}
CARTONES = set(range(1, 41))
CENITALES = {12}
SOLO_MANOS = {8, 9, 10, 11, 12, 19}
SIN_CARA = {26}
TOPE_SIN_GENTE = 3
PIEZA = 8529
TOTAL = PIEZA - (182 + 119 + 48 + 119 + 182)

HOJAS = {2: ['juez', 'quintero', 'sandra', 'salgado', 'apoderada'],
         3: ['juez'], 4: ['quintero', 'sandra'], 6: ['quintero'],
         7: ['quintero', 'juez'], 13: ['juez'], 14: ['apoderada'],
         15: ['sandra'], 16: ['salgado'], 21: ['quintero'],
         22: ['quintero'], 24: ['salgado'], 25: ['salgado'], 28: ['juez'],
         31: ['quintero', 'sandra'], 34: ['juez']}

SALA = 'DH_U2_r08_la_sala'
AUDIENCIA = 'DH_U4_r02_la_audiencia'
REF_PLACA = {
 1: (['DH_U1_r02_carmen_llega'], 'lugar',
     'It is now DAWN and the street is EMPTY: nobody in it. '),
 2: ([SALA], 'lugar', 'Now every table is occupied as described above. '),
 39: (['DH_U1_r10_la_recepcion'], 'estilo', ''),
 40: (['DH_U1_r10_la_recepcion'], 'estilo', ''),
}
for _n in (7, 8, 9, 10, 11, 12, 14, 15, 16, 19, 22, 24, 25, 26, 31, 38):
    REF_PLACA[_n] = ([AUDIENCIA], 'lugar', '')
# 31 oct (leccion de la U3): los planos cerrados llevan como referencia un
# plano cerrado aprobado de la misma sala (U2), no el general.
for _n in (3, 34):
    REF_PLACA[_n] = (['DH_U2_r22_el_juez_valora'], 'lugar', '')
for _n in (13, 28):
    REF_PLACA[_n] = (['DH_U2_r09_el_juez_pregunta'], 'lugar', '')
for _n in (4, 6, 21):
    REF_PLACA[_n] = (['DH_U2_r21_quintero_sustenta'], 'lugar', '')
# 31 oct: r22 salio dos veces con la cara de Acosta de perfil; la referencia
# es la r16 aprobada (Acosta de espaldas, sin rostro, en esta misma sala)
REF_PLACA[22] = (['DH_U4_r16_la_defensa'], 'lugar',
                 'Acosta is seen from behind EXACTLY as in that plate: the back '
                 'of his head only, never his face. ')

DET = {
 (22, 'la_mano_en_el_expediente'): dict(cuadros=72, entra=100, registro='dia',
     personas=('quintero',),
     escena='Extreme close shot of a woman\'s hand resting flat on a closed '
            'thick case file held with a black binder clip, the cuff of a '
            'plain charcoal grey blazer at the wrist.',
     gesto='The fingers press very slightly on the file and relax. The file '
           'does not move. Nothing else moves.'),
 (26, 'las_manos_juntas'): dict(cuadros=60, entra=30, registro='dia',
     personas=('acosta',),
     escena='Extreme close shot of a man\'s two hands joined on a plain table, '
            'the cuffs of a plain dark grey zip jacket at the wrists.',
     gesto='The thumbs move slowly against each other once and stop. The '
           'hands stay on the table. Nothing else moves.'),
}

BROLL = {}

MOV = {
 6: 'quieta (31 oct): solo habla; Kling deforma las caras al hablar',
 24: 'quieta (31 oct): solo habla',
 28: 'quieta (31 oct): solo habla',
 40: 'quieta (31 oct): el clip de Kling disolvia la fila (la gente desaparecia); descartado',
}

LOWER_THIRD = {3: 'Juez de control de garantías', 21: 'Marina Quintero',
               24: 'Abogada Salgado'}


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
