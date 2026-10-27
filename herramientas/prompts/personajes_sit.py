# -*- coding: utf-8 -*-
r"""Hojas de personaje de las situaciones.

POR QUE HOJAS, Y NO SOLO TOKENS
    La biblia lo dejo escrito con el Caso 5: «el texto no alcanza». Una
    persona ya vista se pide pasando su imagen anterior como referencia. En
    las situaciones hay diez personas nuevas que no tienen imagen anterior,
    asi que la primera imagen de cada una NO puede ser una placa cualquiera:
    tiene que ser una hoja hecha para eso -de frente, de tres cuartos, de
    perfil y un primer plano-, que despues entra como referencia en cada
    placa donde aparezca.

    Rosa Elena, Mariana, la fiscal, el perito y el analista ya existen en el
    caso integrador. Su hoja se pide CON su placa del caso integrador como
    referencia, para que la hoja sea esa misma persona y no una prima.

LO QUE LA HOJA NO LLEVA
    Ni rotulos, ni nombres, ni flechas, ni muestras de color, ni cuadricula:
    todo eso el modelo lo dibuja como texto ilegible. La hoja es la persona
    cuatro veces sobre un fondo gris liso, y nada mas.

QUIEN NO TIENE HOJA
    Los servidores sin rostro -comandante, funcionarios, fiscal de turno,
    analista de denuncias, el servidor de la minuta- y los armados en
    silueta. Una hoja de alguien que no lleva cara no tiene nada que fijar.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, r'D:\DAE\_repo\herramientas\prompts')
import base_sit as S                            # noqa: E402

CASO = (r'E:\DAE MASTER\PRIORIDAD 03\CURSO - INVESTIGACION JUDICIAL Y FORENSE '
        r'DE LA DESAPARICION FORZADA\UNIDAD DESAPARICION FORZADA\CASO MIRIAM '
        r'Y MARIANA')
C2 = os.path.join(CASO, r'CAPITULO 2 - RELOJES EN PAUSA Y EL CLAMOR EN LAS REDES\01 PLANOS\_grade')
C4 = os.path.join(CASO, r'CAPITULO 4 - LAS VOCES QUE NO SE APAGAN Y EL DOLOR EN LA VENTANILLA\01 PLANOS\_grade')
C5 = os.path.join(CASO, r'CAPITULO 5 - LA TIERRA HABLA Y LA MATRIZ DEL SILENCIO\01 PLANOS\_grade')

# quien -> (situaciones donde aparece, [referencias del caso integrador])
HOJAS = {
 'carlosalberto': ('A F H I J K', []),
 'rosaelena': ('A F H I', [os.path.join(C4, 'DF_C4_r03_rosaelena_pp.png'),
                           os.path.join(C2, 'DF_C2_r01_rosaelena_patio.png')]),
 'mariana': ('G H', [os.path.join(C2, 'DF_C2_r02_mariana_puerta.png')]),
 'julian': ('B', []),
 'madrejulian': ('B', []),
 'companero': ('B', []),
 'fernando': ('C', []),
 'esposafernando': ('C', []),
 'manuel': ('D', []),
 'familiamanuel': ('D', []),
 'gustavo': ('E', []),
 'fiscal': ('K', [os.path.join(C2, 'DF_C2_r08_la_fiscal_recibe.png')]),
 'investigador': ('K', []),
 'perito': ('K', [os.path.join(C5, 'DF_C5_r08_el_perito.png')]),
 'analista': ('K', [os.path.join(C5, 'DF_C5_r10_el_analista_y_el_tablero.png')]),
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

HOJA_GRUPO = '''
A CHARACTER MODEL SHEET of %(quien)s.

The people stand side by side in a row across a wide frame, on one plain
flat mid-grey background with nothing else in it, each shown full figure
from the front at the same scale, feet on the same invisible ground line,
relaxed, arms at the sides, with calm neutral expressions. Below or beside
each full figure there is NOTHING: no label, no name.

There is no text of any kind: no name, no label, no caption, no number, no
arrow, no colour swatch, no grid, no ruler, no frame or box around anyone.
'''

GRUPO = {'familiamanuel'}

LUZ_HOJA = ('LIGHT: soft even studio light from the upper left, a gentle '
            'shadow side on every figure and a soft contact shadow under the '
            'feet. No glare, no rim light, no bloom.')


def prompt(quien):
    tok = S.CUERPO[quien]
    cuerpo = (HOJA_GRUPO if quien in GRUPO else HOJA) % {'quien': tok}
    p = [cuerpo.strip()]
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
    return 'SIT_HOJA_%s.png' % quien


if __name__ == '__main__':
    import json
    out = {q: {'aparece_en': HOJAS[q][0], 'referencias': HOJAS[q][1],
               'archivo': archivo(q), 'prompt': prompt(q)} for q in HOJAS}
    ruta = r'D:\DAE\_tmp\sit\hojas_sit.json'
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    json.dump(out, open(ruta, 'w', encoding='utf-8'), ensure_ascii=False,
              indent=1)
    for q, v in out.items():
        print('%-15s %-12s refs %d  %5d car' % (q, v['aparece_en'],
                                              len(v['referencias']),
                                              len(v['prompt'])))
