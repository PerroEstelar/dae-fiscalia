# -*- coding: utf-8 -*-
r"""Conforma insertos de detalle de un capitulo DF y los PONE en la linea viva,
en su sitio, sin remontar.

    python detalle_df_poner.py conformar 5 brocha ojos_analista
    python detalle_df_poner.py poner 5 brocha ojos_analista     (desde Resolve)

Por que no se remonta: la regla del caso (DF_Estado_Timelines, 27 oct) es que
a una linea viva se le AGREGA en su sitio sin tocar lo demas; remontar deja
otra «(anterior)» y se puede llevar una edicion a mano.

conformar  crudo de Kling D:\DAE\_tmp\df\mov\crudos\<det>_crudo<n>.mp4 (el de
           numero mas alto) -> limpieza de bandas y topes de piel de
           detalle_sit.aplica cuadro a cuadro (el factor relativo NO: la
           placa ya se igualo a la madre antes de Kling) -> retime ->
           10 TIMELINE SEBASTIAN/DETALLE/<det>_v<cuadros>.mp4
poner      importa al bin .../10 TIMELINE SEBASTIAN/DETALLE del capitulo y lo
           pone en V3 en ranura + entra (la ranura se lee de la misma linea:
           el item de V1 cuyo archivo empieza con DF_C<cap>_r<nn>_).
"""
import glob
import os
import re
import subprocess
import sys

H = r'D:\DAE\_repo\herramientas'
for sub in ('montaje', 'prompts', 'cartones', os.path.join('voz', 'textos')):
    sys.path.insert(0, os.path.join(H, sub))

import numpy as np                                       # noqa: E402

import detalles_df as DD                                 # noqa: E402
import plan_camara_df as PC                              # noqa: E402

CRUDOS = r'D:\DAE\_tmp\df\mov\crudos'
W, Hh = 1920, 1080


def clave(cap, nom):
    for k in DD.DET:
        if k[0] == cap and k[2] == nom:
            return k
    raise KeyError((cap, nom))


def salida(cap, ran, nom):
    d = DD.DET[(cap, ran, nom)]
    tl = os.path.join(PC.RAIZ, PC.CAPS[cap], '10 TIMELINE SEBASTIAN', 'DETALLE')
    return os.path.join(tl, '%s_v%d.mp4' % (DD.archivo(cap, ran, nom), d['cuadros']))


def conformar(cap, noms):
    import detalle_sit as DS
    import sit_pieza as SP
    for nom in noms:
        cap, ran, nom = clave(cap, nom)
        d = DD.DET[(cap, ran, nom)]
        crudos = sorted(glob.glob(os.path.join(CRUDOS, DD.archivo(cap, ran, nom) + '_crudo*.mp4')))
        crudo = crudos[-1]
        out = salida(cap, ran, nom)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        SP.aparta(out, 'reconformado')
        n0 = SP.cuadros(crudo)
        gente = bool(d['personas'])
        rd = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', crudo, '-vf',
                               'scale=%d:%d:flags=lanczos' % (W, Hh), '-f', 'rawvideo',
                               '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
        wr = subprocess.Popen(['ffmpeg', '-y', '-v', 'error', '-f', 'rawvideo', '-pix_fmt',
                               'rgb24', '-s', '%dx%d' % (W, Hh), '-r', '24', '-i', '-',
                               '-vf', 'setpts=%.9f*PTS,fps=24000/1001' % (float(d['cuadros']) / n0),
                               '-frames:v', str(d['cuadros']), '-c:v', 'libx264', '-crf', '12',
                               '-preset', 'medium', '-pix_fmt', 'yuv420p', '-an', out],
                              stdin=subprocess.PIPE)
        while True:
            b = rd.stdout.read(W * Hh * 3)
            if len(b) < W * Hh * 3:
                break
            fr = np.frombuffer(b, np.uint8).reshape(Hh, W, 3)
            wr.stdin.write(DS.aplica(fr, d['acento'], gente, 1.0).tobytes())
        rd.wait()
        wr.stdin.close()
        wr.wait()
        print('%s  %s  %d -> %d/%d' % (nom, os.path.basename(crudo), n0, SP.cuadros(out),
                                       d['cuadros']), flush=True)


def poner(cap, noms):
    import DaVinciResolveScript as dvr
    resolve = dvr.scriptapp('Resolve')
    pr = resolve.GetProjectManager().GetCurrentProject()
    mp = pr.GetMediaPool()
    nombre = 'DF C%d %s' % (cap, PC.CAPS[cap].split(' - ', 1)[1])
    tl = None
    for i in range(1, int(pr.GetTimelineCount()) + 1):
        t = pr.GetTimelineByIndex(i)
        if t.GetName() == nombre:
            tl = t
    assert tl is not None, nombre
    # AppendToTimeline pone en la linea ACTUAL, no en la que uno tiene en la
    # mano: la primera vez (27 oct) los dos detalles cayeron en «SIT G LA
    # VOCERA», que era la actual. Se sacaron de ahi y se agrego esto.
    pr.SetCurrentTimeline(tl)
    assert pr.GetCurrentTimeline().GetName() == nombre
    st = tl.GetStartFrame()
    inicio = {}
    for it in tl.GetItemListInTrack('video', 1):
        m = it.GetMediaPoolItem()
        n = m.GetName() if m else ''
        mm = re.match(r'^DF_C%d_r(\d\d)_' % cap, n)      # no el «_respiro»
        if mm:
            inicio[int(mm.group(1))] = it.GetStart() - st

    def hijo(f, n):
        for x in f.GetSubFolderList():
            if x.GetName().strip() == n:
                return x
        return None
    f = mp.GetRootFolder()
    rel = os.path.relpath(os.path.join(PC.RAIZ, PC.CAPS[cap], '10 TIMELINE SEBASTIAN', 'DETALLE'),
                          r'E:\DAE MASTER').split(os.sep)
    for p in rel:
        f = hijo(f, p) or mp.AddSubFolder(f, p)
    ya = [(it.GetStart() - st, it.GetEnd() - st) for it in tl.GetItemListInTrack('video', 3)]
    for nom in noms:
        cap, ran, nom = clave(cap, nom)
        d = DD.DET[(cap, ran, nom)]
        p = salida(cap, ran, nom)
        pos = inicio[ran] + d['entra']
        if any(a < pos + d['cuadros'] and pos < b for a, b in ya):
            print('%s ya hay algo en V3 en %d: no se pone' % (nom, pos))
            continue
        mp.SetCurrentFolder(f)
        viejos = [c for c in f.GetClipList() if c.GetName() == os.path.basename(p)]
        it = viejos[0] if viejos else (mp.ImportMedia([p]) or [None])[0]
        r = mp.AppendToTimeline([{'mediaPoolItem': it, 'startFrame': 0,
                                  'endFrame': d['cuadros'], 'trackIndex': 3,
                                  'recordFrame': st + pos, 'mediaType': 1}])
        print('%s V3 %d-%d (ranura r%02d en %d + %d)  %s' % (nom, pos, pos + d['cuadros'], ran,
                                                           inicio[ran], d['entra'], bool(r)))
    print('V3 ahora:', [(it.GetStart() - st, it.GetEnd() - st, it.GetMediaPoolItem().GetName())
                        for it in tl.GetItemListInTrack('video', 3)])
    print('largo', tl.GetEndFrame() - st)
    dest = os.path.join(PC.RAIZ, PC.CAPS[cap], '10 TIMELINE SEBASTIAN', '%s.drt' % nombre)
    if os.path.exists(dest):
        import sit_pieza as SP
        SP.aparta(dest, 'antes_de_detalles_extra')
    tl.Export(dest, resolve.EXPORT_DRT)
    print('.drt', os.path.getsize(dest) if os.path.exists(dest) else 'NO')
    resolve.GetProjectManager().SaveProject()


if __name__ == '__main__':
    paso, cap = sys.argv[1], int(sys.argv[2])
    {'conformar': conformar, 'poner': poner}[paso](cap, sys.argv[3:])
    print('LISTO')
