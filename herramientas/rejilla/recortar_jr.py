# -*- coding: utf-8 -*-
r"""Corrige a mano, por PALABRA, los cortes internos de un bloque que la
rejilla automatica puso a mitad de frase.

POR QUE
    `derivar_rejilla_p3c5` corta donde el locutor hizo pausa, y la pausa de
    ElevenLabs no siempre cae en la coma: en el T1 corto «en el estricto |
    orden en que llegan», en el T3 «previsto en el articulo | 349» y en el
    T4 «el nuevo aplicativo | utilizado». Una imagen que cambia a mitad de
    sintagma se oye como un tropiezo.

COMO
    Las fronteras de BLOQUE no se tocan. Dentro de un bloque que aparece en
    CORTES, sus ranuras se rehacen: un corte antes de cada frase ancla, en
    el punto medio entre el final de la palabra anterior y el comienzo de la
    primera palabra del ancla, segun los tiempos por palabra de Scribe
    (`stt_jr.py`). Se comprueba piso y tope y que la suma no cambie.

    python recortar_jr.py cruce_jr_v2.json salida_dir
"""
import json
import os
import re
import sys
import unicodedata

FPS = 24000 / 1001.0
PISO, TOPE = 90, 300      # el T1 r03 mide 94: se acepta (ver README)

# 30 oct. C1: el bloque de la denuncia y la asignacion son dos lugares (la
# ventanilla y el despacho). U1: la fabula pide una imagen por movimiento, y
# los titulos de fase quedaron fundidos con la frase siguiente (`fusionar_
# cortas`): se corta donde arranca la accion nueva.
CORTES = {
 'C1': {'c03_le_corresponde': ['y con posterioridad']},
 'U1': {'u02_el_bloqueo': ['Al intentar adelantar'],
        'u04_el_pinchazo': ['Más adelante'],
        'u12_calcinado': ['La policía llega']},
}


def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.findall(r'[a-z0-9]+', s)


def rehacer(clave, d):
    ran = d['ranuras']
    words = d['words']                     # (start, end, text, bloque)
    nuevas = []
    for r in ran['ranuras']:
        b = r['bloque']
        if b not in CORTES.get(clave, {}):
            nuevas.append(dict(r))
            continue
        if nuevas and nuevas[-1]['bloque'] == b:
            # se extiende la primera ranura del bloque; los cortes se ponen al final
            nuevas[-1]['dur'] += r['dur']
        else:
            nuevas.append(dict(r))
    out = []
    for r in nuevas:
        b = r['bloque']
        if b not in CORTES.get(clave, {}):
            out.append(r)
            continue
        ws = [w for w in words if w[3] == b]
        toks = [(norm(w[2]) or [''])[0] for w in ws]
        a, fin = r['ini'], r['ini'] + r['dur']
        cortes = []
        for ancla in CORTES[clave][b]:
            q = norm(ancla)
            k = next(i for i in range(len(toks)) if toks[i:i + len(q)] == q)
            t = (ws[k - 1][1] + ws[k][0]) / 2.0
            cortes.append(int(round(t * FPS)))
        bordes = [a] + cortes + [fin]
        for i in range(len(bordes) - 1):
            out.append({'ini': bordes[i], 'dur': bordes[i + 1] - bordes[i],
                        'bloque': b})
    return out


if __name__ == '__main__':
    datos = json.load(open(sys.argv[1], encoding='utf-8'))
    dest = sys.argv[2]
    os.makedirs(dest, exist_ok=True)
    for clave, d in sorted(datos.items()):
        ran = d['ranuras']
        nuevas = rehacer(clave, d)
        assert sum(r['dur'] for r in nuevas) == ran['n_ranuras'], clave
        assert all(nuevas[i]['ini'] + nuevas[i]['dur'] == nuevas[i + 1]['ini']
                   for i in range(len(nuevas) - 1)), clave
        malas = [i + 1 for i, r in enumerate(nuevas) if not PISO <= r['dur'] <= TOPE]
        o = dict(ran)
        o['ranuras'] = nuevas
        o['recortado'] = CORTES.get(clave, {})
        json.dump(o, open(os.path.join(dest, 'JR_%s_ranuras.json' % clave), 'w',
                          encoding='utf-8'), ensure_ascii=False, indent=1)
        print('=====', clave, len(nuevas), 'ranuras', 'fuera de piso/tope:', malas or 'ninguna')
        for i, r in enumerate(nuevas, 1):
            a, b = r['ini'] / FPS, (r['ini'] + r['dur']) / FPS
            txt = ' '.join(w[2] for w in d['words'] if a <= w[0] < b)
            print('r%02d %4d %-24s %s' % (i, r['dur'], r['bloque'][:24], txt))
