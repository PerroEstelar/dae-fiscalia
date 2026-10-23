#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""El horneado de camara del P3C4 v2, y cuales ranuras NO se hornean.

EL MOVIMIENTO VA AL SERVICIO DEL KEYFRAME
    Cinco ranuras llevan video generado porque tienen ACCION REAL -alguien
    que se gira y entra, alguien que sube a una camioneta, alguien que llega
    a trabajar, alguien que cierra una carpeta a la fuerza, alguien que se
    aleja por un corredor-. Las otras treinta y cuatro son placa sostenida
    con la camara horneada, que es buena, es estable y no cuesta un credito.

    Es la proporcion de la casa -la serie SRPA generaba 6 de 67- y es lo
    contrario de lo que hacia el Caso 05 del curso TA, donde las 33 ranuras
    eran video generado y nueve salieron rotas.

EL EMPUJE SIGUE DICIENDO ALGO
    ABRE   donde hay FALTA: el sitio vacio, la calle sin nadie, la sala sin
           nadie en el estrado, el corredor sin nadie, la puerta cerrada. La
           ventana se ensancha y el vacio alrededor del unico dato CRECE.
    CIERRA donde hay ACUMULACION: la caja de archivadores, la carpeta
           rebosada, los cuatro puestos, la hoja con dos entradas.
    APENAS sobre las caras y los planos de transito. Un empuje sobre una
           cara se lee como enfasis dramatico y esta serie no enfatiza.

LA RIMA MANDA SOBRE EL SIGNIFICADO
    r01 y r39 son la misma fachada a dos horas. Llevan el MISMO empuje, y
    por eso r39 tampoco se genera aunque tenga gente caminando: si una mitad
    de la rima se mueve de verdad y la otra no, la diferencia que el
    espectador ve ya no es la hora, es el procedimiento.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, r'D:\DAE\_repo\herramientas\prompts')

PLACAS = os.environ.get(
    'P3C4_PLACAS',
    r'E:\DAE MASTER\PRIORIDAD 03\CASO 04 - Puerto de salida\01 PLANOS v2\_grade')
SALIDA = os.environ.get(
    'P3C4_RANURAS',
    r'E:\DAE MASTER\PRIORIDAD 03\CASO 04 - Puerto de salida\10 TIMELINE SEBASTIAN\RANURAS v2')

ABRE = -0.085
CIERRA = 0.070
APENAS = 0.022

# las cinco que llevan video generado, y no se hornean
GENERADAS = {2, 6, 13, 36, 38}

GESTO = {
 1:  (ABRE,   [0.0, 0.0]),    # la fachada al amanecer, vacia   · rima con 39
 3:  (APENAS, [0.03, 0.0]),   # Nora, primer plano
 4:  (CIERRA, [0.0, 0.02]),   # el telefono en el tablero
 5:  (ABRE,   [0.02, 0.0]),   # EL MUELLE. el vacio alrededor del unico hombre
 7:  (ABRE,   [0.0, 0.0]),    # media oficina vacia a las siete
 8:  (CIERRA, [0.0, 0.0]),    # la caja de archivadores, desbordada
 9:  (ABRE,   [0.0, 0.0]),    # el segundo inmueble, sin nada que lo conecte
 10: (CIERRA, [0.03, 0.0]),   # el porton cerrado, de cerca
 11: (ABRE,   [0.0, 0.0]),    # la banca larga y una sola persona en ella
 12: (APENAS, [0.0, -0.02]),  # el reloj
 14: (ABRE,   [0.0, 0.0]),    # el vestibulo entero y una persona
 15: (ABRE,   [0.0, 0.0]),    # el corredor sin nadie
 16: (ABRE,   [0.0, 0.0]),    # la sala desde atras, el estrado vacio
 17: (APENAS, [-0.03, 0.0]),  # el fiscal al atril
 18: (ABRE,   [0.0, 0.0]),    # la silla, y el cardigan encima
 19: (APENAS, [0.0, 0.0]),    # la jueza, primer plano
 20: (ABRE,   [0.0, 0.0]),    # el estrado vacio a contraluz
 21: (ABRE,   [0.0, 0.0]),    # la puerta de la casa, cerrada
 22: (APENAS, [0.03, 0.0]),   # Ivan en la banca
 23: (ABRE,   [0.0, 0.0]),    # el corredor entero entre los dos
 24: (CIERRA, [0.0, 0.0]),    # la cartera cerrada, de cerca
 25: (APENAS, [0.0, 0.0]),    # Lina, primer plano
 26: (ABRE,   [0.0, 0.0]),    # Lina de pie, y el margen vacio alrededor
 27: (ABRE,   [0.0, 0.0]),    # la sala pequena entera
 28: (APENAS, [0.03, 0.0]),   # la otra fiscal levantando la carpeta
 29: (CIERRA, [0.0, 0.0]),    # las dos entradas en una hoja
 30: (APENAS, [0.0, 0.0]),    # el muelle de dia
 31: (CIERRA, [0.0, 0.0]),    # los cuatro puestos
 32: (ABRE,   [0.0, 0.0]),    # la sala de trabajo, y la distancia entre dos
 33: (CIERRA, [0.0, 0.02]),   # la direccion tachada
 34: (APENAS, [0.0, 0.0]),    # la otra fiscal, primer plano
 35: (CIERRA, [0.0, 0.0]),    # la carpeta unica, rebosada
 37: (ABRE,   [0.0, 0.0]),    # la sala vacia, la lampara encendida
 39: (ABRE,   [0.0, 0.0]),    # la misma fachada al final del dia · rima con 1
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
    from escenas_p3c4_v2 import R
    import armar
    largos = {n: v[0] for n, v in R.items()}
    nombres = {n: 'P3C4_r%02d_%s.png' % (n, armar.NOMBRE[n]) for n in R}
    faltan = set(R) - set(GESTO) - GENERADAS
    sobran = set(GESTO) & GENERADAS
    assert not faltan, 'sin empuje: %s' % sorted(faltan)
    assert not sobran, 'generadas y horneadas a la vez: %s' % sorted(sobran)
    os.makedirs(SALIDA, exist_ok=True)
    t = trabajos(largos, nombres)
    destino = sys.argv[1] if len(sys.argv) > 1 else 'camara_p3c4_v2.json'
    json.dump(t, open(destino, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    ab = sum(1 for x in t if x['empuje'] < 0)
    ci = sum(1 for x in t if x['empuje'] > 0.05)
    print('%d horneadas · %d generadas · %d ranuras'
          % (len(t), len(GENERADAS), len(t) + len(GENERADAS)))
    print('abren %d · cierran %d · apenas %d' % (ab, ci, len(t) - ab - ci))
    print('cuadros horneados %d · generados %d · total %d'
          % (sum(x['frames'] for x in t),
             sum(largos[n] for n in GENERADAS), sum(largos.values())))
    e1, e39 = GESTO[1][0], GESTO[39][0]
    print('la rima r01/r39:', 'mismo empuje'
          if e1 == e39 else 'DISTINTO EMPUJE, la rima se rompe')
