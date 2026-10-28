# -*- coding: utf-8 -*-
r"""Tiempos por palabra de las tomas elegidas de la V2 (Scribe, cuenta propia;
la llave no se imprime). Sirven para que cada carton entre con su frase.

    python ch_stt_tramos.py
Salida: D:\DAE\_tmp\ch\stt\tramos\<toma>.json
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, r'D:\DAE\_repo\herramientas\voz')
import ch_transcribir as T     # noqa: E402  (solo usa stt(); su bucle no corre al importar)

RAIZ = r'E:\DAE MASTER\PRIORIDAD 1\PROFE CARLOS HUMBERTO'
CARP = {1: 'CASO 01 - Santiago y Valeria', 2: 'CASO 02 - Rodman', 3: 'CASO 03 - Disney',
        4: 'CASO 04 - Arley y Susana', 5: 'CASO 05 - Juan', 6: 'CASO 06 - Lenin'}
ELEGIDAS = ['C01_r1_b', 'C02_r1_b', 'C02_r2_b', 'C03_r1_a', 'C03_r2_a', 'C03_r3_b', 'C03_r4_b',
            'C03_i1_a', 'C04_r1_b', 'C04_r2_a', 'C05_r1_b', 'C05_r2_b', 'C06_r1_a', 'C06_r2_b']
OUT = r'D:\DAE\_tmp\ch\stt\tramos'

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for e in ELEGIDAS:
        dst = os.path.join(OUT, e + '.json')
        if os.path.exists(dst):
            continue
        n = int(e[1:3])
        src = os.path.join(RAIZ, CARP[n], '03 VOCES', 'v2', 'CH_U1_%s.mp3' % e)
        j = T.stt(src)
        json.dump(j, open(dst, 'w', encoding='utf-8'), ensure_ascii=False)
        print(e, len(j.get('words', [])), flush=True)
    print('LISTO')
