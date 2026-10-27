# -*- coding: utf-8 -*-
r"""Lower thirds de las situaciones en video (A, B, C, D, E y G).

    python lowerthirds_sit.py [A B ...]

Las mismas reglas de `lowerthirds_df.py` (el caso integrador):

UNO POR PIEZA, Y SE LO GANA
    El rotulo nombra a quien el espectador acaba de ver entrar y que la voz ya
    establecio. En las seis situaciones esa persona es la de la r01, la unica
    ranura de cada pieza sin carton encima (medido contra cartones_sit: en
    las seis la r01 esta limpia). El carton gana siempre: no hay un segundo
    rotulo porque todas las demas apariciones caen bajo carton.

CADA DATO ES LO QUE LA VOZ DICE, LITERAL
    Nombre, edad y oficio, del primer bloque de cada guion verbatim. Nunca
    lo que el ejercicio pone a examinar. Cada situacion se ve sola, asi que
    cada una presenta a su persona.

TIEMPOS
    120 cuadros (5 s: nombre y dato), entra 14 cuadros despues de que abre la
    ranura. Numeros en cifras.
"""
import os
import sys

H = r'D:\DAE\_repo\herramientas'
for sub in ('cartones', 'montaje', 'prompts', os.path.join('voz', 'textos')):
    sys.path.insert(0, os.path.join(H, sub))

import rutas_sit as R                                    # noqa: E402

N = 120
OFF = 14

LOWERS = {
    'A': [('lt01_carlosalberto', 1, {
        'nombre': 'Carlos Alberto Morales',
        'dato': '34 años. Transportador rural y líder comunal.'})],
    'B': [('lt01_julian', 1, {
        'nombre': 'Julián David Morales',
        'dato': '22 años. Técnico en mantenimiento de vehículos.'})],
    'C': [('lt01_fernando', 1, {
        'nombre': 'Fernando Ruiz',
        'dato': '45 años. Comerciante de insumos agrícolas.'})],
    'D': [('lt01_manuelantonio', 1, {
        'nombre': 'Manuel Antonio Gómez',
        'dato': '58 años. Agricultor de la vereda La Esperanza.'})],
    'E': [('lt01_gustavoadolfo', 1, {
        'nombre': 'Gustavo Adolfo Ramírez',
        'dato': '38 años. Comerciante de ganado.'})],
    'G': [('lt01_mariana', 1, {
        'nombre': 'Mariana Morales',
        'dato': '16 años. Vocera del colectivo de víctimas.'})],
}


def archivo(L, nom):
    return os.path.join(R.sub(L, '02 CARTONES'), 'LOWER THIRDS', 'SIT_%s_%s.mov' % (L, nom))


def lista(L):
    """[(ranura, cuadros, archivo)] para el montaje."""
    return [(r, N, archivo(L, nom)) for nom, r, _ in LOWERS.get(L, [])]


if __name__ == '__main__':
    import lower_third as LT
    import sit_pieza as SP
    for L in [a.upper() for a in sys.argv[1:]] or sorted(LOWERS):
        for nom, r, spec in LOWERS[L]:
            p = archivo(L, nom)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            SP.aparta(p, 'rehecho')
            LT.render(spec, N, p)
            print('   %s r%02d  entra en el cuadro %d de la ranura  %d cuadros'
                  % (L, r, OFF, SP.cuadros(p)), flush=True)
    print('LISTO')
