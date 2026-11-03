# -*- coding: utf-8 -*-
r"""CASO 3 · El patrullero Wilmer · 25 ranuras · 4697 cuadros. Narra Carlos;
la frase de Wilmer (r19) la dice Andrés.

LO QUE SE OYE ENCIMA (cruce_ed.json)
    r01-r03  seis años en la Policía; turno de noche en el aeropuerto; la
             llamada de la tripulación; dos pasajeros ebrios no quieren bajar
    r04-r08  sube con un compañero, les explica con calma; se niegan y se
             resisten; lo golpean; los pasajeros graban; el video circula
    r09-r13  el traslado: las expresiones racistas; siguen en la estación;
             «ya estamos llamando al coronel»
    r14-r17  el fiscal de turno imputa solo violencia contra servidor
             público, sin el art. 58-3 ni el 134 B; esa noche quedan libres
    r18-r19  semanas después, disculpas; Wilmer a un medio local: «lo que más
             me dolió no fueron los golpes...»
    r20-r25  la revisión: el patrón verbal no se había valorado; la adición a
             la imputación; la dimensión racial restituida

LO QUE NO SE DIBUJA
    Los golpes. La r06 es la mano de Wilmer en el antebrazo del hombre, y el
    corte siguiente son los celulares en alto. Los dos agresores son formas
    oscuras, de espaldas o en sombra: nunca una cara legible. Ningún
    uniforme, insignia ni placa: chaqueta de campo azul noche lisa.

LA LUZ
    Es una pieza de noche. Hero en el andén (r01) y en el código cerrado
    (r16); contraluz en la terminal (r09-r11); luz de techo en la cabina, el
    puesto y la audiencia nocturna (el registro 'dia' con `NOCHE_INTERIOR`).
    La revisión (r20-r23) es de día. Cierra al amanecer, con luz plana (r24).
    Sin acento: la pieza no tiene prenda.

QUIÉN LLEVA CARA
    Wilmer siempre. El fiscal de turno nunca (biblia §3). La fiscal que
    revisa, sí: su decisión es la que corrige. La rima: el formato con UNA
    casilla marcada (r15) y el mismo formato con tres (r23).
"""

R = {}

R[1] = (169, 'hero', ('wilmer',), None, False, 'aeropuerto', '''
Medium-wide shot on the apron of the small airport at night, the camera at
standing height, perfectly level. In the right foreground, %(wilmer)s stands
in three-quarter view from the waist up, a plain handheld radio clipped to
his chest, his eyes on the plane. Behind him, in the middle of the frame, the
plain white passenger jet with no livery stands under one flat white
floodlight, its boarding stair against the open front door, the only lit
thing in the night; everything else falls into deep darkness, the dark hills
beyond. He appears ONCE.
''')

R[2] = (97, 'dia', ('wilmer', 'companero'), None, False, 'terminal', '''
Medium shot in the nearly empty departures hall at night, the camera at
standing height, perfectly level. %(wilmer)s, three-quarter view, holds his
plain radio up to his mouth with his right hand, mid-word, his eyes on the
dark windows toward the apron. Beside him and slightly behind, %(companero)s
turns his head toward him, listening. The plain rows of empty seats and the
polished floor reflecting the ceiling lamps behind them. Each person appears
ONCE.
''')

R[3] = (215, 'dia', ('azafata', 'agresores', 'pasajeros'), None, False, 'cabina', '''
Medium shot down the narrow aisle of the passenger cabin, the camera at
standing height in the aisle, perfectly level. In the middle ground,
%(azafata)s stands in the aisle, three-quarter view, bending slightly toward
two seated men, her right hand open toward the front door of the plane, her
mouth mid-word. The two men are %(agresores)s: seen from behind over the tops
of their seats, one with his arm flung across the back of the seat, the other
with his head tipped back, neither of them getting up. In the rows around
them, %(pasajeros)s turn in their seats to look. Each person appears ONCE.
''')

R[4] = (246, 'dia', ('wilmer', 'companero', 'pasajeros'), None, False, 'cabina', '''
Medium shot looking down the same narrow aisle from the rear of the cabin
toward the front, the camera at standing height, perfectly level.
%(wilmer)s walks down the aisle TOWARD the camera, caught mid-stride, his left
foot planted and his right heel lifted, his two hands open and low at his
sides; behind him, %(companero)s follows. On both sides, %(pasajeros)s in
their seats turn their heads to watch them pass. Ceiling lights of the cabin.
Each policeman appears ONCE.
''')

R[5] = (132, 'dia', ('wilmer', 'agresores'), None, False, 'cabina', '''
Over-the-shoulder shot from BEHIND one of the two drunk passengers in his
seat, the camera at seated height, perfectly level. In the left foreground,
the dark back of his head and his shoulder in a light shirt, in shadow, his
face never visible: he jerks his elbow away toward the window. Standing in the
aisle, %(wilmer)s bends slightly toward him, three-quarter view, his right
hand open and still in the air, palm down, calm, his mouth mid-word, his eyes
on the man. Ceiling light of the cabin. Wilmer appears ONCE.
''')

R[6] = (235, 'dia', ('wilmer', 'agresores'), None, False, 'cabina', '''
Close shot at chest height in the aisle, perfectly level. %(wilmer)s, in
profile facing left, holds the forearm of one of the two passengers firmly
with his right hand, guiding him up out of his seat toward the door; the
passenger is a dark shape twisting away from the camera, his face hidden in
shadow and turned away. Wilmer's face is set, his jaw tight, his eyes on the
man. Nobody strikes anybody in this picture: only the hand on the forearm and
the body twisting away. Ceiling light. Each person appears ONCE.
''')

R[7] = (110, 'dia', ('pasajeros',), None, False, 'cabina', '''
Medium shot across the rows of seats from the side of the cabin, the camera
at seated height, perfectly level. Over the tops of the seat backs, five or
six of %(pasajeros)s hold their mobile phones up high at arm's length, all
aimed in the same direction toward the aisle out of frame; the screens glow
plain grey with nothing legible on them. Their faces are small and half
hidden behind their raised arms and phones. Ceiling light of the cabin.
''')

R[8] = (134, 'hero', ('mano',), None, False, 'ninguno', '''
Close shot of %(mano)s holding a mobile phone in a dark room at night, the
camera at the height of the phone, perfectly level. The phone screen is the
only light: it shows only a small dim picture of the narrow aisle of a plane
with tiny grey figures in it, nothing else on the screen: no interface, no
icons, no buttons, no text, no numbers. The thumb rests at the edge of the
screen. Everything around the hand falls into darkness.
''')

R[9] = (191, 'contraluz', ('wilmer', 'companero', 'agresores'), None, False, 'terminal', '''
Wide shot down the long, empty departures hall at night, the camera at
standing height, perfectly level, looking along the hall toward a lit glass
door at the far end, which is the only bright thing in the frame. Four figures
walk AWAY from the camera toward it, small, seen from behind, caught
mid-stride: %(wilmer)s and %(companero)s, each holding one of %(agresores)s
by the upper arm. Their shadows stretch back toward the camera on the polished
floor. The rows of seats on both sides are empty. Nobody shows a face.
''')

R[10] = (133, 'contraluz', ('wilmer', 'agresores'), None, False, 'terminal', '''
Medium-close shot of %(wilmer)s walking TOWARD the camera through the empty
hall, from the chest up, frontal three-quarter, the camera at his eye level,
perfectly level. His eyes are fixed ahead, his jaw set,
his mouth a straight line. His right hand holds the upper arm of one of the
two passengers, who is CUT by the left edge of the frame: of him we see only a
dark shoulder in a light shirt and the dark back of his head, turned toward
Wilmer, never his face. Wilmer is the only face in the picture. The lit far
end of the hall behind them. Wilmer appears ONCE.
''')

R[11] = (276, 'contraluz', ('wilmer', 'agresores'), None, False, 'terminal', '''
Profile shot from the side as they walk through the empty hall, the camera at
eye level, perfectly level. In the left foreground, out of focus, the dark
back of the head and the shoulder of one of the two passengers, turned toward
Wilmer, his face hidden: he leans in close to Wilmer's ear. In focus in the
middle ground, %(wilmer)s walks on in clean profile facing left, his eyes
ahead, not turning his head, his mouth closed in a straight line. The bright
glass door at the far end of the hall behind him. Wilmer appears ONCE.
''')

R[12] = (238, 'dia', ('wilmer', 'agresores'), None, False, 'estacion_aeropuerto', '''
Medium-wide shot of the small plain police post inside the airport at night,
the camera at standing height, perfectly level. On the left, on the plain
metal bench against the wall, sit %(agresores)s, dark shapes, their faces in
shadow; one leans forward with his elbows on his knees, his head thrust toward
the counter. On the right, at the plain counter, %(wilmer)s stands writing a
report on a plain sheet, three-quarter view, his back half turned to the two
men, his eyes on the page. The glass door onto the empty terminal behind.
Flat ceiling light. Wilmer appears ONCE.
''')

R[13] = (189, 'dia', ('agresores', 'wilmer'), None, False, 'estacion_aeropuerto', '''
Close shot at bench height, perfectly level. In the foreground, the dark hand
of one of the two passengers on the bench holds up a mobile phone toward the
counter, the screen turned away from the camera; his face is out of frame and
his sleeve in shadow. Beyond the phone, out of focus, %(wilmer)s stands at the
counter, three-quarter view, writing, not looking up. Flat ceiling light.
''')

R[14] = (235, 'dia', ('fiscal_c3',), None, False, 'sala_noche', '''
Over-the-shoulder shot from BEHIND the prosecutor at the prosecution table,
the camera at seated height, perfectly level. In the right foreground, seen
from DIRECTLY behind, the back of the head and the grey jacket shoulder of the
prosecutor on duty, a man with short dark hair, filling the right third of the
frame: his face is entirely hidden by his own head, not his ear, not his
cheek, not his nose. On the table before him, a one-page form; his right hand
signs at the bottom with a plain pen, mid-stroke. The form has NO title and NO
heading: only plain grey bars and a few small empty boxes, no letters and no
words anywhere on it. The plain microphone on its short stand.
Across the room, small and out of focus, the defence table with two dark
seated shapes. Flat ceiling light.
''')

R[15] = (236, 'dia', ('fiscal_c3',), None, False, 'sala_noche', '''
Overhead shot looking straight down at a one-page charge form on the
prosecution table. The form is a column of plain grey bars, each with a small
empty square box at its left; exactly ONE box, near the top, is marked with a
plain dark check; all the other boxes are EMPTY. A man's right hand in a grey
jacket sleeve lifts away from the form holding a plain pen. Exactly one hand,
five fingers. No face. A glass of water beside the form.
''')

R[16] = (123, 'hero', (), None, False, 'despacho', '''
Close shot at desk height, perfectly level, of a thick plain book with a
blank plain grey cover lying CLOSED on a desk at night, a plain pen laid on
top of it. One plain desk lamp makes a pool of light on the book; everything
else falls away into darkness. Nobody in the frame. Nothing open, nothing
marked.
''')

R[17] = (108, 'contraluz', ('agresores',), None, False, 'estacion_aeropuerto', '''
Medium-wide shot from inside the small police post toward its glass door, the
camera at standing height, perfectly level. %(agresores)s walk OUT through the
glass door into the empty terminal hall, seen from behind, caught
mid-stride, one of them pulling his jacket on. The bright hall beyond the door
is the only light; the post around the camera is in shadow. The empty metal
bench in the foreground. Their faces are never visible.
''')

R[18] = (235, 'dia', ('wilmer_civil', 'periodista'), None, False, 'entrevista_prensa', '''
Over-the-shoulder shot from behind the reporter, the camera at standing
height, perfectly level. In the left foreground, the back of the head and the
shoulder of %(periodista)s, her arm holding a plain microphone with no logo
toward the man. In focus, %(wilmer_civil)s stands on the pavement in front of a
modest house, three-quarter view, mid-sentence, his eyes on the reporter, his
hands open and low. Beside them, a plain camera on a tripod. Flat daylight.
Wilmer appears ONCE.
''')

R[19] = (186, 'dia', ('wilmer_civil',), None, False, 'entrevista_prensa', '''
Close-up of %(wilmer_civil)s speaking, from the collar up, three-quarter view,
the camera at his eye level, perfectly level. His eyes are on the reporter out
of frame to the left, steady, the iris and the pupil clear; his lips are
parted mid-word. His face is calm and serious: not a smile, not anger. The
head of a plain microphone with no logo enters the bottom left corner of the
frame. The street behind him soft and plain. Flat daylight.
''')

R[20] = (155, 'dia', ('fiscal_revision',), None, False, 'despacho', '''
Medium shot of %(fiscal_revision)s at her desk, three-quarter view, the camera
at seated height, perfectly level. She leans toward a plain open laptop,
watching, her glasses on, her right hand on the touchpad, her left hand
resting flat on an open case folder beside the laptop. The laptop screen faces
away from the camera. Her eyes are on the screen, her mouth a straight line.
Daylight from the window. She appears ONCE.
''')

R[21] = (252, 'dia', ('fiscal_revision',), None, False, 'despacho', '''
Close shot at desk height, perfectly level, of two printed pages of plain grey
bars laid side by side on the desk. A woman's right index finger rests on one
line of the left page and her left index finger on one line of the right page,
both still, as if comparing them; the cuffs of a charcoal blazer at her
wrists. Exactly two hands, exactly ten fingers. All the paper lies flat.
Daylight from the window.
''')

R[22] = (283, 'dia', ('fiscal_revision', 'jueza'), None, False, 'sala', '''
Medium-wide shot of a hearing in daylight, the camera at the side of the room
at seated height, perfectly level. In the left foreground at the prosecution
table, %(fiscal_revision)s STANDS ALONE, three-quarter view, mid-sentence,
holding an open case folder in her left hand and resting the fingertips of
her right hand on the table; her eyes are on the judge. Nobody else stands at
the table or beside her: she appears ONCE, and there is no second woman like
her anywhere in the picture. In the background, behind the plain desk on the
low platform, %(jueza)s listens, writing, small. Daylight from high windows.
''')

R[23] = (170, 'dia', ('fiscal_revision',), None, False, 'sala', '''
Overhead shot looking STRAIGHT DOWN from directly above at the same kind of
one-page charge form lying flat on the prosecution table, the page filling
the middle of the frame, no chairs and no room visible: only the table top. A
column of plain grey bars, each with a small square box at its left. EXACTLY
THREE boxes carry a plain dark check mark -the first, the fourth and the
sixth from the top- and the rest are empty: count them, three checks. A woman's right hand in a charcoal blazer sleeve
lifts away from the form holding a plain pen. Exactly one hand, five fingers.
No face. A glass of water beside the form. Daylight from one side.
''')

R[24] = (213, 'contraluz', ('wilmer',), None, False, 'aeropuerto', '''
Medium shot on the same apron at first light, the camera at standing height,
perfectly level. %(wilmer)s stands in near profile facing left, on duty again
in his plain dark navy field jacket, the radio on his chest, looking toward
the parked white jet with no livery. Behind him the sky is a flat pale grey
just before day, the only bright thing in the frame; the apron and the
terminal are still in soft shadow. His face is calm and steady, his mouth
closed. He appears ONCE.
''')

R[25] = (136, 'contraluz', ('wilmer',), None, False, 'aeropuerto', '''
Close-up of %(wilmer)s, from the collar up, three-quarter view, the camera at
his eye level, perfectly level. He looks ahead past the camera toward the
apron, out of frame to the right, steady, the iris and the pupil clear; his
mouth is a straight line, the corners not raised. The flat pale sky of first
light behind him. His face is fully drawn, clear and dignified.
''')

NOMBRE = {1: 'el_anden', 2: 'la_llamada', 3: 'se_niegan', 4: 'el_pasillo',
          5: 'la_explicacion', 6: 'el_antebrazo', 7: 'los_celulares',
          8: 'el_video', 9: 'el_traslado', 10: 'el_gesto', 11: 'los_insultos',
          12: 'la_estacion', 13: 'el_coronel', 14: 'la_imputacion',
          15: 'una_casilla', 16: 'el_codigo_cerrado', 17: 'en_libertad',
          18: 'el_medio_local', 19: 'su_nombre', 20: 'la_revision',
          21: 'el_patron', 22: 'la_adicion', 23: 'tres_casillas',
          24: 'el_amanecer', 25: 'restituida'}

CON_PERSONA = set(R) - {16}
SILUETAS = set()
# Los insultos (r11-r13) los dice la voz; no se escriben en carton.
CARTONES = {3, 6, 8, 10, 14, 15, 16, 17, 20, 21, 22, 23, 24}
CENITALES = {15, 23}
SOLO_MANOS = {8, 15, 21, 23}
SIN_CARA = {14}
TOPE_SIN_GENTE = 3
TOTAL = 4697
PIEZA = TOTAL + (182 + 119 + 48 + 119 + 182)

HOJAS = {n: ['wilmer'] for n in (1, 2, 4, 5, 6, 9, 10, 11, 12, 13, 18, 19, 24, 25)}

E_OFICINA = 'LP_U4C1_r01_la_noticia'
E_SALA = 'LP_U4C1_r05_la_recusacion'
E_CUARTO = 'LP_U4C2_r05_la_sesion'
E_CALLE = 'LP_U2C1_r01_la_calle_de_bodegas'
E_NOCHE = 'LP_U2C2_r07_la_ventana'
E_RECEPCION = 'DH_U1_r10_la_recepcion'
ANCLAS = {1, 3, 8, 9, 12, 14, 16, 18, 20}

REF_PLACA = {
 1: ([E_NOCHE], 'estilo', ''),
 3: ([E_CUARTO], 'estilo', ''),
 8: ([E_NOCHE], 'estilo', ''),
 9: ([E_NOCHE], 'estilo', ''),
 12: ([E_RECEPCION], 'estilo', ''),
 14: ([E_SALA], 'estilo', ''),
 16: ([E_NOCHE], 'estilo', ''),
 18: ([E_CALLE], 'estilo', ''),
 20: ([E_OFICINA], 'estilo', ''),
 2: (['ED_C3_r09_el_traslado'], 'lugar', ''),
 4: (['ED_C3_r03_se_niegan'], 'lugar', 'It is the SAME cabin. '),
 5: (['ED_C3_r03_se_niegan'], 'lugar', ''),
 6: (['ED_C3_r03_se_niegan'], 'lugar', ''),
 7: (['ED_C3_r03_se_niegan'], 'lugar', ''),
 10: (['ED_C3_r09_el_traslado'], 'lugar', ''),
 11: (['ED_C3_r09_el_traslado'], 'lugar', ''),
 13: (['ED_C3_r12_la_estacion'], 'lugar', ''),
 15: (['ED_C3_r14_la_imputacion'], 'lugar', ''),
 17: (['ED_C3_r12_la_estacion'], 'lugar', ''),
 19: (['ED_C3_r18_el_medio_local'], 'lugar', 'It is the SAME man in the SAME light grey shirt. '),
 21: (['ED_C3_r20_la_revision'], 'lugar', ''),
 22: (['ED_C3_r14_la_imputacion'], 'lugar', 'It is the SAME hearing room, now in daylight. '),
 23: (['ED_C3_r15_una_casilla'], 'mismo', 'It is the SAME form from the SAME overhead camera; only now THREE boxes are checked instead of one, and the hand is a woman\'s in a charcoal sleeve. '),
 24: (['ED_C3_r01_el_anden'], 'lugar', 'It is the SAME apron and the SAME man, now at first light. '),
 25: (['ED_C3_r01_el_anden'], 'lugar', ''),
}

REUSA = {}

DET = {
 (11, 'el_brazo'): dict(cuadros=84, entra=150,
     registro='contraluz',
     personas=('wilmer',),
     escena='Extreme close shot at elbow height of a man\'s right hand in the '
            'sleeve of a plain dark navy field jacket with no badge, holding '
            'the upper arm of another man in a light shirt sleeve: the grip '
            'is firm and steady, the fingers closed but not digging in. '
            'Exactly one hand. No face. The bright far end of the hall '
            'behind, soft.',
     gesto='The two arms move forward together with the walk, the hand '
           'keeping exactly the same grip. Nothing else moves.'),
 (22, 'la_hoja'): dict(cuadros=84, entra=150,
     registro='dia',
     personas=('fiscal_revision',),
     escena='Extreme close shot at table height of a woman\'s right hand in a '
            'charcoal blazer sleeve laying one more printed page of plain '
            'grey bars on top of an open case folder on the prosecution '
            'table, the page settling flat. Exactly one hand, five fingers. '
            'Daylight from one side.',
     gesto='The hand lays the page down flat on the folder, smooths it once '
           'and lifts away. Nothing else moves.'),
}

BROLL = {}

MOV = {
 # 3 nov, pase previo: boca en un plano de habla
 19: 'kling: Wilmer habla al reportero, sereno; parpadea y asienta la cabeza',
 4: 'kling: Wilmer camina por el pasillo de la cabina; los pasajeros giran la cabeza',
 9: 'kling: los cuatro caminan hacia la puerta iluminada del fondo',
 24: 'kling: Wilmer respira y sostiene la mirada; el cielo aclara apenas',
}

LOWER_THIRD = {1: 'Wilmer'}


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
