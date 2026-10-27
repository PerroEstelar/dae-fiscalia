# -*- coding: utf-8 -*-
r"""Arma la linea de tiempo completa de un capitulo dentro de Resolve.

LA GEOMETRIA ES LA DE LA SERIE, MEDIDA SOBRE EL P3C5
    intro 182 · entrada 119 · las ranuras · respiro 48 · cierre 119 ·
    outro 182. Para el capitulo 1 eso da 182+119+2973+48+119+182 = 3623,
    que es exactamente el `pieza` que la rejilla de voz ya traia escrito.
    O sea que la rejilla siempre conto con esta cabeza y esta cola; lo que
    faltaba era ponerlas.

LAS PISTAS
    V1  VIDEO       intro, entrada, ranuras, respiro, cierre, outro.
                    Esta pista sola ya es la pieza completa.
    V2  MOVIMIENTO  los clips generados, cada uno sobre SU ranura. Entran y
                    salen fundidos CONTRA la ranura de V1 -la fundida esta
                    horneada en el archivo, porque la API de Resolve no
                    anima la opacidad de un item-, asi que se prende y se
                    apaga sin que nada salte.
    V3  CARTONES    los cartones verbatim.
    V4  MARCA       la marca de agua, al principio y al final del cuerpo.
    A1  NARRADOR    el master de voz, que entra DESPUES del intro y de la
                    entrada: la voz empieza con la primera ranura.

NO REMONTA UNA LINEA QUE YA TENGA CLIPS
    En el P3C5 remontar una linea que Sebastian habia partido a mano para
    congelar dos planos borro su trabajo. Una linea con clips se modifica
    clip por clip, nunca de cero. Una vacia es basura de un intento fallido
    y esa si se rehace.
"""
import os
import sys

sys.path.insert(0, 'D:/DAE/_repo/herramientas/prompts')
import movimiento_df as M                          # noqa: E402
import plan_camara_df as PC                        # noqa: E402
from armar_df import NOMBRE                        # noqa: E402

T0 = 86400
COMUNES = r'E:\DAE MASTER\00 COMUNES'
INTRO = os.path.join(COMUNES, 'INTRO', 'FGN_intro_version7.mp4')
MARCA = os.path.join(COMUNES, 'MARCA DE AGUA', 'MARCA_DE_AGUA_DAE_7s_fade.mov')
N_INTRO, N_BLANCO, N_RESPIRO, N_MARCA = 182, 119, 48, 168


def plan(cap):
    """Devuelve (v1, v2, v3, v4, voz, ini_cuerpo, total)."""
    E = __import__('escenas_df_c%d' % cap)
    base = os.path.join(PC.RAIZ, PC.CAPS[cap])
    tl = os.path.join(base, '10 TIMELINE SEBASTIAN')
    cart = os.path.join(base, '02 CARTONES')

    v1, v2, v3, t = [], [], [], 0
    v1.append((t, N_INTRO, INTRO)); t += N_INTRO
    v1.append((t, N_BLANCO, os.path.join(cart, 'DF_C%d_carton_entrada.mov' % cap)))
    t += N_BLANCO
    ini = t
    for n in sorted(E.R):
        largo = E.R[n][0]
        nm = 'DF_C%d_r%02d_%s' % (cap, n, NOMBRE[cap][n])
        v1.append((t, largo, os.path.join(tl, 'RANURAS', '%s_v%d.mp4' % (nm, largo))))
        if (cap, n) in M.MOV:
            v2.append((t, largo, os.path.join(tl, 'MOVIMIENTO',
                                              '%s_mov_v%d.mp4' % (nm, largo))))
        if n in E.CARTONES:
            v3.append((t, largo, os.path.join(cart, '%s_carton.mov' % nm)))
        t += largo
    fin = t
    v1.append((t, N_RESPIRO, os.path.join(tl, 'RESPIRO',
                                          'DF_C%d_respiro_v%d.mp4' % (cap, N_RESPIRO))))
    t += N_RESPIRO
    v1.append((t, N_BLANCO, os.path.join(cart, 'DF_C%d_carton_cierre.mov' % cap)))
    t += N_BLANCO
    v1.append((t, N_INTRO, INTRO)); t += N_INTRO

    v4 = [(ini, N_MARCA, MARCA), (fin - N_MARCA, N_MARCA, MARCA)]
    voz = os.path.join(base, '03 VOCES', 'DF_C%d_NARRADOR.wav' % cap)
    return v1, v2, v3, v4, voz, ini, fin - ini, t


def construye(resolve, cap, nombre_linea):
    pr = resolve.GetProjectManager().GetCurrentProject()
    mp = pr.GetMediaPool()
    for i in range(1, int(pr.GetTimelineCount()) + 1):
        t = pr.GetTimelineByIndex(i)
        if t.GetName() != nombre_linea:
            continue
        if (t.GetItemListInTrack('video', 1) or []):
            return None, 'la linea «%s» ya tiene clips: no se remonta' % nombre_linea
        mp.DeleteTimelines([t])

    v1, v2, v3, v4, voz, ini, dur_cuerpo, tot = plan(cap)
    falta = [p for _, _, p in v1 + v2 + v3 + v4 if not os.path.exists(p)]
    if not os.path.exists(voz):
        falta.append(voz)
    if falta:
        return None, 'faltan en disco: %s' % sorted(set(falta))[:4]

    raiz = mp.GetRootFolder()
    carp = None
    for f in raiz.GetSubFolderList():
        if f.GetName() == nombre_linea:
            carp = f
    if carp is None:
        carp = mp.AddSubFolder(raiz, nombre_linea)
    mp.SetCurrentFolder(carp)
    mp.ImportMedia(sorted(set([p for _, _, p in v1 + v2 + v3 + v4] + [voz])))

    # por NOMBRE DE ARCHIVO: RAIZ usa barras normales y os.path.join las
    # invertidas, asi que la ruta que arma este script y la que Resolve
    # devuelve en 'File Path' no son la misma cadena.
    pool = {}
    for it in carp.GetClipList():
        pool[os.path.basename(
            it.GetClipProperty('File Path').replace('/', os.sep))] = it

    tl = mp.CreateEmptyTimeline(nombre_linea)
    pr.SetCurrentTimeline(tl)
    while tl.GetTrackCount('video') < 4:
        tl.AddTrack('video')
    for i, n in ((1, 'VIDEO'), (2, 'MOVIMIENTO'), (3, 'CARTONES'), (4, 'MARCA')):
        tl.SetTrackName('video', i, n)
    tl.SetTrackName('audio', 1, 'NARRADOR')

    for lista, pista in ((v1, 1), (v2, 2), (v3, 3), (v4, 4)):
        if not lista:
            continue
        items = []
        for pos, largo, p in lista:
            it = pool.get(os.path.basename(p))
            if it is None:
                return None, 'no quedo en el pool: %s' % p
            items.append({'mediaPoolItem': it, 'startFrame': 0,
                          'endFrame': largo - 1, 'trackIndex': pista,
                          'recordFrame': T0 + pos, 'mediaType': 1})
        mp.AppendToTimeline(items)

    av = pool.get(os.path.basename(voz))
    if av is not None:
        mp.AppendToTimeline([{'mediaPoolItem': av, 'startFrame': 0,
                              'endFrame': dur_cuerpo - 1, 'trackIndex': 1,
                              'recordFrame': T0 + ini, 'mediaType': 2}])
    return tl, None
