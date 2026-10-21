# -*- coding: utf-8 -*-
"""Cruza, medido, la narracion real contra la rejilla de ranuras del P3C3.

Alineacion: los segmentos de habla de los 15 archivos de bloque se casan en
orden con los segmentos de habla del master. Un segmento de bloque puede
corresponder a uno o a dos segmentos del master (el master conserva alguna
pausa interna que el archivo de bloque no marca). Programacion dinamica
sobre la diferencia de duracion, no emparejamiento codicioso.
"""
import json, sys

FPS = 24000.0 / 1001.0


def alinear(M, B):
    """M: [(ini,fin)] del master.  B: [{'dur':..}] de los bloques."""
    n, m = len(M), len(B)
    INF = float('inf')
    # coste[i][j] = mejor coste casando los primeros i del master con j de B
    c = [[INF] * (m + 1) for _ in range(n + 1)]
    de = [[None] * (m + 1) for _ in range(n + 1)]
    c[0][0] = 0.0
    for i in range(n + 1):
        for j in range(m + 1):
            if c[i][j] == INF:
                continue
            if i < n and j < m:                      # 1 a 1
                d = abs((M[i][1] - M[i][0]) - B[j]['dur'])
                if c[i][j] + d < c[i + 1][j + 1]:
                    c[i + 1][j + 1] = c[i][j] + d
                    de[i + 1][j + 1] = (i, j, 1)
            if i + 1 < n and j < m:                  # 2 del master a 1 de B
                d = abs((M[i + 1][1] - M[i][0]) - B[j]['dur'])
                if c[i][j] + d < c[i + 2][j + 1]:
                    c[i + 2][j + 1] = c[i][j] + d
                    de[i + 2][j + 1] = (i, j, 2)
    i, j, out = n, m, []
    while i or j:
        pi, pj, k = de[i][j]
        out.append((M[pi][0], M[i - 1][1], B[pj], k))
        i, j = pi, pj
    out.reverse()
    return out, c[n][m]


def cruzar(habla, ranuras, offset=301):
    M = [tuple(x) for x in habla['master']]
    B = habla['bloques']
    par, coste = alinear(M, B)
    frases = [{'bloque': b['bloque'], 'i': b['i'], 'frase': b['frase'],
               'ini': round(a * FPS), 'fin': round(z * FPS), 'master': k}
              for a, z, b, k in par]
    filas = []
    for r in ranuras:
        dentro = []
        for f in frases:
            sol = min(r['fin'], f['fin']) - max(r['ini'], f['ini'])
            if sol > 12:                      # mas de medio segundo dentro
                dentro.append((sol, f))
        dentro.sort(key=lambda x: x[1]['ini'])
        filas.append((r, dentro))
    return filas, frases, coste


if __name__ == '__main__':
    habla = json.load(open(sys.argv[1], encoding='utf-8'))
    ranuras = json.load(open(sys.argv[2], encoding='utf-8'))
    filas, frases, coste = cruzar(habla, ranuras)
    print('coste de alineacion %.2f s sobre %d segmentos' % (coste, len(frases)))
    print()
    mal = []
    for r, dentro in filas:
        print('r%02d %5d-%5d  %-28s %s' % (r['n'], r['ini'], r['fin'],
                                           r['plano'], r['encima'] or ''))
        if not dentro:
            print('        (silencio: no se oye nada)')
        for sol, f in dentro:
            print('        %5d-%5d %-18s %s' % (f['ini'], f['fin'],
                                                f['bloque'], f['frase']))
        bl = set(f['bloque'] for _, f in dentro)
        if r['bloque'] not in bl and dentro:
            mal.append((r['n'], r['plano'], r['bloque'], sorted(bl)))
        print()
    print('RANURAS CUYO BLOQUE DECLARADO NO ES EL QUE SE OYE: %d' % len(mal))
    for n, p, dec, oido in mal:
        print('   r%02d %-28s declara %-18s se oye %s' % (n, p, dec, ','.join(oido)))
