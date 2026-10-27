# -*- coding: utf-8 -*-
r"""Las seis situaciones que van en IMAGEN (F a K).

UNA IMAGEN ES UN SOLO MOMENTO, Y HAY QUE ESCOGERLO
    Un contexto de 60 a 100 palabras no da para montaje, pero si para una
    decision de puesta en escena: cual es EL momento que, solo, cuenta la
    situacion. Por cada una hay dos angulaciones -`a` y `b`- para que la
    eleccion se haga mirando y no a ciegas. Se genera una tirada de cada y se
    escoge.

LA LAMINA
    La imagen se entrega de dos formas: la ilustracion limpia, y la LAMINA,
    que es la ilustracion con el contexto verbatim encima en el sistema de
    cartones de la serie (tinte azul, filete amarillo, una sola familia
    tipografica). La consigna no entra: la agencia la marco «No incluir esto
    en la IMAGEN». Por eso las ilustraciones se piden con un LADO LIBRE -de
    pared, de cielo o de penumbra- donde el texto pueda ir sin tapar a nadie.

LAS MISMAS REGLAS QUE EN VIDEO
    Rosa Elena y Mariana son las del caso integrador. El servidor que escribe
    la minuta (I) no lleva cara. Mariana es menor de edad: nada en su postura
    ni en su ropa sale de lo que ya fija su token, y su desaparicion no se
    ilustra -la G la muestra antes, cuando es vocera-.
"""

LADO = {'izq': 'The LEFT THIRD of the frame is calm, uncluttered space -plain '
               'wall, sky or soft shadow- with no figure and no important '
               'object in it.',
        'der': 'The RIGHT THIRD of the frame is calm, uncluttered space -plain '
               'wall, sky or soft shadow- with no figure and no important '
               'object in it.'}

# letra -> {variante: (registro, personas, exterior, lado_libre, escena)}
IM = {}

IM['F'] = {
 'a': ('contraluz', ('rosaelena',), False, 'der', '''
Medium shot of %(rosaelena)s sitting on a plain chair in a small plain public
reception office early in the morning, the camera at her seated eye level and
perfectly level, seen in three-quarter view and placed in the left two thirds
of the frame.

She holds the plastic folder of papers on her lap with both hands, and a plain
dark phone lies on top of it. She is IN DEEP DISTRESS AND HOLDING ON: back
very straight, lips pressed, eyes glassy, looking toward someone out of frame
to the right who has not yet spoken.

The window behind her is the only bright thing in the frame; the room is in
soft shadow.
'''),
 'b': ('dia', ('rosaelena', 'servidor'), False, 'izq', '''
Medium shot across a plain reception desk, the camera at seated eye level and
perfectly level, from behind the shoulder of the public servant who receives
her: only a blurred edge of a plain grey sleeve and a plain blank form on the
desk are in the near foreground, NO FACE of the servant.

Across the desk, in the right two thirds of the frame, %(rosaelena)s sits
facing the camera, her folder held flat against her chest. She is IN DEEP
DISTRESS AND HOLDING ON: eyes on the servant, chin trembling but level.

Ordinary daylight from one dominant direction.
'''),
}

IM['G'] = {
 'a': ('dia', ('mariana',), True, 'izq', '''
Medium shot of %(mariana)s standing at the edge of an excavation site in open
country, the camera at her eye level and perfectly level, placed in the right
two thirds of the frame.

Behind her, out of focus, a rectangle of bare earth is marked off with plain
tape strung between low stakes, with a string grid over it and two small
figures in plain light grey coveralls kneeling at work.

Two or three PLAIN HAND-HELD MICROPHONES and a plain phone held up by hands
that enter from the edge of the frame are pointed toward her: no logo, no
lettering, no colour on any of them, and the people holding them are not in
the picture. She speaks into them. She is RESOLVED AND YOUNG: chin level,
eyes steady, one hand closed around her own phone at her side.

Ordinary daylight from one dominant direction.
'''),
 'b': ('contraluz', ('mariana',), True, 'der', '''
Close shot of %(mariana)s at dusk on the edge of open country, the camera at
her eye level and perfectly level, seen in three-quarter view and placed in
the left two thirds of the frame.

She looks down at the plain dark phone in her hand; its screen glows a plain
flat pale grey with nothing readable on it, lighting her face from below. She
is ALERT AND UNEASY: shoulders a little drawn in, brow tight.

The low pale sky behind her is the only bright thing in the frame.
'''),
}

IM['H'] = {
 'a': ('contraluz', ('rosaelena', 'mariana'), False, 'izq', '''
Medium-wide shot of the front room of a modest rural family house, the camera
at standing eye level and perfectly level, the two women placed in the right
two thirds of the frame.

%(rosaelena)s sits at a plain table covered with spread-out papers, plain
photocopied flyers with a grey rectangle where a photograph would be, and a
plain notebook; one hand rests on the papers, the other on the small of her
own back. She is WORN DOWN AND UNYIELDING.

Behind her, standing by the window, %(mariana)s holds her phone in one hand
and looks out of the window toward the street. She is RESOLVED AND YOUNG, and
watchful.

The two women look in DIFFERENT directions: the mother down at the papers,
the daughter out of the window. The window is the only bright thing in the
frame.
'''),
 'b': ('dia', ('rosaelena', 'mariana'), True, 'der', '''
Medium shot of a plain doorway of a small rural house, the camera at standing
eye level and perfectly level, the door frame splitting the picture into two
spaces, the two women in the left two thirds of the frame.

Inside, in the shadow of the room, %(rosaelena)s sits holding her folder of
papers on her lap. Outside, in the daylight of the yard, %(mariana)s stands
with her phone in hand, about to go out. Each is in her own half of the
picture; they are not looking at each other.

Ordinary daylight outside, one dominant direction; the room inside in soft
shadow.
'''),
}

IM['I'] = {
 'a': ('dia', ('rosaelena', 'servidor'), False, 'izq', '''
Close-medium shot over a plain service counter, the camera on the servant's
side at standing height and perfectly level.

In the near foreground, a man's HAND in a plain grey sleeve writes in a
LARGE OPEN BOUND LEDGER with a plain pen; the ruled pages carry only plain
flat grey bars where handwriting would be, with no readable character. Only
the hand and forearm: NO FACE, no badge, no insignia.

Across the counter, in the right two thirds of the frame and a little out of
focus, %(rosaelena)s stands with her folder held against her chest, watching
the hand write. She is HURT AND ATTENTIVE.

Ordinary daylight from one dominant direction.
'''),
 'b': ('contraluz', ('rosaelena',), False, 'der', '''
Medium shot of %(rosaelena)s standing at a plain counter in a small police
substation, the camera at her eye level and perfectly level, seen in
three-quarter view and placed in the left two thirds of the frame. On the
counter in front of her, a large closed bound ledger.

She is HUMILIATED AND STANDING FIRM: chin raised a little too high, eyes
bright, hand flat on her folder.

The open door behind her is the only bright thing in the frame. No sign, no
flag, no shield, no insignia anywhere.
'''),
}

IM['J'] = {
 'a': ('dia', (), False, 'izq', '''
Overhead shot looking straight down at a large plain table, the camera
perfectly square to the tabletop.

EIGHT DIFFERENT DOCUMENTS are laid out in a neat grid of two rows of four, in
the right two thirds of the frame, each clearly a different kind of thing:
(1) a small bound police logbook open at a ruled page; (2) a stapled typed
interview transcript; (3) a printed map with a few thin radiating lines from
a single point; (4) a printout of a greyscale ground-radar band with a lighter
rounded patch; (5) a form with a hand-drawn grid sketch; (6) a sheet with a
plain outline diagram of a row of teeth; (7) a printout of a row of evenly
spaced narrow peaks on a baseline; (8) a dense grid matrix of small plain
cells. EVERY line of text on every document is a plain flat grey bar: no
readable letter, no number, no stamp, no logo anywhere.

NO PERSON, NO FACE, NO HAND in the frame.

Ordinary daylight from one side rakes across the table so each sheet casts a
small clean shadow.
'''),
 'b': ('dia', ('investigador', 'perito', 'analista'), False, 'der', '''
Medium-wide shot of a plain working room, the camera at standing eye level
and perfectly level, the three people placed in the left two thirds of the
frame.

%(investigador)s, %(perito)s and %(analista)s stand around a large plain
table, each laying down a different document onto the spread of papers in
front of them: a small bound logbook, a printed map with radiating lines, a
printout of a row of narrow peaks. They are FOCUSED AND QUIET: heads bent over
the table.

Every document carries only plain flat grey bars where text would be.
Ordinary daylight from one dominant direction.
'''),
}

IM['K'] = {
 'a': ('contraluz', ('fiscal', 'investigador', 'perito', 'analista'), False,
       'izq', '''
Medium-wide shot of a plain meeting room, the camera at seated eye level and
perfectly level, the four people placed in the right two thirds of the frame.

%(fiscal)s stands at the head of a plain table with both hands resting on a
THICK CLOSED DOCUMENT squared in front of her. Seated around the table,
%(investigador)s, %(perito)s and %(analista)s, each with a plain grey folder
open in front of them, all turned toward her. They are CONCENTRATED AND
UNITED: the stillness of people about to sign off on something.

The window behind the fiscal is the only bright thing in the frame; the room
is in soft shadow. No flag, no shield, no emblem anywhere.
'''),
 'b': ('dia', ('fiscal', 'investigador', 'perito', 'analista'), False, 'der',
       '''
Overhead three-quarter shot of a plain meeting table, the camera above and to
one side, level with the edge of the table, the table placed in the left two
thirds of the frame.

Four pairs of hands -two in plain dark grey sleeves, one in plain light grey
field coveralls with grey gloves pulled off and lying beside them, one in a
plain mid-grey sleeve rolled once- push four plain grey folders toward the
centre, where a THICK CLOSED DOCUMENT lies squared. Faces are cut off by the
frame.

Every cover carries only a plain flat grey bar where a title would be.
Ordinary daylight from one dominant direction.
'''),
}

NOMBRE = {'F': 'rosaelena_en_recepcion', 'G': 'mariana_vocera',
          'H': 'la_madre_y_la_hermana', 'I': 'la_minuta',
          'J': 'las_ocho_piezas', 'K': 'el_equipo'}
