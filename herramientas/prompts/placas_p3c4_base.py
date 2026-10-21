# -*- coding: utf-8 -*-
"""Las clausulas comunes y los tokens del P3C4. Lo que de verdad se envia.

LA LECCION DEL CASO 3: EL BORRADOR LOCAL NO ES LO QUE SE MANDA
    Alli se guardaron seis prompts antes de mandarlos y cuatro traian una
    frase de mas. Aqui el prompt se ARMA con `arma()` y se manda lo armado,
    y lo armado se guarda. No hay dos versiones.
"""
PIEL = ('Skin is a desaturated warm grey: hue around 25 degrees and saturation '
        'no higher than 0.20. It must read as grey with a faint warm tint, '
        'never as brown and never as a saturated skin colour.')

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

TONOS = ('The frame must have three clearly separate tonal zones and all three '
         'must be present: a deep dark, a mid grey, and a genuinely light '
         'value. No large area of near-black and no large area of near-white '
         'anywhere.')

LIMPIA = ('Clean plate: no legible text, no lettering, no numbers, no '
          'signage, no labels, no logos, no emblem, no insignia, no badge, no '
          'coat of arms, no seal with a device in it. Where a document, a '
          'form or a screen carries writing, it is reduced to plain flat grey '
          'bars with no readable character anywhere.')

# La regla SRPA del Caso 3, endurecida: aqui NINGUN operador juridico tiene
# cuerpo. Ver personajes_p3c4.md, seccion 1.
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


def estilo(con_rostro):
    return ('Stylized editorial %sillustration, flat graphic treatment. No ink '
            'outline anywhere: forms are built from broad soft tonal planes, '
            'never from rendered shading, never from texture or brush marks. '
            '%s%s Figures are 8 to 8.5 heads tall. The environment is entirely '
            'in greys. Flat even light, perfectly level camera, no tilt, no '
            'vignette, no lens flare.'
            % ('character ' if con_rostro else '',
               ROSTRO if con_rostro else '', PIEL))


TOKENS = {
 'nora': ('a woman of about forty, medium build, medium height, dark hair tied '
          'back, wearing a plain light grey blouse over plain grey trousers '
          'and grey flat shoes, with a plain institutional yellow band across '
          'the chest of the blouse'),
 'ivan': ('a man of about thirty-five, lean, medium height, short dark hair, '
          'clean shaven, wearing a plain mid-grey collared shirt over plain '
          'grey trousers and grey shoes, with a plain institutional yellow '
          'band running down the front placket of the shirt'),
 'lina': ('a woman of about thirty, slim, medium height, dark hair worn loose '
          'to the shoulders, wearing a plain mid-grey blouse over plain grey '
          'trousers and grey flat shoes, with a plain institutional yellow '
          'belt at the waist, worn over the blouse'),
 'recepcionista': ('a man of about twenty-five, slight build, medium height, '
                   'short dark hair, wearing a plain institutional blue work '
                   'shirt over plain grey trousers and grey shoes'),
}

# El unico acento saturado de cada cuadro se pide como UNICO, que es la
# leccion del Caso 3: grade_placas tiene piso de saturacion 0,45 y `forzar`
# no mueve el tope, asi que una banda generada por debajo no se arregla
# despues.
def unico(cosa='band'):
    return ('THAT %s IS THE ONLY SATURATED COLOUR ANYWHERE IN THE WHOLE IMAGE: '
            'everything else, without exception, is grey.' % cosa.upper())


def arma(escena, con_rostro=False, con_acento=False):
    """con_acento: False, o el nombre de la prenda que lleva el acento."""
    partes = [escena.strip()]
    if con_acento:
        partes.append(unico(con_acento if isinstance(con_acento, str) else 'band'))
    partes += [PLANOS, TONOS, estilo(con_rostro), LIMPIA, SIN_ROLES, NEG]
    return '\n\n'.join(partes)
