# -*- coding: utf-8 -*-
r"""Cartones SUELTOS sobre una linea que Sebastian ya toco (31 oct, U3).

    python cartones_sueltos_jr.py medir  sueltos.json
    python cartones_sueltos_jr.py quemar sueltos.json

`cartones_jr.py U3 --quemar` NO sirve despues de la revision: renumera los
p01..pNN y la linea de Sebastian ya tiene sus cartones movidos y
recortados a mano. Aqui cada carton nuevo lleva su propio nombre
(JR_U3_p17b_carton.mov, ...), se comprueba VERBATIM contra el guion igual
que los de `cartones_jr`, y despues entra a la linea con
`cirugia_jr.py U3 poner V4 <ruta> <pos> <largo>`, que no toca nada mas.

sueltos.json = [{"tema": "U3", "bloque": "b14_no_le_cree",
                 "trozo": "Usted, con un gesto ...", "archivo": "JR_U3_p11b_carton.mov",
                 "ini": 3251, "cuadros": 200}, ...]
`medir` imprime, para cada trozo, el cuadro de la linea en que se oye su
primera palabra (Scribe), el cuadro en que termina la voz del bloque, los
renglones y la densidad si ya trae ini/cuadros. `quemar` exige ini y
cuadros y quema el .mov en 02 CARTONES (aparta uno que ya exista).
"""
import json
import os
import sys

H = r'D:\DAE\_repo\herramientas'
for sub in ('cartones', 'montaje', 'prompts', os.path.join('voz', 'textos')):
    sys.path.insert(0, os.path.join(H, sub))

import cartones_jr as CJ                                   # noqa: E402
from guion_jr import bloques                               # noqa: E402


def w(x):
    CJ.w(x)


def prepara(s):
    tx = {b[0]: ' '.join(b[2].split()) for b in bloques(s['tema'])}
    texto = tx[s['bloque']]
    pos = texto.find(s['trozo'])
    assert pos >= 0, 'el trozo no esta VERBATIM en %s:\n  %s' % (s['bloque'], s['trozo'])
    empieza = pos == 0 or texto[:pos].rstrip().endswith(('.', ':'))
    frase = CJ.presentar(s['trozo'], pos == 0, empieza)
    ok, motivo = CJ.comprobar_arreglo(s['trozo'], frase)
    assert ok, (motivo, frase)
    ini, como = CJ.entra(s['tema'], s['bloque'], texto, s['trozo'])
    _ws, tr = CJ.palabras_stt(s['tema'], s['bloque'])
    fin_voz = CJ.CABEZA + int(round(tr['sale'] * CJ.FPS))
    return dict(s, frase=frase, oye=ini, como=como, fin_voz=fin_voz,
                renglones=CJ.renglones(frase))


if __name__ == '__main__':
    paso, f = sys.argv[1], sys.argv[2]
    for s in json.load(open(f, encoding='utf-8')):
        d = prepara(s)
        dens = ''
        if d.get('cuadros'):
            dens = '%.1f car/s' % (len(d['frase']) / (d['cuadros'] / CJ.FPS))
        w('%s  se oye en %d (%s), voz del bloque hasta %d, %d renglones, %d car  %s'
          % (d['archivo'], d['oye'], d['como'], d['fin_voz'], d['renglones'],
             len(d['frase']), dens))
        w('   ' + d['frase'])
        # `tope` en el json: excepcion pedida (U3 p17c, cuatro renglones: Sebastian
        # pidio DOS cartones para el resto de la cita y en tres no cabe)
        tope = d.get('tope', CJ.TOPE_RENGLONES)
        assert d['renglones'] <= tope, 'mas de %d renglones' % tope
        if paso == 'quemar':
            assert d.get('ini') is not None and d.get('cuadros'), 'falta ini/cuadros'
            w('   quemado ' + CJ.quemar(d))
    w('LISTO')
