# -*- coding: utf-8 -*-
"""Las clausulas comunes y los tokens del P3C5. Lo que de verdad se envia.

LA LECCION DEL CASO 3: EL BORRADOR LOCAL NO ES LO QUE SE MANDA
    Alli se guardaron seis prompts antes de mandarlos y cuatro traian una
    frase de mas. Aqui el prompt se ARMA con `arma()` y se manda lo armado,
    y lo armado se guarda. No hay dos versiones.

LOS CUATRO CON CARA, Y NADIE MAS
    Oscar, Lucia, Renata y Tomas. Ver personajes_p3c5.md: Andres y la
    psicologa son funcionarios y van sin cara, la tercera mujer no se dibuja
    de ninguna forma, y el guia y la voz de «la entrega» tampoco.

    Los cuatro llevan acento amarillo, cada uno en una prenda distinta. NO se
    le da a Tomas un color aparte aunque contra el casi nada quedo probado:
    vestirlo distinto seria adelantar el resultado en el minuto dos.
"""
# Las cuatro de la primera tanda salieron con la piel rosa pese a pedirla
# gris. `piel.py` lo corrige en el grade, pero cuanto menos haya que mover,
# mejor: se nombran los colores que NO son, que es lo que funciona.
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

PLANOS = ('EVERY LARGE SURFACE IN THIS IMAGE IS A PERFECTLY UNIFORM FLAT AREA '
          'OF SOLID GREY, plain and smooth: not stone, not marble, not '
          'granite, not concrete, not plaster texture, not wallpaper, not '
          'wood grain, with no mottling, no speckle, no veining, no blotches, '
          'no camouflage, no maze pattern, no grain, no noise and no pattern '
          'of any kind.')

# r02 de la primera tanda salio con la ventana y la mesa en una masa casi
# blanca. «No large area of near-white» no alcanzo: hay que prohibir el
# quemado por su nombre y fijar cual es el valor mas claro admisible.
TONOS = ('The frame must have three clearly separate tonal zones and all three '
         'must be present: a deep dark, a mid grey, and a genuinely light '
         'value. NO PART OF THIS IMAGE IS BLOWN OUT TO WHITE: the brightest '
         'value anywhere in the picture is a light grey clearly darker than '
         'paper white, and there is no glare, no hotspot, no bloom and no '
         'washed-out area. No large area of near-black either.')

LIMPIA = ('Clean plate: no legible text, no lettering, no numbers, no '
          'signage, no labels, no logos, no emblem, no insignia, no badge, no '
          'coat of arms, no seal with a device in it. Where a document, a '
          'form, a notebook page or a screen carries writing, it is reduced '
          'to plain flat grey bars with no readable character anywhere.')

# La regla SRPA, igual de dura que en el Caso 4: ningun operador juridico
# tiene cuerpo reconocible como tal.
SIN_ROLES = ('No uniform, no robe, no gown, no sash, no insignia, no badge, no '
             'lanyard, no identity card: nobody in this image is marked as an '
             'official of any kind.')

NEG = ('Not a photograph, not a 3D render, not painterly. No ink outlines, no '
       'multicolour gradients, no paper grain, no brush texture, no childish '
       'or cartoon-mascot styling, no big round anime eyes, no soft airbrushed '
       'skin shading. Out-of-focus areas are PAINTED blur: simplified shapes '
       'with soft edges, never circular bokeh discs. No motion blur, no speed '
       'lines and no streaks: the movement is carried by the pose alone, '
       'frozen, never smeared.')

# El encuadre es colombiano y hay que decirlo: sin esto el modelo pone
# oficinas norteamericanas.
LUGAR = ('The setting is an ordinary Colombian public building interior: plain '
         'painted masonry walls, simple metal-framed windows with plain glass, '
         'modest institutional furniture, nothing lavish and nothing '
         'north-american in the fittings.')


# LA CLAUSULA CENITAL, MEDIDA
#     «Overhead shot looking STRAIGHT DOWN» produjo una oblicua con ventanas
#     y pared en el tercio superior del cuadro. No alcanza. Lo que si
#     funciona, probado contra r01: nombrar el aparato -copy stand, escaner-,
#     decir que el plano de la mesa es PARALELO al plano de imagen, y
#     prohibir por su nombre todo lo que no sea mesa.
#
#     Importa el doble porque 22 de las 43 escenas son cenitales y la rima
#     mayor -la mesa de Oscar contra la de Tomas- necesita que el encuadre se
#     repita exacto.
CENITAL = ('NADIR AERIAL VIEW. The camera is mounted directly above the '
           'surface with the lens pointing VERTICALLY DOWNWARD at exactly 90 '
           'degrees to the floor, like a copy-stand or a document scanner. '
           'THE SURFACE IS PARALLEL TO THE IMAGE PLANE and fills the ENTIRE '
           'frame from edge to edge.\n\n'
           'ABSOLUTELY NO WALL, NO WINDOW, NO CEILING, NO FLOOR, NO HORIZON, '
           'NO ROOM AND NO BACKGROUND IS VISIBLE ANYWHERE IN THIS PICTURE. '
           'There is no perspective and no vanishing point: nothing recedes, '
           'nothing converges, and no vertical surface appears. No head, no '
           'face and no shoulder appears anywhere.')


def estilo(con_rostro):
    return ('Stylized editorial %sillustration, flat graphic treatment. No ink '
            'outline anywhere: forms are built from broad soft tonal planes, '
            'never from rendered shading, never from texture or brush marks. '
            '%s%s Figures are 8 to 8.5 heads tall. The environment is almost '
            'fully desaturated, only the faintest trace of colour left in the '
            'greys, close to neutral grey but not quite monochrome. Flat even '
            'light, perfectly level camera, no tilt, no vignette, no lens '
            'flare.'
            % ('character ' if con_rostro else '',
               ROSTRO if con_rostro else '', PIEL))


TOKENS = {
 'oscar': ('a man of about forty-five, heavy-set, medium height, short dark '
           'hair receding at the temples, clean shaven, wearing a plain '
           'mid-grey short-sleeved shirt over plain grey trousers and grey '
           'shoes, with a plain institutional yellow band around the left '
           'upper sleeve'),
 'lucia': ('a woman of about twenty-six, slim, medium height, dark hair tied '
           'back low, wearing a plain light grey long-sleeved blouse over '
           'plain grey trousers and grey flat shoes, with a plain '
           'institutional yellow band at each cuff'),
 'renata': ('a woman of about thirty, medium build, dark hair worn loose to '
            'the shoulders, wearing a plain mid-grey round-neck jumper over '
            'plain grey trousers, with a plain institutional yellow band '
            'across the shoulders of the jumper'),
 'tomas': ('a man of about thirty-eight, lean, tall, short dark hair, a '
           'close-trimmed beard, wearing a plain mid-grey collared shirt '
           'buttoned to the neck over plain grey trousers and grey shoes, '
           'with a plain institutional yellow band around the right wrist'),
}


def unico(cosa='band'):
    """El unico acento saturado del cuadro se pide como UNICO.

    Es la leccion del Caso 3: `grade_placas` tiene piso de saturacion 0,45 y
    `forzar` no mueve el tope, asi que una banda generada por debajo no se
    arregla despues.
    """
    return ('THAT %s IS THE ONLY SATURATED COLOUR ANYWHERE IN THE WHOLE IMAGE: '
            'everything else, without exception, is grey.' % cosa.upper())


def arma(escena, con_rostro=False, con_acento=False, con_lugar=True,
         cenital=False):
    """con_acento: False, o el nombre de la prenda que lleva el acento.

    cenital=True antepone la clausula de camara perpendicular y quita el
    bloque de lugar: en una cenital no se ve la habitacion, asi que describir
    el edificio solo le da al modelo una excusa para inclinar la camara.
    """
    partes = [CENITAL] if cenital else []
    partes.append(escena.strip())
    if cenital:
        con_lugar = False
    if con_acento:
        partes.append(unico(con_acento if isinstance(con_acento, str) else 'band'))
    partes += [PLANOS, TONOS, estilo(con_rostro)]
    if con_lugar:
        partes.append(LUGAR)
    partes += [LIMPIA, SIN_ROLES, NEG]
    return '\n\n'.join(partes)
