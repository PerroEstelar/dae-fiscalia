#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La rejilla de ranuras del P3C3 «Ruta del Golfo».

Cada frontera es un CORTE MEDIDO: sale del `silencedetect` sobre el master de
narración, nunca de una división aritmética. La lista `CORTES` de abajo son los
puntos medios de los 41 silencios de 0,35 s o más que tiene la locución.

LAS TRES PROPUESTAS TIENEN RANURA PROPIA Y LARGA
    Son el material didáctico del caso y hay que poder leerlas. Por eso las
    pausas de la narración se diseñaron para dejarles sitio: 6 s después de
    b4, 4 s después de b6 y 5 s después de b9. La primera lleva tres
    peticiones y se lleva 243 cuadros; el precedente del Caso 2 era 213
    cuadros para una propuesta de una sola frase.

QUE VA EN CADA PISTA
    V1 placa o cama · V2 el clip de movimiento, que cubre la ranura entera y
    se puede apagar · V3 cartón teñido o de narración · V7 lower third.
"""
import json
import sys

# puntos medios de los silencios medidos
CORTES = [61, 202, 351, 445, 613, 916, 1094, 1207, 1261, 1439, 1608, 1826,
          2049, 2115, 2306, 2430, 2704, 2932, 3142, 3375, 3476, 3586, 3646,
          3843, 3947, 4063, 4213, 4478, 4648, 4830, 5004, 5126, 5209, 5283,
          5393, 5594, 5770, 5863, 5947, 5992, 6090]

# los cortes de las tres ranuras de propuesta no van al medio del silencio sino
# justo antes de que vuelva la voz, para ganarle segundos de lectura al carton
CORTES_CARTON = [1676, 2475, 4120]

N_NARRACION = 6100

# (corte_final, plano, clase, bloque, que lleva encima)
#   clase: placa | cama | grafica
RANURAS = [
    (202,  'cama_calle_medellin',       'cama',    'b1_apertura',       'ae01_progresiva'),
    (445,  'kf01_terminal_vehiculo',    'placa',   'b1_apertura',       'lt01_fecha_lugar'),
    (613,  'graf_la_ruta',              'grafica', 'b2_los_cuatro',     None),
    (916,  'kf02_los_cuatro_espaldas',  'placa',   'b2_los_cuatro',     None),
    (1094, 'kf03_luis_computador',      'placa',   'b2_los_cuatro',     'lt02_luis'),
    (1261, 'kf04_marta_giros',          'placa',   'b2_los_cuatro',     'lt03_marta'),
    (1439, 'cama_sello_sin_fecha',      'cama',    'b3_capturas',       'ae02_no_identificada'),
    (1676, 'cama_mesa_equipo',          'cama',    'b4_propuesta_uno',  'prop1_tres_peticiones'),
    (1826, 'kf05_omar_volante',         'placa',   'b5_teresa',         'lt04_omar'),
    (2049, 'kf06_teresa_cocina',        'placa',   'b5_teresa',         'lt05_teresa'),
    (2306, 'cama_tienda_esquina',       'cama',    'b5_teresa',         'ae03_podian_salir'),
    (2475, 'cama_informe_esfero',       'cama',    'b6_sin_esclarecer', 'prop2_agregar_trata'),
    (2704, 'kf07_certificado_empleo',   'placa',   'b7_la_visa',        None),
    (2932, 'cama_visado',               'cama',    'b7_la_visa',        'ae04_materialmente'),
    (3142, 'kf08_nidia_local',          'placa',   'b8_nidia',          'lt06_nidia'),
    (3375, 'kf09_pasaportes_recibos',   'placa',   'b8_nidia',          None),
    (3476, 'cama_cajon',                'cama',    'b8_nidia',          'ae05_sin_relacion'),
    (3646, 'kf10_puesto_control',       'placa',   'b9_migracion',      None),
    (3843, 'kf11_informe_dos_meses',    'placa',   'b9_migracion',      None),
    (3947, 'kf12_viajero_documento',    'placa',   'b9_migracion',      None),
    (4120, 'cama_sala_reunion',         'cama',    'b9_migracion',      'prop3_ignorar'),
    (4478, 'graf_antes_y_despues',      'grafica', 'b10_evaluacion',    None),
    (4648, 'kf13_marta_lejos',          'placa',   'b10_evaluacion',    None),
    (4830, 'kf14_orden_servicio',       'placa',   'b11_omar',          None),
    (5004, 'cama_telefono_omar',        'cama',    'b11_omar',          'ae06_no_atribuido'),
    (5209, 'kf15_conversacion_pantalla','placa',   'b12_conversacion',  None),
    (5393, 'cama_pantalla',             'cama',    'b12_conversacion',  'ae07_si_describen'),
    (5594, 'kf16_cuaderno_teresa',      'placa',   'b13_contabilidad',  'ae08_sin_cierre'),
    (5770, 'graf_los_recursos',         'grafica', 'b14_recursos',      None),
    (5947, 'kf17_dos_viajeros_se_van',  'placa',   'b14_recursos',      None),
    (6100, 'cama_carretera_golfo',      'cama',    'b15_cierre',        'ae09_sin_inercia'),
]


def construir():
    out, ini = [], 0
    for i, (fin, plano, clase, bloque, encima) in enumerate(RANURAS):
        out.append({'n': i + 1, 'plano': plano, 'clase': clase,
                    'bloque': bloque, 'encima': encima,
                    'ini': ini, 'fin': fin, 'frames': fin - ini})
        ini = fin
    return out


def comprobar(r):
    fallos = []
    if r[-1]['fin'] != N_NARRACION:
        fallos.append('la rejilla termina en %d, la narración mide %d'
                      % (r[-1]['fin'], N_NARRACION))
    for x in r:
        if x['fin'] not in CORTES + CORTES_CARTON and x['fin'] != N_NARRACION:
            fallos.append('%s termina en %d, que no es un silencio medido'
                          % (x['plano'], x['fin']))
        if x['frames'] < 95:
            fallos.append('%s mide %d cuadros, menos de 4 s' % (x['plano'], x['frames']))
        if x['frames'] > (380 if x['clase'] == 'grafica' else 320):
            fallos.append('%s mide %d cuadros, demasiado larga' % (x['plano'], x['frames']))
    pos = 0
    for x in r:
        if x['ini'] != pos:
            fallos.append('hueco antes de %s' % x['plano'])
        pos = x['fin']
    return fallos


if __name__ == '__main__':
    r = construir()
    print('%-3s %-28s %-8s %6s %6s %6s  %s'
          % ('n', 'plano', 'clase', 'ini', 'fin', 'cuadros', 'encima'))
    for x in r:
        print('%-3d %-28s %-8s %6d %6d %6d  %s'
              % (x['n'], x['plano'], x['clase'], x['ini'], x['fin'],
                 x['frames'], x['encima'] or ''))
    cl = {}
    for x in r:
        cl[x['clase']] = cl.get(x['clase'], 0) + 1
    print('')
    print('%d ranuras: %s' % (len(r), cl))
    du = [x['frames'] for x in r]
    print('ranura mas corta %d, mas larga %d, media %d'
          % (min(du), max(du), sum(du) // len(du)))
    f = comprobar(r)
    print('FALLOS: %s' % ('ninguno' if not f else ''))
    for x in f:
        print('   - %s' % x)
    if len(sys.argv) > 1:
        json.dump(r, open(sys.argv[1], 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=1)
        print('guardado en %s' % sys.argv[1])
