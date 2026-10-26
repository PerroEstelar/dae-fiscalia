# -*- coding: utf-8 -*-
r"""Las ocho escenas del CAPITULO 4 «Las voces que no se apagan y el dolor en
la ventanilla».

ESTE CAPITULO ES UNA RIMA MAYOR, Y TODO LO DEMAS LE SIRVE
    r01 y r06 son la misma mujer con la misma carpeta contra el pecho, en
    dos sitios: el corredor de las sillas en fila, y la sala donde alguien
    se sienta A SU LADO y no enfrente. Las dos se graduan juntas.

    Y la carpeta cuenta el capitulo sola: entra apretada contra el pecho en
    r01, sigue apretada en r02 y en r03, y en r08 esta APOYADA SOBRE LA MESA.
    Ese es todo el giro etico, dicho con un objeto.

EL PLANO DE MAS PESO
    r03, el primer plano de Rosa Elena en estado VACIO. Es el unico `hero`
    del capitulo y va justo antes del giro.
"""

R = {}

R[1] = (229, 'contraluz', ('rosaelena',), True, False, False, '''
Wide shot down a plain institutional corridor with A ROW OF EMPTY CHAIRS
against one wall, the camera at standing eye level and perfectly level.

%(rosaelena)s sits alone on one of the chairs, small in the frame and far down
the row. She is VACANT: head low, shoulders dropped, arms hanging loose. The
plain plastic folder is pressed flat against her chest with both arms.

Every other chair is empty. Nobody else is in the corridor.

The window at the far end of the corridor is the only bright thing in the
picture and everything nearer the camera sits in deep shadow.

What the camera asserts by placing her this far down an empty row: she has
been here a long time and nobody has come.
''')

R[2] = (274, 'contraluz', ('rosaelena',), True, False, False, '''
Medium shot of a plain service counter with an OPEN HATCH WINDOW, the camera
at standing eye level and perfectly level.

%(rosaelena)s stands on the near side of the counter, seen from the side, the
plain plastic folder still pressed flat against her chest. Her head is
inclined down.

On the FAR side of the hatch, only A PAIR OF HANDS is visible, resting on the
counter beside a closed ledger. NO FACE, no shoulder and no other part of that
person is in the picture. The hands are at rest and are not reaching for
anything.

The hatch is the only bright thing in the picture; the near side sits in deep
shadow.

What the camera asserts by cutting the other person off at the wrists: what
she met here was a procedure, not a person.
''')

R[3] = (171, 'hero', ('rosaelena',), True, False, False, '''
CLOSE-UP of %(rosaelena)s, head and shoulders, facing the camera three-quarters
on, seated.

She is VACANT: head low, shoulders dropped, her eyes level and directed past
the lens at nothing, her mouth closed, her brow flat. She is NOT weeping and
NOT performing grief. She is a woman who has run out of places to ask.

One low, weak light source deep in the frame picks out one side of her face;
everything else falls away into near-black with real depth. The background is
a plain dark wall with nothing on it.
''')

R[4] = (291, 'dia', ('fiscal',), False, False, False, '''
Medium shot of %(fiscal)s standing beside a plain low table in a quiet room,
the camera at her eye level and perfectly level.

She is standing to receive someone: her body turned toward the doorway, ONE
HAND open and extended low toward a chair in an unhurried offering gesture,
the fingers held together and slightly curled, the thumb clearly visible, the
hand seen edge-on so it reads as a hand with thickness and knuckles. THE
FINGERS ARE NEVER SPREAD APART.

Her head is level, her mouth closed, her expression plain ordinary attention
without performed warmth.

Ordinary daylight from a window to one side lands on the table and the chair.
''')

R[5] = (117, 'dia', (), False, False, False, '''
Wide shot of a small plain room set up for receiving someone, the camera at
seated eye level and perfectly level.

A low plain table, TWO CHAIRS placed at an angle to each other and NOT facing
across the table, a plain jug and two glasses on the table, and a window on
one side. The door is open.

THERE IS NOBODY IN THE FRAME. The room is simply ready.

Ordinary daylight from the window lays a clear bright plane across the table
and the two chairs.

What the camera asserts by photographing two chairs placed at an angle:
somebody decided where the chairs would go before she arrived.
''')

R[6] = (237, 'dia', ('rosaelena', 'psicologa'), True, False, False, '''
Medium shot of %(rosaelena)s seated in the small plain room, with
%(psicologa)s seated BESIDE her and slightly turned toward her, NOT across a
table from her, the camera at seated eye level and perfectly level.

Rosa Elena is RESOLVED: upright, chin level, shoulders open. The plain plastic
folder is still in her lap, held with both hands.

The psychologist's hands are visible and still, resting on her own knees. She
is not touching Rosa Elena and not leaning in.

Ordinary daylight from the window lands on both of them equally.

What the camera asserts by seating them side by side: the geometry of the room
changed before anything was said.
''')

R[7] = (206, 'dia', (), False, False, False, '''
Close shot, straight on and slightly from above, of a plain table top, the
camera level.

TWO HANDS IN PLAIN GREY GLOVES hold a long slim swab over an open plain paper
envelope lying flat on the table. The fingers are held together around the
swab, the thumbs clearly visible, the hands seen at a natural angle so each
reads as a hand with thickness and knuckles. The movement is slow and careful
and nothing is being pressed or forced.

The gloves carry no marking of any kind. The envelope is plain, with a single
flat grey bar where a label would be and no readable character anywhere.

NO FACE and no other part of a person is in the picture.

One dominant light from a window out of frame rakes across the table so the
hands throw a clean shadow onto the envelope.
''')

R[8] = (294, 'dia', ('rosaelena', 'fiscal'), True, False, False, '''
Medium shot of %(rosaelena)s and %(fiscal)s seated at the low table in the
small plain room, turned toward each other, the camera at seated eye level and
perfectly level.

THE PLAIN PLASTIC FOLDER IS NOW LYING FLAT ON THE TABLE between them, closed,
and Rosa Elena's hands rest beside it rather than on it. She is RESOLVED:
upright, chin level, shoulders open.

The prosecutor has a plain grey folder of her own squared on the table in
front of her, also closed. Neither of them is holding anything.

Ordinary daylight from the window lands on the table between them and on both
their faces equally.

What the camera asserts by putting the folder down: she has been carrying it
against her chest since the first frame of this chapter, and this is the first
time she has let it go.
''')

CON_PERSONA = {1, 2, 3, 4, 6, 7, 8}
TOPE_SIN_GENTE = 3
CARTONES = {7}
SILUETAS = set()
RIMAS = [(1, 6)]


def comprobar():
    fallos = []
    tot = sum(v[0] for v in R.values())
    if sorted(R) != list(range(1, 9)):
        fallos.append('faltan ranuras')
    if tot != 1819:
        fallos.append('los cuadros suman %d y la rejilla dice 1819' % tot)
    racha = mejor = 0
    for i in range(1, 9):
        racha = 0 if i in CON_PERSONA else racha + 1
        mejor = max(mejor, racha)
    if mejor > TOPE_SIN_GENTE:
        fallos.append('%d ranuras seguidas sin gente' % mejor)
    return fallos, tot, mejor


if __name__ == '__main__':
    print(comprobar())
