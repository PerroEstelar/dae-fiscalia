# -*- coding: utf-8 -*-
r"""CASO 5 · La denuncia de Valentina · 20 ranuras · 3531 cuadros. Narra
Pilar; las dos preguntas del funcionario (r05, r10) las dice Julián.

LO QUE SE OYE ENCIMA (cruce_ed.json)
    r01-r02  Valentina, mujer trans de 29 años, decide denunciar que su
             excompañero la siguió y amenazó; reúne el valor y va a la Fiscalía
    r03-r05  en la recepción le piden la cédula; el nombre no coincide; le
             pregunta en voz alta frente a los que esperan: «¿nombre real o
             apodo?»; ella explica que Valentina es su nombre identitario
    r06-r08  la llama «él» aunque ella lo corrige; consigna el nombre legal y
             «alias Valentina» en observaciones: el campo de los apodos de
             los investigados
    r09-r11  el hostigamiento: «¿su pareja o su amante?»
    r12-r17  el formulario pregunta orientación sexual y no identidad: la
             única casilla; escribe «hombre gay», que ella nunca dijo; no
             transcribe: sustituye
    r18-r20  sale sintiéndose señalada; no vuelve a insistir

QUIÉN LLEVA CARA
    Valentina siempre, con su abrigo mostaza (el acento). Es una mujer: el
    dibujo no la exagera ni la caricaturiza en nada. El funcionario nunca
    (biblia §3): de espaldas, sobre el hombro o en manos. El excompañero es
    una silueta lejana bajo un farol. Los que esperan turno, sin rostro
    legible.

LA PUESTA EN ESCENA
    La calle de noche (r01) y la casa de noche (r20) abren y cierran. En el
    medio, la recepción (r03-r05) y el escritorio de la denuncia (r06-r17):
    contraplanos sobre el hombro del funcionario, primeros planos de ella, y
    el papel -la casilla de observaciones, la única casilla, el sello-.
"""

R = {}

R[1] = (227, 'hero', ('valentina', 'expareja'), None, False, 'calle_noche', '''
Wide shot of a residential street at night, the camera at standing height on
the pavement, perfectly level. In the middle ground, %(valentina)s walks
TOWARD the camera through the pool of light under one white street lamp,
caught mid-stride, her right heel lifted, her mustard coat open; she glances
back over her left shoulder, her face in three-quarter profile, her mouth
closed, her hand holding the strap of her bag tight. Far behind her, at the
end of the street under another lamp, stands %(expareja)s, small, still. Wet
pavement, parked small cars, the dark houses behind their grilles; everything
outside the two pools of light falls into deep darkness. She is a woman of
twenty-nine; nothing exaggerated, no caricature. She appears ONCE.
''')

R[2] = (137, 'dia', ('valentina',), None, False, 'fiscalia_fachada', '''
Medium shot at the entrance of the prosecution office building in the
morning, the camera at the foot of the concrete steps at standing height,
perfectly level. %(valentina)s climbs the steps toward the plain glass door,
three-quarter back view turning to profile, caught mid-step, her right foot
on the higher step; in her right hand, held in front of her, a plain grey
identity card with nothing legible on it. Her chin is level, her eyes on the
door. A few people come and go small at the edges of the frame. Flat daylight.
She appears ONCE.
''')

R[3] = (123, 'dia', ('valentina', 'funcionario'), None, False, 'recepcion', '''
Over-the-shoulder shot from BEHIND the reception counter, the camera at
seated height, perfectly level. In the left foreground, the balding back of
the head and the pale grey shoulder of %(funcionario)s, filling the left third
of the frame: his face is entirely hidden by his own head. Across the counter,
on the other side of the low pane of plain glass, %(valentina)s stands in
three-quarter view and slides her plain grey identity card across the counter
toward him with two fingers, her eyes on him, her mouth closed. Flat
fluorescent light. She appears ONCE.
''')

R[4] = (241, 'dia', ('turno', 'valentina', 'funcionario'), None, False, 'recepcion', '''
Wide shot of the reception hall from behind the rows of plastic waiting
chairs, the camera at seated height, perfectly level. In the foreground and
the middle ground, %(turno)s sit in the chairs seen from behind; several of
them have turned their heads toward the counter, their faces in lost profile,
not readable. At the counter in the background, %(valentina)s stands very
still in three-quarter view, her mustard coat the only colour in the hall,
facing the official, who is a grey shape behind the glass seen from the side.
Flat fluorescent light.
''')

R[5] = (175, 'dia', ('valentina',), None, False, 'recepcion', '''
Close-up of %(valentina)s at the counter, from the collar up, three-quarter
view, the camera at her eye level, perfectly level. She answers: her lips
parted mid-word, her chin level, her eyes steady on the official out of frame
to the left, the iris and the pupil clear. Her face is composed and direct:
not a smile, not tears. The collar of the mustard coat at the bottom of the
frame. The hall behind her soft and plain. She is a woman; nothing
exaggerated, no caricature.
''')

R[6] = (221, 'dia', ('valentina', 'funcionario'), None, False, 'escritorio_denuncia', '''
Over-the-shoulder shot from BEHIND the official at the complaints desk, the
camera at seated height, perfectly level. In the right foreground, the balding
back of the head and the pale grey shoulder of %(funcionario)s, filling the
right third of the frame: his face is entirely hidden by his own head; his
right hand rests on the computer mouse. Across the desk, %(valentina)s sits in
three-quarter view, upright, her right hand raised slightly from the desk, open,
palm toward him, mid-correction, her lips parted on a word, her eyes on him.
The grey partition panels behind her. She appears ONCE.
''')

R[7] = (256, 'dia', ('funcionario',), None, False, 'escritorio_denuncia', '''
Close shot at desk height, perfectly level, of a printed one-page complaint
form of plain grey bars lying on the desk. At the bottom of the form, a wide
empty box; a man's right hand in a pale grey shirt cuff writes inside that
box with a plain pen, mid-stroke, and what he writes is a short plain grey
scribble with no letters. Exactly one hand, five fingers. The rest of the form
plain grey bars. No face. Flat light from one side.
''')

R[8] = (190, 'dia', ('funcionario',), None, False, 'escritorio_denuncia', '''
(reusa la placa de la r07 con otra cámara)
''')

R[9] = (153, 'dia', ('valentina',), None, False, 'escritorio_denuncia', '''
Medium shot of %(valentina)s at the complaints desk, from the side, the camera
at seated height, perfectly level, in clean profile facing left. She speaks,
mid-sentence, leaning slightly forward; on the desk between her two hands
lies her mobile phone, face up, its screen dark. Her eyes are on the official
out of frame to the left. The grey partition behind her. She appears ONCE.
''')

R[10] = (217, 'dia', ('funcionario', 'valentina'), None, False, 'escritorio_denuncia', '''
Over-the-shoulder shot from BEHIND the official, the camera at seated height,
perfectly level. In the left foreground, %(funcionario)s leans BACK in his
chair, his balding head and his pale grey shoulder filling the left third of
the frame, his face hidden by his own head, one hand lifted from the desk.
Across the desk, %(valentina)s has gone still: her eyebrows lifted very
slightly, her mouth closed in a straight line, her two hands flat on the desk
on either side of her phone. Her eyes on him. She appears ONCE.
''')

R[11] = (158, 'dia', ('valentina',), None, False, 'escritorio_denuncia', '''
Close shot of %(valentina)s in clean profile facing right, from the shoulders
up, the camera at her eye level, perfectly level. She looks down at the desk
in front of her, her eyelids lowered, her jaw set, her lips pressed together.
A strand of her dark wavy hair falls forward over her shoulder onto the
mustard coat. The grey partition behind her, soft. She appears ONCE.
''')

R[12] = (161, 'dia', ('funcionario',), None, False, 'escritorio_denuncia', '''
Over-the-shoulder shot from behind the official, close on the ordinary
computer screen on the desk, the camera at his seated eye level, perfectly
level. The screen shows a form made only of plain grey bars and, near the
middle, one row of small empty square boxes; nothing on the screen is
legible: no letters, no numbers, no icons. In the left foreground, his pale
grey shoulder and the back of his head, out of focus; his right hand on the
mouse at the bottom of the frame.
''')

R[13] = (160, 'dia', (), None, False, 'escritorio_denuncia', '''
Overhead shot looking STRAIGHT DOWN at the printed one-page complaint form
lying flat on the desk, the page filling the middle of the frame. The page is
only plain grey bars, and in its exact middle there is ONE single small empty
square box beside one grey bar. That is the ONLY box on the whole page: there
are no other boxes, no rows of boxes, no tick boxes anywhere else, above or
below. A plain pen lies beside the form, a plain rubber stamp at the corner.
Nobody in the frame, no hand. Flat light from one side.
''')

R[14] = (157, 'dia', ('valentina',), None, False, 'escritorio_denuncia', '''
Medium-close shot of %(valentina)s at the desk, frontal three-quarter, the
camera at her seated eye level, perfectly level. She answers the question:
her lips parted mid-word, her chin level, her right hand resting open on the
desk, her eyes on the official out of frame to the right. Calm and precise:
not a smile, not anger. The grey partition behind her. She is a woman;
nothing exaggerated, no caricature. She appears ONCE.
''')

R[15] = (156, 'dia', ('funcionario',), None, False, 'escritorio_denuncia', '''
The same overhead shot of the same printed form on the desk, the single small
box in its middle; now a man's right hand in a pale grey shirt cuff writes
beside that box with the plain pen, mid-stroke, and what he writes is a short
plain grey scribble with no letters. Exactly one hand, five fingers. No face.
''')

R[16] = (208, 'dia', ('valentina',), None, False, 'escritorio_denuncia', '''
Medium shot of %(valentina)s at the desk, three-quarter view, the camera at
her seated eye level, perfectly level. She holds the printed form up in both
hands at chest height, reading it; the page shows only plain grey bars toward
the camera. Her eyes are on the middle of the page, her brows drawn together
very slightly, her mouth closed. The grey partition behind her. She appears
ONCE.
''')

R[17] = (165, 'dia', ('funcionario',), None, False, 'escritorio_denuncia', '''
Close shot at desk height, perfectly level: a man's right hand in a pale grey
shirt cuff presses a plain rubber stamp down onto the bottom of the printed
form on the desk, his wrist straight, the stamp touching the paper; the mark
it leaves is a plain grey rectangle with nothing legible in it. Exactly one
hand. No face. Flat light from one side.
''')

R[18] = (139, 'dia', ('valentina',), None, False, 'fiscalia_fachada', '''
Medium-wide shot at the entrance of the prosecution office building, the
camera at standing height on the pavement, perfectly level. %(valentina)s
comes out through the plain glass door and down the concrete steps, frontal
three-quarter, caught mid-step, the folded form in her left hand, her right
hand pulling her mustard coat closed; her eyes down on the steps. People
going in past her, small. Flat daylight. She appears ONCE.
''')

R[19] = (184, 'contraluz', ('valentina',), None, False, 'fiscalia_fachada', '''
Medium-close shot of %(valentina)s standing still on the pavement at the
foot of the steps, in near profile facing left, the camera at her eye level,
perfectly level. The bright street behind her is the only bright thing in
the frame; she is in soft shadow. She holds the folded form in her hand at
her side, not looking at it; her eyes are on the street, her mouth a straight
line. She appears ONCE.
''')

R[20] = (103, 'hero', ('valentina',), None, False, 'apartamento', '''
Medium shot of the small apartment at night, the camera at seated height,
perfectly level. %(valentina)s sits at the plain table by the window, in
three-quarter back view, her face turned to the window in lost profile,
looking out at the street lamps through the grille. On the table in front of
her, the folded form lies closed, untouched. She wears only her plain grey
high-neck blouse: her mustard coat is NOT on her, it hangs over the back of
the other chair, the only coat in the picture. One plain lamp in the corner is the only light;
everything else falls into deep shadow. She appears ONCE.
''')

NOMBRE = {1: 'la_calle', 2: 'la_entrada', 3: 'la_cedula', 4: 'en_voz_alta',
          5: 'su_nombre', 6: 'la_correccion', 7: 'observaciones',
          8: 'el_campo_de_apodos', 9: 'el_hostigamiento', 10: 'la_pregunta',
          11: 'el_perfil', 12: 'el_formulario', 13: 'la_unica_casilla',
          14: 'la_respuesta', 15: 'la_casilla', 16: 'lo_que_no_dijo',
          17: 'el_sello', 18: 'la_salida', 19: 'senalada',
          20: 'no_volvio'}

CON_PERSONA = set(R) - {13}
SILUETAS = {1}
CARTONES = {1, 4, 7, 8, 10, 12, 13, 15, 17, 19}
CENITALES = {13, 15}
SOLO_MANOS = {7, 15, 17}
SIN_CARA = {12}
TOPE_SIN_GENTE = 3
TOTAL = 3531
PIEZA = TOTAL + (182 + 119 + 48 + 119 + 182)

HOJAS = {n: ['valentina'] for n in (1, 2, 3, 4, 5, 6, 9, 10, 11, 14, 16, 18, 19, 20)}

E_OFICINA = 'LP_U4C1_r01_la_noticia'
E_CALLE = 'LP_U2C1_r01_la_calle_de_bodegas'
E_NOCHE = 'LP_U2C2_r07_la_ventana'
E_RECEPCION = 'DH_U1_r10_la_recepcion'
ANCLAS = {1, 2, 3, 6, 20}

REF_PLACA = {
 1: ([E_NOCHE], 'estilo', ''),
 2: ([E_CALLE], 'estilo', ''),
 3: ([E_RECEPCION], 'estilo', ''),
 6: ([E_OFICINA], 'estilo', ''),
 20: ([E_NOCHE], 'estilo', ''),
 4: (['ED_C5_r03_la_cedula'], 'lugar', 'It is the SAME reception hall and the SAME woman. '),
 5: (['ED_C5_r03_la_cedula'], 'lugar', ''),
 7: (['ED_C5_r06_la_correccion'], 'lugar', ''),
 9: (['ED_C5_r06_la_correccion'], 'lugar', ''),
 10: (['ED_C5_r06_la_correccion'], 'lugar', 'It is the SAME desk, the SAME official and the SAME woman. '),
 11: (['ED_C5_r06_la_correccion'], 'lugar', ''),
 12: (['ED_C5_r06_la_correccion'], 'lugar', ''),
 13: (['ED_C5_r07_observaciones'], 'lugar', ''),
 14: (['ED_C5_r06_la_correccion'], 'lugar', ''),
 15: (['ED_C5_r13_la_unica_casilla'], 'mismo', 'It is the SAME form from the SAME overhead camera; only now a man\'s hand writes beside the single box. '),
 16: (['ED_C5_r06_la_correccion'], 'lugar', ''),
 17: (['ED_C5_r07_observaciones'], 'lugar', ''),
 18: (['ED_C5_r02_la_entrada'], 'lugar', 'It is the SAME entrance and the SAME woman. '),
 19: (['ED_C5_r02_la_entrada'], 'lugar', ''),
}

REUSA = {
 8: (7, dict(encuadre=0.78, empuje=0.05, centro=[0.50, 0.70])),
}

DET = {
 # 4 nov (revision de Sebastian, marcador 1051: «aqui esta hablando un
 # funcionario, no ella, it's misleading»). La r05 abre con la pregunta de
 # Julian (e05, 1037-1094) sobre el primer plano de ella HABLANDO (el Kling de
 # la boca). Un contraplano del funcionario preguntando -de espaldas, como
 # siempre- tapa ese tramo: 1029-1100, el corte justo antes de «Valentina
 # explico» (1105). `abre`: entra en el cuadro 0 de la ranura (un contraplano,
 # no un detalle a mitad de plano).
 (5, 'la_pregunta'): dict(cuadros=71, entra=0, abre=True,
     registro='dia',
     personas=('funcionario', 'valentina'),
     hojas=['valentina'],
     lugar='recepcion',
     ref=(['ED_C5_r03_la_cedula'], 'mismo', 'It is the SAME counter, the SAME '
          'official and the SAME woman, from the SAME camera and light; the '
          'ONLY changes are that he now holds her identity card up beside his '
          'head as he asks his question, his head turned a little toward her, '
          'and that she stands still, waiting, her mouth closed.'),
     escena='Over-the-shoulder shot from BEHIND the reception counter, the '
            'camera at seated height, perfectly level. In the left '
            'foreground, the balding back of the head and the pale grey '
            'shoulder of %(funcionario)s, filling the left third of the frame, '
            'his head turned a little toward her as he speaks: his face is '
            'entirely hidden by his own head. His right hand holds her plain '
            'grey identity card up beside his head, nothing legible on it. '
            'Across the counter, on the other side of the low pane of plain '
            'glass, %(valentina)s stands in three-quarter view, very still, '
            'waiting: her mouth closed in a straight line, her eyes on him, '
            'her hands at her sides. Flat fluorescent light. She appears ONCE.',
     gesto='Nothing moves.'),
 (4, 'la_cedula'): dict(cuadros=84, entra=140,
     registro='dia',
     personas=('funcionario',),
     escena='Extreme close shot at counter height of a man\'s right hand in a '
            'pale grey shirt cuff holding a plain grey identity card up off '
            'the counter between thumb and forefinger; the card is plain '
            'grey with a darker grey rectangle where a photo would be and '
            'plain grey bars, NO face, NO letters, NO numbers. Exactly one '
            'hand. Flat fluorescent light.',
     gesto='The hand tilts the card slowly toward the light and holds it '
           'there. Nothing else moves.'),
 (16, 'el_dedo'): dict(cuadros=84, entra=120,
     registro='dia',
     personas=('valentina',),
     escena='Extreme close shot of a woman\'s right index finger stopped on '
            'the printed form beside a single small square box with a short '
            'plain grey scribble next to it, the cuff of a matte mustard wool '
            'coat at her wrist. Exactly one hand. All the paper lies flat. '
            'Flat light.',
     acento='her wool coat',
     gesto='The finger stays pressed beside the box; the paper does not move. '
           'Only the finger presses a little harder. Nothing else moves.'),
}

BROLL = {}

MOV = {
 # 3 nov, pase previo: boca en un plano de habla
 5: 'kling: Valentina responde, serena; parpadea y respira entre frases',
 1: 'kling: Valentina camina hacia la cámara bajo el farol; la silueta lejana quieta',
 18: 'kling: Valentina baja los escalones y sale de cuadro',
}

LOWER_THIRD = {2: 'Valentina'}


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
        if (d['entra'] < 60 and not d.get('abre')) or d['entra'] + d['cuadros'] > R[n][0]:
            fallos.append('detalle r%02d fuera de su ranura' % n)
    return fallos, tot, mejor
