#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Re-renderiza los cartones calzados al tramo de voz, con margen.

EL PROBLEMA QUE RESUELVE
    Un cartón que dura exactamente lo que dura su frase deja el texto incompleto
    en los dos extremos: la animación de entrada tarda unos cuadros en armar el
    bloque y la de salida empieza antes del último cuadro. Con la animación
    vieja eso eran 35 cuadros por delante y 20 por detrás — el texto se iba
    mientras todavía se oían las últimas palabras.

LA REGLA
    nframes = tramo_de_voz + CABEZA + COLA,  y el clip se coloca CABEZA cuadros
    ANTES de que empiece la frase. Así el texto está completo exactamente
    mientras se habla, y las dos animaciones caen fuera de las palabras.

    Como los cartones del bloque de preguntas van pegados uno detrás de otro,
    al crecer se solapan: por eso en la línea de tiempo se alternan entre la
    pista CARTONES y la pista CARTONES 2.

USO
    cartones_calzados.py <caso>        # 01 02 06 07 08
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cartones_ta as C

# tramo medido de voz de cada cartón, tal como está hoy en la línea de tiempo
TRAMOS = {
    "01": {"n1_alejandro": 111, "n2_ochenta_millones": 91, "n3_la_madrugada": 111,
           "n4_el_abogado": 142, "n5_valorar": 91, "n6_escenario_1": 111,
           "n7_escenario_2": 111, "n8_escenario_3": 111,
           "n9_la_misma_propuesta": 142,
           "p0_el_fiscal_responde": 137, "p1_de_la_misma_manera": 157,
           "p2_la_contraprestacion": 237, "p3_en_cual_de_los_escenarios": 385,
           "p4_debe_negociar_necesariamente": 303},
    "06": {"n1_el_hurto": 111, "n2_varios_meses": 111, "n3_las_camaras": 142,
           "p0_el_fiscal_deberia": 164, "p1_archivar_por_imposibilidad": 122,
           "p2_causal_suficiente": 218, "p3_hasta_que_punto": 94,
           "p4_actividades_exigibles": 149, "p5_preservacion_temprana": 128,
           "p6_asociacion": 104, "p7_que_se_hizo": 248},
    "07": {"n1_ocho_millones": 91, "n2_reconoce": 111, "n3_incumplimiento": 111,
           "p0_el_fiscal_podria": 218, "p1_tipos_penales": 123,
           "p2_elementos_objetivos": 95, "p3_conducta_tipica": 110,
           "p4_ausencia_de_elementos": 128, "p5_actos_de_investigacion": 101,
           "p6_por_que_archivo": 181},
    "08": {"n1_fue_archivada": 111, "n2_seis_meses": 111, "n3_el_rostro": 91,
           "p0_el_fiscal_deberia": 139, "p1_razon_del_archivo": 66,
           "p2_que_nueva_evidencia": 123, "p3_capacidad_de_modificar": 164,
           "p4_que_actuaciones": 135},
}


def specs(caso):
    """Junta las specs de preguntas y de narración de un caso."""
    import importlib
    d = {}
    mod = importlib.import_module("cartones_c%s" % caso)
    for nombre, _n, spec in getattr(mod, "PREGUNTAS", []):
        d[nombre] = spec
    nar = importlib.import_module("cartones_narracion")
    for nombre, _n, spec in nar.NARRACION.get(caso, []):
        d[nombre] = spec
    for nombre, _n, spec in getattr(mod, "NARRACION", []):
        d[nombre] = spec
    return d


# El panel de tinte del bloque de preguntas: (primer cuadro, último cuadro) del
# bloque ya con los márgenes puestos.
PANEL = {"01": (4131, 5380), "06": (1692, 2941),
         "07": (1748, 2734), "08": (1041, 1698)}

if __name__ == "__main__":
    caso = sys.argv[1]
    OUT = "/mnt/user-data/outputs/cartones_calzados_c%s" % caso
    os.makedirs(OUT, exist_ok=True)
    sp = specs(caso)
    total = C.CABEZA + C.COLA
    for nombre, tramo in TRAMOS[caso].items():
        if nombre not in sp:
            print("SIN SPEC: " + nombre)
            continue
        # Los de narración van sueltos y llevan su propio tinte. Los del bloque
        # de preguntas se solapan, así que van SIN tinte: el panel va aparte.
        suelto = nombre.startswith("n")
        C.render_carton(sp[nombre], tramo + total, None, True,
                        "%s/TA%s_%s.mov" % (OUT, caso, nombre), con_tinte=suelto)
    a, b = PANEL[caso]
    C.render_tinte(b - a, "%s/TA%s_tinte_preguntas.mov" % (OUT, caso))
    print("\ncabeza %d  cola %d  -> cada cartón entra %d cuadros antes de su frase"
          % (C.CABEZA, C.COLA, C.CABEZA))
    print("panel de tinte: %d -> %d  (%d cuadros)" % (a, b, b - a))
