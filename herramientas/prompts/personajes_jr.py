# -*- coding: utf-8 -*-
r"""Hojas de personaje de Justicia restaurativa.

POR QUE HOJAS
    La biblia lo dejo escrito con el Caso 5: «el texto no alcanza». Una
    persona que aparece en mas de un plano se pide pasando una imagen suya
    como referencia, y la primera imagen de cada una tiene que ser una hoja
    hecha para eso -de frente, de tres cuartos, de perfil y un primer
    plano-, que despues entra como referencia en cada placa donde aparezca.

QUIEN TIENE HOJA
    Las seis personas con cara que vuelven en varios planos: Ana y la fiscal
    local (C1), Camilo (C2), Diego y Mario (U1) y Juana (U2-U4).

QUIEN NO
    Los que no llevan cara (Juan y su defensor, el legista, los procesados,
    la amiga, el fiscal «usted») y las figuras de lo recordado. Una hoja de
    alguien sin cara no tiene nada que fijar.

LO QUE LA HOJA NO LLEVA
    Ni rotulos, ni nombres, ni flechas, ni muestras de color, ni cuadricula:
    todo eso el modelo lo dibuja como texto ilegible.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, r'D:\DAE\_repo\herramientas\prompts')
import base_jr as S                             # noqa: E402

# quien -> temas donde aparece
HOJAS = {
 'ana': 'C1',
 'fiscal1': 'C1',
 'camilo': 'C2',
 'diego': 'U1',
 'mario': 'U1',
 'juana': 'U2',
}

HOJA = '''
A CHARACTER MODEL SHEET of %(quien)s.

The SAME person is shown FOUR TIMES side by side across a wide frame, all on
one plain flat mid-grey background with nothing else in it: from left to
right, (1) the full figure from the front, (2) the full figure in
three-quarter view, (3) the full figure in profile, and (4) a
head-and-shoulders close-up in three-quarter view. The three full figures
stand at exactly the same scale, feet on the same invisible ground line,
relaxed, arms at the sides, with a calm neutral expression. The close-up
shows the face clearly.

It is ONE person: the same face, the same build, the same hair and the same
clothes in all four. Nothing is added or removed between views.

There is no text of any kind: no name, no label, no caption, no number, no
arrow, no colour swatch, no grid, no ruler, no frame or box around any view.
'''

# Camilo lleva el brazo vendado en la hoja, para que la venda vuelva igual
# en cada placa. Juana lleva el bolso colgado de una mano.
EXTRA = {
 'camilo': ('In the three full figures his right forearm carries the plain '
            'light grey bandage, the arm held a little closer to the body '
            'than the other.'),
 'juana': ('In the three full figures she holds the plain grey handbag by '
           'its short handles in one hand, hanging at her side.'),
}

LUZ_HOJA = ('LIGHT: soft even studio light from the upper left, a gentle '
            'shadow side on every figure and a soft contact shadow under the '
            'feet. No glare, no rim light, no bloom.')


def prompt(quien):
    tok = S.CUERPO[quien]
    p = [(HOJA % {'quien': tok}).strip()]
    if quien in EXTRA:
        p.append(EXTRA[quien])
    if quien in S.VIDA:
        p.append('WHO THIS IS. ' + S.VIDA[quien])
    p.append(LUZ_HOJA)
    p.append(S.PLANOS)
    p.append(S.ESTILO + S.ROSTRO + S.PIEL + ' ' + S.FIGURA)
    p.append(S.CAMARA)
    if quien in S.CON_ACENTO:
        p.append(S.ACENTO)
    p.append(S.LIMPIA)
    p.append(S.SIN_ROLES)
    p.append(S.NEG)
    return '\n\n'.join(x.strip() for x in p if x and x.strip())


def archivo(quien):
    return 'JR_HOJA_%s.png' % quien


if __name__ == '__main__':
    import json
    out = {q: {'aparece_en': HOJAS[q], 'archivo': archivo(q),
               'prompt': prompt(q)} for q in HOJAS}
    ruta = r'D:\DAE\_tmp\jr\hojas_jr.json'
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    json.dump(out, open(ruta, 'w', encoding='utf-8'), ensure_ascii=False,
              indent=1)
    for q, v in out.items():
        print('%-14s %-4s %5d car' % (q, v['aparece_en'], len(v['prompt'])))
