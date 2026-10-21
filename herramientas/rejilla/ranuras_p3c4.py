#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La rejilla de ranuras del P3C4 «Puerto de salida».

CADA FRONTERA ES UN CORTE MEDIDO, Y ADEMAS ESTA FILTRADO
    Sale del `silencedetect` sobre el master de narracion. Pero aqui el crudo
    no sirve tal cual: la locucion tiene 70 pausas de 0,22 s o mas y 62 de
    0,35 s o mas. Montar una ranura por cada una daria 63 planos de 5,3 s de
    media -un corte cada cinco segundos durante seis minutos- y 6.300 creditos
    en placas.

    La seleccion se hace con dos reglas, las dos medidas:

    1. LAS FRONTERAS DE BLOQUE SON OBLIGATORIAS. Son 17 y ahi cambia el
       locutor. Una imagen montada encima de un cambio de voz esta mal
       montada, y el filtro por duracion se comia cuatro de ellas.
    2. EL RESTO SE VA CAYENDO POR LA PAUSA MAS CORTA PRIMERO, mientras la
       ranura que queda al unir no pase de 300 cuadros -12,5 s-. La pausa
       larga es la que el guion puso a proposito; la corta es una coma.

    Quedan 39 ranuras de 205 cuadros de media, que es exactamente la densidad
    del Caso 3 (203) en una pieza un minuto mas larga.

EL TOPE DE 300 NO ES ARBITRARIO: ES UN ACANTILADO
    Probado de 200 a 360. Entre 200 y 280 no se puede quitar NADA, porque el
    hueco natural mas largo ya mide 285 y la condicion falla para toda
    candidata. A 300 caen 23 de golpe y salen 39 ranuras; a 360, 30 ranuras de
    267 cuadros de media, y un plano de 267 cuadros donde no pasa nada se
    parte -eso ya esta escrito en CLAUDE.md-.

LA VELOCIDAD REAL DE ESTAS DOS VOCES
    726 palabras en 333,92 s de master = 130,5 ppm contando las pausas. La
    formula de la serie usa 137 y sobreestima un 5 %: la estimacion daba 6:07
    y la pieza mide 6:01. Para presupuestar los casos 5 y siguientes, 130 es
    el numero.

LA PIEZA
    intro 182 + entrada 119 + ranuras 8006 + respiro 48 + cierre 119 +
    outro 182 = 8.656 cuadros = 6:01,0 a 23,976.

LO QUE FALTA EN ESTA TABLA
    El reparto: que placa, que carton y que lower third va en cada ranura.
    Se llena cuando este decidido el repertorio, y ANTES de montar se corre
    `cruce.py` para comprobar, medido, que cada ranura lleva la imagen que
    corresponde a la frase que se oye encima.
"""
FPS = 24000 / 1001.0

INTRO = 182
ENTRADA = 119
RESPIRO = 48
CIERRE = 119
OUTRO = 182

T_RANURAS = INTRO + ENTRADA           # 301, donde empieza el bloque
N_RANURAS = 8006
FIN = T_RANURAS + N_RANURAS + RESPIRO + CIERRE + OUTRO

# (inicio relativo al bloque, cuadros, bloque de voz que se oye encima)
RANURAS = [
    (    0,  240, 'b01_apertura'),
    (  240,  180, 'b01_apertura'),
    (  420,  150, 'b01_apertura'),
    (  570,  146, 'b02_las_dos_lineas'),
    (  716,  244, 'b02_las_dos_lineas'),
    (  960,  209, 'b02_las_dos_lineas'),
    ( 1169,  285, 'b03_solicitud'),
    ( 1454,  260, 'b04_prop_cuentas'),
    ( 1714,  162, 'b05_prop_registro'),
    ( 1876,  234, 'b05_prop_registro'),
    ( 2110,  152, 'b06_captura_nora'),
    ( 2262,  208, 'b06_captura_nora'),
    ( 2470,  209, 'b07_recepcionista'),
    ( 2679,  167, 'b07_recepcionista'),
    ( 2846,  167, 'b08_prop_permanente'),
    ( 3013,  272, 'b09_medida_nora'),
    ( 3285,  257, 'b09_medida_nora'),
    ( 3542,  102, 'b09_medida_nora'),
    ( 3644,  152, 'b10_decision_jueza'),
    ( 3796,  237, 'b10_decision_jueza'),
    ( 4033,  131, 'b10_decision_jueza'),
    ( 4164,  215, 'b11_medida_ivan'),
    ( 4379,  300, 'b11_medida_ivan'),
    ( 4679,  294, 'b12_prop_no_se_oye'),
    ( 4973,  206, 'b13_imputacion_lina'),
    ( 5179,  232, 'b13_imputacion_lina'),
    ( 5411,  289, 'b13_imputacion_lina'),
    ( 5700,  285, 'b14_prop_silencio'),
    ( 5985,  118, 'b14_prop_silencio'),
    ( 6103,  285, 'b15_imputacion_ivan'),
    ( 6388,  113, 'b15_imputacion_ivan'),
    ( 6501,  161, 'b16_tres_modificaciones'),
    ( 6662,  189, 'b16_tres_modificaciones'),
    ( 6851,  241, 'b16_tres_modificaciones'),
    ( 7092,  109, 'b17_prop_precisiones'),
    ( 7201,  205, 'b17_prop_precisiones'),
    ( 7406,  145, 'b17_prop_precisiones'),
    ( 7551,  292, 'b18_cierre'),
    ( 7843,  163, 'b18_cierre'),
]


def revisar():
    """Integridad de la rejilla. No juzga el reparto, solo la aritmetica."""
    fallos = []
    if sum(d for _, d, _ in RANURAS) != N_RANURAS:
        fallos.append('las ranuras suman %d y el bloque es %d'
                      % (sum(d for _, d, _ in RANURAS), N_RANURAS))
    for i in range(len(RANURAS) - 1):
        if RANURAS[i][0] + RANURAS[i][1] != RANURAS[i + 1][0]:
            fallos.append('hueco o solape entre la %d y la %d' % (i + 1, i + 2))
    if RANURAS[0][0] != 0:
        fallos.append('la primera ranura no empieza en 0')
    corta = [i + 1 for i, (_, d, _) in enumerate(RANURAS) if d < 96]
    if corta:
        fallos.append('ranuras por debajo del piso de lectura: %s' % corta)
    larga = [i + 1 for i, (_, d, _) in enumerate(RANURAS) if d > 300]
    if larga:
        fallos.append('ranuras por encima del tope de 300: %s' % larga)
    return fallos


if __name__ == '__main__':
    print('%3s %7s %7s %6s %7s  %s'
          % ('#', 'ini', 'fin', 'dur', 'seg', 'bloque'))
    for i, (a, d, b) in enumerate(RANURAS, 1):
        print('%3d %7d %7d %6d %7.1f  %s' % (i, a, a + d, d, d / FPS, b))
    n = len(RANURAS)
    tot = sum(d for _, d, _ in RANURAS)
    print()
    print('%d ranuras - %d cuadros - media %.0f (%.1f s)'
          % (n, tot, tot / n, tot / n / FPS))
    print('pieza %d cuadros = %d:%04.1f'
          % (FIN, int(FIN / FPS) // 60, (FIN / FPS) % 60))
    f = revisar()
    print('REVISION:', 'sin fallos' if not f else '')
    for x in f:
        print('   ', x)
