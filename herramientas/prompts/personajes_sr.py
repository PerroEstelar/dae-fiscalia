# -*- coding: utf-8 -*-
r"""Hojas de personaje de los casos del curso SRPA (PRIORIDAD 1) (es
`personajes_ei`).

QUIEN TIENE HOJA (vuelve en tres o más planos y lleva cara)
    NICO  el chico (y su versión rapada, pedida con la hoja como referencia
          'mismo': solo cambia el pelo), el defensor público, la vendedora
          de la plaza, la enfermera del CAE.
QUIEN NO: los comerciantes (silueta), los funcionarios del CAE (de espaldas),
    los patrulleros (se fijan con su primera placa aprobada), la familia del
    cliente (ídem).
Formato y dibujo: una hoja aprobada de la serie en la cuenta nueva
(EI_ESTILO_HOJA_*), nunca su persona.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, r'D:\DAE\_repo\herramientas\prompts')
import base_sr as S                             # noqa: E402
from personajes_ed import HOJA, LUZ_HOJA        # noqa: E402
from personajes_ei import ESTILO_HOJA           # noqa: E402

HOJAS = {'nico': 'NICO', 'defensor': 'NICO', 'vendedora': 'NICO', 'enfermera': 'NICO'}
ESTILO = {'nico': 'EI_ESTILO_HOJA_hombre', 'defensor': 'EI_ESTILO_HOJA_hombre',
          'vendedora': 'EI_ESTILO_HOJA_mujer', 'enfermera': 'EI_ESTILO_HOJA_mujer'}

EXTRA = {
 'nico': ('In the three full figures his hands are pushed into the front pouch '
          'of the sweatshirt; a knotted plain plastic bag hangs from one wrist. '
          'He is a boy of fifteen: clearly younger, shorter and slighter than a '
          'grown man, about seven and a half heads tall.'),
 'defensor': ('In the three full figures he holds a thin plain cardboard folder '
              'under one arm and his reading glasses in the other hand.'),
 'vendedora': ('In the three full figures she holds a long ladle in one hand and '
               'a folded plain cloth in the other.'),
 'enfermera': ('In the three full figures she holds a plain clipboard against '
               'her chest with both gloved hands.'),
}

RAPADO = ('The reference image is the approved character sheet of THIS SAME boy. '
          'Keep EVERYTHING exactly as it is -the same face, the same body, the '
          'same clothes, the same four views, the same format and drawing-; '
          'ONLY ONE THING CHANGES: his hair has been shaved off completely, his '
          'head is shaved to the scalp, a very short even dark grey stubble all '
          'over, in all four views.')


def prompt(quien):
    tok = S.CUERPO[quien]
    p = [(HOJA % {'quien': tok}).strip()]
    if quien in EXTRA:
        p.append(EXTRA[quien])
    if quien in S.VIDA:
        p.append('WHO THIS IS. ' + S.VIDA[quien])
    p.append(LUZ_HOJA)
    p.append(S.C_ESTILO + S.C_ROSTRO + S.C_PIEL + S.C_FIGURA)
    if quien == 'nico':
        p.append(S.C_NICO)
    if quien in S.CON_ACENTO:
        p.append(S.C_ACENTO % S.PRENDA[quien])
    else:
        p.append(S.C_SIN_ACENTO)
    p.append(S.C_LIMPIA)
    p.append(S.C_NEG)
    p.append(ESTILO_HOJA)
    return '\n\n'.join(' '.join(x.split()) for x in p if x and x.strip())


def archivo(quien):
    return 'SR_HOJA_%s.png' % quien


if __name__ == '__main__':
    out = {q: {'aparece_en': HOJAS[q], 'archivo': archivo(q), 'estilo': ESTILO[q],
               'prompt': prompt(q)} for q in HOJAS}
    ruta = sys.argv[1] if len(sys.argv) > 1 else r'D:\DAE\_tmp\sr\hojas_sr.json'
    json.dump(out, open(ruta, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
