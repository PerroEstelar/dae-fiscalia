#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Cruza cada ranura del P3C5 con la FRASE que se oye encima de ella.

POR QUE ESTO EXISTE
    Es la leccion mas cara del Caso 3. Alli la rejilla se armo leyendo los
    NOMBRES de los archivos en vez de abrir las imagenes, y doce ranuras
    quedaron mal calzadas -ocho seguidas en la cola, corridas una casilla
    entera-. Hubo que remontar la pieza completa.

    Saber que BLOQUE se oye encima de una ranura no alcanza: un bloque dura
    veinte segundos y lleva tres frases distintas. Lo que hay que saber para
    disenar la escena es QUE FRASE, y eso se mide.

COMO SE MIDE
    Dentro de una misma locucion el tiempo hablado es proporcional a los
    CARACTERES -medido en las ocho piezas de la serie: 1,2 a 1,4 cuadros por
    caracter, y constante dentro de un mismo bloque-. Asi que se reparte la
    duracion medida de cada bloque entre sus frases segun su largo en
    caracteres, y de ahi sale donde empieza y termina cada frase.

    No se usa `silencedetect` para esto: el locutor no hace una pausa en cada
    frase, y una frase puede partirse en dos tramos.
"""
import json
import os
import re
import sys

FPS = 24000 / 1001.0


def frases(texto):
    """Parte un bloque en frases, quitando las marcas de respiro."""
    t = re.sub(r'<break[^>]*/>', ' ', texto)
    t = re.sub(r'\s+', ' ', t).strip()
    partes = re.split(r'(?<=[.:])\s+', t)
    return [p.strip() for p in partes if p.strip()]


def main(rejilla_json, tramos_json, guion_mod, salida):
    sys.path.insert(0, os.path.dirname(guion_mod))
    G = __import__(os.path.basename(guion_mod).replace('.py', ''))
    texto = {n: t for n, _, t in G.BLOQUES}

    rej = json.load(open(rejilla_json, encoding='utf-8'))
    tr = {t['bloque']: t for t in json.load(open(tramos_json, encoding='utf-8'))['tramos']}

    # cada frase, con su ventana de cuadros dentro del master
    ventanas = []
    for nom, t in tr.items():
        fs = frases(texto[nom])
        n = sum(len(f) for f in fs)
        a = t['entra'] * FPS
        for f in fs:
            d = (t['dur'] * FPS) * len(f) / n
            ventanas.append({'bloque': nom, 'frase': f,
                             'ini': int(round(a)), 'fin': int(round(a + d))})
            a += d
    ventanas.sort(key=lambda v: v['ini'])

    filas = []
    for i, r in enumerate(rej['ranuras'], 1):
        a, b = r['ini'], r['ini'] + r['dur']
        encima = []
        for v in ventanas:
            sol = min(b, v['fin']) - max(a, v['ini'])
            if sol > 0:
                encima.append((sol, v))
        encima.sort(key=lambda x: -x[0])
        principal = encima[0][1] if encima else None
        filas.append({
            'n': i, 'ini': a, 'dur': r['dur'], 'bloque': r['bloque'],
            'frase': principal['frase'] if principal else '',
            'cubre': round(encima[0][0] / r['dur'], 2) if encima else 0.0,
            'otras': [v['frase'] for _, v in encima[1:]],
        })
    json.dump(filas, open(salida, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return filas


if __name__ == '__main__':
    filas = main(*sys.argv[1:5])
    for f in filas:
        print('%2d  %5d +%3d  %-24s  %d%%' % (f['n'], f['ini'], f['dur'],
                                              f['bloque'][:24], int(f['cubre'] * 100)))
        print('      %s' % f['frase'][:150])
        for o in f['otras'][:2]:
            print('      + %s' % o[:120])
    print('\n%d ranuras cruzadas' % len(filas))
    flojas = [f['n'] for f in filas if f['cubre'] < 0.5]
    print('ranuras donde la frase principal cubre menos de la mitad: %s'
          % (flojas or 'ninguna'))
