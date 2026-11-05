# -*- coding: utf-8 -*-
r"""Hojas de personaje del curso Estándares interamericanos (es `personajes_ed`).

QUIEN TIENE HOJA (vuelve en tres o más planos y lleva cara)
    S01  el líder, su esposa, la hija, el hijo, la abogada
    S04  el servidor
    S06  el fiscal, la madre
    S07  el analista, el fiscal
    S08  la hermana, la madre, el fiscal
    Los demás con cara (la fiscal de S01, el testigo, la médica, la
    antropóloga, la investigadora) se fijan con su primera placa aprobada.

QUIEN NO: los que van sin cara (la amenaza, los patrulleros, la fuente, los
    forenses, la funcionaria de S01).

LA CUENTA NUEVA (5 nov): las hojas de los cursos anteriores viven en la cuenta
    vieja de Magnific y aquí no existen. Cada hoja nueva se pide con UNA hoja
    aprobada de Enfoque diferencial como referencia de FORMATO y DIBUJO
    (ESTILO_HOJA), nunca de persona: así la serie no se mueve de cuenta a
    cuenta.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, r'D:\DAE\_repo\herramientas\prompts')
import base_ei as S                             # noqa: E402
from personajes_ed import HOJA, LUZ_HOJA        # noqa: E402

HOJAS = {
 'lider': 'S01', 'esposa': 'S01', 'hija': 'S01', 'hijo': 'S01', 'abogada': 'S01',
 'servidor': 'S04',
 'fiscal_s06': 'S06', 'madre_s06': 'S06',
 'analista': 'S07', 'fiscal_s07': 'S07',
 'hermana': 'S08', 'madre_s08': 'S08', 'fiscal_s08': 'S08',
}

EXTRA = {
 'lider': ('In the three full figures he holds a plain straw hat in one hand at '
           'his side; the mustard ruana hangs straight from his shoulders, front '
           'and back.'),
 'esposa': ('In the three full figures she holds a thick plain clear plastic '
            'document folder against her chest with both hands.'),
 'hija': ('In the three full figures her hands rest one over the other in '
          'front of her.'),
 'hijo': ('In the three full figures his hands hang relaxed at his sides.'),
 'abogada': ('In the three full figures she holds a plain closed notebook and a '
             'plain pen.'),
 'servidor': ('In the three full figures he holds a thick plain bound book with '
              'a blank cover under one arm and a plain pencil in the other hand.'),
 'fiscal_s06': ('In the three full figures he holds a plain manila case folder '
                'and his reading glasses folded in one hand.'),
 'madre_s06': ('In the three full figures she holds a plain clear plastic '
               'sleeve with a single sheet inside, the sheet only plain grey '
               'bars.'),
 'analista': ('In the three full figures he holds a plain mobile phone, screen '
              'dark, in one hand.'),
 'fiscal_s07': ('In the three full figures he holds a plain manila case folder '
                'under one arm.'),
 'hermana': ('In the three full figures she holds a plain mobile phone, screen '
             'dark, in one hand.'),
 'madre_s08': ('In the three full figures her hands are clasped in front of her.'),
 'fiscal_s08': ('In the three full figures he holds a plain manila case folder.'),
}

ESTILO_HOJA = ('The reference image is a finished character model sheet from '
               'this same series, of ANOTHER person: use it ONLY for the format '
               '(four views on a plain mid-grey background), the drawing, the '
               'treatment and the grey of the skin. Never copy that person\'s '
               'face, hair, body or clothes: the person here is the one '
               'described above.')


def prompt(quien):
    tok = S.CUERPO[quien]
    p = [(HOJA % {'quien': tok}).strip()]
    if quien in EXTRA:
        p.append(EXTRA[quien])
    if quien in S.VIDA:
        p.append('WHO THIS IS. ' + S.VIDA[quien])
    p.append(LUZ_HOJA)
    p.append(S.C_ESTILO + S.C_ROSTRO + S.C_PIEL + S.C_FIGURA)
    if quien in S.CON_ACENTO:
        p.append(S.C_ACENTO % S.PRENDA[quien])
    p.append(S.C_LIMPIA)
    p.append(S.C_NEG)
    p.append(ESTILO_HOJA)
    return '\n\n'.join(' '.join(x.split()) for x in p if x and x.strip())


def archivo(quien):
    return 'EI_HOJA_%s.png' % quien


if __name__ == '__main__':
    import json
    out = {q: {'aparece_en': HOJAS[q], 'archivo': archivo(q),
               'prompt': prompt(q)} for q in HOJAS}
    ruta = sys.argv[1] if len(sys.argv) > 1 else r'D:\DAE\_tmp\ei\hojas_ei.json'
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    json.dump(out, open(ruta, 'w', encoding='utf-8'), ensure_ascii=False,
              indent=1)
    for q, v in out.items():
        print('%-14s %-4s %5d car' % (q, v['aparece_en'], len(v['prompt'])))
