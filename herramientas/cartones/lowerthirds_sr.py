# -*- coding: utf-8 -*-
r"""Lower thirds de los CASOS del curso SRPA y justicia restaurativa
(herramienta de EI / Justicia restaurativa).

    python lowerthirds_sr.py [NICO]

LAS REGLAS DE LA SERIE
    Rótulo solo para quien el texto NOMBRA y se ve con cara, en su primera
    placa, y nunca encima de un cartón. El dato es literal de la voz.
    Un rótulo con un oficio y sin nombre («Defensor público») no presenta a
    nadie y le quita tiempo al cartón (EI, 5 nov): el defensor, los
    comerciantes, los patrulleros y la enfermera van sin rótulo.

CASO NICO (12 nov)
    Nico, en la r02 (la primera placa con su cara). El dato es el de la voz:
    «vivía un adolescente de aproximadamente 15 años» (con la mayúscula
    inicial, el único arreglo permitido). Entra cuando la voz dice «como
    "Nico"» (Scribe), no al abrir la ranura, y dura 120 cuadros.
"""
import os
import sys

H = r'D:\DAE\_repo\herramientas'
for sub in ('cartones', 'montaje', 'prompts', os.path.join('voz', 'textos')):
    sys.path.insert(0, os.path.join(H, sub))

import rutas_sr as R                                     # noqa: E402

N = 120
OFF = 14
CABEZA = 182 + 119

# (nombre de archivo, ranura, spec, (bloque, trozo que se oye al entrar))
LOWERS = {
    'NICO': [('lt01_nico', 2, {
        'nombre': 'Nico',
        'dato': 'Un adolescente de aproximadamente 15 años'},
        ('n01_nico', 'como «Nico».'))],
}


def archivo(L, nom):
    return os.path.join(R.sub(L, '02 CARTONES'), 'LOWER THIRDS',
                        'SR_%s_%s.mov' % (L, nom))


def _pos(L):
    """Cuadro de la linea en que abre cada ranura."""
    E = __import__('escenas_sr_%s' % L.lower())
    pos, t = {}, CABEZA
    for n in sorted(E.R):
        pos[n] = t
        t += E.R[n][0]
    return pos


def _entra(L, e):
    """Cuadro de la linea en que entra el rotulo: la palabra de Scribe, o
    OFF cuadros despues de abrir la ranura."""
    pos = _pos(L)
    if len(e) > 3 and e[3]:
        import cartones_sr as CS
        from guion_sr import bloques
        bl, trozo = e[3]
        tx = {b[0]: ' '.join(b[2].split()) for b in bloques(L)}[bl]
        a, _ = CS.entra(L, bl, tx, trozo)
        return a
    return pos[e[1]] + OFF


def en_linea(L):
    """[(cuadro de la linea, cuadros, archivo)]."""
    return [(_entra(L, e), e[2].get('cuadros', N), archivo(L, e[0]))
            for e in LOWERS.get(L, [])]


def lista(L):
    """[(ranura, cuadros, archivo, entra)] para `sr_pieza.capas`: `entra` es
    relativo a la apertura de la ranura."""
    pos = _pos(L)
    return [(e[1], e[2].get('cuadros', N), archivo(L, e[0]), _entra(L, e) - pos[e[1]])
            for e in LOWERS.get(L, [])]


if __name__ == '__main__':
    import lower_third as LT
    import sr_pieza as GP
    temas = [a.upper() for a in sys.argv[1:]] or sorted(LOWERS)
    for L in temas:
        for e, (r, n, p, off) in zip(LOWERS[L], lista(L)):
            os.makedirs(os.path.dirname(p), exist_ok=True)
            GP.aparta(p, 'rehecho')
            LT.render(e[2], n, p)
            print('   %s r%02d  entra en el cuadro %d de la ranura (%d de la linea)  %d cuadros'
                  % (L, r, off, _pos(L)[r] + off, GP.cuadros(p)), flush=True)
    print('LISTO')
