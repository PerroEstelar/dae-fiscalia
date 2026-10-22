#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""El horneado de camara de las 43 placas del Caso 5.

EL MOVIMIENTO DICE ALGO, O NO SE PONE
    Igual que en el Caso 4: en una pieza de seis minutos sostenida sobre
    placas fijas, la direccion del empuje es lo unico que la imagen puede
    hacer por si sola. Va asignado por lo que la placa SIGNIFICA.

    ABRE   las placas de FALTA -el cuaderno solo en una mesa enorme, la mitad
           de la hoja en blanco, el renglon sin nombre, la silla vacia al lado
           de la onda, el sitio de la cuarta-. La ventana se ensancha mientras
           el plano dura, asi que el vacio alrededor del unico dato CRECE.

    CIERRA las placas de ACUMULACION -el bloque unico con su banda, el rollo
           sin cortar, la transcripcion entera, los cuatro informes iguales,
           la pagina que mezcla dos cosas-. La ventana se cierra y el cuadro
           se llena.

    APENAS las ocho con rostro y las de transito. Un empuje sobre una cara se
           lee como enfasis dramatico y esta serie no enfatiza: expone.

LAS RIMAS LLEVAN EL MISMO EMPUJE, Y ESO MANDA SOBRE EL SIGNIFICADO
    Es la regla que el Caso 4 dejo escrita para r01 y r39. Si las dos mitades
    de una rima llevan camaras distintas, la diferencia que el espectador ve
    ya no es la del caso: es la del movimiento.

    r33 / r35   LA RIMA MAYOR. Por significado r33 pediria CIERRA -cuatro
                cosas llenando la mesa- y r35 pediria ABRE -dos cosas y una
                extension vacia-. Van las dos en APENAS. La camara se queda
                casi quieta en las dos y la UNICA diferencia entre los dos
                planos es lo que hay sobre la mesa, que es exactamente el
                resultado de la practica probatoria. Mover la camara aqui
                seria que el video opine sobre lo que ya dice la mesa.
    r01 / r43   las bandejas. ABRE en las dos: al abrir crece el vacio de las
                dos bandejas iguales, y al cerrar el mismo movimiento descubre
                que ya no son iguales.
    r21 / r22   la onda con Lucia y sin nadie. APENAS en las dos.
    r27 / r28   Lucia con la anotacion y sin ella. APENAS en las dos.

    r12 y r13 tambien son un par, pero no comparten encuadre -una es cenital
    de una pagina y la otra un plano de manos en un corredor-, asi que no es
    una rima de camara y cada una lleva el empuje que le toca.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

PLACAS = os.environ.get(
    'P3C5_PLACAS',
    r'E:\DAE MASTER\PRIORIDAD 03\CASO 05 - Voces, registros y cuentas\01 PLANOS\_grade')
SALIDA = os.environ.get(
    'P3C5_RANURAS',
    r'E:\DAE MASTER\PRIORIDAD 03\CASO 05 - Voces, registros y cuentas\10 TIMELINE SEBASTIAN\RANURAS')
REJILLA = os.environ.get(
    'P3C5_REJILLA',
    r'E:\DAE MASTER\PRIORIDAD 03\CASO 05 - Voces, registros y cuentas\06 AUDIO\P3C5_rejilla.json')

ABRE = -0.085      # la ventana se ensancha: crece el aire
CIERRA = 0.070     # la ventana se cierra: se llena el cuadro
APENAS = 0.022

GESTO = {
    'r01': (ABRE,   [0.0, 0.0]),    # dos bandejas vacias   · rima con r43
    'r02': (ABRE,   [0.03, 0.0]),   # lo que se ofrece, y la mesa vacia detras
    'r03': (APENAS, [0.03, 0.0]),   # Oscar de pie
    'r04': (ABRE,   [0.0, 0.0]),    # el corredor sin nadie
    'r05': (APENAS, [-0.03, 0.0]),  # Tomas sentado
    'r06': (CIERRA, [0.0, 0.0]),    # los tres bloques, separados
    'r07': (ABRE,   [0.0, 0.03]),   # la mitad de abajo en blanco
    'r08': (CIERRA, [0.0, 0.0]),    # el bloque unico con su banda
    'r09': (CIERRA, [0.0, 0.0]),    # los anexos, todos en la misma pila
    'r10': (CIERRA, [0.0, 0.0]),    # las dos copias, una por lado
    'r11': (CIERRA, [0.0, 0.0]),    # la banda, de cerca
    'r12': (CIERRA, [0.0, 0.02]),   # la pagina que mezcla dos cosas
    'r13': (APENAS, [0.03, 0.0]),   # el telefono pasando de manos
    'r14': (APENAS, [0.0, 0.0]),    # el cuaderno en su sitio
    'r15': (CIERRA, [0.0, 0.02]),   # la pagina del cuaderno, densa
    'r16': (APENAS, [0.0, 0.0]),    # levantar el cuaderno
    'r17': (ABRE,   [0.0, 0.0]),    # el cuaderno solo en la mesa enorme
    'r18': (ABRE,   [0.0, 0.0]),    # una linea y el resto en blanco
    'r19': (ABRE,   [0.0, 0.03]),   # la pluma sobre el blanco
    'r20': (CIERRA, [0.04, 0.0]),   # el rollo sin cortar
    'r21': (APENAS, [0.0, 0.0]),    # la onda, con Lucia   · rima con r22
    'r22': (APENAS, [0.0, 0.0]),    # la onda, sin nadie   · rima con r21
    'r23': (APENAS, [0.0, 0.0]),    # Renata en la pantalla
    'r24': (CIERRA, [0.0, 0.0]),    # la carpeta puesta delante
    'r25': (CIERRA, [0.0, 0.0]),    # los dos patrones iguales
    'r26': (CIERRA, [0.0, 0.0]),    # los flujos, todos iguales
    'r27': (APENAS, [0.0, 0.0]),    # Lucia con la anotacion · rima con r28
    'r28': (APENAS, [0.0, 0.0]),    # Lucia sin la hoja      · rima con r27
    'r29': (CIERRA, [0.0, 0.0]),    # la transcripcion entera
    'r30': (ABRE,   [0.0, 0.0]),    # las dos cosas, con aire entre ellas
    'r31': (ABRE,   [0.0, 0.0]),    # la puerta abierta
    'r32': (APENAS, [0.0, 0.0]),    # Oscar sentado
    'r33': (APENAS, [0.0, 0.0]),    # LA MESA DE OSCAR  · rima mayor con r35
    'r34': (ABRE,   [0.0, 0.0]),    # el acta, apartada
    'r35': (APENAS, [0.0, 0.0]),    # LA MESA DE TOMAS  · rima mayor con r33
    'r36': (ABRE,   [0.0, 0.0]),    # el renglon en blanco
    'r37': (ABRE,   [0.0, 0.0]),    # la mano sobre el blanco
    'r38': (CIERRA, [0.0, 0.0]),    # las tres hojas
    'r39': (CIERRA, [0.0, 0.0]),    # los cuatro informes iguales
    'r40': (ABRE,   [0.0, 0.0]),    # el sitio de la cuarta, vacio
    'r41': (APENAS, [0.0, 0.0]),    # la puerta y el pago, lado a lado
    'r42': (CIERRA, [0.0, 0.0]),    # empezar a separar
    'r43': (ABRE,   [0.0, 0.0]),    # las bandejas desiguales · rima con r01
}


def trabajos():
    rej = json.load(open(REJILLA, encoding='utf-8'))['ranuras']
    largos = {i + 1: r['dur'] for i, r in enumerate(rej)}
    out = []
    for f in sorted(os.listdir(PLACAS)):
        if not f.endswith('.png'):
            continue
        clave = f.split('_')[1]                 # P3C5_r07_nombre.png -> r07
        n = largos[int(clave[1:])]
        emp, der = GESTO[clave]
        # al abrir, la ventana arranca mas cerrada para no pasarse de 1,0
        enc = 0.88 if emp >= 0 else 0.86
        out.append({'modo': 'camara',
                    'fuente': os.path.join(PLACAS, f),
                    'salida': os.path.join(SALIDA, '%s_v%d.mp4' % (f[:-4], n)),
                    'frames': n, 'encuadre': enc, 'empuje': emp,
                    'deriva': der, 'vibra': 5.0})
    return out


if __name__ == '__main__':
    os.makedirs(SALIDA, exist_ok=True)
    t = trabajos()
    destino = sys.argv[1] if len(sys.argv) > 1 else 'camara_p3c5.json'
    json.dump(t, open(destino, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('%d trabajos · %d cuadros en total'
          % (len(t), sum(x['frames'] for x in t)))
    ab = sum(1 for x in t if x['empuje'] < 0)
    ci = sum(1 for x in t if x['empuje'] > 0.05)
    print('abren %d · cierran %d · apenas %d' % (ab, ci, len(t) - ab - ci))
    for a, b, q in (('r33','r35','la rima mayor'), ('r01','r43','las bandejas'),
                    ('r21','r22','la onda'), ('r27','r28','Lucia')):
        ea, eb = GESTO[a][0], GESTO[b][0]
        print('   %-16s %s y %s: %s' % (q, a, b,
              'mismo empuje' if ea == eb else 'DISTINTO EMPUJE, la rima se rompe'))
