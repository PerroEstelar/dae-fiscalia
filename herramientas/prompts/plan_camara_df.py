#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""El horneado de camara del curso de Desaparicion Forzada.

TODO SE HORNEA, Y EL MOVIMIENTO GENERADO VA ENCIMA EN OTRA PISTA
    En el P3 unas ranuras se horneaban y otras se generaban, y en la linea
    ocupaban el mismo sitio. Aqui no: las 57 ranuras se hornean -placa
    sostenida con empuje, que no cuesta creditos y nunca se deforma- y el
    movimiento generado se monta ENCIMA, en su propia pista, para que
    Sebastian lo prenda y lo apague con un clic.

    O sea que si un clip generado sale mal, apagar la pista deja la pieza
    entera en pie. Es la primera vez que el movimiento no es un riesgo.

LOS TRES EMPUJES SON LOS DE LA SERIE
    ABRE    -0,085   el plano se abre: sitio, aire, respiro
    CIERRA  +0,070   el plano se cierra: el dato, el objeto, la frase
    APENAS  +0,022   una cara o una figura quieta, casi nada
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ABRE = -0.085
CIERRA = 0.070
APENAS = 0.022

RAIZ = ('E:/DAE MASTER/PRIORIDAD 03/CURSO - INVESTIGACION JUDICIAL Y FORENSE '
        'DE LA DESAPARICION FORZADA/UNIDAD DESAPARICION FORZADA/'
        'CASO MIRIAM Y MARIANA')
CAPS = {1: 'CAPITULO 1 - EL ECO EN LA PLAZA Y LA RESPUESTA DE PAPEL',
        2: 'CAPITULO 2 - RELOJES EN PAUSA Y EL CLAMOR EN LAS REDES',
        3: 'CAPITULO 3 - EL ENGRANAJE ROTO Y EL MAPA DE COMPETENCIAS',
        4: 'CAPITULO 4 - LAS VOCES QUE NO SE APAGAN Y EL DOLOR EN LA VENTANILLA',
        5: 'CAPITULO 5 - LA TIERRA HABLA Y LA MATRIZ DEL SILENCIO'}

#  ranura -> (empuje, [deriva_x, deriva_y])
GESTO = {}

GESTO[1] = {
 1:  (ABRE,   [0.0, 0.0]),    # la plaza al abrir
 2:  (APENAS, [0.03, 0.0]),   # Miriam en su puesto
 3:  (ABRE,   [0.0, 0.0]),    # la casa con la puerta cerrada
 4:  (CIERRA, [0.0, 0.02]),   # el monedero vacio
 5:  (APENAS, [-0.03, 0.0]),  # Miriam, primer plano
 6:  (CIERRA, [0.0, 0.0]),    # las tres siluetas
 7:  (APENAS, [0.0, 0.0]),    # desde dentro del puesto
 8:  (CIERRA, [0.0, 0.02]),   # la caja vacia
 9:  (ABRE,   [0.0, 0.0]),    # el potrero vacio
 10: (ABRE,   [0.0, 0.0]),    # el camino de vuelta
 11: (APENAS, [0.03, 0.0]),   # Gregoria y el televisor
 12: (ABRE,   [0.0, 0.0]),    # la cuadra de noche
 13: (ABRE,   [0.0, 0.0]),    # EL PUESTO CERRADO · el plano que carga
 14: (CIERRA, [0.0, 0.02]),   # la minuta
 15: (APENAS, [0.0, 0.0]),    # la ventanilla vacia
 16: (ABRE,   [0.0, 0.0]),    # los tres puestos
}


GESTO[2] = {
 1:  (APENAS, [0.03, 0.0]),   # Rosa Elena en el patio
 2:  (APENAS, [-0.03, 0.0]),  # Mariana en la puerta
 3:  (ABRE,   [0.0, 0.0]),    # la marcha por la calle
 4:  (CIERRA, [0.0, 0.02]),   # el cartel en el poste
 5:  (ABRE,   [0.0, 0.0]),    # la subestacion
 6:  (CIERRA, [0.0, 0.02]),   # EL TELEFONO EN EL PISO - el plano que carga
 7:  (CIERRA, [0.0, 0.0]),    # Rosa Elena entra al corredor
 8:  (APENAS, [0.03, 0.0]),   # la fiscal recibe
 9:  (CIERRA, [0.0, 0.02]),   # los dos formatos
 10: (ABRE,   [0.0, 0.0]),    # la sala de trabajo
 11: (CIERRA, [0.0, 0.0]),    # el mapa en pantalla
}

GESTO[3] = {
 1:  (ABRE,   [0.0, 0.0]),    # el despacho
 2:  (APENAS, [0.0, 0.0]),    # los dos escritorios de espaldas
 3:  (APENAS, [0.03, 0.0]),   # la caja por el pasillo
 4:  (CIERRA, [0.0, 0.02]),   # la caja en el piso
 5:  (APENAS, [0.0, 0.0]),    # la fiscal en la puerta
 6:  (ABRE,   [0.0, 0.0]),    # la mesa de cinco
 7:  (CIERRA, [0.0, 0.02]),   # tres carpetas, cenital
 8:  (CIERRA, [0.0, 0.02]),   # el mismo documento
 9:  (CIERRA, [0.0, 0.02]),   # dos carpetas
}

GESTO[4] = {
 1:  (ABRE,   [0.0, 0.0]),    # el pasillo de sillas vacias
 2:  (APENAS, [0.03, 0.0]),   # la ventanilla
 3:  (APENAS, [-0.03, 0.0]),  # Rosa Elena, primer plano
 4:  (APENAS, [0.0, 0.0]),    # la fiscal de pie
 5:  (ABRE,   [0.0, 0.0]),    # la sala de atencion, vacia
 6:  (APENAS, [0.0, 0.0]),    # la psicologa al lado
 7:  (CIERRA, [0.0, 0.02]),   # las manos con guantes
 8:  (CIERRA, [0.0, 0.02]),   # LA ENTREVISTA - suelta la carpeta
}

GESTO[5] = {
 1:  (ABRE,   [0.0, 0.0]),    # tres mesas de trabajo
 2:  (CIERRA, [0.0, 0.02]),   # dos documentos cruzados
 3:  (ABRE,   [0.0, 0.0]),    # el camino de noche
 4:  (CIERRA, [0.0, 0.02]),   # el georradar
 5:  (ABRE,   [0.0, 0.0]),    # la cuadricula
 6:  (CIERRA, [0.0, 0.02]),   # las manos en la tierra
 7:  (CIERRA, [0.0, 0.02]),   # la bandeja
 8:  (APENAS, [0.03, 0.0]),   # el perito
 9:  (CIERRA, [0.0, 0.0]),    # la pantalla del laboratorio
 10: (APENAS, [-0.03, 0.0]),  # el analista y el tablero
 11: (CIERRA, [0.0, 0.0]),    # el tablero
 12: (ABRE,   [0.0, 0.0]),    # el predio al atardecer
 13: (CIERRA, [0.0, 0.02]),   # EL DOCUMENTO CERRADO - el ultimo plano
}


def trabajos(cap, nombres, largos, desde_grade=True):
    """Devuelve la lista de trabajos de `camara.render` para un capitulo."""
    base = os.path.join(RAIZ, CAPS[cap])
    pl = os.path.join(base, '01 PLANOS', '_grade' if desde_grade else '')
    sal = os.path.join(base, '10 TIMELINE SEBASTIAN', 'RANURAS')
    os.makedirs(sal, exist_ok=True)
    out = []
    for n in sorted(GESTO[cap]):
        f = nombres[n]
        emp, der = GESTO[cap][n]
        out.append({'modo': 'camara',
                    'fuente': os.path.join(pl, f),
                    'salida': os.path.join(sal, '%s_v%d.mp4' % (f[:-4], largos[n])),
                    'frames': largos[n],
                    'encuadre': 0.88 if emp >= 0 else 0.86,
                    'empuje': emp, 'deriva': der, 'vibra': 5.0})
    return out
