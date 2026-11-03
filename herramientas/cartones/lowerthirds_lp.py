# -*- coding: utf-8 -*-
r"""Lower thirds de Derechos humanos (herramienta de Justicia restaurativa) (en la primera placa con cara).

    python lowerthirds_lp.py [T1 T3 T4]

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

import rutas_lp as R                                     # noqa: E402

N = 120
OFF = 14

# Ley 1826 (3 nov): solo llevan rotulo las personas que el texto NOMBRA y que
# se ven con cara: el supervisor de la U2 C1 (en la r05, su primer plano; la
# r01 lleva el carton de fecha y lugar) y Maria Elena en la U2 C2 (r02). Los
# procesados no llevan rotulo (de espaldas o en silueta) y en la U4 nadie
# tiene nombre.
LOWERS = {
    'U2C1': [('lt01_supervisor', 5, {'nombre': 'Jorge Eliécer Benavides',
                                     'dato': 'Supervisor de zona'})],
    'U2C2': [('lt01_mariaelena', 2, {'nombre': 'María Elena Gutiérrez Ríos'})],
}


def archivo(L, nom):
    return os.path.join(R.sub(L, '02 CARTONES'), 'LOWER THIRDS',
                        'LP_%s_%s.mov' % (L, nom))


def lista(L):
    """[(ranura, cuadros, archivo, entra)] para el montaje. `entra` es OFF
    salvo que la entrada de LOWERS traiga un cuarto valor."""
    return [(e[1], e[2].get('cuadros', N), archivo(L, e[0]),
             e[3] if len(e) > 3 else OFF)
            for e in LOWERS.get(L, [])]


if __name__ == '__main__':
    import lower_third as LT
    import lp_pieza as GP
    # `U2:lt03_carmen` rinde solo ese (los que ya estan en una linea tocada
    # no se reescriben)
    pedidos = [a for a in sys.argv[1:]]
    solo = {tuple(a.split(':', 1)) for a in pedidos if ':' in a}
    temas = sorted({a.split(':')[0].upper() for a in pedidos}) or sorted(LOWERS)
    for L in temas:
        for e in LOWERS[L]:
            nom, r, spec = e[0], e[1], e[2]
            if solo and (L, nom) not in {(x.upper(), y) for x, y in solo}:
                continue
            p = archivo(L, nom)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            GP.aparta(p, 'rehecho')
            LT.render(spec, spec.get('cuadros', N), p)
            print('   %s r%02d  entra en el cuadro %d de la ranura  %d cuadros'
                  % (L, r, e[3] if len(e) > 3 else OFF, GP.cuadros(p)), flush=True)
    print('LISTO')
