# -*- coding: utf-8 -*-
r"""Calcula QUE DICE LA VOZ durante cada ranura de carton.

LA REGLA ES DE SEBASTIAN Y YA ESTA EN LA BIBLIA (seccion 9)
    «mostly we should stick to verbatum trancript from the narrators voice
    at the exact time they are saying it ... just so we canbetter justify
    things to la fiscalia, whatever proferoes say its what hoes, we USUlly
    dont paraphrase, or re arrange or dchange syntaxes».

    Asi que el carton no resume el bloque: lleva LA FRASE QUE SE ESTA
    OYENDO mientras el carton esta en pantalla.

COMO SE SABE CUAL FRASE
    La rejilla da cuando entra y cuando sale cada bloque de voz, y las
    ranuras dicen que trozo del bloque cubre cada plano. Repartiendo los
    caracteres del bloque sobre su duracion se sabe que ventana del texto
    cae dentro de la ranura, y de ahi se toma la ORACION COMPLETA que mas
    se superpone con esa ventana.

    El reparto por caracteres es una aproximacion -la voz no va a ritmo
    constante-, asi que esto PROPONE y la frase se mira contra el audio
    antes de quemar el carton.

EL MARGEN DE ARREGLO, QUE TAMBIEN ES DE SEBASTIAN
    26 de octubre: «tu influencia en el verbatim puede existir dentro de un
    rango de accion menor, como decir escribir ciertas cosas con algun
    agregado que le de mayor sentido a la frase mientras sea de una forma
    minima, por ejemplo en ese caso podria ser SE ACTIVA el mecanismo de
    busqueda urgente».

    Cuando la ranura cae en mitad de una oracion, el fragmento que suena
    puede no sostenerse solo: «activa el Mecanismo de Busqueda Urgente»
    arranca en minuscula y en un verbo sin sujeto. El arreglo permitido es
    el MINIMO que lo deja leerse como frase -una particula, un articulo, la
    mayuscula inicial- y nada mas.

    Lo que NO se puede: cambiar una palabra que el profesor escribio,
    quitarla, reordenarla, resumir, ni agregar contenido. Por eso
    `comprobar_arreglo` exige que TODAS las palabras del fragmento original
    sigan ahi, en el mismo orden y sin cambiar: el arreglo solo puede
    AGREGAR. Si una palabra desaparece o se sustituye, el arreglo se
    rechaza y el carton no se quema.

    Y queda `frase_cruda` guardada junto a `frase`, para que cualquiera
    pueda ver contra el audio exactamente que se agrego.
"""
import json
import os
import re
import sys
import unicodedata

sys.path.insert(0, 'D:/DAE/_repo/herramientas/prompts')
sys.path.insert(0, 'D:/DAE/_repo/herramientas/voz/textos')
import guion_df as G                               # noqa: E402
import plan_camara_df as PC                        # noqa: E402
from armar_df import NOMBRE                        # noqa: E402

FPS = 23.976

# (capitulo, ranura) -> la frase con su arreglo minimo.
#     Solo entran aqui los fragmentos que no se sostienen solos. Las
#     oraciones completas no se tocan, y la cita de C1 r14 tampoco: abre
#     con comilla angular, asi que ya se lee como lo que es.
ARREGLOS = {
    (2, 9): ('Se activa el Mecanismo de Búsqueda Urgente, de la Ley 971 de '
             '2005, y simultáneamente la Alerta Rosa, de la Ley 2326 de 2023 '
             'y el Decreto 1428 de 2024.'),
}


def _palabras(t):
    t = unicodedata.normalize('NFD', t.lower())
    t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    return [w for w in re.split(r'[^0-9a-z]+', t) if w]


def comprobar_arreglo(crudo, arreglado):
    """El arreglo solo puede AGREGAR: todas las palabras del fragmento
    original tienen que seguir ahi, en el mismo orden y sin cambiar."""
    a, b = _palabras(crudo), _palabras(arreglado)
    i = 0
    for w in b:
        if i < len(a) and w == a[i]:
            i += 1
    if i != len(a):
        return False, 'el arreglo perdio o cambio palabras del original'
    agregadas = len(b) - len(a)
    if agregadas > 3:
        return False, 'el arreglo agrega %d palabras: ya no es minimo' % agregadas
    return True, 'agrega %d palabra(s)' % agregadas


def oraciones(t):
    """Parte en oraciones sin romper la comilla angular ni los decimales."""
    t = ' '.join(t.split())
    partes, cur = [], ''
    for i, ch in enumerate(t):
        cur += ch
        if ch in '.:' and i + 1 < len(t) and t[i + 1] == ' ':
            if re.match(r'\d', t[i + 1:i + 2] or ' '):
                continue
            if cur.strip().endswith('«') or cur.count('«') > cur.count('»'):
                continue
            partes.append(cur.strip())
            cur = ''
    if cur.strip():
        partes.append(cur.strip())
    return partes


def propone(cap, ranuras=None):
    b = os.path.join(PC.RAIZ, PC.CAPS[cap], '03 VOCES')
    rr = json.load(open(os.path.join(b, 'DF_C%d_ranuras.json' % cap),
                        encoding='utf-8'))['ranuras']
    tr = {t['bloque']: t for t in
          json.load(open(os.path.join(b, 'DF_C%d_rejilla.json' % cap),
                         encoding='utf-8'))['tramos']}
    tx = {e[0]: e[2] for e in G.bloques(cap)}
    mod = __import__('escenas_df_c%d' % cap)
    out = []
    for n in sorted(mod.CARTONES if ranuras is None else ranuras):
        r = rr[n - 1]
        t, texto = tr[r['bloque']], ' '.join(tx[r['bloque']].split())
        ini_s, fin_s = r['ini'] / FPS, (r['ini'] + r['dur']) / FPS
        a = (max(ini_s, t['entra']) - t['entra']) / t['dur']
        z = (min(fin_s, t['sale']) - t['entra']) / t['dur']
        ca, cz = a * len(texto), z * len(texto)
        mejor, pos, p = None, 0, -1
        for o in oraciones(texto):
            i = texto.index(o, pos)
            pos = i + len(o)
            sol = max(0, min(cz, i + len(o)) - max(ca, i))
            if sol > p:
                p, mejor = sol, (o, i)
        crudo, i0 = mejor
        frase = ARREGLOS.get((cap, n), crudo)
        if frase is not crudo:
            ok, motivo = comprobar_arreglo(crudo, frase)
            assert ok, ('C%d r%02d: %s\n  crudo:     %s\n  arreglado: %s'
                        % (cap, n, motivo, crudo, frase))
        f0 = int(round((t['entra'] + t['dur'] * i0 / len(texto)) * FPS)) - r['ini']
        out.append({'cap': cap, 'ranura': n, 'nombre': NOMBRE[cap][n],
                    'cuadros': r['dur'], 'bloque': r['bloque'],
                    'voz': [e[1] for e in G.bloques(cap)
                            if e[0] == r['bloque']][0],
                    'entrada': max(2, min(f0, r['dur'] - 60)),
                    'frase': frase, 'frase_cruda': crudo,
                    'arreglado': frase != crudo})
    return out


if __name__ == '__main__':
    todo = []
    for c in (1, 2, 3, 4, 5):
        todo += propone(c)
    for d in todo:
        print('=== C%d r%02d %s  (%d cuadros, entra en %d, voz %s)%s'
              % (d['cap'], d['ranura'], d['nombre'], d['cuadros'],
                 d['entrada'], d['voz'],
                 '  ARREGLADO' if d['arreglado'] else ''), flush=True)
        if d['arreglado']:
            ok, motivo = comprobar_arreglo(d['frase_cruda'], d['frase'])
            print('    suena : %s' % d['frase_cruda'])
            print('    carton: %s' % d['frase'])
            print('    (%s)' % motivo)
        else:
            print('    %s' % d['frase'])
        print()
    json.dump(todo, open(r'D:\DAE\_tmp\df\cartones_df.json', 'w',
                         encoding='utf-8'), ensure_ascii=False, indent=1)
    print('%d cartones, %d con arreglo minimo'
          % (len(todo), sum(1 for d in todo if d['arreglado'])))
