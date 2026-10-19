#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rejilla del P3C1. El iman se pega a la pausa real mas cercana, radio 3,0 s.

EL IMAN SOLO SE PEGA A RESPIROS, NO A COMAS
    MINIMO_PAUSA filtra la lista de silencios antes de imantar. Una pausa
    intra-frase de 0,25 s no es un punto de corte: en el C5U4 el iman sin
    filtro prefirio una de 0,25 a 0,97 s de distancia sobre el respiro real
    de 1,10 que estaba a 1,35, y dejo una ranura por debajo del piso.
"""
import json, sys
sys.path.insert(0, '/home/claude/c5/voz')
from rejilla import FPS, iman

RADIO = 3.0
MINIMO_PAUSA = 0.50

PLAN = {
    # el iman pone el corte de b1 en el respiro escrito, a 3,7 s. Con la
    # fachada primero esa ranura quedaba en 89 cuadros, corta para un
    # establecedor. Con el carton de encuadre primero, los 3,7 s le caen
    # justo a una frase de seis palabras y la fachada se lleva los 9,5 s.
    'b1_encargo':     ['ae01_establecidos', 'kf01_fachada'],
    'b2_acuerdo':     ['kf03_cristina_telefono', 'ae02_el_acuerdo',
                       'kf04_victor_recepcion'],
    'b3_bisagra':     ['kf05_pasillo', 'ae03_no_todas'],
    'b4_daniela':     ['kf06_terminal', 'kf07_daniela_cu', 'ae04_deuda'],
    'b5_salir':       ['kf08_tienda', 'kf09_camilo_carro'],
    'b6_paula':       ['kf10_paula_llega', 'kf11_paula_cu', 'ae05_paula'],
    'b7_elena':       ['kf12_elena_limpieza', 'kf13_elena_cu', 'ae06_cambio',
                       'kf14_cuaderno'],
    'b8_permanencia': ['ae07_linea_tiempo', 'kf15_cristina_lejos'],
    'b9_camilo':      ['kf16_carro_noche', 'kf17_camilo_cu',
                       'kf18_daniela_ventanilla'],
    'b10_juliana':    ['kf19_agencia_diana', 'kf20_juliana_llega',
                       'ae09_interrumpido'],
    'b11_yeimi':      ['kf21_yeimi_llega', 'ae10_mensajes', 'kf22_yeimi_cu'],
    # una sola ranura: la ficha de las nueve es el remate y necesita leerse
    # entera. Partida en dos quedaba en 82 cuadros, muy por debajo de lo que
    # pide leer nueve nombres.
    'b12_cierre':     ['ae11_las_nueve'],
}

# Los unicos tres que se generan con Kling. La regla de la casa es 6 de 67, y
# la razon tecnica es que el rostro dibujado se rompe al animarse: estos tres
# no tienen cara cerca.
KLING = ['kf01_fachada', 'kf05_pasillo', 'kf16_carro_noche']

# piso y techo por tipo: un carton de AE que pase de ~220 cuadros se siente
# parado, y por debajo de 96 no se alcanza a leer.
RANGO = {'ae': (96, 225), 'kf': (96, 290)}


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
    print('%-3s %-26s %-16s %8s %8s %7s %s' %
          ('n', 'plano', 'bloque', 'ini', 'fin', 'cuadros', ''))
    for x in rs:
        marca = 'KLING' if x['plano'] in KLING else ''
        print('%-3d %-26s %-16s %8.2f %8.2f %7d %s' %
              (x['n'], x['plano'], x['bloque'], x['ini'], x['fin'], x['frames'], marca))
    tot = sum(x['frames'] for x in rs)
    cs = [x['frames'] for x in rs]
    print('\n%d ranuras | %d cuadros | mas corta %d (%.1f s) | mas larga %d (%.1f s)'
          % (len(rs), tot, min(cs), min(cs) / FPS, max(cs), max(cs) / FPS))
    print('ranuras de Kling:', [(x['plano'], x['frames']) for x in rs if x['plano'] in KLING])
    malas = []
    for x in rs:
        lo, hi = RANGO['ae' if x['plano'].startswith('ae') else 'kf']
        if not (lo <= x['frames'] <= hi):
            malas.append((x['plano'], x['frames'], lo, hi))
    print('fuera de rango:', malas or 'ninguna')
    json.dump(rs, open('ranuras.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
