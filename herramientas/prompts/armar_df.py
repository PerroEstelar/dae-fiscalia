# -*- coding: utf-8 -*-
r"""Arma el prompt final de cada ranura del caso MIRIAM Y MARIANA y lo deja
en json, con las mismas comprobaciones que el P3C5.

La clausula de lugar va POR RANURA, no por caso: la plaza es exterior y la
subestacion es interior, y pedirle «ordinary Colombian institutional
furniture» a un potrero no tiene sentido.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, r'D:\DAE\_repo\herramientas\prompts')
from base_df_v1 import arma, TOKENS              # noqa: E402

NOMBRE = {
 1: {1: 'plaza_abre', 2: 'miriam_puesto', 3: 'casa_cerrada',
     4: 'monedero_y_zapatos', 5: 'miriam_pp', 6: 'tres_siluetas',
     7: 'desde_el_puesto', 8: 'caja_vacia', 9: 'el_potrero_vacio',
     10: 'camino_de_vuelta', 11: 'gregoria_recibe', 12: 'la_cuadra_de_noche',
     13: 'el_puesto_cerrado', 14: 'la_minuta', 15: 'la_ventanilla_vacia',
     16: 'tres_puestos'},
 2: {1: 'rosaelena_patio', 2: 'mariana_puerta', 3: 'la_marcha',
     4: 'el_cartel', 5: 'la_subestacion', 6: 'el_telefono_en_el_piso',
     7: 'rosaelena_entra', 8: 'la_fiscal_recibe', 9: 'los_dos_formatos',
     10: 'la_sala_de_trabajo', 11: 'el_mapa_en_pantalla'},
 3: {1: 'el_despacho', 2: 'los_dos_escritorios', 3: 'la_caja_por_el_pasillo',
     4: 'la_caja_en_el_piso', 5: 'la_fiscal_en_la_puerta',
     6: 'la_mesa_de_cinco', 7: 'tres_carpetas', 8: 'el_mismo_documento',
     9: 'dos_carpetas'},
 4: {1: 'el_pasillo_de_sillas', 2: 'la_ventanilla', 3: 'rosaelena_pp',
     4: 'la_fiscal_de_pie', 5: 'la_sala_de_atencion',
     6: 'la_psicologa_al_lado', 7: 'las_manos_con_guantes',
     8: 'la_entrevista'},
 5: {1: 'tres_mesas', 2: 'dos_documentos', 3: 'el_camino_de_noche',
     4: 'el_georradar', 5: 'la_cuadricula', 6: 'las_manos_en_la_tierra',
     7: 'la_bandeja', 8: 'el_perito', 9: 'la_pantalla_del_laboratorio',
     10: 'el_analista_y_el_tablero', 11: 'el_tablero',
     12: 'el_predio_al_atardecer', 13: 'el_documento_cerrado'},
}


def construir(cap):
    mod = __import__('escenas_df_c%d' % cap)
    out = {}
    for n, (cuad, reg, gente, acento, sil, ext, txt) in sorted(mod.R.items()):
        cuerpo = txt % TOKENS if '%(' in txt else txt
        p = arma(cuerpo, registro=reg, personas=gente, con_acento=acento,
                 con_lugar=True, con_rostro=True, exterior=ext, silueta=sil)
        out['C%d_r%02d_%s' % (cap, n, NOMBRE[cap][n])] = {
            'capitulo': cap, 'ranura': n, 'cuadros': cuad, 'luz': reg,
            'gente': list(gente), 'acento': bool(acento), 'silueta': bool(sil),
            'exterior': bool(ext), 'carton': n in mod.CARTONES, 'prompt': p}
    return out, mod


if __name__ == '__main__':
    cap = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    o, mod = construir(cap)
    f, tot, mejor = mod.comprobar()
    assert not f, f
    d = r'D:\DAE\_tmp\df'
    os.makedirs(d, exist_ok=True)
    ruta = os.path.join(d, 'prompts_df_c%d.json' % cap)
    json.dump(o, open(ruta, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('%-28s %-10s %5s %7s %7s %7s %s'
          % ('placa', 'luz', 'cuad', 'acento', 'silueta', 'carton', 'car'))
    for k, v in sorted(o.items()):
        print('%-28s %-10s %5d %7s %7s %7s %d'
              % (k, v['luz'], v['cuadros'], 'si' if v['acento'] else '-',
                 'si' if v['silueta'] else '-', 'si' if v['carton'] else '-',
                 len(v['prompt'])))
    print('')
    print('%d placas · %d cuadros · racha sin gente %d · prompt medio %d car'
          % (len(o), tot, mejor, sum(len(v['prompt']) for v in o.values()) // len(o)))
