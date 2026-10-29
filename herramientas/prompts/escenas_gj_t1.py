# -*- coding: utf-8 -*-
r"""TEMA 1 «El despacho de los 2.000 casos» · cuatro ranuras · pieza 1176.

LA RANURA Y LO QUE SE OYE ENCIMA (recorte por palabra, recortar_gj.py)
    r01 145  Un fiscal recien nombrado asume la direccion de un despacho con
             mas de 2.000 casos acumulados.
    r02 133  Al no conocer la mision, la vision ni los objetivos de la
             Fiscalia General de la Nacion,
    r03  94  su equipo atiende las denuncias en el estricto orden en que
             llegan,
    r04 154  gastando tiempo importante en casos menores mientras los delitos
             graves se quedan sin investigar.

UNA SOLA ESCENA, UN DESPACHO, UNA MANANA
    r01 el fiscal entra y el despacho lo supera en numero; r02 lo que el
    despacho tapo; r03 la ventanilla, donde se ve el orden de llegada; r04
    la mesa en cenital: lo que se trabaja y lo que espera.

LA MISION EN LA PARED (r02)
    En las oficinas publicas colombianas la mision y la vision estan
    enmarcadas en la pared de la entrada: es un objeto real de la
    institucion, no un simbolo inventado. Aqui el cuadro esta, pero una torre
    de carpetas crecio delante de el. El texto del cuadro son barras grises.
    El fiscal pasa de espaldas: la falla es del despacho, y una falla no cae
    sobre un rostro.

QUIEN LLEVA CARA
    El fiscal, en r01, el unico plano frontal de la pieza. El equipo nunca:
    sus manos en r03 y r04. La gente de la fila, de espaldas y pequena.
"""

R = {}

R[1] = (145, 'dia', ('fiscal1',), None, False, 'oficina', '''
Medium-wide shot inside a small Colombian prosecutor's office, the camera low
in the far corner of the room at seated height, perfectly level, looking back
toward the open door.

%(fiscal1)s has just stepped in through the door: his briefcase is still in
his right hand and his jacket is still on. One step inside, he has stopped.
His weight is on his back foot, his head is turned a little toward the
tallest tower of files, his eyes travel up it, his mouth is a closed straight
line. He is NOT dismayed and NOT heroic: he is a man counting. No smile, the
corners of the mouth do not rise.

The room is FULL of case files: hundreds of plain grey cardboard folders,
each one a separate case, stacked in tall uneven towers on the desk, packed
on two plain metal shelves from floor to ceiling, piled on the visitor chairs
and standing in columns on the floor along the walls, more than the room was
ever built to hold. In the foreground, out of focus, the edge of one tower
frames the left side of the picture. Every folder is plain, with no label,
no number and no writing.

Daylight from a window on one side of the room lays a bright plane across
the floor and the towers.
''')

R[2] = (133, 'dia', ('fiscal1',), None, False, 'oficina', '''
Medium shot of a plain painted wall in the entrance of a Colombian public
office, the camera at standing eye level and perfectly level, square to the
wall.

On the wall hangs a large plain framed panel behind glass, the kind every
public office in Colombia has at its entrance: two columns of text under two
short headings. Here every line of it is a plain flat grey bar: no readable
character anywhere. In front of the panel, on a low metal filing cabinet, a
tower of plain grey case folders has been stacked so high that it now covers
the lower half of the panel.

%(fiscal1)s walks PAST it from left to right, seen from BEHIND and slightly to
one side, a folder under his arm, his face turned away toward the office
ahead, NOT looking at the panel. Mid-stride: his back foot is still lifted.
His face is not visible at all.

What the camera asserts: the panel is where the eye goes, and nobody in the
picture looks at it.

Ordinary daylight from one side; the glass of the frame carries a soft plain
reflection, no glare.
''')

R[3] = (94, 'dia', ('equipo1', 'publico1'), False, False, 'oficina', '''
Medium-wide shot from BEHIND a plain service counter in a Colombian public
office, the camera at the height of the shoulders of the two people working
behind it and perfectly level, looking out over the counter.

In the foreground, out of focus, the backs and shoulders of %(equipo1)s:
only the back of their heads, their shoulders and their hands are seen, NEVER
their faces. One of them reaches across the counter to take a sheet of paper
from the person at the front of the line; the paper is half-way between the
two hands.

Beyond the counter, %(publico1)s stand in ONE long single-file line that runs
away from the counter, out through the open door and on down the corridor,
each person behind the next. They are small in the frame, patient, facing the
counter; no face is detailed.

Plain fluorescent ceiling light and daylight from the corridor windows.
''')

R[4] = (154, 'dia', ('equipo1',), False, False, 'oficina', '''
Overhead shot looking STRAIGHT DOWN onto a long plain grey office desk, the
camera directly above it and perfectly square to the desktop.

On the LEFT half of the desk, in the bright light, the work of the day: a pair
of hands in plain grey sleeves is closing a THIN folder that holds a single
sheet, beside a neat finished pile of more thin folders, each one only a
sheet or two thick. A plain rubber stamp and a pen lie by the hands.

On the RIGHT half of the desk, in the shadow beyond the edge of the light,
waits a heavy stack of THICK case files, each one many centimetres thick,
bulging and tied around with plain string. Nobody's hand is near them. They
have not been opened.

NO face and NO head appear anywhere in the picture: only the hands and the
forearms of the person working, coming in from the bottom edge.

Every folder and sheet is plain, with no label and no readable writing: where
there would be writing there are only plain flat grey bars.

What the camera asserts: the light is on the small cases; the serious ones
sit in the dark.
''')

NOMBRE = {1: 'el_fiscal_llega', 2: 'la_mision_tapada', 3: 'la_fila',
          4: 'la_mesa'}

CON_PERSONA = {1, 2, 3, 4}
SILUETAS = set()
CARTONES = {3, 4}
CENITALES = {4}
SOLO_MANOS = {4}
TOPE_SIN_GENTE = 3
PIEZA = 1176
TOTAL = PIEZA - (182 + 119 + 48 + 119 + 182)

# quien entra como referencia (su hoja) en cada placa
HOJAS = {1: ['fiscal1'], 2: ['fiscal1']}

DET = {
 (4, 'el_sello'): dict(cuadros=72, entra=70, registro='dia',
     personas=('equipo1',),
     escena='Extreme close shot of a hand in a plain grey sleeve holding a '
            'plain rubber stamp just above a thin plain folder lying on a '
            'grey desk, in bright daylight. No writing anywhere: the folder '
            'cover is plain.',
     gesto='The hand presses the stamp down onto the folder once and lifts '
           'it again. The folder does not move. Nothing else moves.'),
}

BROLL = {
 'el_pasillo': ('dia', 'Wide shot of a plain corridor in a Colombian public '
                'office with closed doors along one side and plain metal '
                'chairs against the wall, nobody in it. No lettering.'),
}

MOV = {
 1: 'kling: el fiscal deja de mirar la torre y baja la vista; respira',
 3: 'kling: la fila avanza un paso; la hoja pasa de una mano a la otra',
}

LOWER_THIRD = {1: 'Fiscal recién nombrado'}


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
