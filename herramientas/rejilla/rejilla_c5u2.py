#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rejilla del C5U2.

METODO: el mismo del C5U1 -partir el bloque en partes iguales e imantar cada
frontera a la pausa real mas cercana- con el radio abierto a 3,0 s.

Por que se volvio a este y no al de "elegir la mejor combinacion de pausas":
aquel subia los cortes en pausa de 4 a 5 de 9, pero a cambio producia ranuras
de 13,9 s y 15,9 s. Medido radio 2,0 / 2,5 / 3,0 / 4,0 / 5,0, el 3,0 da 4 de 9
en pausa sin ninguna ranura por encima de 11,3 s. Se prefiere el reparto parejo:
una ranura de 16 s se nota mas que un corte que cae 0,4 s despues de la pausa.

Ademas la locucion se regrabo con <break time="0.9s"/> en los puntos de corte
previstos, asi que ahora si hay una pausa real cerca de cada punto medio.
"""
import json, sys
sys.path.insert(0, '/home/claude/c5/voz')
from rejilla import FPS, iman

RADIO = 3.0

PLAN = {
    'b1_siniestro':  ['kf01_via', 'kf02_camion'],
    # b2 se parte en tres: el corte aritmetico de dos ranuras caia en mitad
    # de frase (unico de los 16 que lo hacia). Se regrabo el bloque con una
    # segunda respiracion antes de 'La pretension' y la cifra se lleva su
    # propia pieza, como en el C5U1 se la llevaban el saldo y los giros.
    'b2_pretension': ['kf03_sala', 'kf04_banca', 'ae02b_pretension'],
    'b3_patrimonio': ['kf05_carpeta'],
    'b4_inventario': ['kf06_casa', 'kf07_camioneta', 'ae08_sociedad'],
    'b5_victimas':   ['kf09_flota', 'ae10_patrimonios'],
    # b6 tambien a tres: con dos, kf12_llaves -la placa mas plana del set-
    # se quedaba 12,6 s en pantalla. El reloj vuelve al final, igual que en
    # el C5U1 volvian los tractocamiones.
    'b6_reloj':      ['ae11_reloj', 'kf12_llaves', 'ae11b_reloj'],
    'b7_caucion':    ['kf13_aseguradora', 'kf04b_banca'],
    # slot 2 era kf06b_casa: el texto de ahi habla de la venta y de la caucion,
    # no de la casa. Va un segundo horneado del mostrador vacio de la
    # aseguradora -la caucion que nadie puede pagar-.
    'b8_cierre':     ['ae14_inventario', 'kf13b_aseguradora', 'ae14b_pregunta'],
}


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
        if len(cortes) != len(planos) + 1:      # el iman junto dos cortes
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
    centros = [(p['ini'] + p['fin']) / 2.0 for p in sil]
    print('%2s  %-20s %-14s %8s %8s %6s %6s  %s' % (
        'n', 'plano', 'bloque', 'entra', 'sale', 'cuadr', 'seg', 'corte'))
    tot = 0; fuera = 0
    for i, x in enumerate(rs):
        tot += x['frames']
        if i == 0:
            est = 'inicio'
        else:
            d = min(abs(c - x['ini']) for c in centros)
            est = 'en pausa' if d < 0.06 else 'a %.2f s' % d
            if d >= 0.06: fuera += 1
        print('%2d  %-20s %-14s %8.2f %8.2f %6d %6.1f  %s' % (
            x['n'], x['plano'], x['bloque'], x['ini'], x['fin'],
            x['frames'], x['frames'] / FPS, est))
    print('%d ranuras, %d cuadros, %.1f s' % (len(rs), tot, tot / FPS))
    print('cortes fuera de pausa:', fuera, 'de', len(rs) - 1)
    print('enanas (<48):', [x['n'] for x in rs if x['frames'] < 48] or 'ninguna')
    print('muy largas (>300):', [x['n'] for x in rs if x['frames'] > 300] or 'ninguna')
    json.dump(rs, open('ranuras.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
