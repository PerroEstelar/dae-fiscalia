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
    "02": {"n1_los_dos": 132, "n2_medios": 91, "n3_la_posicion": 179,
           "n4_120_millones": 112, "n5_concertada": 166, "n6_400_millones": 82,
           "n7_la_defensa": 147, "n8_propone": 160,
           "p0_el_fiscal_determina": 230, "p1_es_viable": 137,
           "p2_esta_acreditado": 106, "p3_reintegro_minimo": 83,
           "p4_la_garantia": 137, "p5_puede_negociar": 186,
           "p6_reintegro_inferior": 186},
    "03": {"n1_ambos_participan": 228, "n2_el_arma": 184, "n3_como_autor": 250,
           "n4_la_defensa_propone": 216, "n5_no_seria_admisible": 244,
           "n6_calificacion_que_no_corresponde": 246, "n7_segunda_propuesta": 250,
           "n8_solo_la_sancion": 196, "n9_ira_e_intenso_dolor": 202,
           "n10_no_existe_informacion": 250, "n11_el_juez_distingue": 160,
           "n12_domiciliaria": 213, "n13_los_subrogados": 250, "p0_con_base": 96,
           "p1_por_que_no_puede": 219, "p2_la_diferencia": 274, "p3_sin_respaldo": 284,
           "p4_los_subrogados": 327},
    "04": {"n1_el_hurto": 111, "n2_dieciocho_millones": 91,
           "n3_tecnico_de_sistemas": 142, "n4_no_existen_elementos": 142,
           "n5_la_defensa_propone": 111, "n6_dificultades": 91, "n7_la_rebaja": 142,
           "p0_el_fiscal_determina": 195, "p1_reconocer_marginalidad": 197,
           "p2_fundamento_factico": 97, "p3_elementos_probatorios": 88,
           "p4_relacion_con_la_conducta": 96, "p5_creando_o_reconociendo": 214,
           "p6_moneda_de_cambio": 204},
    "05": {"n1_laura": 207, "n2_coordino": 160, "n3_doscientos_cincuenta": 137,
           "n4_se_recaudaron": 250, "n5_base_probatoria": 250, "n6_la_defensa": 250,
           "n7_apertura": 250, "n8_lo_que_no": 250, "n9_precisa_los_hechos": 220,
           "n10_intercambio": 265, "n11_sin_respaldo": 250, "n12_nueva_propuesta": 250,
           "n13_que_recibe": 246, "n14_cierre": 250, "n15_el_beneficio": 250,
           "n16_la_victima": 278, "p0_en_el_marco": 80, "p1_la_apertura": 241,
           "p2_el_intercambio": 134, "p3_el_cierre": 254},
    "06": {"n1_el_hurto": 111, "n2_varios_meses": 111, "n3_las_camaras": 142,
           "p0_el_fiscal_deberia": 164, "p1_archivar_por_imposibilidad": 122,
           "p2_causal_suficiente": 218, "p3_hasta_que_punto": 94,
           "p4_actividades_exigibles": 149, "p5_preservacion_temprana": 128,
           "p6_asociacion": 104, "p7_que_se_hizo": 248},
    "07": {"n1_la_denuncia": 96, "n2_ocho_millones": 91, "n3_materiales": 86,
           "n4_se_robo": 85, "n5_el_contrato": 140, "n6_reconoce": 173,
           "n7_incumplimiento": 166, "n8_apropiarselo": 159,
           "p0_el_fiscal_podria": 218, "p1_tipos_penales": 123,
           "p2_elementos_objetivos": 95, "p3_conducta_tipica": 110,
           "p4_ausencia_de_elementos": 128, "p5_actos_de_investigacion": 101,
           "p6_por_que_archivo": 181},
    "08": {"n1_lesiones": 63, "n2_no_permitian": 118, "n3_seis_meses": 50,
           "n4_otro_video": 72, "n5_el_rostro": 142, "n6_el_abogado": 129,
           "p0_el_fiscal_deberia": 139, "p1_razon_del_archivo": 66,
           "p2_que_nueva_evidencia": 123, "p3_capacidad_de_modificar": 164,
           "p4_que_actuaciones": 135},
    "09": {"n1_lesiones": 107, "n2_maniobra_brusca": 110, "n3_el_nino": 83,
           "n4_el_fiscal_propone": 165, "p0_reflexionar": 152, "p1_conducta_tipica": 64,
           "p2_circunstancia": 163, "p3_mediante_archivo": 146, "p4_el_mecanismo": 164}
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
PANEL = {"01": (4131, 5380), "02": (1971, 3066), "03": (5145, 6375), "05": (6098, 6837), "09": (895, 1696), "04": (2289, 3410), "06": (1692, 2941),
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
