# -*- coding: utf-8 -*-
r"""Las bases de la V2: de cada linea centralizada (casos 1, 2, 3, 5 y 6) se
rinden cuatro cosas, sin tocar la linea (las pistas que se apagan se vuelven
a dejar como estaban):

    full    la V1 tal cual, en calidad de master (base del parche)
    limpio  solo imagen, sin las pistas de cartones (V5 en adelante): para
            poner encima un carton nuevo donde haga falta
    voz     solo la narracion (A4 y A5), con la ganancia de la linea
    fondo   todo el audio menos la narracion

    python ch_stems.py [casos...]      (Resolve abierto en DAE MASTER - CURSOS)
Salida: <caso>\05 EXPORTS\_base v2\CH_U1_C0N_<cosa>.mp4/.mov y bases.json
"""
import json
import os
import sys
import time

RAIZ = r'E:\DAE MASTER\PRIORIDAD 1\PROFE CARLOS HUMBERTO'
CARP = {1: 'CASO 01 - Santiago y Valeria', 2: 'CASO 02 - Rodman', 3: 'CASO 03 - Disney',
        5: 'CASO 05 - Juan', 6: 'CASO 06 - Lenin'}
VOZ_PISTAS = {4, 5}
CARTON_DESDE = 5


def w(*a):
    print(*a, flush=True)


def largo(tl):
    st = tl.GetStartFrame()
    fin = 0
    for k in range(1, 5):
        for it in tl.GetItemListInTrack('video', k) or []:
            e = it.GetEnd() - st
            if e < 5000:
                fin = max(fin, e)
    return fin + 1


def render(pr, tl, dest, nm, n, video=True, audio=True, fmt=('mp4', 'H264_NVIDIA')):
    """28 oct: la primera vuelta dejo 'full' sin video y las pistas de audio en
    AAC. SetRenderSettings rechaza el diccionario ENTERO si una clave no vale
    para el contenedor (lpcm en mp4) y quedan los ajustes del render anterior.
    Ahora: video en mp4 con aac, audio solo en mov con lpcm, se mira lo que
    devuelve cada llamada y se comprueba el archivo con ffprobe."""
    import subprocess
    st = tl.GetStartFrame()
    pr.DeleteAllRenderJobs()
    ok_f = pr.SetCurrentRenderFormatAndCodec(*fmt)
    s = {'SelectAllFrames': False, 'MarkIn': st, 'MarkOut': st + n - 1, 'TargetDir': dest,
         'CustomName': nm, 'ExportVideo': video, 'ExportAudio': audio,
         'FormatWidth': 1920, 'FormatHeight': 1080}
    if video:
        s['VideoQuality'] = 80000
    if audio:
        s.update({'AudioCodec': 'aac' if fmt[0] == 'mp4' else 'lpcm',
                  'AudioSampleRate': 48000})
        if fmt[0] != 'mp4':
            s['AudioBitDepth'] = 24
    ok_s = pr.SetRenderSettings(s)
    if not ok_s:
        w('   SetRenderSettings False con', s)
        return 'AJUSTES'
    job = pr.AddRenderJob()
    pr.StartRendering([job])
    t0 = time.time()
    while True:
        e = pr.GetRenderJobStatus(job).get('JobStatus')
        if e in ('Complete', 'Failed', 'Cancelled') or time.time() - t0 > 900:
            break
        if e == 'Ready' and not pr.IsRenderingInProgress() and time.time() - t0 > 20:
            pr.StartRendering([job])
            t0 = time.time()
        time.sleep(2)
    out = [f for f in os.listdir(dest) if f.startswith(nm + '.')]
    if not out:
        return e + ' SIN ARCHIVO'
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'stream=codec_type,codec_name',
                        '-of', 'csv=p=0', os.path.join(dest, out[0])], capture_output=True,
                       text=True).stdout.split()
    tipos = ' '.join(sorted(set(r)))
    if video and 'video' not in tipos:
        return e + ' SIN VIDEO ' + tipos
    if not video and audio and 'pcm' not in tipos:
        return e + ' AUDIO NO PCM ' + tipos
    return e + ' ' + tipos


def duplicado(pr, mp, tl, sufijo, b_trabajo):
    """SetTrackEnable devuelve True pero no apaga la pista (28 oct, comprobado:
    GetIsTrackEnabled sigue en True y el render sale igual). Se trabaja sobre
    un DUPLICADO de la linea al que se le quitan los items; el duplicado se
    guarda en un bin de trabajo, no se borra."""
    nombre = 'ZZ trabajo - %s - %s' % (tl.GetName(), sufijo)
    for i in range(1, int(pr.GetTimelineCount()) + 1):
        t = pr.GetTimelineByIndex(i)
        if t.GetName() == nombre:
            return t
    pr.SetCurrentTimeline(tl)
    d = tl.DuplicateTimeline(nombre)
    root = mp.GetRootFolder()
    for c in mp.GetCurrentFolder().GetClipList() + root.GetClipList():
        if c.GetName() == nombre and c.GetClipProperty('Type') == 'Timeline':
            mp.MoveClips([c], b_trabajo)
    return d


def quitar(tl, kind, pistas):
    items = []
    for k in pistas:
        items += tl.GetItemListInTrack(kind, k) or []
    if items:
        tl.DeleteClips(items, False)
    return len(items)


def main(casos):
    import DaVinciResolveScript as dvr
    resolve = dvr.scriptapp('Resolve')
    pr = resolve.GetProjectManager().GetCurrentProject()
    mp = pr.GetMediaPool()
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import ch_migrar as CM
    tls = {pr.GetTimelineByIndex(i).GetName(): pr.GetTimelineByIndex(i)
           for i in range(1, int(pr.GetTimelineCount()) + 1)}
    bases = {}
    for n in casos:
        nl = 'CH U1 CASO %02d - %s' % (n, CARP[n].split(' - ', 1)[1])
        tl = tls[nl]
        pr.SetCurrentTimeline(tl)
        N = largo(tl)
        dest = os.path.join(RAIZ, CARP[n], '05 EXPORTS', '_base v2')
        os.makedirs(dest, exist_ok=True)
        rel = os.path.relpath(os.path.join(RAIZ, CARP[n]), r'E:\DAE MASTER').split(os.sep)
        b_trabajo = CM.bin_de(mp, rel + ['_trabajo (no usar)'])
        nv, na = int(tl.GetTrackCount('video')), int(tl.GetTrackCount('audio'))
        hay = lambda nm: any(f.startswith(nm + '.') for f in os.listdir(dest))
        r = {}
        if not hay('CH_U1_C%02d_full' % n):
            pr.SetCurrentTimeline(tl)
            r['full'] = render(pr, tl, dest, 'CH_U1_C%02d_full' % n, N)
        if not hay('CH_U1_C%02d_limpio' % n):
            d = duplicado(pr, mp, tl, 'limpio', b_trabajo)
            pr.SetCurrentTimeline(d)
            q = quitar(d, 'video', range(CARTON_DESDE, nv + 1))
            r['limpio'] = '%s (-%d items)' % (render(pr, d, dest, 'CH_U1_C%02d_limpio' % n, N, audio=False), q)
        if not hay('CH_U1_C%02d_voz' % n):
            d = duplicado(pr, mp, tl, 'voz', b_trabajo)
            pr.SetCurrentTimeline(d)
            q = quitar(d, 'audio', [k for k in range(1, na + 1) if k not in VOZ_PISTAS])
            r['voz'] = '%s (-%d items)' % (render(pr, d, dest, 'CH_U1_C%02d_voz' % n, N, video=False,
                                                    fmt=('mov', 'ProRes422')), q)
        if not hay('CH_U1_C%02d_fondo' % n):
            d = duplicado(pr, mp, tl, 'fondo', b_trabajo)
            pr.SetCurrentTimeline(d)
            q = quitar(d, 'audio', [k for k in range(1, na + 1) if k in VOZ_PISTAS])
            r['fondo'] = '%s (-%d items)' % (render(pr, d, dest, 'CH_U1_C%02d_fondo' % n, N, video=False,
                                                      fmt=('mov', 'ProRes422')), q)
        pr.SetCurrentTimeline(tl)
        bases[n] = {'linea': nl, 'largo': N, 'dir': dest, 'resultado': r}
        w(nl, N, r)
    old = {}
    p = r'D:\DAE\_tmp\ch\bases.json'
    if os.path.exists(p):
        old = json.load(open(p, encoding='utf-8'))
    old.update({str(k): v for k, v in bases.items()})
    json.dump(old, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    resolve.GetProjectManager().SaveProject()


if __name__ == '__main__':
    main([int(x) for x in sys.argv[1:]] or [1, 2, 3, 5, 6])
    w('LISTO')
