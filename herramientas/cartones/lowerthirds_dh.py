# -*- coding: utf-8 -*-
r"""Lower thirds de Derechos humanos (herramienta de Justicia restaurativa) (en la primera placa con cara).

    python lowerthirds_dh.py [T1 T3 T4]

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

import rutas_dh as R                                     # noqa: E402

N = 120
OFF = 14

# Derechos humanos, 31 oct: los rotulos de nombre se llenan por video con
# el montaje (nombre y dato literales del guion).
# Nombre y, cuando la voz lo dice, el dato literal. Ninguno comparte ranura
# con un carton (medido con Scribe, 31 oct): el juez de la U2 r09 se cae (su
# pregunta es carton y la voz ya lo nombra en b05); la apoderada de la U4 pasa
# a la r32 (la r14 lleva «Peligro para la victima»); Sandra en la U4 se cae
# (la r15 lleva «Obstruccion de la justicia»; tiene rotulo en la U3 y la U5).
# Revision del montaje (31 oct): la abogada Salgado de la U2 r04 quedaba
# debajo del carton «el articulo 17 del Pacto...» (b02 partido en dos): se
# cae; la voz la nombra en b01 y su rotulo va en la U4 r24.
LOWERS = {
    'U1': [('lt01_carmen', 3, {'nombre': 'Carmen Elisa Rojas',
                               'dato': 'Vocera de la mesa de víctimas del municipio.'},
            40),
           # 31 oct, revision: el carton «Y una vecina...» sigue hasta el
           # cuadro 43 de la r08; el rotulo entra 24 despues y dura 96 (no
           # cruza el corte a la r09)
           ('lt02_andres', 8, {'nombre': 'Andrés Peña', 'cuadros': 96}, 67)],
    'U2': [('lt01_julian', 1, {'nombre': 'Julián Mora', 'dato': 'Asistente'}),
           ('lt02_quintero', 2, {'nombre': 'Marina Quintero', 'dato': 'Fiscal'})],
    'U3': [('lt01_sandra', 14, {'nombre': 'Sandra Ibáñez'})],
    # U4, revision: los cartones de la r02 y la r23 siguen encima de la r04 y
    # la r24. Quintero pasa a la r21 (su plano medio), Salgado entra en el
    # cuadro 52 de la r24, y la apoderada se cae: no habla en la U4 y sus dos
    # ranuras (r14, r32) estan cubiertas por cartones.
    'U4': [('lt01_juez', 3, {'nombre': 'Juez de control de garantías'}),
           ('lt02_quintero', 21, {'nombre': 'Marina Quintero', 'dato': 'Fiscal'}),
           ('lt03_salgado', 24, {'nombre': 'Abogada Salgado',
                                 'dato': 'Defensora de Wilmer Acosta.'}, 52)],
    'U5': [('lt01_julian', 1, {'nombre': 'Julián Mora', 'dato': 'Asistente'}),
           # el carton «Hoy vence el termino...» cruza a la r02 hasta su cuadro 49
           ('lt02_sandra', 2, {'nombre': 'Sandra Ibáñez'}, 74),
           ('lt03_quintero', 4, {'nombre': 'Marina Quintero', 'dato': 'Fiscal'})],
}


def archivo(L, nom):
    return os.path.join(R.sub(L, '02 CARTONES'), 'LOWER THIRDS',
                        'DH_%s_%s.mov' % (L, nom))


def lista(L):
    """[(ranura, cuadros, archivo, entra)] para el montaje. `entra` es OFF
    salvo que la entrada de LOWERS traiga un cuarto valor."""
    return [(e[1], e[2].get('cuadros', N), archivo(L, e[0]),
             e[3] if len(e) > 3 else OFF)
            for e in LOWERS.get(L, [])]


if __name__ == '__main__':
    import lower_third as LT
    import dh_pieza as GP
    for L in [a.upper() for a in sys.argv[1:]] or sorted(LOWERS):
        for e in LOWERS[L]:
            nom, r, spec = e[0], e[1], e[2]
            p = archivo(L, nom)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            GP.aparta(p, 'rehecho')
            LT.render(spec, spec.get('cuadros', N), p)
            print('   %s r%02d  entra en el cuadro %d de la ranura  %d cuadros'
                  % (L, r, e[3] if len(e) > 3 else OFF, GP.cuadros(p)), flush=True)
    print('LISTO')
