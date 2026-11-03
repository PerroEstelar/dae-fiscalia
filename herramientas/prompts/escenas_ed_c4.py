# -*- coding: utf-8 -*-
r"""CASO 4 · La niña del resguardo de Putumayo · 19 ranuras · 3772 cuadros.
Narra Pilar.

LO QUE SE OYE ENCIMA (cruce_ed.json)
    r01-r04  el resguardo cerca de Puerto Guzmán; la niña pasa cada día
             frente a la casa del Taita; su autoridad en un cabildo débil;
             conoce su rutina; la llama a su casa; abusa de ella
    r05-r09  la madre acude al cabildo; deliberan; no tienen fuerza ni
             mecanismos contra el Taita, la máxima autoridad
    r10-r16  la madre acude a la justicia ordinaria; el fiscal no sabe cómo
             proceder; los colegas no se ponen de acuerdo; la mesa técnica
             recomienda devolver el caso; lo remite al resguardo
    r17-r19  punto muerto: ni el cabildo ni la Fiscalía lo asumen; el Taita
             sigue en su cargo, sin medida de protección para la víctima

LO QUE NO SE DIBUJA, NUNCA
    La niña. Ni de frente, ni de espaldas, ni de lejos, ni en sombra. Está su
    camino (r01, las huellas de unas botas pequeñas en el barro rojo) y su
    morral, que lleva la madre (r05, r10, r17). El abuso no tiene imagen: la
    r04 es la puerta cerrada al atardecer con el bastón de mando al lado. El
    Taita es SILUETA siempre: no tiene cara (biblia §3 y la regla de la
    serie para quien agrede).

QUIÉN LLEVA CARA
    La madre, siempre, con su blusa mostaza: es el acento del caso. El
    fiscal también -duda, no decide mal por cuenta propia-, pero el plano de
    la remisión (r16) es solo manos y el cartón del error no cae sobre su
    cara. Los colegas y los funcionarios de la mesa, pequeños.

LA RIMA
    r02 el Taita en su porche al principio; r19 el mismo porche al final, con
    la madre de espaldas en primer plano: «permanecía en ejercicio de su
    cargo».
"""

R = {}

R[1] = (254, 'dia', (), None, False, 'resguardo', '''
Wide shot of a red-earth path through the reserve on a misty morning, the
camera at standing height on the path, perfectly level. The path runs from
the foreground into the distance between tall plantains and chontaduro
palms, and halfway along it passes in front of a wooden house raised on short
posts with a plain zinc roof and a wooden porch. The path is wet and empty;
nothing lies or stands on it. Low cloud on the green hills. Nobody in the
frame: no child, no person anywhere.
''')

R[2] = (228, 'contraluz', ('taita',), None, True, 'casa_taita', '''
Medium-wide shot of the wooden house raised on short posts, seen from the
path, the camera at standing height, perfectly level. On the wooden porch
stands %(taita)s, a solid dark silhouette, frontal, tall and still, his right
hand resting on the top of his tall carved staff of authority, whose plain
ribbons hang from its head. Behind him, through the open back of the porch,
the bright green forest is the only bright thing in the frame; the porch and
the house are in deep shadow. He has no face, no features, no skin tone.
''')

R[3] = (264, 'contraluz', (), None, False, 'casa_taita', '''
Shot from INSIDE the dark wooden house, the camera at standing height in the
room, perfectly level, looking out through the open doorway onto the bright
red-earth path outside. The doorway is the only bright thing in the frame; the
plank walls around it are in deep shadow. Leaning against the door frame, in
dark silhouette, the tall carved staff of authority with its ribbons. On the
path outside, nobody: only the plantains and the light. Nobody in the frame.
''')

R[4] = (147, 'hero', (), None, False, 'casa_taita', '''
Medium shot of the closed plank door of the wooden house at dusk, the camera
at standing height on the path, perfectly level. The door is shut. Beside it,
leaning against the wall of the porch, the tall carved staff of authority with
its ribbons hanging still. The light is low and weak and comes from deep in
the frame, from the last grey of the sky behind the roof; the porch and the
door fall into near-black. Nobody in the frame. Nothing else.
''')

R[5] = (191, 'dia', ('madre',), None, False, 'resguardo', '''
Medium shot of %(madre)s walking fast along the red-earth path TOWARD the
camera, from the knees up, frontal three-quarter, the camera at her eye
level, perfectly level. She is caught mid-stride, her left foot planted, her
right heel lifted. In her right hand she carries a child's small plain school
backpack by its top loop, plain grey with no print and no letters. Her eyes
are fixed ahead, past the camera, her mouth a straight line. The plantains
on both sides, mist in the trees behind her. She appears ONCE.
''')

R[6] = (148, 'dia', ('madre', 'cabildantes'), None, False, 'cabildo', '''
Wide shot of the community house of the cabildo from the edge of its circle
of benches, the camera at seated height, perfectly level. In the middle of
the packed-earth floor, %(madre)s STANDS, three-quarter view, mid-sentence,
her right hand open toward the people seated in front of her, the small grey
backpack hanging from her left hand. Around her, on the plain wooden benches
in a circle, sit %(cabildantes)s, listening, their eyes on her. The forest all
around through the open sides of the house, under the high thatched roof.
She appears ONCE.
''')

R[7] = (186, 'dia', ('cabildantes',), None, False, 'cabildo', '''
Medium shot of three of %(cabildantes)s seated side by side on one plain
wooden bench of the cabildo, the camera at seated height, perfectly level,
frontal. All three look DOWN at the packed-earth floor in front of their feet:
their heads bowed about thirty degrees, their eyes lowered, their hands
clasped between their knees. Nobody speaks. The posts of the open house and
the forest behind them, soft. Their faces are small and lowered.
''')

R[8] = (109, 'dia', ('taita',), None, True, 'cabildo', '''
Close shot of the head of the tall carved staff of authority, the camera at
the height of the carving, perfectly level: the carved wooden top and the
plain coloured ribbons hanging from it, held upright by a dark hand in
silhouette gripping the shaft just below; no face, no body beyond the hand
and the wrist, all of it a solid dark shape. Behind, out of focus, the open
side of the cabildo house and the forest.
''')

R[9] = (197, 'contraluz', ('taita', 'cabildantes'), None, True, 'cabildo', '''
Wide shot of the cabildo house from inside, the camera at seated height,
perfectly level. In the foreground and the middle ground, %(cabildantes)s sit
in their circle of benches with their backs half turned to the camera. At the
far open side of the house, against the bright forest, stands %(taita)s, a
solid dark silhouette, tall, his staff of authority upright in his hand,
watching them. He has no face. The bright forest behind him is the only
bright thing in the frame.
''')

R[10] = (124, 'dia', ('madre',), None, False, 'resguardo', '''
Medium shot of a long plain wooden river boat with a small outboard motor on
the wide brown river, the camera at water level from the bank, perfectly
level. %(madre)s sits in the middle of the boat, in profile facing left, the
small plain grey backpack held on her lap with both hands, her eyes on the
river ahead. The dark green forest on the far bank, low cloud. The boatman is
a small figure seen from behind at the motor. She appears ONCE.
''')

R[11] = (251, 'dia', ('fiscal_c4', 'madre'), None, False, 'fiscalia_pueblo', '''
Medium shot of the small Fiscalía office of the river town, the camera at
seated height, perfectly level. Behind the plain desk, %(fiscal_c4)s sits in
frontal three-quarter view, his left elbow on the desk and his fingertips
rubbing his forehead, his eyes down on an open case folder, unsure. In the
right foreground, %(madre)s sits in the visitor chair in three-quarter back
view, upright, the small grey backpack on her lap, her face turned toward
him. A plain standing fan, metal shelving with folders, the window onto the hot
street. Each person appears ONCE.
''')

R[12] = (183, 'dia', ('fiscal_c4', 'colegas'), None, False, 'fiscalia_pueblo', '''
Over-the-shoulder shot from behind %(fiscal_c4)s, who stands in the doorway
of a colleague's office holding the open case folder, his face turned away
from the camera. In the room, two of %(colegas)s at their desks: a man leans
back in his chair, mid-word, one hand open on the desk, palm down, as if
telling him to keep the case; a woman beside him listens with her arms folded. Their
faces are small. Daylight from the window.
''')

R[13] = (213, 'dia', ('fiscal_c4', 'colegas'), None, False, 'fiscalia_pueblo', '''
Medium shot at standing height, perfectly level, in the small office. In the
middle stands %(fiscal_c4)s, frontal three-quarter, the open case folder held
against his chest, looking from one side to the other. On the left edge, a
colleague points toward the window, toward the forest and the river beyond,
mid-word; on the right edge, another colleague holds both hands out, palms
up, toward the folder. The two colleagues are cut by the edges of the frame,
their faces small and in three-quarter back view. Daylight. The prosecutor
appears ONCE.
''')

R[14] = (199, 'dia', ('fiscal_c4',), None, False, 'fiscalia_pueblo', '''
Medium-close shot of %(fiscal_c4)s at his desk, three-quarter view, the camera
at seated height, perfectly level. He holds the receiver of the plain desk
telephone to his ear with his left hand, mid-word, while his right hand writes
a short list on a plain notepad, the lines plain grey scribbles. His eyes are
on the notepad, his brow drawn together, concentrated. The standing fan and
the window behind him. He appears ONCE.
''')

R[15] = (288, 'dia', ('fiscal_c4', 'funcionarios'), None, False, 'mesa_tecnica', '''
Wide shot of the interinstitutional meeting at the long plain table, the
camera at seated height just BEHIND %(fiscal_c4)s at the near end of the
table, perfectly level: his back and shoulder in the left foreground, his face
not visible. Along both sides of the table sit %(funcionarios)s; most of them
are raising their right hands to vote, open palms at shoulder height, while
two keep their hands on the table. Plain folders and glasses of water in front
of each. The blank projector screen and the window onto green hills behind.
''')

R[16] = (139, 'dia', ('fiscal_c4',), None, False, 'fiscalia_pueblo', '''
Overhead shot looking straight down at the prosecutor's desk: a man's two
hands in light grey shirt sleeves rolled to the elbow slide a closed plain
grey case folder into a large plain brown envelope, the folder halfway in.
Beside the envelope, a plain rubber stamp and a pen. Exactly two hands,
exactly ten fingers. No face. Daylight from one side.
''')

R[17] = (98, 'dia', ('madre',), None, False, 'resguardo', '''
Medium shot of %(madre)s standing alone on the muddy bank of the wide brown
river, in three-quarter back view, the camera at standing height behind her
and to her left, perfectly level. The small plain grey backpack hangs from
her right hand at her side. She looks out at the river, still. The far bank of
forest and the low cloud. Nobody else. She appears ONCE.
''')

R[18] = (256, 'dia', ('madre',), None, False, 'fiscalia_pueblo', '''
Medium shot outside the small Fiscalía office of the river town, the camera
at seated height on the street, perfectly level. %(madre)s sits on the plain
concrete step in front of the closed door, three-quarter view, a large plain
brown envelope lying unopened on her knees under her two hands, the small grey
backpack on the step beside her. She looks down the hot street, not at the
envelope, her mouth a straight line. A few parked motorcycles. Hard flat
daylight. She appears ONCE.
''')

R[19] = (297, 'hero', ('madre', 'taita'), None, True, 'resguardo', '''
Wide shot at dusk on the red-earth path, the camera at standing height,
perfectly level. In the right foreground, %(madre)s stands in three-quarter
back view, the small grey backpack in her hand, looking toward the house. In
the background, on the porch of the wooden house raised on posts, stands
%(taita)s, a solid dark silhouette with his tall staff of authority upright in
his hand, still. The light is low and weak and comes from the last grey of
the sky behind the house; everything else falls into near-black, the
plantains a dark mass. The silhouette has no face.
''')

NOMBRE = {1: 'el_camino', 2: 'el_taita', 3: 'la_puerta_abierta',
          4: 'la_puerta_cerrada', 5: 'la_madre', 6: 'el_cabildo',
          7: 'la_deliberacion', 8: 'el_baston', 9: 'la_autoridad',
          10: 'el_rio', 11: 'el_fiscal', 12: 'quedarse', 13: 'devolverlo',
          14: 'la_gestion', 15: 'la_mesa_tecnica', 16: 'la_remision',
          17: 'punto_muerto', 18: 'el_sobre', 19: 'en_ejercicio'}

CON_PERSONA = set(R) - {1, 3, 4}
SILUETAS = {2, 8, 9, 19}
CARTONES = {2, 4, 7, 9, 11, 13, 15, 16, 18, 19}
CENITALES = {16}
SOLO_MANOS = {8, 16}
SIN_CARA = {15}
TOPE_SIN_GENTE = 3
TOTAL = 3772
PIEZA = TOTAL + (182 + 119 + 48 + 119 + 182)

HOJAS = {5: ['madre'], 6: ['madre'], 10: ['madre'], 11: ['fiscal_c4', 'madre'],
         12: ['fiscal_c4'], 13: ['fiscal_c4'], 14: ['fiscal_c4'],
         15: ['fiscal_c4'], 17: ['madre'], 18: ['madre'], 19: ['madre']}

E_OFICINA = 'LP_U4C1_r01_la_noticia'
E_CUARTO = 'LP_U4C2_r05_la_sesion'
E_LADERA = 'LP_U2C2_r01_la_ladera'
E_NOCHE = 'LP_U2C2_r07_la_ventana'
ANCLAS = {1, 2, 6, 11, 15}

REF_PLACA = {
 1: ([E_LADERA], 'estilo', ''),
 2: ([E_LADERA], 'estilo', ''),
 6: ([E_LADERA], 'estilo', ''),
 11: ([E_OFICINA], 'estilo', ''),
 15: ([E_CUARTO], 'estilo', ''),
 3: (['ED_C4_r02_el_taita'], 'lugar', 'It is the SAME wooden house, seen from inside. '),
 4: (['ED_C4_r02_el_taita'], 'lugar', 'It is the SAME wooden house, now at dusk. '),
 5: (['ED_C4_r01_el_camino'], 'lugar', ''),
 7: (['ED_C4_r06_el_cabildo'], 'lugar', ''),
 8: (['ED_C4_r06_el_cabildo'], 'lugar', ''),
 9: (['ED_C4_r06_el_cabildo'], 'lugar', ''),
 10: (['ED_C4_r01_el_camino'], 'estilo', ''),
 12: (['ED_C4_r11_el_fiscal'], 'lugar', ''),
 13: (['ED_C4_r11_el_fiscal'], 'lugar', ''),
 14: (['ED_C4_r11_el_fiscal'], 'lugar', ''),
 16: (['ED_C4_r11_el_fiscal'], 'lugar', ''),
 17: (['ED_C4_r10_el_rio'], 'lugar', 'It is the SAME wide brown river and the SAME woman, now standing alone on its muddy bank; there is no boat. '),
 18: (['ED_C4_r11_el_fiscal'], 'lugar', 'It is the SAME office building, seen from the street outside. '),
 19: (['ED_C4_r02_el_taita'], 'lugar', 'It is the SAME wooden house and porch, now at dusk, seen from farther back on the path. '),
}

REUSA = {}

DET = {
 (15, 'las_manos'): dict(cuadros=90, entra=150,
     registro='dia',
     personas=('funcionarios',),
     escena='Close shot at table height along the long plain table: four or '
            'five raised open right hands at shoulder height, palms forward, '
            'of men and women in plain grey sleeves, one behind the other '
            'down the table, and between them two hands resting flat on '
            'closed plain folders. No faces: the frame is cut at the '
            'shoulders. Daylight from the window.',
     gesto='The raised hands stay up, steady, and one of the resting hands '
           'slowly rises to join them. Nothing else moves.'),
}

BROLL = {}

MOV = {
 # 3 nov, pase previo: boca en un plano de habla
 13: 'kling: el fiscal mira a un colega y al otro; los dos hablan con las manos',
 10: 'kling: la lancha avanza por el río; ella quieta con el morral',
 17: 'kling: el río corre; el viento mueve apenas la ropa; ella quieta',
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
        fallos.append('rotulo y carton en la misma ranura: %s' % (set(LOWER_THIRD) & CARTONES))
    for (n, _), d in DET.items():
        if d['entra'] < 60 or d['entra'] + d['cuadros'] > R[n][0]:
            fallos.append('detalle r%02d fuera de su ranura' % n)
    return fallos, tot, mejor
