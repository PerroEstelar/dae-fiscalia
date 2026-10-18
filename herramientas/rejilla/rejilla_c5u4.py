#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rejilla del C5U4 «Los Ilustres». Mismo metodo: imantar cada frontera a la
pausa real mas cercana, radio 3,0 s."""
import json, sys
sys.path.insert(0, '/home/claude/c5/voz')
from rejilla import FPS, iman

RADIO = 3.0
# EL IMAN SOLO SE PEGA A RESPIROS, NO A COMAS
#     Los respiros que se marcan en el guion con <break> miden 0,9 s y salen
#     medidos entre 0,85 y 1,6. Pero el detector tambien encuentra las pausas
#     internas de frase, de 0,25 a 0,35 s, que NO son sitio para cortar: el
#     plano cambia en mitad de una enumeracion y se nota.
#
#     En el C5U4 eso partio una ranura en dos: el iman de b8 prefirio una pausa
#     de 0,25 s a 0,97 s de distancia sobre el respiro real de 1,10 s que
#     estaba a 1,35, y dejo una ranura de 83 cuadros. Con el filtro, el corte
#     se va al respiro y la ranura queda en 150.
MINIMO_PAUSA = 0.50

PLAN = {
    # Seis bloques de tres ranuras y dos de dos. La regla es el reparto de
    # PALABRAS, no el gusto: un bloque de 50 palabras largas no sostiene dos
    # planos de 11 s, y uno de 30 no da para tres de 4,7.
    'b1_entramado':  ['kf01_sala', 'ae01_velo', 'kf01b_sala'],
    # b2 va a dos: el corte cae en los dos puntos de la frase (el de la
    # enumeracion y el del cierre) y la pieza de las cuatro medidas necesita
    # la ranura larga para que las cuatro quepan leidas.
    'b2_resolucion': ['kf03_resolucion', 'ae02_medidas'],
    'b3_comprador':  ['kf04_hotel', 'ae03_diligencias', 'kf05_escritura'],
    'b4_socios':     ['kf06_estacion', 'ae04_setenta_treinta', 'kf06b_estacion'],
    'b5_finca':      ['kf08_finca', 'kf09_folio', 'kf08b_finca'],
    'b6_antes':      ['kf10_tractocamiones', 'ae05_linea_tiempo', 'kf10b_tractocamiones'],
    'b7_oferta':     ['kf12_carta', 'kf12b_carta', 'ae06_tres_por_ciento'],
    'b8_cierre':     ['ae07_inventario', 'kf15_pasillo', 'ae08_pregunta'],
}

# Las ranuras que llevarian clip de Kling: no pueden pasar de 193 cuadros, que
# es lo que rinde un clip de 8 s, para no tener que retimar con flujo optico
# como en el C5U2.
#
# Quedan fuera por diseno, no por falta de presupuesto:
#   kf03_resolucion y kf12_carta son documentos quietos sobre un escritorio; el
#   empuje horneado dice lo mismo y es gratis.
#   kf09_folio, kf05_escritura y kf15_pasillo, igual.
KLING = ['kf01_sala', 'kf04_hotel', 'kf06_estacion', 'kf08_finca',
         'kf10_tractocamiones']


def construir(rejilla_json, silencios_json):
    r = json.load(open(rejilla_json, encoding='utf-8'))
    sil = [p for p in json.load(open(silencios_json, encoding='utf-8'))
           if p['dur'] >= MINIMO_PAUSA]
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

    print('%2s  %-24s %-16s %8s %8s %6s %6s  %s' % (
        'n', 'plano', 'bloque', 'entra', 'sale', 'cuadr', 'seg', 'corte'))
    tot = 0; mal = []
    for i, x in enumerate(rs):
        tot += x['frames']
        est = 'inicio' if i == 0 else (dentro(x['ini']) or '*** PARTE FRASE ***')
        if i and not dentro(x['ini']): mal.append(x['n'])
        aviso = '' if x['plano'] not in KLING or x['frames'] <= 193 else '  <- KLING SE QUEDA CORTO'
        print('%2d  %-24s %-16s %8.2f %8.2f %6d %6.1f  %s%s' % (
            x['n'], x['plano'], x['bloque'], x['ini'], x['fin'],
            x['frames'], x['frames'] / FPS, est, aviso))
    print('%d ranuras, %d cuadros, %.1f s' % (len(rs), tot, tot / FPS))
    print('cortes que parten frase:', mal or 'ninguno', 'de', len(rs) - 1)
    print('enanas (<96):', [x['n'] for x in rs if x['frames'] < 96] or 'ninguna')
    print('muy largas (>300):', [x['n'] for x in rs if x['frames'] > 300] or 'ninguna')
    largos = [(x['plano'], x['frames']) for x in rs if x['plano'] in KLING and x['frames'] > 193]
    print('ranuras de Kling por encima de 193:', largos or 'ninguna')
    json.dump(rs, open('ranuras.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
