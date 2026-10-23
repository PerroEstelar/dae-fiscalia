# -*- coding: utf-8 -*-
"""Las clausulas comunes del P3C4 v2, bajo la BIBLIA_puesta_en_escena_P3.

QUE CAMBIA CONTRA LA v1, Y POR QUE
    La v1 prohibia, textualmente, el plano hero de la serie:

        'Flat even light, perfectly level camera, no tilt, no vignette'
        'No large area of near-black either'

    El plano que Sebastian senalo como el mejor de la serie SRPA -kf08_noche-
    mide p50 45 con el 69 % del cuadro por debajo de 60. Con la clausula de
    arriba ese plano no se puede pedir.

    Aqui la luz vuelve a ser una herramienta: hay una fuente DOMINANTE, hay
    sombra real y hay profundidad. Lo que se conserva es la camara a nivel y
    sin efectos de lente, que es lo que mantiene el registro sobrio.

LOS TRES REGISTROS
    DIA        oficinas, audiencias, mostradores            p50 80-110
    CONTRALUZ  corredores, puertas, ventanas                p50 55-80
    HERO       uno o dos por pieza, el plano de mas peso    p50 40-55

    El registro entra como clausula y ademas se mide despues en el grade.
"""

PIEL = ('Skin is a desaturated warm grey: hue around 25 degrees and saturation '
        'no higher than 0.20. It must read as GREY with only a faint warm '
        'tint: never pink, never peach, never tan, never brown and never a '
        'saturated skin colour.')

ROSTRO = ('Faces ARE drawn and expressive, but simplified and graphic: clearly '
          'defined eyes with brow, a simple nose and a simple mouth, readable '
          'at a glance, with no photographic detail, no skin pores, no '
          'individual hair strands, no caricature. Facial surfaces are built '
          'from FLAT tonal planes meeting at hard edges, never from soft '
          'airbrushed gradients on the cheek, forehead or jaw. ')

# LA SUPERFICIE SIGUE SIENDO LISA, PERO YA NO TIENE QUE SER PLANA DE TONO
#     La v1 pedia 'A PERFECTLY UNIFORM FLAT AREA OF SOLID GREY', y eso mata la
#     caida de luz sobre una pared. Lo que hay que prohibir es la TEXTURA
#     -moteado, veta, grano-, no el degradado de iluminacion.
PLANOS = ('Every large surface is smooth and free of material texture: not '
          'stone, not marble, not granite, not concrete, not plaster texture, '
          'not wallpaper, not wood grain, with no mottling, no speckle, no '
          'veining, no blotches, no camouflage pattern, no paper grain and no '
          'noise. A surface MAY carry a smooth gradient of light across it, '
          'and it may fall into shadow: that is light, not texture.')

REGISTRO = {
 # El registro de dia nombraba 'one dominant side window out of frame', y
 # eso no tiene sentido en una calle. Ahora nombra una DIRECCION, que vale
 # igual adentro y afuera.
 'dia': ('LIGHT: ordinary daylight arriving from ONE dominant direction. Mid '
         'grey overall, with a clearly lighter plane where the light lands '
         'and a clearly darker one away from it, and a real cast shadow. '
         'There is a genuinely light value and a genuine dark in the frame, '
         'and the brightest value is a light grey clearly darker than paper '
         'white.'),
 'contraluz': ('LIGHT: the only bright thing in the frame is a doorway, a '
               'window or the far end of a corridor, and it is BEHIND the '
               'subject. Everything nearer the camera sits in deep shadow and '
               'reads mostly as silhouette and edge. More than half the frame '
               'is dark. No glare, no bloom, no lens flare, no visible light '
               'rays.'),
 'hero': ('LIGHT: low-key. One low, weak light source deep in the frame; '
          'everything else falls away into near-black. More than half of the '
          'picture is dark and the dark has real depth, not a flat black '
          'fill. Long soft gradient across the ground. The background '
          'dissolves into haze. No glare, no bloom, no lens flare.'),
}

# La camara se queda a nivel. Es lo unico que queda de la clausula vieja, y es
# lo que impide que el modelo se ponga a hacer angulaciones de thriller.
CAMARA = ('Perfectly level camera, no dutch tilt, no fisheye, no vignette, no '
          'lens flare, no depth-of-field bokeh discs.')

LIMPIA = ('Clean plate: no legible text, no lettering, no numbers, no '
          'signage, no labels, no logos, no emblem, no insignia, no badge, no '
          'coat of arms, no seal with a device in it. Where a document, a '
          'form, a notebook page or a screen carries writing, it is reduced '
          'to plain flat grey bars with no readable character anywhere.')

SIN_ROLES = ('No uniform, no robe, no gown, no sash, no insignia, no badge, no '
             'lanyard, no identity card: nobody in this image is marked as an '
             'official of any kind.')

ESTILO = ('Stylized editorial character illustration, flat graphic treatment. '
          'No ink outline anywhere: forms are built from broad soft tonal '
          'planes, never from rendered shading, never from texture or brush '
          'marks. ')

FIGURA = ('Figures are 8 to 8.5 heads tall. Colombian features, varied from '
          'one person to the next, carried by facial structure, hair and '
          'silhouette rather than by skin colour. The environment is almost '
          'fully desaturated, only the faintest trace of colour left in the '
          'greys.')

LUGAR = ('The setting is ordinary Colombian: plain painted masonry, simple '
         'metal-framed windows with plain glass, modest institutional '
         'furniture, nothing lavish and nothing north-american in the '
         'fittings.')

NEG = ('Not a photograph, not a 3D render, not painterly. No ink outlines, no '
       'multicolour gradients, no brush texture, no childish or cartoon-mascot '
       'styling, no big round anime eyes, no exaggerated features, no soft '
       'airbrushed skin shading. Out-of-focus areas are PAINTED blur: '
       'simplified shapes with soft edges, never circular bokeh discs. No '
       'motion blur, no speed lines and no streaks.')

ACENTO = ('That accent band is the ONLY saturated colour anywhere in the whole '
          'image: everything else, without exception, is grey.')

# LOS TOKENS, CON VIDA
#     La v1 daba edad y ropa. Eso basta para repetir un cuerpo y no basta para
#     que haya alguien adentro. Cada uno lleva ahora de donde viene, en que
#     estado esta en esta pieza, y UNA COSA SUYA que vuelve en mas de un plano.
# LOS TOKENS, PARTIDOS EN DOS
#     El cuerpo va EN LINEA dentro de la frase de la escena, asi que tiene que
#     ser una aposicion y nada mas: si se le mete ahi la biografia, la frase
#     se rompe a la mitad -«...looking along the road rather than at the lens
#     stands SMALL beside its front wheel»- y el modelo pierde el hilo.
#
#     La vida y el estado van en un parrafo aparte, WHO THESE PEOPLE ARE, que
#     es donde el modelo los lee como caracterizacion y no como sintaxis.
CUERPO = {
 'nora': ('NORA, a woman of about forty, medium build, medium height, dark '
          'hair tied back at the nape with a few strands loose, in a plain '
          'light grey blouse over plain grey trousers and flat grey shoes, '
          'with a plain institutional yellow band across the chest of the '
          'blouse, a soft grey cardigan folded over one forearm'),
 'ivan': ('IVAN, a man of about thirty-five, lean, medium height, short dark '
          'hair, clean shaven, in a plain mid-grey collared shirt with the '
          'sleeves rolled twice over plain grey trousers and grey shoes, with '
          'a plain institutional yellow band running down the front placket '
          'of the shirt'),
 'lina': ('LINA, a woman of about thirty, slim, medium height, dark hair worn '
          'loose to the shoulders, in a plain mid-grey blouse over plain grey '
          'trousers and flat grey shoes, with a plain institutional yellow '
          'cuff band on the left sleeve'),
 'recepcionista': ('THE YOUNG DESK CLERK, a man of about twenty-five, slight '
                   'build, medium height, short dark hair, in a plain '
                   'institutional blue work shirt over plain grey trousers '
                   'and grey shoes'),
 'fiscal': ('THE PROSECUTOR, a man of about fifty, heavy build, broad '
            'shouldered, grey at the temples, in a plain dark grey shirt with '
            'the collar open and the sleeves pushed up, over plain grey '
            'trousers, no tie'),
 'investigador': ('THE INVESTIGATOR, a man of about thirty, medium build, '
                  'short dark hair, in a plain mid grey zip jacket worn open '
                  'over a plain grey t-shirt and grey trousers'),
 'jueza': ('THE JUDGE, a woman of about fifty-five, medium build, dark hair '
           'cut short and greying, in a plain mid grey jacket over a plain '
           'light grey blouse, with no robe, no gown and no insignia of any '
           'kind'),
 'otra_fiscal': ('THE SECOND PROSECUTOR, a woman of about forty, slim, dark '
                 'hair gathered at the back, in a plain light grey blouse '
                 'over plain grey trousers'),
 'representante': ('THE VICTIM REPRESENTATIVE, a woman of about forty-five, '
                   'medium build, dark hair in a low bun, in a plain mid grey '
                   'jacket over a plain grey blouse'),
 'vecina': ('THE NEIGHBOUR, a woman of about sixty, short, heavy build, grey '
            'hair tied back, in a plain grey housecoat over a plain grey '
            'dress and flat grey sandals'),
}

VIDA = {
 'nora': ('Nora has worked in rented rooms and small front desks for twenty '
          'years and stands like someone used to being looked at while she '
          'waits. She keeps the cardigan folded over her arm and never puts '
          'it on. Here she is DISTANT: head level and turned slightly away, '
          'shoulders neutral, arms relaxed, answering nothing.'),
 'ivan': ('Ivan drives for a living and reads a road before he reads a '
          'person. A plain dark grey phone is in his hand or within reach of '
          'it. Here he is RESOLVED: upright and square, chin level, still, '
          'looking along the road rather than at the lens.'),
 'lina': ('Lina came to the city to work and has spent a year answering for a '
          'sentence that names nothing. She holds the same thin folded paper '
          'in both hands, already soft at the creases. Here she is GUARDED: '
          'head inclined down, chin tucked, shoulders rounded inward, arms '
          'close to the body.'),
 'recepcionista': ('The desk clerk took the night shift because it let him '
                   'study in the mornings. A ring of plain keys is in his '
                   'hand or on the counter in front of him. Here he is '
                   'EMPTIED: head slightly lowered, shoulders dropped, arms '
                   'hanging.'),
 'fiscal': ('Twenty-six years in the same building. A plain metal thermos '
            'stands on his desk. Here he is RESOLVED: square to his work, '
            'chin level, unhurried.'),
 'investigador': ('Newer at this than everyone around him, and eager. He '
                  'carries a grey box file under one arm wherever he goes.'),
 'jueza': ('She has heard four of these today. A pair of plain reading '
           'glasses is pushed up on her head or folded in her hand. Here she '
           'is RESOLVED: upright, chin level, shoulders open, hands still.'),
 'otra_fiscal': ('She inherited this file three weeks ago and is reading it '
                 'for the first time. A grey enamel mug sits beside her '
                 'work.'),
 'representante': ('She holds a plain grey document wallet against her chest '
                   'with both arms and does not put it down.'),
 'vecina': ('She is holding a cloth, as if she had come to the door in the '
            'middle of something.'),
}

TOKENS = CUERPO          # lo que se interpola en la escena

EXTERIOR = ('The setting is an ordinary Colombian street or waterfront: '
            'plain rendered walls, plain kerbs, modest low buildings, nothing '
            'lavish, nothing picturesque and nothing north-american in the '
            'fittings. No palm-tree postcard framing, no tourist colour.')


def arma(escena, registro='dia', personas=(), con_acento=False,
         con_lugar=True, con_rostro=True, exterior=False):
    """Arma el prompt final. Lo armado es lo que se manda y lo que se guarda."""
    p = [escena.strip()]
    if personas:
        p.append('WHO THESE PEOPLE ARE. '
                 + ' '.join(VIDA[x] for x in personas))
    p.append(REGISTRO[registro])
    p.append(PLANOS)
    p.append(ESTILO + (ROSTRO if (con_rostro and personas) else '')
             + (PIEL + ' ' if personas else '') + FIGURA)
    p.append(CAMARA)
    if con_acento:
        p.append(ACENTO)
    if con_lugar:
        p.append(EXTERIOR if exterior else LUGAR)
    p.append(LIMPIA)
    p.append(SIN_ROLES)
    p.append(NEG)
    return '\n\n'.join(x.strip() for x in p if x and x.strip())
