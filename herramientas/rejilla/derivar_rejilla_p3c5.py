#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Deriva la rejilla de ranuras del P3C5 midiendo el master de narracion.

EL PROCEDIMIENTO ES EL DEL CASO 4, Y NO SE CAMBIA
    1. `silencedetect` sobre el master. El crudo NO sirve tal cual: hay
       decenas de pausas y montar una ranura por cada una daria un corte cada
       cinco segundos y miles de creditos en placas de mas.
    2. Las fronteras de BLOQUE son obligatorias: ahi cambia el locutor, y una
       imagen montada encima de un cambio de voz esta mal montada.
    3. El resto se va cayendo por la pausa MAS CORTA primero, mientras la
       ranura que queda al unir no pase del tope. La pausa larga es la que el
       guion puso a proposito; la corta es una coma.

EL TOPE DE 300 CUADROS
    Medido en el Caso 4: por debajo de 280 no se puede quitar nada porque el
    hueco natural mas largo ya mide mas que eso; por encima de 360 salen
    planos de 267 cuadros donde no pasa nada, y esos hay que partirlos. 300
    es el numero de la serie.

EL PISO DE 96 CUADROS
    Cuatro segundos: por debajo, un carton no se alcanza a leer.
"""
import json
import os
import re
import subprocess
import sys

FPS = 24000 / 1001.0
TOPE = 300
PISO = 96

INTRO = 182
ENTRADA = 119
RESPIRO = 48
CIERRE = 119
OUTRO = 182

FF = os.environ.get('FFMPEG', 'ffmpeg')


def silencios(wav, umbral='-34dB', dur=0.22):
    s = subprocess.run([FF, '-nostats', '-i', wav,
                        '-af', 'silencedetect=noise=%s:d=%.2f' % (umbral, dur),
                        '-f', 'null', '-'],
                       capture_output=True, text=True,
                       encoding='utf-8', errors='replace').stderr
    ini = [float(x) for x in re.findall(r'silence_start: (-?\d+\.?\d*)', s)]
    fin = [float(x) for x in re.findall(r'silence_end: (-?\d+\.?\d*)', s)]
    return list(zip(ini, fin))[:len(fin)]


def reparar(r):
    """Deja toda ranura entre el piso y el tope, sin mover las fronteras de
    bloque.

    Las dos averias son reales y salieron aqui: el `silencedetect` deja
    ranuras de 81 y 85 cuadros pegadas a una frontera de bloque -no se leen-,
    y un tramo de 404 dentro de b16 donde el locutor no hace una sola pausa
    -no se sostiene-.

    Unir va PRIMERO y partir va despues, porque unir puede crear una ranura
    larga que el segundo paso arregla, mientras que al reves se parte algo que
    despues hay que volver a unir. Se une siempre con un vecino DEL MISMO
    BLOQUE: una ranura a caballo de un cambio de locutor esta mal montada.
    """
    cambiado = True
    while cambiado:
        cambiado = False
        for i, (a, d, b) in enumerate(r):
            if d >= PISO:
                continue
            ops = []
            if i > 0 and r[i - 1][2] == b:
                ops.append(i - 1)
            if i + 1 < len(r) and r[i + 1][2] == b:
                ops.append(i + 1)
            if not ops:
                continue
            j = min(ops, key=lambda k: r[k][1])
            lo, hi = min(i, j), max(i, j)
            r[lo] = (r[lo][0], r[lo][1] + r[hi][1], r[lo][2])
            del r[hi]
            cambiado = True
            break
        if cambiado:
            continue
        for i, (a, d, b) in enumerate(r):
            if d <= TOPE:
                continue
            n = -(-d // TOPE)                 # techo de la division
            base = d // n
            trozos = [base] * n
            for k in range(d - base * n):
                trozos[k] += 1
            off, nuevas = a, []
            for t in trozos:
                nuevas.append((off, t, b))
                off += t
            r[i:i + 1] = nuevas
            cambiado = True
            break
    return r


def main(wav, tramos_json, salida):
    info = json.load(open(tramos_json, encoding='utf-8'))
    tramos = info['tramos']
    total = int(round(info['dur'] * FPS))

    huecos = silencios(wav)
    # candidata = (cuadro del corte, largo de la pausa en segundos)
    cand = []
    for a, b in huecos:
        if a <= 0.01 or b >= info['dur'] - 0.05:
            continue                      # cabeza y cola no son cortes
        cand.append((int(round((a + b) / 2.0 * FPS)), b - a))

    # las fronteras de bloque, que son obligatorias
    obliga = set()
    for i in range(len(tramos) - 1):
        medio = (tramos[i]['sale'] + tramos[i + 1]['entra']) / 2.0
        c = int(round(medio * FPS))
        # se pega a la candidata mas cercana para no inventar un corte
        if cand:
            c = min((x for x in cand), key=lambda x: abs(x[0] - c))[0]
        obliga.add(c)

    cortes = sorted(set(x[0] for x in cand) | obliga)
    largo = {c: d for c, d in cand}

    # se van cayendo por la pausa mas corta primero
    quitables = sorted((c for c in cortes if c not in obliga),
                       key=lambda c: largo.get(c, 0.0))
    for c in quitables:
        i = cortes.index(c)
        a = cortes[i - 1] if i > 0 else 0
        b = cortes[i + 1] if i + 1 < len(cortes) else total
        if b - a <= TOPE:
            cortes.remove(c)

    bordes = [0] + cortes + [total]
    ranuras = []
    for i in range(len(bordes) - 1):
        a, b = bordes[i], bordes[i + 1]
        # que bloque se oye encima: el que cubre el centro de la ranura
        centro = (a + b) / 2.0 / FPS
        bloque = tramos[0]['bloque']
        for t in tramos:
            if t['entra'] <= centro <= t['sale']:
                bloque = t['bloque']
                break
            if t['entra'] > centro:
                break
            bloque = t['bloque']
        ranuras.append((a, b - a, bloque))

    ranuras = reparar(ranuras)

    pieza = INTRO + ENTRADA + total + RESPIRO + CIERRE + OUTRO
    out = {'n_ranuras': total, 'pieza': pieza, 'tope': TOPE, 'piso': PISO,
           'ranuras': [{'ini': a, 'dur': d, 'bloque': b} for a, d, b in ranuras]}
    json.dump(out, open(salida, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return ranuras, total, pieza, len(cand), len(obliga)


if __name__ == '__main__':
    r, total, pieza, ncand, nobl = main(sys.argv[1], sys.argv[2], sys.argv[3])
    print('%3s %7s %7s %6s %6s  %s' % ('#', 'ini', 'fin', 'dur', 'seg', 'bloque'))
    for i, (a, d, b) in enumerate(r, 1):
        print('%3d %7d %7d %6d %6.1f  %s' % (i, a, a + d, d, d / FPS, b))
    n = len(r)
    print('\n%d pausas candidatas, %d fronteras de bloque obligatorias' % (ncand, nobl))
    print('%d ranuras - %d cuadros - media %.0f (%.1f s)'
          % (n, total, total / n, total / n / FPS))
    cortas = [i + 1 for i, (_, d, _) in enumerate(r) if d < PISO]
    largas = [i + 1 for i, (_, d, _) in enumerate(r) if d > TOPE]
    print('por debajo del piso de %d: %s' % (PISO, cortas or 'ninguna'))
    print('por encima del tope de %d: %s' % (TOPE, largas or 'ninguna'))
    print('suman %d, el bloque mide %d -> %s'
          % (sum(d for _, d, _ in r), total,
             'cuadra' if sum(d for _, d, _ in r) == total else 'NO CUADRA'))
    print('pieza %d cuadros = %d:%04.1f'
          % (pieza, int(pieza / FPS) // 60, (pieza / FPS) % 60))
