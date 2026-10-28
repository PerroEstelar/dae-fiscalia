# -*- coding: utf-8 -*-
r"""Las bases de la V2, UNA por llamada (28 oct).

Por que existe: ch_stems.py lanzado como proceso suelto se quedaba colgado con
el trabajo en 'Ready' (el mismo render, desde run_inline, sale en 9 s). Asi que
el trabajo se lanza desde la sesion de Resolve y se consulta despues:

    kick(pr, n, cosa)   deja andando el render de `cosa` del caso n y vuelve
    estado(pr)          como va el trabajo y, si termino, que trae el archivo

cosa: full (V1 tal cual, video+aac) | limpio (solo imagen, sin V5..V8) |
      voz (solo A4/A5, mov lpcm 24) | fondo (todo menos A4/A5, mov lpcm 24)
Los duplicados de trabajo se reutilizan si ya existen (no se borra nada).
"""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ch_stems as S        # noqa: E402
import ch_migrar as CM      # noqa: E402

COSAS = ('full', 'limpio', 'voz', 'fondo')


def linea(pr, n):
    nl = 'CH U1 CASO %02d - %s' % (n, S.CARP[n].split(' - ', 1)[1])
    for i in range(1, int(pr.GetTimelineCount()) + 1):
        t = pr.GetTimelineByIndex(i)
        if t.GetName() == nl:
            return t
    raise KeyError(nl)


def destino(n):
    d = os.path.join(S.RAIZ, S.CARP[n], '05 EXPORTS', '_base v2')
    os.makedirs(d, exist_ok=True)
    return d


def kick(pr, n, cosa):
    mp = pr.GetMediaPool()
    tl = linea(pr, n)
    N = S.largo(tl)
    dest = destino(n)
    nm = 'CH_U1_C%02d_%s' % (n, cosa)
    if any(f.startswith(nm + '.') for f in os.listdir(dest)):
        return 'YA EXISTE ' + nm
    if cosa == 'full':
        d = tl
    else:
        rel = os.path.relpath(os.path.join(S.RAIZ, S.CARP[n]), r'E:\DAE MASTER').split(os.sep)
        b = CM.bin_de(mp, rel + ['_trabajo (no usar)'])
        d = S.duplicado(pr, mp, tl, cosa, b)
        nv, na = int(tl.GetTrackCount('video')), int(tl.GetTrackCount('audio'))
        if cosa == 'limpio':
            S.quitar(d, 'video', range(S.CARTON_DESDE, nv + 1))
        elif cosa == 'voz':
            S.quitar(d, 'audio', [k for k in range(1, na + 1) if k not in S.VOZ_PISTAS])
        else:
            S.quitar(d, 'audio', [k for k in range(1, na + 1) if k in S.VOZ_PISTAS])
    pr.SetCurrentTimeline(d)
    st = d.GetStartFrame()
    video = cosa in ('full', 'limpio')
    audio = cosa != 'limpio'
    pr.DeleteAllRenderJobs()
    fmt = ('mp4', 'H264_NVIDIA') if video else ('mov', 'ProRes422')
    if not pr.SetCurrentRenderFormatAndCodec(*fmt):
        return 'FORMATO ' + str(fmt)
    s = {'SelectAllFrames': False, 'MarkIn': st, 'MarkOut': st + N - 1, 'TargetDir': dest,
         'CustomName': nm, 'ExportVideo': video, 'ExportAudio': audio}
    if video:
        s.update({'FormatWidth': 1920, 'FormatHeight': 1080, 'VideoQuality': 80000})
    if audio:
        s.update({'AudioCodec': 'aac' if video else 'lpcm', 'AudioSampleRate': 48000})
        if not video:
            s['AudioBitDepth'] = 24
    # Recien cambiada la linea actual, SetRenderSettings a veces devuelve
    # False con un diccionario que un segundo despues acepta (28 oct).
    import time
    # Y despues de un render de solo audio en mov, el diccionario entero no
    # entra hasta que se pasan las claves una por una (28 oct).
    for _ in range(5):
        if pr.SetRenderSettings(s):
            break
        malas = [k for k, v in s.items() if not pr.SetRenderSettings({k: v})]
        time.sleep(1)
    else:
        return 'AJUSTES (claves que no entran: %s) %s' % (malas, s)
    job = pr.AddRenderJob()
    pr.StartRendering([job], False)
    return 'ANDANDO %s %s N=%d' % (nm, job, N)


def estado(pr):
    jobs = pr.GetRenderJobList() or []
    out = []
    for j in jobs:
        e = pr.GetRenderJobStatus(j['JobId'])
        linea_ = '%s %s %s%%' % (j.get('OutputFilename'), e.get('JobStatus'),
                                 e.get('CompletionPercentage'))
        if e.get('JobStatus') == 'Complete':
            p = os.path.join(j.get('TargetDir'), j.get('OutputFilename'))
            r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries',
                                'stream=codec_type,codec_name:format=duration', '-of', 'csv=p=0', p],
                               capture_output=True, text=True).stdout.split()
            linea_ += ' | ' + ' '.join(r) + ' | %d MB' % (os.path.getsize(p) // 2 ** 20)
        out.append(linea_)
    return out, pr.IsRenderingInProgress()
