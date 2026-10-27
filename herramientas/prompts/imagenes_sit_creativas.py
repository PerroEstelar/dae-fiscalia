# -*- coding: utf-8 -*-
r"""Las ilustraciones de las situaciones en IMAGEN, segunda vuelta: una
puesta en escena que impresione.

POR QUE HAY UNA SEGUNDA VUELTA
    27 de octubre, Sebastian: «te pido que los casos de ilustracion seas mucho
    mas creativo de lo normal para que causen una impresion». Las angulaciones
    `a` y `b` de `imagenes_sit` son correctas y son planos de video: un
    momento, bien encuadrado. Una imagen sola, que se mira quieta mientras se
    lee un parrafo, aguanta -y pide- una idea grafica: escala, una silueta que
    contiene otra cosa, una sombra que dice lo que la cara no, un plano
    cenital que vuelve el expediente un mapa.

    Cada situacion trae dos ideas (`c` y `d`); de cada una se piden dos
    tiradas y se escoge mirando.

LO QUE NO SE NEGOCIA, AUNQUE SEA UNA IDEA
    - el estilo de la serie (bloque de `base_sit.arma`), la camara a nivel,
      el gris con el UNICO acento mostaza de quien es buscado o de quien busca;
    - ningun hecho se dibuja: ni la desaparicion de Mariana, ni el abordaje,
      ni la amenaza; los mensajes son burbujas grises sin una letra;
    - el servidor que escribe la minuta no lleva cara;
    - ninguna reja, insignia, bandera, escudo ni texto legible;
    - y el LADO LIBRE, porque la lamina pone ahi el contexto verbatim.

LAS IDEAS
    F  c  doble exposicion: el perfil de Rosa Elena contiene el camino
          a la vereda al anochecer, con dos luces traseras que se van.
       d  escala: Rosa Elena muy pequena al fondo de un hall vacio a las
          08:30, la luz de la manana se detiene antes de sus pies.
    G  c  claroscuro: Mariana frente a los microfonos, media cara en luz,
          la exhumacion pequena en el horizonte.
       d  cenital: el rectangulo de tierra con su cuadricula de cuerda es un
          diagrama, y al borde de la cinta, Mariana con los microfonos.
    H  c  espalda con espalda: madre e hija miran hacia afuera, cada una
          hacia su propio peso -los volantes del camino, el telefono-.
       d  sombras: las dos en el mismo cuarto, y en la pared desnuda sus
          sombras grandes se superponen.
    I  c  perspectiva forzada: el libro de poblacion enorme en primer
          termino, la mano escribiendo; Rosa Elena pequena del otro lado.
       d  cenital del mostrador: el borde parte el cuadro en dos; de un lado
          la mano que escribe, del otro las manos de ella sobre su carpeta.
    J  c  knolling: las ocho piezas en rejilla sobre una mesa oscura, y las
          manos del equipo en los bordes.
       d  constelacion: las ocho piezas en un tablero, unidas por hilos
          grises tensos hacia el centro; el equipo de espaldas, a contraluz.
    K  c  desde la mesa: el informe cerrado enorme y nitido en primer
          termino; detras, los cuatro inclinados sobre el.
       d  convergencia cenital: cuatro carpetas empujadas hacia el centro,
          los brazos forman una cruz, las sombras largas.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

LADO = {'izq': 'The LEFT THIRD of the frame is calm, uncluttered space -plain '
               'wall, sky, tabletop or soft shadow- with no figure and no '
               'important object in it.',
        'der': 'The RIGHT THIRD of the frame is calm, uncluttered space -plain '
               'wall, sky, tabletop or soft shadow- with no figure and no '
               'important object in it.'}

# letra -> {variante: (registro, personas, exterior, lado_libre, escena)}
IM = {}

IM['F'] = {
 'c': ('dia', ('rosaelena',), False, 'izq', '''
Editorial poster illustration built as a DOUBLE EXPOSURE, the camera
perfectly level.

A large head-and-shoulders PROFILE of %(rosaelena)s facing LEFT, placed in the
right two thirds of the frame against a plain pale grey wall. Her face and
the mustard shawl over her shoulders are drawn normally, in flat tonal planes:
she is IN DEEP DISTRESS AND HOLDING ON, lips pressed, eyes fixed ahead.

INSIDE the dark mass of her hair and the back of her head, as in a double
exposure, a second picture shows through: an unpaved rural road winding up
between dark hills at dusk toward a far ridge, and on it, very small and far
away, the two pale rear lights of a pickup truck going away. The landscape is
contained by the outline of her head and fades softly into it; it does not
spill onto the wall.

The landscape is grey like everything else; only the shawl is mustard.
'''),
 'd': ('contraluz', ('rosaelena',), False, 'der', '''
Very wide shot of a vast, empty, high-ceilinged public reception hall early
in the morning, the camera at seated eye level and perfectly level.

At the far end of a long row of plain plastic chairs, VERY SMALL in the
frame and placed in the left two thirds, %(rosaelena)s sits alone, her
plastic folder on her lap and a plain dark phone held in both hands, its
screen dark. She is IN DEEP DISTRESS AND HOLDING ON: back very straight.

A tall plain window at the far side throws one long clean shaft of morning
light across the bare floor; the bright patch STOPS just short of her feet,
and she sits in the shadow beside it. On the bare wall above the chairs, a
plain round wall clock with simple tick marks and NO numbers, its hands at
half past eight.

The window is the only bright thing in the frame; the hall falls into soft
shadow.
'''),
}

IM['G'] = {
 'c': ('dia', ('mariana',), True, 'izq', '''
Medium close shot of %(mariana)s outdoors at the edge of open country, the
camera at her eye level and perfectly level, placed in the right two thirds
of the frame, seen in three-quarter view.

Strong low side light from the right cuts her face in two: one half in clean
light, one half in deep shadow, in two flat tonal planes. She is RESOLVED AND
YOUNG: chin level, eyes steady, speaking.

From the left edge, two or three PLAIN HAND-HELD MICROPHONES held by hands
that enter from outside the frame point toward her: no logo, no lettering,
no colour on any of them, and the people holding them are not in the
picture. One of her hands is closed around her own phone, the mustard cuff
at her wrist.

Far behind her on the low horizon, small and out of focus, a line of plain
tape on low stakes and two kneeling figures in light grey coveralls. A huge
pale sky.
'''),
 'd': ('dia', ('mariana', 'perito'), True, 'izq', '''
Overhead shot looking straight down from high above an exhumation site in
open country, the camera perfectly square to the ground, the whole scene
placed in the right two thirds of the frame.

A clean RECTANGLE OF BARE EARTH, a smooth matte plane clearly darker than the
dry grass around it, is marked off with plain tape strung between low stakes
and crossed by a TAUT STRING GRID held just above the ground, each string
casting its thin shadow. Inside two of the squares %(perito)s and a second
worker in the same plain light grey coveralls kneel at work, seen from
above. Nothing is visible in the ground: no bone, no body, no cloth.

Just outside the tape, %(mariana)s stands seen from above, small, with three
plain hand-held microphones held toward her by hands that enter from the
edge of the frame; the people holding them are cut off by the frame. Long
afternoon shadows fall across the grass in one direction.

The picture reads as a clean graphic diagram of lines, rectangles and
shadows, with one small mustard accent at her cuffs.
'''),
}

IM['H'] = {
 'c': ('contraluz', ('rosaelena', 'mariana'), True, 'izq', '''
Medium-wide shot of two women standing BACK TO BACK in the middle of an
unpaved rural road at dusk, the camera at standing eye level and perfectly
level, the two placed in the right two thirds of the frame.

%(rosaelena)s faces left: she holds a thick stack of plain photocopied flyers
against her chest -each flyer a plain sheet with a grey rectangle where a
photograph would be and grey bars where text would be- and looks down the
road. She is WORN DOWN AND UNYIELDING.

%(mariana)s faces right, her back against her mother's back: she holds a
plain dark phone whose screen glows a flat pale grey, and looks at it. She is
ALERT AND UNEASY, shoulders drawn in.

The two never look at each other. On the mother's side the road runs away
toward the hills; on the daughter's side the dusk is darker. The pale band of
sky at the horizon is the only bright thing in the frame.
'''),
 'd': ('hero', ('rosaelena', 'mariana'), False, 'der', '''
Medium-wide shot of the bare front room of a modest rural house at night,
lit by ONE plain table lamp, the camera at standing eye level and perfectly
level, the scene placed in the left two thirds of the frame.

%(rosaelena)s sits at a plain table covered with spread-out photocopied flyers
-plain sheets with a grey rectangle where a photograph would be-, one hand
flat on them. She is WORN DOWN AND UNYIELDING. Behind her, standing by the
dark window, %(mariana)s looks at the pale glow of the phone in her hand. She
is ALERT AND UNEASY.

On the BARE WALL behind them the lamp throws their two SHADOWS, large and
soft-edged, and the two shadows OVERLAP into one dark shape, while the two
women themselves look in different directions.

Everything outside the pool of the lamp falls away into near-black.
'''),
}

IM['I'] = {
 'c': ('dia', ('rosaelena', 'servidor'), False, 'izq', '''
Shot taken from the level of a plain service counter, on the servant's side,
the camera low and perfectly level, the scene placed in the right two thirds
of the frame.

In the near foreground, ENORMOUS by forced perspective, a large open bound
ledger lies on the counter, its ruled pages carrying only plain flat grey bars
where handwriting would be. A man's HAND in a plain grey sleeve writes in it
with a plain pen; only the hand and forearm are in the picture: NO FACE, no
badge, no insignia.

Across the counter, small and a little out of focus beyond the curve of the
ledger, %(rosaelena)s stands with her folder held against her chest, watching
the hand write. She is HURT AND ATTENTIVE. On the bare wall behind her, a
plain round wall clock with simple tick marks and NO numbers.

Ordinary daylight from one dominant direction.
'''),
 'd': ('dia', ('rosaelena', 'servidor'), False, 'der', '''
Overhead shot looking straight down at a plain service counter, the camera
perfectly square to the counter top, the scene placed in the left two thirds
of the frame.

The FRONT EDGE OF THE COUNTER runs straight across the picture and divides it
in two. On the upper side, a large open bound ledger with plain flat grey bars
where handwriting would be, and a man's HAND in a plain grey sleeve writing in
it with a plain pen: only the hand and forearm, NO FACE. On the lower side,
resting on the very edge of the counter, two older woman's hands lie flat on a
plain plastic folder of papers, with the mustard edge of a shawl at the
wrists.

Ordinary daylight from one dominant direction lays clean shadows across the
counter top.
'''),
}

IM['J'] = {
 'c': ('dia', ('investigador', 'perito', 'analista'), False, 'izq', '''
Overhead shot looking straight down at a large plain dark grey table, the
camera perfectly square to the tabletop, in the precise flat-lay style called
knolling, the arrangement placed in the right two thirds of the frame.

EIGHT DIFFERENT PIECES OF A CASE FILE lie in a precise grid of two rows of
four, perfectly aligned, with equal gaps, each one a different kind of thing:
(1) a small bound logbook open at a ruled page; (2) a stapled typed
interview transcript; (3) a printed map with thin lines radiating from one
point; (4) a greyscale ground-radar printout with a lighter rounded patch;
(5) a form with a hand-drawn grid sketch; (6) a sheet with a plain outline
diagram of a row of teeth; (7) a printout of evenly spaced narrow peaks on a
baseline; (8) a dense matrix of small plain cells. EVERY line of text on every
document is a plain flat grey bar: no readable letter, no number, no stamp, no
logo.

At the edges of the table, three pairs of HANDS reach in -one in plain dark
grey sleeves, one in light grey field coveralls with grey gloves, one in a
plain mid-grey sleeve- each setting down or squaring one of the pieces. Faces
are outside the frame.

Ordinary daylight from one side rakes across the table so each sheet casts a
small clean shadow.
'''),
 'd': ('contraluz', ('investigador', 'perito', 'analista'), False, 'der', '''
Medium-wide shot of a plain working room in the evening, the camera at
standing eye level and perfectly level, the scene placed in the left two
thirds of the frame.

On a large plain board on the wall, EIGHT DIFFERENT DOCUMENTS are pinned
-a small logbook page, a typed transcript, a map with radiating lines, a
ground-radar printout, a grid sketch, a diagram of a row of teeth, a printout
of narrow peaks, a matrix of small cells-, every line of text a plain flat
grey bar. TAUT PALE GREY THREADS run from each document to a single plain
blank card pinned at the centre of the board, so the eight pieces form a
constellation converging on it.

In front of the board, seen from behind and in three-quarter back view,
%(investigador)s, %(perito)s and %(analista)s stand looking at it, small
against it.

The board is lit by a single plain lamp; the window light behind them is
the brightest thing; the room falls into shadow.
'''),
}

IM['K'] = {
 'c': ('contraluz', ('fiscal', 'investigador', 'perito', 'analista'), False,
       'izq', '''
Shot taken from the surface of a plain meeting table, the camera at table
height and perfectly level, the scene placed in the right two thirds of the
frame.

In the near foreground, sharp and large, a THICK CLOSED BOUND DOCUMENT lies
squared on the table, its cover plain grey with a single flat grey bar where
a title would be.

Beyond it, a little out of focus, the four members of the team stand and lean
over the table toward it: %(fiscal)s at the centre with both hands resting on
the table edge, %(investigador)s, %(perito)s and %(analista)s around her.
They are CONCENTRATED AND UNITED: the stillness of people about to sign off on
something.

The window behind them is the only bright thing in the frame; the room is in
soft shadow. No flag, no shield, no emblem anywhere.
'''),
 'd': ('dia', ('fiscal', 'investigador', 'perito', 'analista'), False, 'der',
       '''
Overhead shot looking straight down at a plain square meeting table, the
camera perfectly square to the tabletop, the table placed in the left two
thirds of the frame.

At the four sides of the table, four people seen from directly above -the
tops of their heads and their shoulders- each push a plain grey folder toward
the centre with one hand, so that their four arms form a cross. At the
centre, where the folders meet, lies a THICK CLOSED DOCUMENT, squared. One of
the four wears plain light grey field coveralls; the others plain dark and
mid-grey jackets.

Ordinary daylight from one low dominant direction throws four long clean
shadows across the table. Every cover carries only a plain flat grey bar
where a title would be.
'''),
}


def prompts():
    import base_sit as S
    out = {}
    for L, vs in sorted(IM.items()):
        for v, (reg, gente, ext, lado, txt) in sorted(vs.items()):
            cuerpo = txt % S.TOKENS if '%(' in txt else txt
            cuerpo = cuerpo.strip() + '\n\n' + LADO[lado]
            out['SIT_%s_%s' % (L, v)] = {
                'luz': reg, 'gente': list(gente), 'lado_libre': lado,
                'prompt': S.arma(cuerpo, registro=reg, personas=gente,
                                 exterior=ext)}
    return out


if __name__ == '__main__':
    o = prompts()
    p = r'D:\DAE\_tmp\sit\prompts_img_creativas.json'
    json.dump(o, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for k, v in o.items():
        print(k, v['luz'], v['gente'], v['lado_libre'], len(v['prompt']))
