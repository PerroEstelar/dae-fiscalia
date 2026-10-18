#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rejilla del C5U3. Mismo metodo del C5U2: imantar cada frontera a la pausa
real mas cercana, radio 3,0 s."""
import json, sys
sys.path.insert(0, '/home/claude/c5/voz')
from rejilla import FPS, iman

RADIO = 3.0

PLAN = {
    # b1 y b2 son los bloques largos (24,5 s y 21,1 s). Con dos ranuras cada uno,
    # la de Kling se pasaba de 193 cuadros y el corte de b2 caia en mitad de frase.
    # Con tres, el iman tiene mas pausas donde agarrarse y la ranura de Kling cabe.
    'b1_hipotesis':    ['kf01_sede', 'ae01_hipotesis', 'kf01b_sede'],
    'b2_diligencia':   ['kf02_allanamiento', 'ae02_cinco_bienes', 'kf02b_allanamiento'],
    'b3_vehiculos':    ['kf03_parqueadero', 'kf03b_parqueadero'],
    'b4_bodega':       ['kf04_bodega', 'kf05_repuestos', 'ae03_tercero'],
    'b5_servidores':   ['kf06_servidores', 'ae04_depreciacion'],
    'b6_caja':         ['kf07_caja', 'kf08_computadores', 'ae05_producto_prueba'],
    'b7_apartamentos': ['kf09_apartamentos', 'kf09b_apartamentos'],
    'b8_cierre':       ['ae06_inventario', 'kf04b_bodega', 'ae07_pregunta'],
}

# las ranuras que llevarian clip de Kling: no pueden pasar de 193 cuadros,
# que es lo que rinde un clip de 8 s, para no tener que retimar como en el C5U2
# kf06_servidores sale de la lista: un rack es estatico y la ranura pide 238
# cuadros. Se hornea con empuje, que es gratis y no se nota menos.
KLING = ['kf01_sede', 'kf02_allanamiento', 'kf03_parqueadero',
         'kf04_bodega', 'kf07_caja']


def construir(rejilla_json, silencios_json):
    r = json.load(open(rejilla_json, encoding='utf-8'))
    sil = json.load(open(silencios_json, encoding='utf-8'))
    ranuras = []
    for tr in r['tramos']:
        planos = PLAN[tr['bloque']]
        a, b = tr['entra'], tr['sale']
        cortes = [a] + [iman(a + (b - a) * k / len(planos), sil, RADIO)
                        for k in range(1, len(planos))] + [b]
        cortes = sorted(set(round(c, 3) for c in cortes))
        if len(cortes) != len(planos) + 1:
            cortes = [a + (b - a) * k / len(planos) for k in range(len(planos) + 1)]
        for k, p in enumerate(planos):
            ranuras.append({'plano': p, 'bloque': tr['bloque'],
                            'ini': round(cortes[k], 3), 'fin': round(cortes[k + 1], 3)})
    for i in range(len(ranuras) - 1):
        ranuras[i]['fin'] = ranuras[i + 1]['ini']
    ranuras[-1]['fin'] = r['dur']
    for n, x in enumerate(ranuras, 1):
        x['n'] = n
        x['frames'] = int(round((x['fin'] - x['ini']) * FPS))
    return ranuras


if __name__ == '__main__':
    rs = construir('rejilla.json', 'silencios.json')
    sil = json.load(open('silencios.json'))
    r = json.load(open('rejilla.json', encoding='utf-8'))
    tr = r['tramos']
    huecos = [(tr[i]['sale'], tr[i + 1]['entra']) for i in range(len(tr) - 1)]

    def dentro(t):
        for p in sil:
            if p['ini'] - 0.05 <= t <= p['fin'] + 0.05:
                return 'silencio %.2f s' % p['dur']
        for a, b in huecos:
            if a - 0.05 <= t <= b + 0.05:
                return 'hueco entre bloques'
        return None

    print('%2s  %-22s %-16s %8s %8s %6s %6s  %s' % (
        'n', 'plano', 'bloque', 'entra', 'sale', 'cuadr', 'seg', 'corte'))
    tot = 0; mal = []
    for i, x in enumerate(rs):
        tot += x['frames']
        est = 'inicio' if i == 0 else (dentro(x['ini']) or '*** PARTE FRASE ***')
        if i and not dentro(x['ini']): mal.append(x['n'])
        aviso = '' if x['plano'] not in KLING or x['frames'] <= 193 else '  <- KLING SE QUEDA CORTO'
        print('%2d  %-22s %-16s %8.2f %8.2f %6d %6.1f  %s%s' % (
            x['n'], x['plano'], x['bloque'], x['ini'], x['fin'],
            x['frames'], x['frames'] / FPS, est, aviso))
    print('%d ranuras, %d cuadros, %.1f s' % (len(rs), tot, tot / FPS))
    print('cortes que parten frase:', mal or 'ninguno', 'de', len(rs) - 1)
    print('enanas (<48):', [x['n'] for x in rs if x['frames'] < 48] or 'ninguna')
    print('muy largas (>300):', [x['n'] for x in rs if x['frames'] > 300] or 'ninguna')
    largos = [(x['plano'], x['frames']) for x in rs if x['plano'] in KLING and x['frames'] > 193]
    print('ranuras de Kling por encima de 193:', largos or 'ninguna')
    json.dump(rs, open('ranuras.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
