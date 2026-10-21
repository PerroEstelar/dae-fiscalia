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

LA COLA SE REHIZO EL 21 DE OCTUBRE, MEDIDA CONTRA LA VOZ
    La primera version de esta tabla se armo leyendo los NOMBRES de los
    archivos de placa, no lo que las placas muestran. Costo caro:
    `cama_sello_sin_fecha` no es un sello, son once capturas de pantalla sobre
    un escritorio. De ahi salieron doce ranuras mal calzadas, y ocho seguidas
    en la cola -r23 a r30- corridas exactamente una casilla.

    El origen del corrimiento fue `kf13_marta_lejos`: tenia ranura propia
    dentro de b10, pero b10 solo da audio para una y la grafica de antes y
    despues se la lleva entera. Salio de la linea.

    El metodo que hay que repetir en los casos 4 y 5, ANTES de montar:
    `silencedetect` sobre el master de narracion, casar los archivos de
    bloque contra el master por duracion con programacion dinamica, y cruzar
    cada ranura con la frase que se oye encima. Esta en cruce.py.

CUIDADO CON AppendToTimeline Y EL MISMO MEDIO DOS VECES
    Resolve coloca el intro en 0 y el outro en 6568 sin problema cuando los
    dos van en el MISMO lote. Si el intro ya esta puesto y se intenta colocar
    el outro despues, en otra llamada, AppendToTimeline devuelve [None] y no
    coloca nada: no acepta el mismo media pool item una segunda vez en la
    misma pista. Por eso existe ahora
    `00 COMUNES/INTRO/FGN_outro_v7_182.mp4`, que son los 182 cuadros del
    intro como medio aparte. Para montajes incrementales, usar ese.

EL REPERTORIO SE REHIZO EL 21 DE OCTUBRE
    Sebastian: *"muestra mas a los personajes a media accion, no puros cuadros
    vacios"*. Tenia razon y el numero lo decia: de 28 placas, 21 eran entorno
    vacio. Me habia ido a la convencion de "cama institucional" y la habia
    estirado a casi toda la pieza, en vez de aplicar el metodo de prompts hero
    que esta escrito en CLAUDE.md -la camara es el argumento, el gesto unico
    antes que la cara, la emocion va en las manos, media accion y nunca el
    pico-.

    Entran dieciseis placas nuevas. Donde el caso no permite caras -el equipo,
    los funcionarios- la accion va en las MANOS: la mesa en cenital con ocho
    manos y una hoja a media deslizada, el dedo detenido a mitad de un renglon,
    la mano que acaba de soltar un documento que nadie recoge. Eso respeta la
    biblia SRPA -"sin personal identificable"- y es ademas el plano canonico
    del metodo.

LO QUE SALE DE LA LINEA, Y POR QUE
    kf13_marta_lejos   el guion no le da frase propia; su nombre y su dato
                       entran en el carton ae00, sobre el plano del grupo.
    kf14_orden_servicio  Sebastian marco sus filetes casi negros; la frase de
                       Omar se la queda su primer plano al volante.
    kf04_marta_giros, kf03_luis_computador, kf05_omar_volante, kf06_teresa_cocina,
    kf08_nidia_local, kf12_viajero_documento, cama_cajon, cama_pantalla,
    kf07_certificado_empleo, kf09_pasaportes_recibos, kf10_puesto_control,
    kf11_informe_dos_meses, cama_mesa_equipo, cama_sala_reunion,
    cama_tienda_esquina, kf01_terminal_vehiculo
                       reemplazadas por su version con gente en accion.

QUE VA EN CADA PISTA
    V1 placa o cama · V2 el clip de movimiento, que cubre la ranura entera y
    se puede apagar · V3 cartón teñido o de narración · V7 lower third.
"""
import json
import sys

# puntos medios de los silencios medidos
CORTES = [61, 202, 351, 445, 613, 916, 1094, 1207, 1261, 1439, 1608, 1826,
          2049, 2115, 2306, 2430, 2704, 2932, 3142, 3375, 3476, 3586, 3646,
          3843, 3947, 4063, 4213, 4478, 4649, 4829, 5004, 5126, 5210, 5283,
          5393, 5594, 5770, 5863, 5947, 5992, 6090]

# los cortes de las tres ranuras de propuesta no van al medio del silencio sino
# justo antes de que vuelva la voz, para ganarle segundos de lectura al carton
CORTES_CARTON = [1676, 2475, 4120]

N_NARRACION = 6100

# (corte_final, plano, clase, bloque, que lleva encima)
#   clase: placa | cama | grafica
RANURAS = [
    (202,  'cama_calle_medellin',       'cama',    'b1_apertura',       'ae01_progresiva'),
    (445,  'r02_terminal_viajeros',     'placa',   'b1_apertura',       'lt01_fecha_lugar'),
    (613,  'graf_la_ruta',              'grafica', 'b2_los_cuatro',     None),
    (916,  'kf02_los_cuatro_espaldas',  'placa',   'b2_los_cuatro',     'ae00_los_cuatro'),
    (1094, 'cama_formulario',           'cama',    'b2_los_cuatro',     'ae02_no_identificada'),
    (1261, 'cama_sello_sin_fecha',      'cama',    'b3_capturas',       None),
    (1439, 'r07_luis_cuenta',           'placa',   'b3_capturas',       'lt02_luis'),
    (1676, 'r08_mesa_manos',            'cama',    'b4_propuesta_uno',  'prop1_tres_peticiones'),
    (1826, 'r09_teresa_cocina',         'placa',   'b5_teresa',         'lt05_teresa'),
    (2049, 'cama_pasillo',              'cama',    'b5_teresa',         None),
    (2306, 'r11_tienda_esquina',        'placa',   'b5_teresa',         'ae03_podian_salir'),
    (2475, 'cama_informe_esfero',       'cama',    'b6_sin_esclarecer', 'prop2_agregar_trata'),
    (2704, 'r13_certificado_luz',       'cama',    'b7_la_visa',        None),
    (2932, 'cama_visado',               'cama',    'b7_la_visa',        'ae04_materialmente'),
    (3142, 'r15_nidia_mostrador',       'placa',   'b8_nidia',          'lt06_nidia'),
    (3375, 'r16_pasaportes_cenital',    'cama',    'b8_nidia',          None),
    (3476, 'r17_dos_carpetas',          'cama',    'b8_nidia',          'ae05_sin_relacion'),
    (3646, 'r18_puesto_control',        'cama',    'b9_migracion',      'ae10_un_puesto'),
    (3843, 'r19_informe_dedo',          'cama',    'b9_migracion',      'ae11_dos_meses'),
    (3947, 'r20_documento_mostrador',   'cama',    'b9_migracion',      None),
    (4120, 'r21_sala_alto',             'placa',   'b9_migracion',      'prop3_ignorar'),
    (4478, 'graf_antes_y_despues',      'grafica', 'b10_evaluacion',    None),
    (4649, 'r23_omar_volante',          'placa',   'b11_omar',          'lt04_omar'),
    (4829, 'cama_telefono_omar',        'cama',    'b11_omar',          'ae06_no_atribuido'),
    (5004, 'kf15_conversacion_pantalla','placa',   'b12_conversacion',  'cap01_viernes x2'),
    (5126, 'r26_pantalla_mensajes',     'cama',    'b12_conversacion',  'ae07_si_describen'),
    (5393, 'r27_cuaderno_bajo',         'cama',    'b13_contabilidad',  'ae08_sin_cierre'),
    (5770, 'graf_los_recursos',         'grafica', 'b14_recursos',      None),
    (5947, 'kf17_dos_viajeros_se_van',  'placa',   'b15_cierre',        None),
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
