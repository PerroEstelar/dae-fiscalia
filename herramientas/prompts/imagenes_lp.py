# -*- coding: utf-8 -*-
r"""Las láminas del curso Ley 1826 (U1: cinco casos de estudio; U3: tres).

EL ENCARGO (Sebastián, 3 nov): «ilustraciones muy vívidas e imaginativas que
retraten bellamente, casi como un afiche de cine, con carácter y con nuestro
estilo gráfico, de qué se trata el caso, y a un lado el texto». La forma es
la de las láminas de «16 situaciones» (`lamina_sit.py`): ilustración a sangre
y en su LADO LIBRE el panel azul con el texto verbatim. La idea gráfica es la
de su segunda vuelta (`imagenes_sit_creativas.py`): doble exposición, escala,
una sombra que dice lo que la cara no, el cenital que vuelve el expediente un
mapa. La F de esa serie es la referencia de estilo de todas.

LO QUE NO SE NEGOCIA, AUNQUE SEA UN AFICHE
    - el estilo de la serie (`base_lp.arma`), la cámara a nivel, el gris con
      UN acento mostaza: la prenda de la víctima;
    - ningún hecho violento se dibuja: ni el golpe, ni el insulto (las
      palabras son burbujas grises sin una letra), ni el encierro con
      alguien adentro; José A.C. y el acusador privado son SILUETA;
    - el asistente que redacta mal no lleva cara;
    - el procesado de la U3 C2 no se dibuja como «el loco»: no se estigmatiza
      una enfermedad; se ve de espaldas, lejos, sin rasgos;
    - ninguna reja de cárcel, insignia, bandera, escudo ni texto legible;
    - el LADO LIBRE, porque ahí va el texto.

CADA LÁMINA TRAE DOS IDEAS (`c`, `d`); se pide una tirada de cada una y se
escoge mirando. Solo si ninguna sirve se repite la mejor.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import base_lp as S                             # noqa: E402

LADO = {'izq': 'POSTER LAYOUT: the LEFT 40 PERCENT of the frame is calm, '
               'uncluttered space -plain wall, sky, tabletop or soft shadow- '
               'with no figure, no face and no important object in it: a '
               'block of text will be laid over it later. Everything that '
               'matters sits in the right 60 percent.',
        'der': 'POSTER LAYOUT: the RIGHT 40 PERCENT of the frame is calm, '
               'uncluttered space -plain wall, sky, tabletop or soft shadow- '
               'with no figure, no face and no important object in it: a '
               'block of text will be laid over it later. Everything that '
               'matters sits in the left 60 percent.'}

AFICHE = ('This is a striking EDITORIAL FILM-POSTER ILLUSTRATION with one bold '
          'graphic idea, strong silhouettes and a clear focal point, in the '
          'flat graphic style of this series. It is ONE single picture: not a '
          'collage of panels, not a comic page, no inset frames, no borders.')

HOJA = ('The FIRST reference image is a character model sheet: use it ONLY for '
        'the identity of the woman -face, hair, build and clothes, the mustard '
        'scarf- and never for its framing, its grey background or its repeated '
        'views: she appears ONCE in this picture. Keep exactly the grey of her '
        'skin on the sheet.')

ESTILO_REF = ('The LAST reference image is a finished poster illustration from '
              'this same series, of ANOTHER story: use it ONLY for the drawing, '
              'the treatment, the palette and the poster quality -flat graphic '
              'illustration built from broad simplified tonal planes, no '
              'rendered texture, no photographic detail- and never for its '
              'people, its place or its composition.')

# clave -> {variante: (registro, personas, lugar, lado_libre, escena)}
IM = {}

IM['U1C1'] = {
 'c': ('hero', ('maria', 'jose'), 'ninguno', 'izq', '''
A DOUBLE EXPOSURE poster. A large head-and-shoulders PROFILE of %(maria)s
facing LEFT fills the right 60 percent of the frame against a plain dark grey
night background. Her face and the mustard scarf are drawn normally in flat
tonal planes: lips pressed, eyes fixed ahead, holding on.

INSIDE the dark mass of her hair and the back of her head, as in a double
exposure, a second picture shows through: a narrow street of a Colombian
barrio at night, a row of small brick houses with flat roofs, every window
DARK except ONE lit window; in that lit window, small and far away, stands
%(jose)s, only a solid dark shape against the light. The street is contained
by the outline of her head and fades softly into it; it does not spill out.

The many dark windows are the nights nobody wrote down; only one is lit.
''' ),
 'd': ('hero', ('maria', 'jose'), 'barrio', 'der', '''
Low-angle night view of a narrow street of barrio Prado Alto, a Colombian
city barrio, the camera at knee height and perfectly level. In the left 60
percent of the frame, %(maria)s stands on the pavement in the foreground with
her back to the camera, seen from the waist up, looking at a small two-storey
brick house across the street. Every window of the street is dark except ONE
lit window on the upper floor of that house; on the bright curtain of that
window falls the large shadow of %(jose)s, only a dark shape, motionless.
A single street lamp, cables overhead, hazy mountains far behind.
'''),
}

IM['U1C2'] = {
 'c': ('dia', ('asistente',), 'despacho', 'izq', '''
Overhead shot looking straight down at a plain grey desk, the camera square
to the desk. In the right 60 percent of the frame lies an open charge sheet,
its pages covered in plain grey bars; onto its main page, MANY other
documents have been laid and pinned in an overflowing heap -typed interview
transcripts, medical report forms with plain grey boxes, clipped stapled
pages- spilling over the edges of the page and off the desk like a
landslide of paper. At the bottom edge, only the two hands and forearms of
%(asistente)s, the cuffs of a plain light grey shirt, are pressing ONE MORE
page onto the heap. No face anywhere. Every page carries only plain grey
bars, never a readable character.
'''),
 'd': ('dia', ('defensora',), 'sala', 'der', '''
Medium-wide shot of a Colombian hearing room, the camera at standing height
and perfectly level. In the left 60 percent of the frame, %(defensora)s
stands at the defence table and holds up a charge sheet in one hand: its
pages have unfolded downward like a long paper accordion, page after page
stuffed with clipped transcripts and medical forms, the folded strip falling
all the way down past the table to the floor and curling there. Her other
hand is open toward it, mid-argument. Behind her, the judge's desk and the
benches, quiet, out of focus. Every page carries only plain grey bars.
'''),
}

IM['U1C3'] = {
 'c': ('hero', ('maria',), 'casa', 'izq', '''
A tall plain MIRROR hangs on the wall of the narrow hallway of a modest
home at night, in the right 60 percent of the frame, the camera at eye level
and perfectly level. The glass is cracked into THREE large pieces but they
are still held inside ONE single plain frame. Each piece reflects one
fragment of the same night: in the first, a closed plain wooden door with
its key turned in the lock; in the second, a woman's hand holding her own
upper arm through the sleeve of a light grey blouse; in the third, three
plain empty grey speech bubbles with no letters in them. Beside the mirror,
%(maria)s stands in profile looking into it, still, her hand on the frame.
One frame holds the three pieces: it is one single night.
'''),
 'd': ('hero', ('maria', 'jose'), 'casa', 'der', '''
Overhead cutaway view looking straight down into a small modest home at
night with its roof taken off, like a doll's house seen from above, the
whole floor plan placed in the left 60 percent of the frame as ONE continuous
drawing. In the bedroom, %(maria)s sits on the edge of the bed holding her
own upper arm, a plain mobile phone face down beside her; the bedroom door
is CLOSED with the key turned in it. In the hallway just outside that door
stands %(jose)s, only a dark shape seen from above. Three plain empty grey
speech bubbles with no letters float above the hallway. The rest of the
home -living room, kitchen- is quiet and dark.
'''),
}

IM['U1C4'] = {
 'c': ('dia', ('maria', 'perito'), 'consultorio', 'izq', '''
A forensic medical examination room by day, the camera at seated height and
perfectly level. In the right 60 percent of the frame, %(maria)s sits on the
plain examination couch, calm, her sleeves pushed up: her forearms are clean,
with no mark of any kind. At the desk beside her, %(perito)s looks at a
plain chart covered only in empty grey boxes. On the bare pale wall BEHIND
her falls HER SHADOW, large and sharp, and the shadow is CRACKED like broken
glass, split by dark jagged lines, while she herself is whole. Only the
shadow shows what is not visible on her skin.
'''),
 'd': ('hero', ('maria',), 'ninguno', 'der', '''
A DOUBLE EXPOSURE poster. A large head-and-shoulders PROFILE of %(maria)s
facing RIGHT fills the left 60 percent of the frame against a plain pale grey
background: her face is calm and composed, the mustard scarf drawn normally.

INSIDE the dark mass of her hair and the back of her head, as in a double
exposure, a second picture shows through: a dim narrow corridor of a home
at night ending in a CLOSED plain door with a thin line of light under it,
and on the floor in front of it, a dropped plain mobile phone. The
corridor is contained by the outline of her head and fades softly into it;
the outside of her is untouched.
'''),
}

IM['U1C5'] = {
 'c': ('hero', ('maria', 'jose'), 'casa', 'izq', '''
A small one-storey Colombian home at night seen from the front with its
front wall cut away, like a doll's house, ONE flat roof over everything,
placed in the right 60 percent of the frame, the camera level. Inside, the
signs of a shared life: two coats on the same hook by the door, two cups on
the small table, a double bed made for two, two toothbrushes in one glass.
%(maria)s stands at the kitchen counter; at the table sits %(jose)s, only a
dark shape. Above the flat roof, in the dark sky, FIVE moons in a gentle arc,
each one a different phase, from a thin crescent to full: five months under
the same roof.
'''),
 'd': ('dia', ('maria',), 'casa', 'der', '''
Close still life at the front door of a modest home at dusk, the camera at
waist height and perfectly level, everything in the left 60 percent of the
frame: on one plain wall hook hang TWO coats, a woman's and a man's, the
sleeves touching; below them, two pairs of shoes side by side on the mat;
on a small shelf, a plain dish holding TWO sets of house keys. Mid-action,
the hand of %(maria)s, the mustard scarf end visible at the edge, sets her
keys down into the dish next to the others. Through the half-open door, the
small table with two plates.
'''),
}

IM['U3C1'] = {
 'c': ('hero', ('apoderado', 'inversionistas'), 'ninguno', 'izq', '''
An ensemble film-poster composition at night, the camera at eye level and
perfectly level, everything in the right 60 percent of the frame.
%(inversionistas)s stand in three loose rows looking UP, their faces lit cold
from above by a GIANT smartphone screen hanging in the dark sky like a moon:
on the screen, a single smooth line climbs high and then DROPS straight down,
no numbers, no symbols, no letters. In front of them, %(apoderado)s faces the
viewer, holding a thick plain folder of signed pages against his chest.
'''),
 'd': ('dia', ('apoderado',), 'despacho', 'der', '''
Overhead shot looking straight down at a long plain meeting table, the camera
square to it, placed in the left 60 percent of the frame. Around the table,
FIFTEEN plain chairs. In front of THIRTEEN of them lies a single sheet of
paper with a signature drawn as a plain grey scribble and a plain pen laid
across it; in front of the remaining TWO chairs the sheets are blank and the
pens untouched. At the head of the table, the two hands of %(apoderado)s,
the cuffs of a dark grey suit, square a thick stack of signed pages.
'''),
}

IM['U3C2'] = {
 'c': ('contraluz', ('comerciante',), 'ninguno', 'izq', '''
Inside a small neighbourhood shop at closing time, the camera at counter
height and perfectly level, everything in the right 60 percent of the frame.
Behind her plain counter, %(comerciante)s stands holding a single sheet of
paper, her written request, and looks toward the shop door. On the counter
in the foreground lies a THICK closed folder of medical-legal reports with
plain grey covers, lit by one small lamp, larger in the frame than she is.
Through the shop window, far away and out of focus, a lone figure walks away
down the street, only a pale shape seen from behind, no features. Shelves of
plain unbranded goods, a gap on one shelf.
'''),
 'd': ('dia', ('comerciante',), 'despacho', 'der', '''
Overhead shot looking straight down at a plain grey desk, the camera square
to it, placed in the left 60 percent of the frame. A woman's hand, the cuff
of a plain grey work apron, pushes a single sheet of paper -her request-
across the desk. On top of that sheet, another hand in a plain grey suit
sleeve has just set down a THICK closed folder of medical-legal psychiatric
reports with plain grey covers, so heavy it pins the request flat under it.
Two shadows on the desk: the small sheet, the big folder.
'''),
}

IM['U3C3'] = {
 'c': ('contraluz', ('acusador',), 'ninguno', 'izq', '''
A film-poster composition at the foot of the wide plain stone-free concrete
steps of a Colombian courthouse, late afternoon, the camera low and level,
everything in the right 60 percent of the frame. %(acusador)s stands at the
top of the steps, huge, back-lit, a solid dark shape in a suit; his long
shadow falls down the steps over THREE small witnesses who hesitate at the
bottom, one turning back. One of his hands is held behind his back, and in
it, the only bright thing on him, a small plain paper slip: a receipt, hidden.
No emblem, no lettering, no column capitals with carvings.
'''),
 'd': ('dia', ('acusador',), 'oficina', 'der', '''
A plain desk in a small workplace office by day, the camera at seated height
and perfectly level, placed in the left 60 percent of the frame. On the desk,
a growing PILE of identical plain official envelopes, one more just slid on
top. Behind the desk, the frosted glass of the office door shows the large
dark shadow of %(acusador)s, a man in a suit, waiting on the other side. In
the foreground, a small plain paper slip -a receipt- lies half under the
pile, in shadow, almost hidden.
'''),
}


def prompt(clave, var, con_hoja=False, con_estilo=True):
    reg, gente, lugar, lado, txt = IM[clave][var]
    esc = txt % S.TOKENS if '%(' in txt else txt
    esc = AFICHE + '\n\n' + esc.strip() + '\n\n' + LADO[lado]
    if con_hoja:
        esc += '\n\n' + HOJA
    if con_estilo:
        esc += '\n\n' + ESTILO_REF
    silueta_sola = all(p in S.SIN_ROSTRO for p in gente) and bool(gente)
    return S.arma(esc, registro=reg, personas=gente, lugar=lugar,
                  con_rostro=not silueta_sola)


def todos():
    out = {}
    for k in IM:
        for v in IM[k]:
            out['LP_%s_img_%s' % (k, v)] = {
                'clave': k, 'var': v, 'lado': IM[k][v][3],
                'hoja': 'maria' in IM[k][v][1],
                'prompt': prompt(k, v, con_hoja='maria' in IM[k][v][1])}
    return out


if __name__ == '__main__':
    import json
    o = todos()
    json.dump(o, open(sys.argv[1] if len(sys.argv) > 1 else 'imagenes_lp.json',
                      'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for n, v in o.items():
        print('%-20s %s %5d' % (n, v['lado'], len(v['prompt'])))
