# -*- coding: utf-8 -*-
r"""Lower thirds de Gerencia judicial (uno por caso, en la r01).

    python lowerthirds_gj.py [T1 T3 T4]

Las reglas de `lowerthirds_sit.py`:

UNO POR PIEZA, EN LA R01
    La r01 es la presentacion -la unica ranura sin carton- y el rotulo nombra
    a quien el espectador acaba de ver entrar. Aqui nadie tiene nombre: el
    documento dice «un fiscal recien nombrado», «usted es fiscal delegado»,
    «usted ejerce funciones de coordinacion». El rotulo dice eso, y el dato
    es un trozo literal de la misma frase.

CADA DATO ES LO QUE LA VOZ DICE, LITERAL
    T1  Fiscal recién nombrado · Despacho con más de 2.000 casos acumulados.
        (los 2.000 van en cifras: es el unico dato numerico del caso)
    T3  Fiscal delegado · Empresa prestadora de servicios públicos.
    T4  Funciones de coordinación · Fiscalía General de la Nación.

TIEMPOS
    120 cuadros, entra 14 cuadros despues de que abre la ranura.
"""
import os
import sys

H = r'D:\DAE\_repo\herramientas'
for sub in ('cartones', 'montaje', 'prompts', os.path.join('voz', 'textos')):
    sys.path.insert(0, os.path.join(H, sub))

import rutas_gj as R                                     # noqa: E402

N = 120
OFF = 14

LOWERS = {
    'T1': [('lt01_fiscal', 1, {
        'nombre': 'Fiscal recién nombrado',
        'dato': 'Despacho con más de 2.000 casos acumulados.'})],
    'T3': [('lt01_fiscal_delegado', 1, {
        'nombre': 'Fiscal delegado',
        'dato': 'Empresa prestadora de servicios públicos.'})],
    'T4': [('lt01_coordinacion', 1, {
        'nombre': 'Funciones de coordinación',
        'dato': 'Fiscalía General de la Nación.'})],
}


def archivo(L, nom):
    return os.path.join(R.sub(L, '02 CARTONES'), 'LOWER THIRDS',
                        'GJ_%s_%s.mov' % (L, nom))


def lista(L):
    """[(ranura, cuadros, archivo)] para el montaje."""
    return [(r, N, archivo(L, nom)) for nom, r, _ in LOWERS.get(L, [])]


if __name__ == '__main__':
    import lower_third as LT
    import gj_pieza as GP
    for L in [a.upper() for a in sys.argv[1:]] or sorted(LOWERS):
        for nom, r, spec in LOWERS[L]:
            p = archivo(L, nom)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            GP.aparta(p, 'rehecho')
            LT.render(spec, N, p)
            print('   %s r%02d  entra en el cuadro %d de la ranura  %d cuadros'
                  % (L, r, OFF, GP.cuadros(p)), flush=True)
    print('LISTO')
