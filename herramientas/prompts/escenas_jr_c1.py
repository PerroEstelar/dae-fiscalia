# -*- coding: utf-8 -*-
r"""CASO 1 «Una discusión en un sitio público» · nueve ranuras · pieza 2344.

LA RANURA Y LO QUE SE OYE ENCIMA (recortar_jr.py: c03 partido en «y con
posterioridad», porque la denuncia y la asignacion son dos lugares)
    r01 238  El 01 de enero de 2025, en un sitio publico, se presenta una
             discusion entre Juan Rodriguez y Ana Perez, mayores de edad.
    r02 177  El joven Juan se exalta... golpea... a Ana; ella cae y es
    r03 177  llevada al hospital mas cercano... recibe los cuidados...
    r04  91  La senora Perez pone en conocimiento la noticia criminal
    r05 178  y, con posterioridad, le corresponde a usted este caso...
    r06 287  En la tercera ocasion que la victima asiste al medico legista...
             incapacidad definitiva... de 65 dias.
    r07 167  Al salir de la audiencia concentrada el senor Rodriguez,
             acompanado por su defensor de confianza o privado,
    r08 190  le manifiestan, al fiscal, el decidido interes de acudir al
             mecanismo de justicia restaurativa (JR) de la mediacion,
    r09 189  ...han intentado dialogar con la victima... rechazados.

CINCO LUGARES, UN DIA DE ENERO Y LOS MESES DESPUES
    La plaza de barrio el primero de enero (r01, r02); el hospital (r03); la
    ventanilla de denuncias y el despacho de la fiscal local (r04, r05);
    el consultorio del legista (r06); el corredor del juzgado (r07, r08); la
    puerta de la casa de Ana, al final del dia (r09).

LO QUE NO SE DIBUJA
    Los golpes. La r02 es el piso de la plaza con lo que quedo: el bolso y
    unos papeles. Nadie en cuadro. Juan nunca lleva cara: en r07 y r08 es la
    espalda que sale de la audiencia y el hombro desde el que se ve a la
    fiscal. El «rechazo» de r09 es una reja cerrada con Ana detras, sin
    nadie mas en la calle.

QUIEN LLEVA CARA
    Ana (r01, r03, r06, r09) y la fiscal local (r05, r08).
"""

R = {}

R[1] = (238, 'dia', ('ana', 'juan'), None, False, 'ciudad', '''
Wide shot of a small plaza in a Colombian neighbourhood on the first morning
of the year: shops closed behind roll-down shutters, a plain concrete bench,
a few street trees, the plaza almost empty. The camera at standing height,
perfectly level, across the plaza.

In the middle distance %(ana)s and %(juan)s stand about two metres apart,
facing each other, in the middle of an argument that has not yet become
anything else. Ana faces the camera three-quarter: her chin up, her mouth
open on a word, both hands open at waist height, palms up, the gesture of
someone saying «what do you mean». Juan is seen from BEHIND, his back to the
camera, his shoulders squared, his arms at his sides, one hand half closed.
His face is not visible at all. Nobody touches anybody. Two people further
away cross the far side of the plaza without looking.

What the camera asserts: this is still a conversation, and the plaza is
listening.
''')

R[2] = (177, 'dia', (), False, False, 'ciudad', '''
Close shot at ground level of the plain concrete pavement of the same plaza,
the camera about thirty centimetres above the ground, perfectly level,
looking along the pavement toward the closed shutter of a shop a few metres
away, out of focus.

On the pavement, nearest the camera: a plain grey woman's handbag lying on
its side with its strap trailing across the kerb, and three or four sheets
of paper spilled from it, flat on the ground, each sheet carrying only plain
flat grey bars where writing would be. Nothing else: no person, no shoe, no
hand, no mark on the ground. The morning light comes low from one side and
lays a long shadow from the handbag across the concrete.

What the camera asserts: something happened here a moment ago, and we did
not watch it.
''')

R[3] = (177, 'contraluz', ('ana',), None, False, 'hospital', '''
Medium shot in a public hospital corridor. The camera at seated height,
perfectly level, looking down the corridor toward a pair of swing doors with
small windows at the far end: that doorway is the only bright thing in the
picture, and everything nearer sits in shadow.

%(ana)s sits on a plain metal bench against the corridor wall, in the
foreground on the left, in three-quarter view. A plain light grey blanket is
over her shoulders on top of her clothes and the scarf; she holds a folded
cold compress against the left side of her head with her right hand, her
elbow on her knee, her eyes open and lowered, her mouth a closed straight
line. She is not crying and not in a drama: she is waiting. Her face reads
as planes of shadow with the light from the doors on one edge of it. Nobody
else in the corridor.
''')

R[4] = (91, 'dia', ('ana',), None, False, 'oficina', '''
Medium shot of a plain public-office reception window: a counter with a
glass partition and a small opening at the bottom, seen from the public
side, the camera at standing height, perfectly level, slightly to one side.

%(ana)s stands at the window seen from BEHIND and to one side, her back
three-quarter to the camera, her face turned toward the glass and not
visible. Her left hand rests on the counter; with her right she pushes a
plain sheet of paper under the opening in the glass. On the other side of
the glass, a clerk's two hands in a plain grey sleeve receive it; the clerk
is otherwise out of frame. The paper carries only plain flat grey bars.
''')

R[5] = (178, 'dia', ('fiscal1',), None, False, 'oficina', '''
Medium shot inside a small prosecutor's office, the camera at seated eye
level across the desk, perfectly level.

%(fiscal1)s sits at her plain grey desk, three-quarter to the camera. A
hand in a plain light grey sleeve -an assistant, otherwise out of frame on
the right- has just set a thin plain grey case folder on the desk in front
of her and is drawing back. The prosecutor has stopped what she was doing:
her pen is still in her right hand, resting on the open notebook, and her
eyes have gone to the folder. Her mouth is closed, her brow level: no
surprise, no sigh, only attention. On the folder, only a plain flat grey bar
where a label would be. Daylight from the window on the left; a plain metal
filing shelf behind her.
''')

R[6] = (287, 'dia', ('ana', 'legista'), None, False, 'hospital', '''
Medium shot in a plain examination room: a plain examination bed with a
light grey sheet, a plain desk with a chair, one window with plain glass.
The camera at seated height beside the desk, perfectly level.

%(ana)s sits on the edge of the examination bed, upright, her hands folded
in her lap, her scarf on, her eyes on the person writing. She is calm; her
mouth is closed; nothing hurts her now. In the right foreground, out of
focus and large, %(legista)s: the sleeve of a plain light grey coat and two
hands at the desk, one holding a plain clipboard flat, the other writing on
it with a plain grey pen. On the clipboard only plain flat grey bars, no
character anywhere. Daylight from the window falls on Ana and on the sheet.

What the camera asserts: the third visit, the one where the number is
written down.
''')

R[7] = (167, 'contraluz', ('juan', 'defensor1'), None, False, 'sala', '''
Wide shot of a plain corridor outside a hearing room, the camera at standing
height in the corridor, perfectly level, looking toward a tall doorway at
the far end that opens onto bright daylight: the only bright thing in the
picture.

%(juan)s and %(defensor1)s walk away from the camera toward that doorway,
side by side, seen entirely from BEHIND, mid-stride, the lawyer a half step
ahead with his folder under his arm, the young man with his hands in the
pockets of his hooded jacket. Their faces are not visible at all. Behind
them, nearer the camera, the double door of the hearing room stands half
open, plain, with a small plain window in each leaf. Plain benches along
the corridor wall, empty.
''')

R[8] = (190, 'dia', ('fiscal1', 'juan', 'defensor1'), None, False, 'sala', '''
Over-the-shoulder shot in the same corridor, the camera at standing height
just behind the lawyer's shoulder, perfectly level.

In the foreground, large and out of focus, the backs of two heads and
shoulders: %(defensor1)s on the left and %(juan)s on the right, both facing
away from the camera, their faces not visible. Facing them, in focus,
%(fiscal1)s stands with her back near the corridor wall, a plain grey
folder held against her chest with both arms. She is listening: her head
very slightly tilted, her eyes on the lawyer, her mouth closed in a straight
line, her brow level. She has not answered yet and her face does not say
what she will answer. Daylight from a high plain window on one side.
''')

R[9] = (189, 'hero', ('ana',), None, False, 'barrio', '''
Medium shot of the front door of a plain house on a Colombian street at the
end of the day, seen from the pavement, the camera at standing height,
perfectly level, square to the door.

The door is a plain metal security grille, CLOSED, with a solid door open
behind it; the only light in the picture comes from inside the house,
through the grille, and the street around it is already dark. Behind the
grille, half hidden by its bars, %(ana)s stands in the doorway, in profile
to the camera, her right hand resting on the inside bolt of the grille, her
face turned a little away toward the inside of the house, her eyes lowered.
Her scarf catches the inside light. Nobody is on the street: no other
figure, no shadow of a person, nothing on the pavement.

What the camera asserts: the grille is closed, she closed it, and the
street side is where we are standing.
''')

NOMBRE = {1: 'la_plaza', 2: 'el_bolso', 3: 'el_hospital', 4: 'la_ventanilla',
          5: 'la_fiscal_recibe', 6: 'el_legista', 7: 'el_corredor',
          8: 'la_fiscal_escucha', 9: 'la_reja'}

# ranura que reusa la placa de otra: (madre, parametros de camara)
REUSA = {}

CON_PERSONA = {1, 3, 4, 5, 6, 7, 8, 9}
SILUETAS = set()
CARTONES = {1, 6, 8, 9}
CENITALES = set()
SOLO_MANOS = set()
SIN_CARA = {4, 7}
TOPE_SIN_GENTE = 3
PIEZA = 2344
TOTAL = PIEZA - (182 + 119 + 48 + 119 + 182)

HOJAS = {1: ['ana'], 3: ['ana'], 4: ['ana'], 5: ['fiscal1'], 6: ['ana'],
         8: ['fiscal1'], 9: ['ana']}

DET = {
 (6, 'el_boligrafo'): dict(cuadros=72, entra=120, registro='dia',
     personas=('legista',),
     escena='Extreme close shot of a hand in the sleeve of a plain light grey '
            'coat writing with a plain grey pen on a plain clipboard that '
            'lies flat on a desk; the page carries only plain flat grey '
            'bars. Daylight from the left.',
     gesto='The pen moves along one line from left to right, writing, and '
           'stops at the end of the line. The clipboard does not move. '
           'Nothing else moves.'),
 (9, 'el_cerrojo'): dict(cuadros=72, entra=60, registro='hero',
     personas=('ana',),
     escena='Close shot, from the inside of the house, of a woman\'s hand '
            'resting on the plain metal bolt of a closed security grille, '
            'the cuff of a mid-grey cardigan at the wrist, the dark street '
            'beyond the bars out of focus. The only light comes from inside, '
            'from behind the camera.',
     gesto='The hand slides the bolt the last centimetre home and stays on '
           'it. Nothing else moves.'),
}

BROLL = {
 'la_plaza_vacia': ('dia', 'Wide shot of the same small Colombian plaza, '
                    'empty, the shutters down, a plain bench, morning light.'),
}

MOV = {
 1: 'kling: las dos personas lejanas cruzan la plaza y salen; Ana y Juan quietos',
 3: 'kling: la puerta del fondo se abre y pasa una figura; Ana quieta',
 7: 'kling: los dos siguen caminando hacia la puerta clara',
}

LOWER_THIRD = {1: 'Ana Pérez', 5: 'Fiscal local'}


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
