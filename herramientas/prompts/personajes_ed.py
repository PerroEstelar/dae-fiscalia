# -*- coding: utf-8 -*-
r"""Hojas de personaje del curso Enfoque diferencial (es `personajes_lp`).

POR QUE HOJAS (biblia §6: «el texto no alcanza»)
    Una persona que aparece en mas de un plano se pide pasando su hoja
    -de frente, de tres cuartos, de perfil y un primer plano- como
    referencia en cada placa donde aparezca, y desde la segunda placa de la
    misma escena, ademas, la placa aprobada (REF_PLACA). Sebastian, 31 oct:
    «crea personajes consistentes, no tengas miedo de reusarlos en
    diferentes planos, mas cerca o lejos, diferentes angulos».

QUIEN TIENE HOJA
    Los ocho que vuelven en tres o mas planos y llevan cara: Molano y
    Yolanda (C1), Jairo y Mauricio (C2), Wilmer (C3), la madre y el fiscal
    (C4), Valentina (C5). Los demas con cara (la defensora, el juez, la
    psicologa, la madre de Yolanda, la activista, el companero, la azafata,
    los cabildantes) se fijan con su primera placa aprobada como referencia.

QUIEN NO
    Los que van sin cara (el vecino, el coronel, los agresores, el Taita,
    el funcionario de C5, los fiscales que deciden mal). Una hoja de alguien
    sin cara no fija nada.

LO QUE LA HOJA NO LLEVA
    Ni rotulos, ni nombres, ni flechas, ni muestras de color, ni cuadricula:
    todo eso el modelo lo dibuja como texto ilegible.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, r'D:\DAE\_repo\herramientas\prompts')
import base_ed as S                             # noqa: E402

# quien -> piezas donde aparece (solo quien vuelve en tres o mas planos)
HOJAS = {
 'molano': 'C1', 'yolanda': 'C1',
 'jairo': 'C2', 'mauricio': 'C2',
 'wilmer': 'C3',
 'madre': 'C4', 'fiscal_c4': 'C4',
 'nina': 'C4',          # 4 nov: Yaneth, por pedido de Sebastian
 'valentina': 'C5',
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

# El objeto de cada uno va en la hoja, para que vuelva igual en cada placa.
EXTRA = {
 'molano': ('In the three full figures he holds a thick plain case file under '
            'one arm and his reading glasses in the other hand.'),
 'yolanda': ('In the three full figures her hands rest one over the other in '
             'front of her; the cardigan hangs open and straight on both sides.'),
 'jairo': ('In the three full figures he carries a plain book with a blank '
           'cover under one arm.'),
 'mauricio': ('In the three full figures he holds a small plain bunch of keys '
              'in one hand.'),
 # 4 nov: el uniforme de la Policia Nacional (base_ed.UNIFORME_POLICIA)
 'wilmer': ('In the three full figures his hands hang relaxed and open at his '
            'sides and he wears the cap; the vest is lime yellow-green with '
            'only its two silver-grey reflective bands, and the shirt, the '
            'trousers and the cap are plain dark olive-green cloth with nothing '
            'on the chest, the sleeves or the shoulders.'),
 'madre': ('In the three full figures she holds a small plain child\'s school '
           'backpack by its strap.'),
 'fiscal_c4': ('In the three full figures he holds a plain manila case folder.'),
 'nina': ('In the three full figures she wears the small plain grey school '
          'backpack on both shoulders and her hands hang relaxed at her sides; '
          'she stands like an ordinary schoolchild. The close-up shows her '
          'calm, serious face.'),
 'valentina': ('In the three full figures she holds a plain identity card in one '
               'hand; the coat hangs open and straight on both sides.'),
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
    if quien in S.PATRULLEROS:
        p.append(S.UNIFORME_POLICIA)
    p.append(LUZ_HOJA)
    # 3 nov (ED): las clausulas cortas de la serie (base_ed.C_*), como las placas
    p.append(S.C_ESTILO + S.C_ROSTRO + S.C_PIEL
             + (S.C_FIGURA_NINA if quien == 'nina' else S.C_FIGURA))
    if quien == 'nina':
        p.append(S.C_NINA)
    if quien in S.CON_ACENTO:
        p.append(S.C_ACENTO % S.PRENDA[quien])
    p.append(S.C_LIMPIA)
    p.append(S.C_NEG)
    return '\n\n'.join(' '.join(x.split()) for x in p if x and x.strip())


def archivo(quien):
    return 'ED_HOJA_%s.png' % quien


if __name__ == '__main__':
    import json
    out = {q: {'aparece_en': HOJAS[q], 'archivo': archivo(q),
               'prompt': prompt(q)} for q in HOJAS}
    ruta = r'D:\DAE\_tmp\ed\hojas_ed.json'
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    json.dump(out, open(ruta, 'w', encoding='utf-8'), ensure_ascii=False,
              indent=1)
    for q, v in out.items():
        print('%-14s %-4s %5d car' % (q, v['aparece_en'], len(v['prompt'])))
