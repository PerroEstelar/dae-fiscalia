# -*- coding: utf-8 -*-
r"""SITUACION G «La vocera» · cinco ranuras · pieza 1565 cuadros (1:05).

La agencia la marco IMAGEN; paso a video el 27 de octubre por indicacion de
Sebastian, porque es la unica de las seis con secuencia. La forma de imagen
se conserva en IMAGENES/SITUACION G.

CUATRO MOMENTOS, CINCO PLANOS
    1. la exhumacion en la Finca El Vergel, Mariana al borde de la cinta (r01)
    2. Mariana ante los microfonos (r02)
    3. las 18:00: la puerta de la casa, Rosa Elena mirando la calle (r03)
    4. el telefono: la mano de Mariana y los mensajes, antes (r04)
    5. la familia entra a la Fiscalia de noche (r05)

MARIANA ES MENOR DE EDAD, Y SU DESAPARICION NO SE DIBUJA
    Se la ve ANTES -como vocera, de dia, con los microfonos- y despues solo
    su ausencia: la puerta abierta, la calle vacia. Los mensajes son burbujas
    grises sin una letra; lo que dicen no esta en el documento y no se
    inventa. La mano es suya porque lleva el puno mostaza.

LA PIEZA TERMINA EN LA PUERTA, NO EN LA RESPUESTA
    La situacion acaba cuando la familia llega a pedir auxilio. Lo que la
    Fiscalia hace -el MBU, la Alerta Rosa- es la pregunta del ejercicio, asi
    que r05 es Rosa Elena entrando, de espaldas, hacia la puerta iluminada.

EL CARTON DEJA LIBRE EL TERCIO IZQUIERDO
    En r02 Mariana va en los dos tercios derechos del cuadro: es el plano
    sobre el que puede caer texto, y el carton no le tapa la cara.
"""

R = {}

R[1] = (250, 'dia', ('mariana', 'perito'), None, False, True, '''
Wide shot of an exhumation site on open rural land, the camera at standing
eye level and perfectly level.

A rectangle of BARE EARTH is marked off with plain tape strung between low
stakes, with a taut string grid over it. Inside it %(perito)s and a second
worker in the same plain light grey coveralls kneel at work, small in the
frame, their faces not readable at this distance.

Just outside the tape, in the foreground at one side, %(mariana)s stands
watching, seen in three-quarter back view, her hands closed around her phone.
She is STILL AND ATTENTIVE.

THE GROUND IS BARE EARTH, a smooth matte mid-dark grey plane clearly darker
than the dry grass around it, never paving. Nothing is visible in the ground:
no bone, no body, no cloth, no object of any kind.

Ordinary daylight from one dominant direction; pasture and a line of trees
behind.
''')

R[2] = (201, 'dia', ('mariana',), None, False, True, '''
Medium shot of %(mariana)s standing outdoors at the edge of a rural field,
the camera at her eye level and perfectly level, placed in the RIGHT TWO
THIRDS of the frame; the left third is calm open sky and pasture with no
figure in it.

Two or three PLAIN HAND-HELD MICROPHONES and a plain phone, held up by hands
that enter from the edge of the frame, point toward her: no logo, no
lettering, no colour on any of them, and the people holding them are not in
the picture. She speaks into them. She is RESOLVED AND YOUNG: chin level,
eyes steady, one hand closed around her own phone at her side. Modest, loose
everyday clothes, an ordinary upright stance.

Behind her, out of focus, plain tape strung between low stakes.

Ordinary daylight from one dominant direction.
''')

R[3] = (118, 'contraluz', ('rosaelena',), None, False, True, '''
Medium-wide shot of the front of a modest small-town house at dusk, the
camera on the street at standing eye level and perfectly level.

The plain front door stands open and %(rosaelena)s stands in the doorway,
one hand on the door frame, looking down the street toward the camera's left.
She is WAITING AND AFRAID: the body leaning forward a little, the other hand
pressed flat against her chest.

The street is empty: no figure, no vehicle.

The warm-grey light of the room behind her is the only bright thing in the
frame; the street and the house front fall into dusk shadow.
''')

R[4] = (139, 'contraluz', (), True, False, False, '''
Extreme close shot of a young woman's HAND holding a plain dark phone at
dusk, the camera level, the hand and the phone filling most of the frame.
At the wrist, the plain matte mustard-yellow cuff of a light grey sleeve.

The phone screen glows a plain flat pale grey and shows THREE PLAIN GREY
ROUNDED MESSAGE BUBBLES stacked one under another, each filled with nothing
but a smooth flat grey bar: no letter, no number, no emoji, no name, no
readable character anywhere.

NO FACE and no other part of a person is in the picture. The fingers are
held together around the phone, the thumb clearly visible.

The glow of the screen is the only bright thing in the frame; around it the
dusk falls into soft shadow.
''')

R[5] = (207, 'contraluz', ('rosaelena',), None, False, True, '''
Wide shot of the entrance of a plain public building at night, the camera on
the pavement at standing eye level and perfectly level.

%(rosaelena)s walks fast toward the open glass door, seen from behind, her
plastic folder pressed against her chest, small in the frame. The doorway
ahead of her is lit from inside.

The building is plain painted masonry: no sign, no flag, no shield, no
emblem, no lettering of any kind.

The lit doorway is the only bright thing in the frame; the street and the
facade fall into night shadow.

What the camera asserts: she is asking for help, and the picture stops at
the door.
''')

NOMBRE = {1: 'la_exhumacion', 2: 'los_microfonos', 3: 'la_puerta_abierta',
          4: 'los_mensajes', 5: 'hacia_la_fiscalia'}

CON_PERSONA = {1, 2, 3, 4, 5}
SILUETAS = set()
CARTONES = {3, 4, 5}
TOPE_SIN_GENTE = 3
TOTAL = 1565 - (182 + 119 + 48 + 119 + 182)

DET = {
 (2, 'el_microfono'): dict(cuadros=90, entra=60, registro='dia',
     personas=(),
     escena='Close shot of a hand holding a plain hand-held microphone with '
            'no logo, pointed toward someone just out of frame, an open '
            'field softly out of focus behind.',
     gesto='The hand tilts the microphone a few degrees closer and holds '
           'it there.'),
 (3, 'la_mano_en_el_marco'): dict(cuadros=72, entra=30, registro='contraluz',
     escena='Close shot of an older woman\'s hand gripping the edge of a plain '
            'wooden door frame at dusk, a matte mustard shawl edge just '
            'visible at the wrist.',
     gesto='The fingers tighten on the door frame and stay there.'),
}

BROLL = {
 'la_casa_de_noche': ('hero', 'Wide shot of a modest small-town house at '
                      'night, one window lit, the street empty.'),
 'la_cinta_al_atardecer': ('contraluz', 'Wide shot of the exhumation site '
                           'at dusk, the tape and the string grid against the '
                           'low sky, nobody there.'),
}

MOV = {
 1: 'la cinta se mueve con el viento (ya esta en la placa)',
 3: 'solo luz: el anochecer baja un tono (rampa de luma)',
 4: 'solo luz: la pantalla se apaga al final del plano (rampa de luma, sin '
    'modelo: es justo lo que dice la voz)',
}


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
    return fallos, tot, mejor
