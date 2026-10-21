# -*- coding: utf-8 -*-
"""Que palabras se oyen encima de cada ranura. MEDIDO, y ANTES de disenar.

POR QUE ESTO VA PRIMERO Y NO AL FINAL
    En el Caso 3 este cruce se corrio DESPUES de montar y encontro doce
    ranuras mal calzadas, ocho de ellas seguidas y corridas una casilla
    entera. Rehacerlas costo una tanda de placas. Aqui se corre antes de
    pedir una sola imagen: cada plano se disena contra la frase que de verdad
    va a sonar encima de el.

COMO SE ALINEA, SIN ADIVINAR
    El master lo armamos nosotros, asi que la posicion de cada BLOQUE es
    exacta (tramos_p3c4.json). Dentro del bloque hay que repartir el texto
    entre sus silencios medidos, y eso se hace por PROPORCION DE CARACTERES:
    el habla de una misma voz avanza a caracteres por segundo casi constante,
    asi que el reparto por caracteres predice bien donde cae cada frase.

    No se usa el conteo de palabras: las palabras largas y cortas duran
    distinto y el error se acumula a lo largo de un bloque de veinticinco
    segundos.
"""
import json
import os
import re
import sys

sys.path.insert(0, r'/mnt/user-data/uploads/DAE/_repo/herramientas/voz/textos')
sys.path.insert(0, '.')


def texto_limpio(t):
    t = re.sub(r'<break[^>]*/>', ' ', t)
    return re.sub(r'\s+', ' ', t).strip()


def trozos(t):
    """El texto del bloque partido donde el oido puede partirlo: en los
    <break> explicitos y, dentro de ellos, en punto seguido."""
    out = []
    for parte in re.split(r'<break[^>]*/>', t):
        parte = re.sub(r'\s+', ' ', parte).strip()
        if not parte:
            continue
        for fr in re.split(r'(?<=[.:])\s+', parte):
            fr = fr.strip()
            if fr:
                out.append(fr)
    return out


def mapa_tiempo(frases, t0, t1):
    """Cada frase, a su ventana de tiempo, por proporcion de caracteres."""
    tot = sum(len(f) for f in frases) or 1
    out, t = [], t0
    for f in frases:
        d = (t1 - t0) * len(f) / tot
        out.append({'frase': f, 'entra': t, 'sale': t + d})
        t += d
    return out


def main():
    from guion_p3c4 import BLOQUES
    tr = json.load(open('tramos_p3c4.json', encoding='utf-8'))
    rj = json.load(open('ranuras_p3c4.json', encoding='utf-8'))
    FPS = rj['fps']

    porbloque = {n: t for n, v, t in BLOQUES}
    voz = {n: v for n, v, t in BLOQUES}
    linea = []
    for t in tr['tramos']:
        fr = trozos(porbloque[t['bloque']])
        linea += [dict(x, bloque=t['bloque'], voz=voz[t['bloque']])
                  for x in mapa_tiempo(fr, t['entra'], t['sale'])]

    filas = []
    for r in rj['ranuras']:
        a, b = r['ini'] / FPS, r['fin'] / FPS
        dentro = [x for x in linea if x['sale'] > a + 0.15 and x['entra'] < b - 0.15]
        filas.append({'n': r['n'], 'ini': r['ini'], 'dur': r['dur'],
                      'bloque': r['bloque'],
                      'voz': dentro[0]['voz'] if dentro else '?',
                      'texto': ' '.join(x['frase'] for x in dentro)})
    return filas


if __name__ == '__main__':
    filas = main()
    for f in filas:
        print('--- r%02d  %5d  %3d cuadros  %4.1f s  %s (%s)'
              % (f['n'], f['ini'], f['dur'], f['dur'] / (24000 / 1001.0),
                 f['bloque'], f['voz']))
        print('    %s' % f['texto'])
    json.dump(filas, open('cruce_p3c4.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    vacias = [f['n'] for f in filas if not f['texto']]
    print('\nRANURAS SIN FRASE ATRIBUIDA:', vacias or 'ninguna')
