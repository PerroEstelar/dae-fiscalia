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
    El abuso no tiene imagen: la r04 es la puerta cerrada al atardecer con el
    bastón de mando al lado. El Taita es SILUETA siempre: no tiene cara
    (biblia §3 y la regla de la serie para quien agrede).

LA NIÑA (4 nov, revisión de Sebastián: «I know it's a minor but it's
fictional, please go ahead and create a character sheet and insert her in
this environment»). Hasta el pase previo no se dibujaba. Ahora es Yaneth
(hoja `nina`): una niña común camino a la escuela (r01, con su rótulo) y al
lado de su madre en el punto muerto (r17, r18, r19). Nunca en la casa del
Taita ni cerca de él; en la r19 está de espaldas, de la mano de la madre, y
el Taita lejos, en su porche. `base_ed.C_NINA` va en cada placa donde está.

QUIÉN LLEVA CARA
    La madre, siempre, con su blusa mostaza: es el acento del caso. El
    fiscal también -duda, no decide mal por cuenta propia-, pero el plano de
    la remisión (r16) es solo manos y el cartón del error no cae sobre su
    cara. Los colegas y los funcionarios de la mesa, pequeños.

LA RIMA
    r02 el Taita en su porche al principio; r19 el mismo porche al final, con
    la madre y la niña de espaldas en primer plano: «permanecía en ejercicio
    de su cargo». El contrapicado del Taita (inserto de la r19) cierra.

REVISIÓN DE SEBASTIÁN (4 nov, marcadores en SU línea v2; cirugía, sin
remontar, solo stills):
    415  r01  presentar a la niña: hoja + placa 'mismo' con ella en el camino
              y rótulo «Yaneth Payaguaje · Niña de la comunidad»
    590  r02  «Taita» con tilde en la primera a: palabra injertada en el
              máster (`voz/taita_c4.py`)
    849  r03  otro ángulo: picado general del resguardo desde la ladera
    1121 r04  muy oscura: GRIS + SIN_TECHO
    3198 r15  el inserto con manos levantadas sobra después del plano de la
              votación: la misma mesa con las manos quietas (la_mesa)
    3466 r17, 3550 r18, 3836 r19  la niña con su madre ('mismo'); la r19
              además GRIS + SIN_TECHO
    3979 r19  inserto de apoyo: contrapicado del Taita en sombra
"""

R = {}

R[1] = (254, 'dia', ('nina',), None, False, 'resguardo', '''
Wide shot of a red-earth path through the reserve on a misty morning, the
camera at standing height on the path, perfectly level. The path runs from
the foreground into the distance between tall plantains and chontaduro
palms, and halfway along it passes in front of a wooden house raised on short
posts with a plain zinc roof and a wooden porch. On the path, in the middle
ground between the camera and the house, %(nina)s walks TOWARD the camera on
her way to school, frontal three-quarter view, mid-stride, the small plain
grey school backpack on both shoulders, both hands holding its straps, her
eyes on the path ahead. Her whole figure is visible from her braid to her
boots, about two fifths of the frame height. The wooden house stays behind
her, far back on the path. Low cloud on the green hills. She is the only
person in the frame and appears ONCE.
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

R[3] = (264, 'dia', (), None, False, 'resguardo', '''
High wide shot from the green hillside above the reserve, the camera on the
slope pointing DOWN over the whole community, the horizon level. Below, the
red-earth path winds between the tall plantains and chontaduro palms past
scattered wooden houses raised on short posts with plain zinc roofs. In the
near middle ground, at a bend of the path, the wooden house with its porch;
further along, the large high thatched roof of the open community house of
the cabildo; beyond, the wide brown river and the forest, low cloud on the
far hills. Three or four tiny figures of people of the community far away on
the path, going about their day, too small to read. Morning daylight.
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

R[17] = (98, 'dia', ('madre', 'nina'), None, False, 'resguardo', '''
Medium shot of %(madre)s standing on the muddy bank of the wide brown river,
in three-quarter back view, the camera at standing height behind her and to
her left, perfectly level. The small plain grey backpack hangs from her right
hand at her side. At her left side stands her daughter, %(nina)s, also in
three-quarter back view, her head at the height of her mother's chest, her
right hand holding her mother's left hand. Both look out at the river, still.
The far bank of forest and the low cloud. Nobody else. Each person appears
ONCE.
''')

R[18] = (256, 'dia', ('madre', 'nina'), None, False, 'fiscalia_pueblo', '''
Medium shot outside the small Fiscalía office of the river town, the camera
at seated height on the street, perfectly level. %(madre)s sits on the plain
concrete step in front of the closed door, three-quarter view, a large plain
brown envelope lying unopened on her knees under her two hands. Beside her on
the step, close against her side, sits her daughter, %(nina)s, the small
plain grey school backpack on her lap under her hands. Both look down the hot
street, not at the envelope, their mouths straight lines. A few parked
motorcycles. Hard flat daylight. Each person appears ONCE.
''')

R[19] = (297, 'hero', ('madre', 'nina', 'taita'), None, True, 'resguardo', '''
Wide shot at dusk on the red-earth path, the camera at standing height,
perfectly level. In the right foreground, %(madre)s stands in three-quarter
back view, the small grey backpack in her hand, looking toward the house;
close at her side stands her daughter, %(nina)s, also in three-quarter back
view, her head at the height of her mother's chest, holding her mother's
other hand and looking toward the house too. In the background, on the porch
of the wooden house raised on posts, stands %(taita)s, a solid dark
silhouette with his tall staff of authority upright in his hand, still, far
from them. The light is low and weak and comes from the last grey of the sky
behind the house; the shadows are a deep grey in which the forms can still be
read, never pure black, the plantains a dark grey mass. The silhouette has no
face.
''')

NOMBRE = {1: 'el_camino', 2: 'el_taita', 3: 'la_puerta_abierta',
          4: 'la_puerta_cerrada', 5: 'la_madre', 6: 'el_cabildo',
          7: 'la_deliberacion', 8: 'el_baston', 9: 'la_autoridad',
          10: 'el_rio', 11: 'el_fiscal', 12: 'quedarse', 13: 'devolverlo',
          14: 'la_gestion', 15: 'la_mesa_tecnica', 16: 'la_remision',
          17: 'punto_muerto', 18: 'el_sobre', 19: 'en_ejercicio'}

CON_PERSONA = set(R) - {3, 4}
SILUETAS = {2, 8, 9, 19}
CARTONES = {2, 4, 7, 9, 11, 13, 15, 16, 18, 19}
CENITALES = {16}
SOLO_MANOS = {8, 16}
SIN_CARA = {15}
TOPE_SIN_GENTE = 3
TOTAL = 3772
PIEZA = TOTAL + (182 + 119 + 48 + 119 + 182)

HOJAS = {1: ['nina'], 5: ['madre'], 6: ['madre'], 10: ['madre'],
         11: ['fiscal_c4', 'madre'], 12: ['fiscal_c4'], 13: ['fiscal_c4'],
         14: ['fiscal_c4'], 15: ['fiscal_c4'], 17: ['madre', 'nina'],
         18: ['madre', 'nina'], 19: ['madre', 'nina']}

E_OFICINA = 'LP_U4C1_r01_la_noticia'
E_CUARTO = 'LP_U4C2_r05_la_sesion'
E_LADERA = 'LP_U2C2_r01_la_ladera'
E_NOCHE = 'LP_U2C2_r07_la_ventana'
ANCLAS = {1, 2, 6, 11, 15}

REF_PLACA = {
 # 4 nov (revision): las placas con la nina son el MISMO plano aprobado
 1: (['ED_C4_r01_el_camino'], 'mismo', 'It is the SAME path, the SAME house, '
     'the SAME camera and the SAME light; the ONLY change is the girl walking '
     'on the path toward the camera.'),
 2: ([E_LADERA], 'estilo', ''),
 6: ([E_LADERA], 'estilo', ''),
 11: ([E_OFICINA], 'estilo', ''),
 15: ([E_CUARTO], 'estilo', ''),
 3: (['ED_C4_r01_el_camino'], 'lugar', 'It is the SAME reserve, the SAME '
     'red-earth path and the SAME wooden house, now seen from high on the '
     'hillside above, with the whole community below. '),
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
 17: (['ED_C4_r17_punto_muerto'], 'mismo', 'It is the SAME river bank, the '
      'SAME woman in the SAME place and pose, the SAME camera and light; the '
      'ONLY change is that her daughter now stands at her left side, holding '
      'her hand.'),
 18: (['ED_C4_r18_el_sobre'], 'mismo', 'It is the SAME street, the SAME step, '
      'the SAME woman with the SAME envelope, the SAME camera and light; the '
      'ONLY change is that her daughter now sits beside her on the step with '
      'the small grey backpack on her lap.'),
 19: (['ED_C4_r19_en_ejercicio'], 'mismo', 'It is the SAME path at dusk, the '
      'SAME house and porch with the SAME silhouette, the SAME woman, the SAME '
      'camera; the ONLY changes are that her daughter now stands close at her '
      'side holding her hand, and that the shadows are a lighter deep grey '
      'where the forms can be read, never pure black.'),
}

REUSA = {}

DET = {
 # 4 nov (revision, marcador 3198): el inserto de las manos levantadas venia
 # pegado al plano de la votacion y se leia raro. La misma mesa, la misma
 # gente presente, nadie levanta la mano. Es el MISMO plano que el inserto
 # anterior (`mismo_de`), quieto.
 (15, 'la_mesa'): dict(cuadros=90, entra=150,
     registro='dia',
     personas=('funcionarios',),
     mismo_de='ED_C4_r15_las_manos_det',
     cambio='It is the SAME close shot along the SAME table with the SAME '
            'people and the SAME light; the ONLY change is that NOBODY raises '
            'a hand: every hand rests on the table.',
     escena='Close shot at table height along the long plain table during the '
            'meeting: the hands of the men and women in plain grey sleeves rest '
            'on the table one behind the other down its length -two hands '
            'folded together, a hand lying flat on a closed plain folder, a '
            'hand holding a plain pen beside a notepad, a hand next to a glass '
            'of water-. Every hand rests on the table; nobody raises a hand. '
            'No faces: the frame is cut at the shoulders. Daylight from the '
            'window.',
     gesto='Nothing moves.'),
 # 4 nov (revision, marcador 3979): el plano de apoyo del final, de abajo
 # hacia arriba, el Taita en sombra. Hasta el corte al respiro.
 (19, 'el_contrapicado'): dict(cuadros=94, entra=203,
     registro='hero',
     personas=('taita',),
     # primera tirada: de frente, a la altura del piso del porche, y una
     # mujer de mostaza al borde derecho. Se pide el angulo por sus efectos.
     escena='Low-angle shot from the red-earth path at dusk, the camera on '
            'the ground at the foot of the porch steps and pointing steeply '
            'UP at %(taita)s, who stands at the top of the steps on the porch '
            'of his wooden house: we see him from below, his legs and body '
            'large in the frame and his head small against the zinc roof '
            'edge and the last grey of the sky; the undersides of the roof '
            'beams are visible above him. His tall carved staff of authority '
            'is upright in his right hand, its plain ribbons hanging still, '
            'the SAME staff as in the reference. Behind him, the dark plank '
            'wall and the doorway of his house. He is the ONLY person in the '
            'frame: nobody else anywhere, no woman, no child. He has no face, '
            'no features, no skin tone: a shadowy shape. The shadows are a '
            'deep grey where the planks can still be read, never pure black. '
            'The vertical posts lean in toward the top because the camera '
            'looks up, but the camera is not rolled.',
     gesto='Nothing moves.'),
}

BROLL = {}

MOV = {
 # 3 nov, pase previo: boca en un plano de habla
 13: 'kling: el fiscal mira a un colega y al otro; los dos hablan con las manos',
 10: 'kling: la lancha avanza por el río; ella quieta con el morral',
 # 17: retirado el 4 nov (la placa nueva lleva a la nina; el clip era de la
 # madre sola)
}

# 4 nov (revision): la nina tiene nombre en la voz -«Yaneth Payaguaje, niña de
# la comunidad»- y se presenta en la r01 (lowerthirds_ed, C4)
LOWER_THIRD = {1: 'Yaneth Payaguaje · Niña de la comunidad'}

# 4 nov (revision, marcadores 1121 y 3836: «graded too dark, blacks are too
# black»). La regla de la biblia §11 (la serie es gris): la curva de sombra en
# todo el C4, y las dos que marco sin techo. Medido en su linea (p2/p50):
# r04 13/16 y r19 15/17; las de dia 22-23/83-86; r02 y r09 (contraluz) 20/60.
GRIS = (30, 130)
SIN_TECHO = {4, 19}

# 4 nov: la r01 cambia (Yaneth en el camino) y el respiro de su linea es la
# r01 vacia: se queda como esta.
RESPIRO_FIJO = True


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
