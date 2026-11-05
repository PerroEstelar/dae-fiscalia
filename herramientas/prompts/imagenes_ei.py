# -*- coding: utf-8 -*-
r"""Las láminas del curso Estándares interamericanos: S02 S03 S05 S09 S10 S11.

Es `imagenes_lp` (las láminas de Ley 1826, y antes las de «16 situaciones»):
ilustración tipo AFICHE DE CINE, a sangre, con una idea gráfica fuerte, y en
su LADO LIBRE el panel azul con el texto VERBATIM de la situación
(`lamina_ei`). La referencia de estilo es una lámina aprobada de Ley 1826
(LP U1C3, subida a la cuenta nueva como EI_ANCLA_afiche3).

LO QUE NO SE NEGOCIA, AUNQUE SEA UN AFICHE
    - el estilo de la serie (`base_ei.arma`), la cámara a nivel, el gris;
      UN acento mostaza solo donde hay alguien que falta (S05: la bufanda de
      la persona desaparecida, la misma de S04; S09: el saco del hijo);
    - ninguna desaparición, detención, masacre ni violencia: S10 (La Rochela)
      es el TIEMPO de los procesos -expedientes que se vuelven montaña-, no
      el hecho;
    - ningún texto legible: libros, sentencias y fachadas lisas, sin una
      letra (la fachada del Palacio de Justicia sin su inscripción);
    - el LADO LIBRE, porque ahí va el texto. S10 lleva la lectura de la
      sentencia y su panel es ancho: la ilustración se queda en el 42 %.

CADA LÁMINA TRAE DOS IDEAS (`c`, `d`); se pide una tirada de cada una y se
escoge mirando.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import base_ei as S                             # noqa: E402

LADO = {}
for lado, libre, lleno in (('izq', 'LEFT', 'right'), ('der', 'RIGHT', 'left')):
    for pct, resto, sufijo in ((40, 60, ''), (55, 45, '_ancho')):
        LADO[lado + sufijo] = (
            'POSTER LAYOUT: the %s %d PERCENT of the frame is calm, uncluttered '
            'space -plain wall, sky, tabletop or soft shadow- with no figure, no '
            'face and no important object in it: a block of text will be laid '
            'over it later. Everything that matters sits in the %s %d percent.'
            % (libre, pct, lleno, resto)
            # la marca de la serie va arriba en el lado lleno (lamina_ei): S05 y
            # S11 salieron con una cabeza justo debajo
            + ' The top %s corner of the frame -the upper quarter of the outer '
            'fifth- stays plain wall, window or sky: no head and no face there.'
            % lleno)

AFICHE = ('This is a striking EDITORIAL FILM-POSTER ILLUSTRATION with one bold '
          'graphic idea, strong silhouettes and a clear focal point, in the '
          'flat graphic style of this series. It is ONE single picture: not a '
          'collage of panels, not a comic page, no inset frames, no borders.')

# S05 y S11 (5 nov): las primeras (`c`) eran afiche puro -dos tomos como
# monolitos con el equipo diminuto, un expediente que pasa entre dos manos sin
# cuerpo- y Sebastian las vio raras. Las nuevas (`e`, `f`) son UN MOMENTO
# CORRIENTE, a escala humana, como las que funcionaron (S02, S03, S09).
LEGIBLE = ('This is a clear, calm EDITORIAL ILLUSTRATION of one ordinary '
           'working moment, readable at a glance: real people at true human '
           'scale in a real place, nothing symbolic, nothing oversized, no '
           'visual metaphor, in the flat graphic style of this series. It is '
           'ONE single picture: not a collage of panels, not a comic page, no '
           'inset frames, no borders. Every hand belongs to a person whose '
           'body is visible in the picture.')
CABECERA_LEGIBLE = {('S05', 'e'), ('S05', 'f'), ('S11', 'e'), ('S11', 'f')}

ESTILO_REF = ('The LAST reference image is a finished poster illustration from '
              'this same series, of ANOTHER story: use it ONLY for the drawing, '
              'the treatment, the palette and the poster quality -flat graphic '
              'illustration built from broad simplified tonal planes, no '
              'rendered texture, no photographic detail- and never for its '
              'people, its place or its composition.')

CUERPO = {
 'servidor_s02': ('A PROSECUTION OFFICIAL, a Colombian man of about forty-five, '
                  'short dark hair greying at the temples, plain dark-rimmed '
                  'glasses, in a plain grey suit and a plain white shirt with no '
                  'tie'),
 'fiscal_s03': ('A PROSECUTOR, a Colombian woman of about thirty-five, straight '
                'dark hair in a low ponytail, in a plain dark grey blazer over a '
                'plain light grey blouse'),
 'colegas_s03': ('THREE COLLEAGUES of different ages, two men and one woman, in '
                 'plain shirts and blazers in shades of grey'),
 'equipo_s05': ('TWO INVESTIGATORS, a Colombian man of about forty in a plain '
                'grey shirt and a Colombian woman of about thirty-five in a plain '
                'dark blazer, seen small'),
 'investigador_s05': ('AN INVESTIGATOR, a Colombian man of about forty, short '
                      'dark hair, clean-shaven, in a plain grey shirt with the '
                      'sleeves rolled to the forearm'),
 'investigadora_s05': ('AN INVESTIGATOR, a Colombian woman of about thirty-five, '
                       'dark hair tied back, in a plain dark grey blazer over a '
                       'plain white blouse'),
 'madre_s09': ('A MOTHER, a Colombian woman of about sixty-five, small and '
               'upright, grey hair in a low bun, in a plain dark grey cardigan and '
               'a plain dark skirt'),
 'funcionario_s10': ('A JUDICIAL OFFICIAL, a tiny distant figure in a plain dark '
                     'suit seen from behind'),
 'manos_s11': ('TWO ANONYMOUS HANDS of ordinary adults in plain grey suit cuffs; '
               'no face anywhere'),
 'fiscal_s11': ('A PROSECUTOR, a Colombian woman of about forty-five, short '
                'dark hair, plain thin-rimmed glasses, in a plain charcoal suit '
                'jacket over a plain light grey blouse'),
 'colega_s11': ('A COLLEAGUE, a Colombian man of about thirty, short dark hair, '
                'in a plain light grey shirt and plain dark trousers'),
 'gente_s11': ('THREE PEOPLE in plain dark office clothes, tiny on the square, '
               'seen from behind'),
}
TOKENS = dict(S.CUERPO, **CUERPO)
SIN_ROSTRO = set(S.SIN_ROSTRO) | {'equipo_s05', 'funcionario_s10', 'manos_s11',
                                  'gente_s11', 'colegas_s03'}

# clave -> {variante: (registro, personas, lugar, lado_libre, prenda, escena)}
IM = {}

IM['S02'] = {
 'c': ('hero', ('servidor_s02',), 'ninguno', 'izq', None, '''
A dark meeting room lit only by a projector. In the right 60 percent of the
frame, %(servidor_s02)s stands in three-quarter view in front of a large
projection screen; projected on the screen, a simple pale diagram: the plain
outlines of the continents -the Americas, Europe and Africa- with a few plain
circles drawn around groups of them and thin lines linking the circles, no
letters, no numbers, no symbols. In his left hand a small stack of plain
index cards; with his right hand he holds ONE card up into the beam of the
projector, studying it closely, brows drawn together, his face half lit. The
light of the projector crosses the room in a soft beam.
'''),
 'd': ('dia', ('servidor_s02',), 'ninguno', 'der', None, '''
Overhead shot looking straight down at a long plain grey table, the camera
square to it, everything in the left 60 percent of the frame. On the table,
FIVE plain index cards are laid out in a neat row, each carrying only a few
plain grey bars; the third card lies slightly askew. A man's hand in a plain
grey suit cuff holds a plain pencil hovering just above that third card.
Beside the row, an open laptop whose screen shows the same pale diagram of
continent outlines circled and linked by thin lines, no letters.
'''),
}

IM['S03'] = {
 'c': ('dia', ('fiscal_s03', 'colegas_s03'), 'ninguno', 'izq', None, '''
A working meeting in a plain office of a Colombian prosecution unit, the
camera at seated height and perfectly level, everything in the right 60
percent of the frame. Around a plain table sit %(colegas_s03)s and, in the
foreground in three-quarter view, %(fiscal_s03)s. In the middle of the table,
stacked like a small city, lie very different kinds of legal sources, each a
different shape: one thick treaty volume with a plain cover, a few slim
stapled reports, a tall stack of bound court decisions with a plain ribbon
marker, a ring binder of rules. Each person reaches for or points at a
DIFFERENT one; the woman in the foreground holds her hand above the treaty
volume, deciding. No letters on any cover.
'''),
 'd': ('contraluz', ('fiscal_s03',), 'ninguno', 'der', None, '''
A tall legal library with shelves up to the ceiling, the camera low and
perfectly level, everything in the left 60 percent of the frame. %(fiscal_s03)s
stands on a plain library ladder halfway up, in three-quarter back view,
reaching toward a shelf; around her the shelves hold clearly different
kinds of sources: rows of thick bound volumes, boxes of slim reports, ring
binders, single treaty volumes standing apart. A tall window behind the
shelves throws a band of light across them. No letters on any spine.
'''),
}

IM['S05'] = {
 'c': ('hero', ('equipo_s05',), 'ninguno', 'izq', 'bufanda', '''
A poster composition on a long dark desk at night, the camera at desk height
and perfectly level, everything in the right 60 percent of the frame. Two
ENORMOUS bound volumes with blank covers stand upright on the desk like two
monoliths: the left one older and worn at the edges, the right one newer.
Between and below them, small, %(equipo_s05)s sit reading at the desk under a
single plain lamp, their long shadows thrown up the faces of the two volumes.
In front of them lies an open case folder with a sealed clear evidence bag on
it holding a folded matte mustard knitted scarf. No letters anywhere.
'''),
 'd': ('contraluz', ('equipo_s05',), 'ninguno', 'der', 'bufanda', '''
Over-the-shoulder shot at a plain reading table by a tall window, the camera
at seated height and perfectly level, everything in the left 60 percent of
the frame. Two thick bound volumes lie open side by side, their pages only
plain grey bars, a plain bookmark in each; two hands, a man's and a woman's,
rest one on each volume. At the edge of the table, the closed case folder
with a sealed clear evidence bag holding a folded matte mustard knitted
scarf. The window light falls across both open books.
'''),
 'e': ('dia', ('investigadora_s05', 'investigador_s05'), 'ninguno', 'izq',
       'bufanda', '''
A plain working office of a Colombian prosecution unit in the daytime, a
medium shot with the camera at seated eye level and perfectly level,
everything in the right 55 percent of the frame. At a plain wooden table,
%(investigadora_s05)s and %(investigador_s05)s sit side by side in
three-quarter view, both looking down at the same page. In front of them lie
TWO printed court judgments, two thick stapled documents of plain white
pages, open side by side: she points with a pen at a paragraph of the left
one, he holds the right one open with one hand and leans in to compare. The
pages show only plain grey lines, no letters. At the near corner of the
table, a closed plain case folder, and lying flat on it a small clear
evidence bag holding a matte mustard knitted scarf folded FLAT into a neat
small rectangle, its short fringe visible at one end. Behind them a plain
bare wall and a window onto a plain overcast sky. Everything at true human
scale.
'''),
 'f': ('dia', ('investigadora_s05', 'investigador_s05'), 'ninguno', 'izq',
       'bufanda', '''
A plain working office of a Colombian prosecution unit, a tall window behind
the people, a medium shot with the camera at standing chest height and
perfectly level, everything in the right 55 percent of the frame.
%(investigadora_s05)s stands by the table holding a thick printed court
judgment open in both hands, reading a passage aloud; %(investigador_s05)s
sits at the table and looks up at her, his hand resting on a second printed
judgment open in front of him, a plain pen on it. The pages show only plain
grey lines, no letters. On the table, near him, a closed plain case folder
with a small clear evidence bag lying flat on it, holding a matte mustard
knitted scarf folded FLAT into a neat small rectangle. Behind them a plain
bare wall. Everything at true human scale.
'''),
}

IM['S09'] = {
 'c': ('contraluz', ('madre_s09',), 'ninguno', 'izq',
       'the folded knitted sweater on her lap', '''
A long empty courthouse corridor, the camera at seated height and perfectly
level, everything in the right 60 percent of the frame. A single tall plain
door stands WIDE OPEN, and behind it there is only a blank plain wall, close,
with nothing beyond. Facing that open door, on a long worn wooden bench,
%(madre_s09)s sits upright and waits, in three-quarter view, a folded matte
mustard-yellow knitted sweater held on her lap in both hands. Light from a
high window falls across the floor in long bands; dust in the air.
'''),
 'd': ('hero', ('madre_s09',), 'ninguno', 'der',
       'the folded knitted sweater in her hands', '''
A DOUBLE EXPOSURE poster. A large head-and-shoulders PROFILE of %(madre_s09)s
facing RIGHT fills the left 60 percent of the frame against a plain dark grey
background; at the bottom of the frame her two hands hold a folded matte
mustard-yellow knitted sweater against her chest. Inside the dark mass of her
hair and the back of her head, as in a double exposure, a second picture
shows through: an endless judicial archive, shelves of old case folders tied
with plain string receding into darkness, year after year, all of them
closed. The archive is contained by the outline of her head and fades softly
into it.
'''),
}

IM['S10'] = {
 'c': ('contraluz', ('funcionario_s10',), 'ninguno', 'izq_ancho', None, '''
A poster composition, everything in the right 45 percent of the frame, the
camera low and perfectly level. On a long plain table, a towering stack of
old court case folders tied with plain string rises higher and higher until,
at the top, the stack becomes the steep green mountains of Santander, Colombia
-their ridges, their forests, a winding mountain road climbing them- under a
pale grey sky: the files and the mountains are one shape. At the foot of the
stack, tiny, %(funcionario_s10)s reads at a small desk under a plain lamp. No
letters on any folder.
'''),
 'd': ('dia', (), 'ninguno', 'der_ancho', None, '''
A high court room seen from the public seats, the camera at seated height and
perfectly level, everything in the left 45 percent of the frame. The long
judges' bench of plain wood stands empty under tall windows; on it rise
several tall stacks of old case folders tied with plain string, some of them
yellowed and bowed with age. Above the bench, a plain round wall clock with
hands and NO numerals. Long bands of daylight across the empty room. No
flag, no emblem, no letters anywhere.
'''),
}

IM['S11'] = {
 'c': ('hero', ('manos_s11',), 'ninguno', 'izq', None, '''
A poster still life on a long dark table under one plain lamp, the camera at
table height and perfectly level, everything in the right 60 percent of the
frame. THREE objects stand in a row, each with its own pool of light: first,
a thick bound judgment volume, closed, tied with a plain ribbon; second, a
plain case folder being passed across the table from one hand to another
-%(manos_s11)s-; third, a plain clipboard with a single sheet of grey check
marks in a column and a plain pen beside it. Behind them, through a tall
window, the dark silhouette of a large stone courthouse. No letters anywhere.
'''),
 'd': ('dia', ('gente_s11',), 'ninguno', 'der', None, '''
The plain stone facade of a large modern courthouse on a wide paved city
square in Bogota at dawn, seen frontally from across the square, the camera
low and perfectly level, everything in the left 60 percent of the frame: a
massive, almost windowless wall of pale stone with NO inscription and no
lettering of any kind, and the Andean hills behind under a pale sky. Crossing
the square toward it, %(gente_s11)s walk apart from one another: one carries
a thick bound volume, one a plain case folder, one a plain clipboard. Long
morning shadows. No flag, no statue, no letters.
'''),
 'e': ('dia', ('fiscal_s11', 'colega_s11'), 'ninguno', 'izq', None, '''
A plain office of a Colombian prosecution unit in the daytime, a medium shot
with the camera at seated eye level and perfectly level, everything in the
right 55 percent of the frame. %(fiscal_s11)s sits at her plain desk in
three-quarter view. Standing beside the desk, %(colega_s11)s hands her a
SHORT stapled document of three or four plain white pages, and she takes it
with one hand, already looking at it. On the desk next to her lies the full
judgment: one very thick bound volume, closed, with a plain blank cover, so
the thin summary and the thick judgment read clearly side by side. Both
people are seen whole from the waist up. Behind them a plain bare wall and a
window onto a plain overcast sky. No letters anywhere.
'''),
 'f': ('dia', ('fiscal_s11',), 'ninguno', 'izq', None, '''
Over-the-shoulder view from just behind and beside %(fiscal_s11)s, seated at
her plain desk in front of a tall window, the camera at seated height and
perfectly level, everything in the right 55 percent of the frame. We see her
shoulder, her hair and the side of her face in profile. She holds a short
stapled summary of a few plain white pages; the page facing us shows exactly
THREE short paragraphs clearly separated by white space, each a small block
of plain grey lines with a plain small dark square at its left, and the tip
of her pen rests beside the first block. On the desk next to her, the full
judgment: one very thick bound volume, closed, with a plain blank cover. No
letters anywhere, no check marks.
'''),
}


def prompt(clave, var, con_estilo=True):
    reg, gente, lugar, lado, prenda, txt = IM[clave][var]
    esc = txt % TOKENS if '%(' in txt else txt
    cab = LEGIBLE if (clave, var) in CABECERA_LEGIBLE else AFICHE
    esc = cab + '\n\n' + esc.strip() + '\n\n' + LADO[lado]
    if con_estilo:
        esc += '\n\n' + ESTILO_REF
    silueta_sola = bool(gente) and all(p in SIN_ROSTRO for p in gente)
    # las personas de lamina no estan en base_ei.VIDA: arma solo usa VIDA para
    # las que esten; el token ya va en la escena
    return S.arma(esc, registro=reg, personas=gente, lugar=lugar,
                  con_rostro=not silueta_sola, con_acento=prenda)


def todos():
    out = {}
    for k in IM:
        for v in IM[k]:
            out['EI_%s_img_%s' % (k, v)] = {
                'clave': k, 'var': v, 'lado': IM[k][v][3],
                'prompt': prompt(k, v)}
    return out


if __name__ == '__main__':
    import json
    o = todos()
    json.dump(o, open(sys.argv[1] if len(sys.argv) > 1 else 'imagenes_ei.json',
                      'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for n, v in o.items():
        print('%-16s %-9s %5d' % (n, v['lado'], len(v['prompt'])))
