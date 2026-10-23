#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""El horneado de camara del P3C5 v2, y cuales ranuras NO se hornean.

CINCO GENERADAS, Y SON LAS CINCO CON ACCION REAL
    r04  la calle de Medellin: la gente pasa, el edificio no.
    r12  Andres se detiene en la puerta abierta y mira adentro.
    r13  el telefono pasa de una mano a la otra. Es el beat del bloque.
    r19  la pluma se queda suspendida sobre el blanco y NO baja.
    r42  levanta un grupo de hojas y lo deja aparte.

    Las otras 38 son placa sostenida con la camara horneada.

POR QUE r27 NO SE GENERA AUNQUE LO PIDA
    r27 y r28 son Lucia con la anotacion y sin ella: el mismo encuadre, la
    misma silla, la misma pared, y lo UNICO que cambia tiene que ser las
    manos y la mirada. Si una mitad se mueve de verdad y la otra no, el
    espectador ve el procedimiento y no el caso. Es la misma regla que dejo
    a r39 del Caso 4 fuera del movimiento.

LAS TRES RIMAS LLEVAN EL MISMO EMPUJE
    r01 / r43   las dos bandejas, lo ofrecido y lo admitido.
    r33 / r35   LA RIMA MAYOR, las dos mesas del resultado.
    r27 / r28   Lucia con la hoja y sin ella.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, r'D:\DAE\_repo\herramientas\prompts')

PLACAS = os.environ.get(
    'P3C5_PLACAS',
    r'E:\DAE MASTER\PRIORIDAD 03\CASO 05 - Voces, registros y cuentas\01 PLANOS v2\_grade')
SALIDA = os.environ.get(
    'P3C5_RANURAS',
    r'E:\DAE MASTER\PRIORIDAD 03\CASO 05 - Voces, registros y cuentas\10 TIMELINE SEBASTIAN\RANURAS v2')

ABRE = -0.085
CIERRA = 0.070
APENAS = 0.022

GENERADAS = {4, 12, 13, 19, 42}

GESTO = {
 1:  (ABRE,   [0.0, 0.0]),    # las dos bandejas vacias      · rima con 43
 2:  (ABRE,   [0.0, 0.0]),    # la sala entera, sin nadie
 3:  (APENAS, [0.03, 0.0]),   # Oscar en el corredor
 5:  (APENAS, [-0.03, 0.0]),  # Tomas contra la pared
 6:  (ABRE,   [0.0, 0.0]),    # tres carpetas con aire entre ellas
 7:  (ABRE,   [0.0, 0.0]),    # la silla que falta en la fila
 8:  (CIERRA, [0.0, 0.0]),    # la caja que no cierra
 9:  (CIERRA, [0.0, 0.02]),   # los anexos, sin separar
 10: (ABRE,   [0.0, 0.0]),    # el despacho entero, una persona
 11: (CIERRA, [0.0, 0.0]),    # la banda, de muy cerca
 14: (APENAS, [0.0, 0.0]),    # el cuaderno en la ventana
 15: (CIERRA, [0.0, 0.02]),   # la pagina, densa
 16: (APENAS, [-0.03, 0.0]),  # la fiscal sustentando
 17: (ABRE,   [0.0, 0.0]),    # el cuaderno solo en la mesa enorme
 18: (ABRE,   [0.0, 0.0]),    # una sola linea y el resto en blanco
 20: (ABRE,   [0.0, 0.0]),    # la sala de escucha vacia
 21: (APENAS, [0.0, 0.0]),    # Lucia y la onda que reconoce
 22: (APENAS, [0.0, 0.0]),    # la onda sin nadie, la silla vacia
 23: (APENAS, [0.0, 0.0]),    # Renata en la pantalla
 24: (CIERRA, [0.0, 0.0]),    # la carpeta puesta delante
 25: (ABRE,   [0.0, 0.0]),    # el atril vacio a contraluz
 26: (CIERRA, [0.0, 0.0]),    # la grafica, todo junto
 27: (APENAS, [0.0, 0.0]),    # Lucia con la anotacion    · rima con 28
 28: (APENAS, [0.0, 0.0]),    # Lucia sin la hoja         · rima con 27
 29: (APENAS, [0.0, 0.0]),    # Lucia, primer plano
 30: (APENAS, [0.03, 0.0]),   # el defensor preguntando
 31: (ABRE,   [0.0, 0.0]),    # la puerta abierta, nadie
 32: (APENAS, [0.0, 0.0]),    # Oscar, primer plano
 33: (APENAS, [0.0, 0.0]),    # LA MESA DE OSCAR          · rima mayor con 35
 34: (ABRE,   [0.0, 0.0]),    # el acta apartada
 35: (APENAS, [0.0, 0.0]),    # LA MESA DE TOMAS          · rima mayor con 33
 36: (APENAS, [0.0, 0.0]),    # Tomas, primer plano
 37: (ABRE,   [0.0, 0.0]),    # Tomas solo en toda la fila
 38: (APENAS, [0.0, 0.0]),    # la fiscal en el alegato
 39: (CIERRA, [0.0, 0.0]),    # cuatro carpetas iguales
 40: (ABRE,   [0.0, 0.0]),    # el sitio de la cuarta, vacio
 41: (ABRE,   [0.0, 0.0]),    # la llave y el dinero, con aire
 43: (ABRE,   [0.0, 0.0]),    # las bandejas desiguales   · rima con 1
}


def trabajos(largos, nombres):
    out = []
    for n in sorted(GESTO):
        f = nombres[n]
        emp, der = GESTO[n]
        enc = 0.88 if emp >= 0 else 0.86
        out.append({'modo': 'camara',
                    'fuente': os.path.join(PLACAS, f),
                    'salida': os.path.join(SALIDA, '%s_v%d.mp4' % (f[:-4], largos[n])),
                    'frames': largos[n], 'encuadre': enc, 'empuje': emp,
                    'deriva': der, 'vibra': 5.0})
    return out


if __name__ == '__main__':
    from escenas_p3c5_v2 import R, RIMAS
    import armar_p3c5_v2 as armar
    largos = {n: v[0] for n, v in R.items()}
    nombres = {n: 'P3C5_r%02d_%s.png' % (n, armar.NOMBRE[n]) for n in R}
    faltan = set(R) - set(GESTO) - GENERADAS
    sobran = set(GESTO) & GENERADAS
    assert not faltan, 'sin empuje: %s' % sorted(faltan)
    assert not sobran, 'generadas y horneadas a la vez: %s' % sorted(sobran)
    os.makedirs(SALIDA, exist_ok=True)
    t = trabajos(largos, nombres)
    json.dump(t, open(sys.argv[1] if len(sys.argv) > 1 else 'camara_p3c5_v2.json',
                      'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    ab = sum(1 for x in t if x['empuje'] < 0)
    ci = sum(1 for x in t if x['empuje'] > 0.05)
    print('%d horneadas · %d generadas · %d ranuras'
          % (len(t), len(GENERADAS), len(t) + len(GENERADAS)))
    print('abren %d · cierran %d · apenas %d' % (ab, ci, len(t) - ab - ci))
    print('cuadros horneados %d · generados %d · total %d'
          % (sum(x['frames'] for x in t), sum(largos[n] for n in GENERADAS),
             sum(largos.values())))
    for a, b in RIMAS:
        ga = GESTO.get(a, ('GENERADA',))[0]
        gb = GESTO.get(b, ('GENERADA',))[0]
        print('   rima r%02d/r%02d: %s' % (a, b,
              'mismo empuje' if ga == gb else 'DISTINTO (%s vs %s)' % (ga, gb)))
