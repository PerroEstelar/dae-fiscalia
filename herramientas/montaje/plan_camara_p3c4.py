#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El horneado de camara de las 36 placas del Caso 4.

EL MOVIMIENTO DICE ALGO, O NO SE PONE
    La camara de esta serie es lenta y casi invisible, pero no es decorativa:
    en una pieza de seis minutos sostenida sobre placas fijas, la direccion
    del empuje es lo unico que la imagen puede hacer por si sola.

    Aqui va asignada por lo que la placa SIGNIFICA, no por variar:

    ABRE   las placas de falta -el estrado vacio, el microfono apartado, la
           silla de la defensa, la orden en blanco, la hoja de una sola linea,
           el escritorio sin orden-. La ventana se ensancha mientras el plano
           dura, asi que el vacio alrededor del unico dato CRECE. Es la misma
           decision que el repertorio ya tomo con la escala: lo que no esta
           sustentado se filma con aire, y el aire aumenta.

    CIERRA las placas de acumulacion -el escrito denso, las cuentas de mas,
           el episodio detallado, las seis carpetas, las tres hojas-. La
           ventana se cierra y el cuadro se llena.

    APENAS las seis placas con rostro, y las de transito. Un empuje sobre una
    cara se lee como enfasis dramatico y esta serie no enfatiza: expone.

LA RIMA DE APERTURA Y CIERRE SE RESPETA
    r01 y r39 son las mismas seis carpetas con la misma camara cenital. Llevan
    el MISMO encuadre y el MISMO empuje -cerrando las dos- para que la unica
    diferencia entre el primer plano y el ultimo sea la que el caso quiere:
    al abrir estan superpuestas y en desorden, al cerrar separadas y con
    pestaña.

LA SEMILLA SALE DEL NOMBRE
    Para que el pulso de mano sea distinto en cada placa y reproducible entre
    corridas. No se fija a mano.
"""
import json
import os
import sys

sys.path.insert(0, '/home/claude/p3c4/voz')
import ranuras_p3c4 as R

PLACAS = '/home/claude/p3c4/grade/FINAL'
SALIDA = '/home/claude/p3c4/ranuras/out'

ABRE = -0.085      # la ventana se ensancha: crece el aire
CIERRA = 0.070     # la ventana se cierra: se llena el cuadro
APENAS = 0.022

#  ranura -> (empuje, deriva)
GESTO = {
    'r01': (CIERRA, [0.0, 0.0]),       # las seis carpetas, en desorden
    'r02': (APENAS, [0.03, 0.0]),      # Nora en el umbral
    'r03': (ABRE, [0.0, 0.0]),         # la recepcion vacia
    'r04': (CIERRA, [0.0, 0.0]),       # tres fuentes sobre la mesa
    'r05': (APENAS, [-0.03, 0.0]),     # Ivan y el telefono
    'r07': (CIERRA, [0.0, 0.02]),      # seis meses: el pulso sobre la hoja
    'r08': (CIERRA, [0.0, 0.0]),       # las cuentas de mas
    'r09': (ABRE, [0.04, 0.0]),        # la fachada vecina: solo un comentario
    'r10': (ABRE, [0.0, 0.0]),         # la orden en blanco
    'r11': (CIERRA, [0.0, 0.0]),       # la orden vigente, completa
    'r12': (CIERRA, [0.0, 0.02]),      # la hora real, escrita
    'r13': (APENAS, [0.03, 0.0]),      # el recepcionista entra
    'r14': (ABRE, [0.0, 0.0]),         # sin orden: el escritorio con una nota
    'r15': (ABRE, [0.05, 0.0]),        # el renglon que no termina
    'r16': (CIERRA, [0.0, 0.0]),       # el escrito denso
    'r17': (CIERRA, [0.0, 0.0]),       # las condiciones
    'r18': (APENAS, [0.0, 0.0]),       # dos casillas
    'r19': (APENAS, [0.0, 0.0]),       # Nora escucha
    'r20': (ABRE, [0.0, 0.0]),         # el estrado vacio
    'r21': (ABRE, [0.04, 0.0]),        # el microfono apartado
    'r22': (APENAS, [0.0, 0.0]),       # Ivan sentado
    'r23': (ABRE, [0.0, 0.0]),         # un solo sobre nuevo
    'r24': (APENAS, [0.0, 0.0]),       # las dos peticiones
    'r25': (APENAS, [-0.03, 0.0]),     # Lina de pie
    'r26': (ABRE, [0.0, 0.0]),         # una sola linea
    'r27': (CIERRA, [0.0, 0.0]),       # el sello sobre la hoja
    'r28': (APENAS, [0.0, 0.0]),       # dos entradas
    'r29': (ABRE, [0.0, 0.0]),         # la silla de la defensa
    'r30': (CIERRA, [0.0, 0.0]),       # el episodio detallado
    'r31': (APENAS, [0.03, 0.0]),      # las tres marcas
    'r32': (CIERRA, [0.0, 0.0]),       # dos pasajes nuevos
    'r33': (APENAS, [0.0, 0.02]),      # la direccion corregida
    'r34': (ABRE, [0.0, 0.0]),         # la pantalla de mensajeria
    'r35': (CIERRA, [0.0, 0.0]),       # las tres hojas aplanadas
    'r37': (CIERRA, [0.0, 0.0]),       # la carpeta sin indice
    'r39': (CIERRA, [0.0, 0.0]),       # las seis carpetas, separadas
}


def trabajos():
    largos = {i + 1: d for i, (_, d, _) in enumerate(R.RANURAS)}
    out = []
    for f in sorted(os.listdir(PLACAS)):
        if not f.endswith('.png'):
            continue
        clave = f[:3]
        n = largos[int(clave[1:])]
        emp, der = GESTO[clave]
        # al abrir, la ventana arranca mas cerrada para no pasarse de 1,0
        enc = 0.88 if emp >= 0 else 0.86
        out.append({'modo': 'camara', 'fuente': '%s/%s' % (PLACAS, f),
                    'salida': '%s/P3C4_%s_v%d.mp4' % (SALIDA, f[:-4], n),
                    'frames': n, 'encuadre': enc, 'empuje': emp,
                    'deriva': der, 'vibra': 5.0})
    return out


if __name__ == '__main__':
    t = trabajos()
    json.dump(t, open('camara_p3c4.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print('%d trabajos · %d cuadros en total'
          % (len(t), sum(x['frames'] for x in t)))
    ab = sum(1 for x in t if x['empuje'] < 0)
    ci = sum(1 for x in t if x['empuje'] > 0.05)
    print('abren %d · cierran %d · apenas %d' % (ab, ci, len(t) - ab - ci))
