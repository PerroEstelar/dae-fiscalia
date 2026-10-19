#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rejilla del P3C2. Mismo iman: radio 3,0 s, pausas de 0,50 s o mas.

LA FORMA DEL PLAN SALE DE LA FORMA DEL CASO
    Cuatro personas, y al lado de cada una la propuesta equivocada que el
    equipo hizo sobre ella. Por eso cada bloque de propuesta va ENTERO a
    carton: la propuesta es texto, no es escena, y ponerla sobre una cara
    la convierte en opinion de esa persona.

    Y por eso `b8_propuesta_samuel` va partido en dos cartones: son dos
    propuestas distintas -suplir la version con el informe de Dario, y
    descartarlo por no poder comunicarse- y leidas de corrido se confunden
    en una sola.
"""
import json, sys
sys.path.insert(0, '/home/claude/c5/voz')
from rejilla import FPS, iman

RADIO = 3.0
MINIMO_PAUSA = 0.50

PLAN = {
    'b1_llegada':          ['ae01_primer_contacto', 'kf01_fachada_taller'],
    # el orden lo manda la voz: «seis personas, dos conservan» -> carton;
    # «las otras cuatro senalan» -> el taller; «no hay candados» -> la puerta.
    # Ademas asi el carton cae en la ranura de 217 y no en la de 238, que se
    # pasaba del techo de lectura.
    'b2_seis':             ['ae02_seis_personas', 'kf02_taller_interior',
                            'kf03_puerta_sin_candado'],
    'b3_mara':             ['kf04_mara_cu', 'ae03_pasaporte'],
    'b4_mara_sale':        ['kf05_escalera_domingo', 'kf06_mara_entera',
                            'ae04_pide'],
    'b5_propuesta_mara':   ['ae05_la_propuesta'],
    'b6_samuel':           ['kf07_samuel_cu', 'ae06_lo_que_vio'],
    'b7_dario':            ['kf08_dario_traduce', 'kf09_samuel_aparte'],
    'b8_propuesta_samuel': ['ae07_suplir', 'ae08_descartarse'],
    'b9_elisa':            ['kf10_elisa_entera', 'ae09_por_la_tia',
                            'ae10_ya_escuchada'],
    'b10_propuesta_elisa': ['ae11_repetir', 'kf11_elisa_cu'],
    'b11_patricia':        ['kf12_patricia_cu', 'kf13_mensajes',
                            'ae12_no_verificado'],
    'b12_cierre':          ['ae13_cinco_decisiones', 'kf14_taller_vacio',
                            'ae14_hipotesis'],
}

# Ninguna ranura se genera con Kling en esta pieza. Se decide con el montaje
# delante, igual que en el Caso 1.
KLING = []

# `ae14_hipotesis` queda en 227 cuadros, dos por encima del techo. Se deja:
# es el remate de la pieza -«es, por ahora, una hipotesis»- y moverlo obligaba
# a poner la placa del taller vacio en la ultima ranura, que le quita a esa
# frase el unico sitio donde puede leerse sola.
RANGO = {'ae': (96, 225), 'kf': (96, 290)}
TOLERADAS = {'ae14_hipotesis'}


def construir(rejilla_json, silencios_json):
    r = json.load(open(rejilla_json, encoding='utf-8'))
    sil = [s for s in json.load(open(silencios_json, encoding='utf-8'))
           if (s['fin'] - s['ini'] if isinstance(s, dict) else s[1] - s[0]) >= MINIMO_PAUSA]
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
    print('%-3s %-26s %-22s %8s %8s %7s' %
          ('n', 'plano', 'bloque', 'ini', 'fin', 'cuadros'))
    for x in rs:
        print('%-3d %-26s %-22s %8.2f %8.2f %7d' %
              (x['n'], x['plano'], x['bloque'], x['ini'], x['fin'], x['frames']))
    tot = sum(x['frames'] for x in rs)
    cs = [x['frames'] for x in rs]
    print('\n%d ranuras | %d cuadros | mas corta %d (%.1f s) | mas larga %d (%.1f s)'
          % (len(rs), tot, min(cs), min(cs) / FPS, max(cs), max(cs) / FPS))
    malas = []
    for x in rs:
        lo, hi = RANGO['ae' if x['plano'].startswith('ae') else 'kf']
        if not (lo <= x['frames'] <= hi) and x['plano'] not in TOLERADAS:
            malas.append((x['plano'], x['frames'], lo, hi))
    print('fuera de rango:', malas or 'ninguna')
    json.dump(rs, open('ranuras.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
