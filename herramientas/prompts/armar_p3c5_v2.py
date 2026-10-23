# -*- coding: utf-8 -*-
"""Arma el prompt final de cada ranura del P3C5 v2 y lo deja en json."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_p3c5_v2 import arma, TOKENS
from escenas_p3c5_v2 import R, CARTONES, PROPUESTAS, SIN_ROSTRO, comprobar

# la clausula de lugar va por RANURA: la escena A es calle, pero B, C, D...
# son interiores
EXTERIORES = {4, 5}

NOMBRE = {1:'dos_bandejas',2:'sala_vacia',3:'oscar_corredor',4:'medellin_calle',
 5:'tomas_pared',6:'tres_carpetas',7:'la_silla_que_falta',8:'andres_caja',
 9:'la_caja_abierta',10:'despacho_contraluz',11:'la_banda',12:'andres_umbral',
 13:'el_telefono_que_llega',14:'el_cuaderno_en_la_ventana',15:'la_pagina',
 16:'fiscal_sustenta',17:'el_cuaderno_solo',18:'la_linea_acordada',
 19:'la_pluma_suspendida',20:'sala_escucha_vacia',21:'lucia_reconoce',
 22:'la_onda_sin_nadie',23:'renata_presente',24:'la_carpeta_delante',
 25:'el_atril_vacio',26:'la_grafica',27:'lucia_consulta',28:'lucia_sin_hoja',
 29:'lucia_pp',30:'defensor_pregunta',31:'la_puerta_abierta',32:'oscar_pp',
 33:'la_mesa_de_oscar',34:'el_acta_aparte',35:'la_mesa_de_tomas',36:'tomas_pp',
 37:'tomas_solo',38:'fiscal_alegato',39:'cuatro_iguales',
 40:'el_sitio_de_la_cuarta',41:'la_puerta_y_el_pago',42:'empezar_a_separar',
 43:'dos_bandejas_desiguales'}


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
    json.dump(o, open('prompts_p3c5_v2.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print('%d ranuras · %d cuadros · prompt medio %d caracteres'
          % (len(o), tot, sum(len(v['prompt']) for v in o.values()) // len(o)))
