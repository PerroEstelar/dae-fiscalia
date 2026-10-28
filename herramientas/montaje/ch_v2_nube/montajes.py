import json, os
R = 'E:\\DAE MASTER\\PRIORIDAD 1\\PROFE CARLOS HUMBERTO\\'
CARP = {1: 'CASO 01 - Santiago y Valeria', 2: 'CASO 02 - Rodman', 3: 'CASO 03 - Disney',
        4: 'CASO 04 - Arley y Susana', 5: 'CASO 05 - Juan', 6: 'CASO 06 - Lenin'}
LARGO = {1: 2650, 2: 2548, 3: 2547, 5: 2520, 6: 2252}
OUT = 'out/'
def base(n): return R + CARP[n] + '\\05 EXPORTS\\_base v2\\CH_U1_C%02d_full.mp4' % n
def pieza(n, f): return R + CARP[n] + '\\02 CARTONES\\v2\\' + f
def wav(n, k): return R + CARP[n] + '\\03 VOCES\\v2\\CH_U1_C%02d_%s_v2.wav' % (n, k)
def simple(n, piezas=()):
    L = LARGO[n]
    m = dict(caso=n, linea='CH U1 CASO %02d - %s v2' % (n, CARP[n].split(' - ', 1)[1]), largo=L,
             video=[dict(archivo=base(n), ini=0, fin=L, pista=1, en=0)],
             audio=[dict(archivo=wav(n, 'voz'), pista=1, en=0, ini=0, fin=L),
                    dict(archivo=wav(n, 'fondo'), pista=2, en=0, ini=0, fin=L)])
    for p in piezas:
        m['video'].append(dict(archivo=pieza(n, p['archivo']), ini=0, fin=p['cuadros'], pista=2, en=p['cuadro_v1']))
    json.dump(m, open(OUT + 'montaje_c%02d.json' % n, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return m
simple(1); simple(5)
simple(6, json.load(open(OUT + 'c6/piezas.json')))
print(open(OUT + 'montaje_c06.json').read())


def compuesto(n, largo, video):
    """video: lista de (archivo_win, ini, fin, pista, en)."""
    m = dict(caso=n, linea='CH U1 CASO %02d - %s v2' % (n, CARP[n].split(' - ', 1)[1]), largo=largo,
             video=[dict(archivo=a, ini=i, fin=f, pista=p, en=e) for a, i, f, p, e in video],
             audio=[dict(archivo=wav(n, 'voz'), pista=1, en=0, ini=0, fin=largo),
                    dict(archivo=wav(n, 'fondo'), pista=2, en=0, ini=0, fin=largo)])
    json.dump(m, open(OUT + 'montaje_c%02d.json' % n, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return m


if __name__ == '__main__' and 'c2' in __import__('sys').argv:
    T, D = 2088, 116
    compuesto(2, 2548 + D, [(base(2), 0, T, 1, 0), (pieza(2, 'CH_U1_C02_inserto_restaurativa.mp4'), 0, D, 1, T),
                            (base(2), T, 2548, 1, T + D)])
    print(open(OUT + 'montaje_c02.json').read()[:600])


if __name__ == '__main__' and 'c3' in __import__('sys').argv:
    T = 2233
    pz = json.load(open(OUT + 'c3/piezas.json'))
    vid = [(base(3), 0, T, 1, 0), (base(3), T, 2547, 1, T + 474)]
    for p in pz:
        vid.append((pieza(3, p['archivo']), 0, p['cuadros'], p['pista'], p['en']))
    compuesto(3, 2547 + 474, vid)
    print('c3 ok', len(vid))

if __name__ == '__main__' and 'c4' in __import__('sys').argv:
    pz = json.load(open(OUT + 'c4/piezas.json'))
    V1 = R + CARP[4] + '\\05 EXPORTS\\CH U1 CASO 04 - V1 entregado.mov'
    vid = [(V1, 0, 759, 1, 0), (V1, 851, 1950, 1, 923), (V1, 2069, 2383, 1, 2287)]
    for p in pz['piezas']:
        vid.append((pieza(4, p['archivo']), 0, p['cuadros'], p['pista'], p['en']))
    compuesto(4, 2383 + 72 + 146, vid)
    print('c4 ok', len(vid))
