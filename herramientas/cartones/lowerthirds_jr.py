# -*- coding: utf-8 -*-
r"""Lower thirds de Justicia restaurativa (en la primera placa con cara).

    python lowerthirds_jr.py [T1 T3 T4]

Las reglas de `lowerthirds_sit.py`:

UNO POR PIEZA, EN LA R01
    La r01 es la presentacion -la unica ranura sin carton- y el rotulo nombra
    a quien el espectador acaba de ver entrar. Aqui nadie tiene nombre: el
    documento dice «un fiscal recien nombrado», «usted es fiscal delegado»,
    «usted ejerce funciones de coordinacion». El rotulo dice eso, y el dato
    es un trozo literal de la misma frase.

CADA DATO ES LO QUE LA VOZ DICE, LITERAL (Justicia restaurativa, 30 oct)
    C1  Ana Pérez · «El 01 de enero de 2025, en un sitio público» (r01, que
        por eso va sin cartón)
    U2-U4  Juana (r01): «prima de Alberto, víctima de tortura»
    Sin rotulo el C2 y la U1: la primera hoja de contacto los ponia encima
    de un carton (el perfil de la victima ya dice el nombre de Camilo; la
    voz y los cartones nombran a Diego y a Mario). Rotulo y carton no
    conviven en la misma ranura.

TIEMPOS
    120 cuadros, entra 14 cuadros despues de que abre la ranura.
"""
import os
import sys

H = r'D:\DAE\_repo\herramientas'
for sub in ('cartones', 'montaje', 'prompts', os.path.join('voz', 'textos')):
    sys.path.insert(0, os.path.join(H, sub))

import rutas_jr as R                                     # noqa: E402

N = 120
OFF = 14

LOWERS = {
    'C1': [('lt01_ana', 1, {
        'nombre': 'Ana Pérez',
        'dato': 'El 01 de enero de 2025, en un sitio público.'})],
    # 31 oct, Sebastian: Camilo si lleva rotulo, en la r04, sobre el primer
    # plano que la cierra (COMPUESTAS): entra en el cuadro 96 de la ranura,
    # cuando ya salio el carton p01, no en el 14 (rotulo y carton no
    # conviven). El dato es literal de la voz (n07).
    'C2': [('lt01_camilo', 4, {
        'nombre': 'Camilo Andrés Ferreira Buitrago',
        'dato': '27 años, trabajador independiente.'}, 96)],
    'U2': [('lt01_juana', 1, {
        'nombre': 'Juana',
        'dato': 'Prima de Alberto, víctima de tortura.'})],
    'U3': [('lt01_juana', 1, {
        'nombre': 'Juana',
        'dato': 'Prima de Alberto, víctima de tortura.'})],
    'U4': [('lt01_juana', 1, {
        'nombre': 'Juana',
        'dato': 'Prima de Alberto, víctima de tortura.'})],
}


def archivo(L, nom):
    return os.path.join(R.sub(L, '02 CARTONES'), 'LOWER THIRDS',
                        'JR_%s_%s.mov' % (L, nom))


def lista(L):
    """[(ranura, cuadros, archivo, entra)] para el montaje. `entra` es OFF
    salvo que la entrada de LOWERS traiga un cuarto valor."""
    return [(e[1], N, archivo(L, e[0]), e[3] if len(e) > 3 else OFF)
            for e in LOWERS.get(L, [])]


if __name__ == '__main__':
    import lower_third as LT
    import jr_pieza as GP
    for L in [a.upper() for a in sys.argv[1:]] or sorted(LOWERS):
        for e in LOWERS[L]:
            nom, r, spec = e[0], e[1], e[2]
            p = archivo(L, nom)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            GP.aparta(p, 'rehecho')
            LT.render(spec, N, p)
            print('   %s r%02d  entra en el cuadro %d de la ranura  %d cuadros'
                  % (L, r, e[3] if len(e) > 3 else OFF, GP.cuadros(p)), flush=True)
    print('LISTO')
