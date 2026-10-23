# -*- coding: utf-8 -*-
"""Arma el prompt final de cada ranura y lo deja en json. Lo armado es lo que
se manda y lo que se guarda: no hay borrador aparte."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_p3c4_v2 import arma, TOKENS
from escenas_p3c4_v2 import R, CARTONES, PROPUESTAS, SIN_ROSTRO, comprobar

# LA CLAUSULA DE LUGAR VA POR RANURA, NO POR ESCENA
#     La escena A es el alojamiento: su fachada es exterior pero r02 y r03
#     ocurren adentro. Marcarlas como exteriores les metia «plain kerbs,
#     modest low buildings» a un primer plano contra una pared.
EXTERIORES = {1, 4, 5, 6, 9, 10, 21, 30, 39}

NOMBRE = {1:'fachada_amanecer',2:'nora_umbral',3:'nora_pp',4:'tablero_muelle',
 5:'muelle_hero',6:'ivan_puerta',7:'fiscal_siete',8:'caja_investigador',
 9:'segundo_inmueble',10:'porton_timbre',11:'nora_banca',12:'reloj',
 13:'recepcionista_llega',14:'recepcion_vacia',15:'corredor_vacio',
 16:'sala_desde_atras',17:'fiscal_atril',18:'silla_cardigan',19:'jueza_pp',
 20:'estrado_contraluz',21:'puerta_casa',22:'ivan_banca',23:'corredor_dos',
 24:'cartera_cerrada',25:'lina_pp',26:'lina_de_pie',27:'sala_pequena',
 28:'otra_fiscal_carpeta',29:'dos_entradas',30:'muelle_dia',31:'cuatro_puestos',
 32:'sala_trabajo',33:'direccion_tachada',34:'otra_fiscal_pp',
 35:'carpeta_unica',36:'cerrar_carpeta',37:'sala_vacia',38:'corredor_salida',
 39:'fachada_tarde'}


def construir():
    out = {}
    for n, (cuad, esc, plano, reg, gente, acento, txt) in sorted(R.items()):
        t = txt % TOKENS if '%(' in txt else txt
        out['r%02d_%s' % (n, NOMBRE[n])] = {
            'ranura': n, 'cuadros': cuad, 'escena': esc, 'plano': plano,
            'luz': reg, 'gente': gente, 'carton': n in CARTONES,
            'propuesta': n in PROPUESTAS,
            'prompt': arma(t, registro=reg, personas=gente,
                           con_acento=acento, con_rostro=n not in SIN_ROSTRO,
                           exterior=n in EXTERIORES),
        }
    return out


if __name__ == '__main__':
    f, tot = comprobar()
    assert not f, f
    o = construir()
    json.dump(o, open('prompts_p3c4_v2.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print('%d ranuras · %d cuadros · prompt medio %d caracteres'
          % (len(o), tot, sum(len(v['prompt']) for v in o.values()) // len(o)))
