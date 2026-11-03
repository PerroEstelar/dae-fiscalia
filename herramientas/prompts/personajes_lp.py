# -*- coding: utf-8 -*-
r"""Hojas de personaje del curso Ley 1826 (es `personajes_dh`).

POR QUE HOJAS (biblia §6: «el texto no alcanza»)
    Una persona que aparece en mas de un plano se pide pasando su hoja
    -de frente, de tres cuartos, de perfil y un primer plano- como
    referencia en cada placa donde aparezca, y desde la segunda placa de la
    misma escena, ademas, la placa aprobada (REF_PLACA). Sebastian, 31 oct:
    «crea personajes consistentes, no tengas miedo de reusarlos en
    diferentes planos, mas cerca o lejos, diferentes angulos».

QUIEN TIENE HOJA
    Los nueve con cara: Carmen Elisa, Andres, el Entrevistador 1, Sandra,
    Quintero, Julian, la abogada Salgado, el juez y la apoderada.

QUIEN NO
    Wilmer Acosta (de espaldas siempre), los presos del epilogo, los vecinos
    y los colegas del fondo. Una hoja de alguien sin cara no fija nada.

LO QUE LA HOJA NO LLEVA
    Ni rotulos, ni nombres, ni flechas, ni muestras de color, ni cuadricula:
    todo eso el modelo lo dibuja como texto ilegible.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, r'D:\DAE\_repo\herramientas\prompts')
import base_lp as S                             # noqa: E402

# quien -> piezas donde aparece (solo quien vuelve en tres o mas planos)
HOJAS = {
 'maria': 'U1',
 'supervisor': 'U2C1',
 'mariaelena': 'U2C2',
 'fiscal_mujer': 'U2C2',
 'mediador': 'U4C2',
 'ciudadana': 'U4C3',
 'estudiante': 'U4C3',
 'defensor': 'U4C1',
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
 'maria': ('In the three full figures her hands rest one over the other in front '
           'of her; the scarf hangs straight down the front on both sides.'),
 'supervisor': ('In the three full figures he holds his mobile phone flat in one '
                'hand.'),
 'mariaelena': ('In the three full figures she holds a plain dark handbag against '
                'her side; the cardigan hangs open and straight on both sides.'),
 'fiscal_mujer': ('In the three full figures she holds a thick plain case file '
                  'against her side.'),
 'mediador': ('In the three full figures he holds a plain grey notepad.'),
 'ciudadana': ('In the three full figures her hands are clasped in front of her; '
               'the cardigan hangs open and straight on both sides.'),
 'estudiante': ('In the three full figures he holds a plain grey folder against '
                'his chest.'),
 'defensor': ('In the three full figures he holds a slim black folder flat '
              'against his side.'),
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
    return 'LP_HOJA_%s.png' % quien


if __name__ == '__main__':
    import json
    out = {q: {'aparece_en': HOJAS[q], 'archivo': archivo(q),
               'prompt': prompt(q)} for q in HOJAS}
    ruta = r'D:\DAE\_tmp\lp\hojas_lp.json'
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    json.dump(out, open(ruta, 'w', encoding='utf-8'), ensure_ascii=False,
              indent=1)
    for q, v in out.items():
        print('%-14s %-4s %5d car' % (q, v['aparece_en'], len(v['prompt'])))
