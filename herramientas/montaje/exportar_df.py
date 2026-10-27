# -*- coding: utf-8 -*-
r"""Renderiza los cinco capitulos y saca las dos entregas.

LA RECETA ES LA DE LA FISCALIA, YA MEDIDA
    Resolve rinde MP4 / H264_NVIDIA con VideoQuality 80000 -unos 32 Mbps-
    como master de archivo, y de ahi sale el MP4 de entrega con x264 crf 18
    preset slow tune animation. El master pesado no se entrega: se guarda.

    `VideoQuality` hay que ponerlo EXPLICITO. Si se omite, el render hereda
    la calidad que tenga la pagina Deliver en ese momento, que fue como una
    entrega salio a 8 Mbps sin un solo error.

Y UNA COPIA LIGERA PARA REVISAR EN EL TELEFONO
    720p, crf 25, AAC 128k, faststart. En el P3C5 eso dejo 6:13 en 16,2 MB,
    que es lo que Sebastian pidio para poder mirarlo sin descargar.
"""
import os
import subprocess
import sys
import time

sys.path.insert(0, 'D:/DAE/_repo/herramientas/prompts')
import plan_camara_df as PC                        # noqa: E402

import DaVinciResolveScript as dvr                 # noqa: E402

resolve = dvr.scriptapp('Resolve')
pr = resolve.GetProjectManager().GetCurrentProject()
TMP = r'D:\DAE\_tmp\df\render'
os.makedirs(TMP, exist_ok=True)

lineas = {}
for i in range(1, int(pr.GetTimelineCount()) + 1):
    t = pr.GetTimelineByIndex(i)
    if t.GetName().startswith('DF C'):
        lineas[int(t.GetName()[4])] = t

caps = [int(a) for a in sys.argv[1:]] or [1, 2, 3, 4, 5]
for cap in caps:
    tl = lineas.get(cap)
    if tl is None:
        print('cap %d: no hay linea' % cap, flush=True)
        continue
    pr.SetCurrentTimeline(tl)
    pr.DeleteAllRenderJobs()
    nombre = 'DF_C%d_master' % cap
    ok = pr.SetRenderSettings({
        'SelectAllFrames': True,
        'TargetDir': TMP,
        'CustomName': nombre,
        'FormatWidth': 1920,
        'FormatHeight': 1080,
        'VideoQuality': 80000,          # EXPLICITO, ver el encabezado
        'AudioCodec': 'lpcm',
        'AudioBitDepth': 24,
        'AudioSampleRate': 48000,
    })
    pr.SetCurrentRenderFormatAndCodec('mp4', 'H264_NVIDIA')
    job = pr.AddRenderJob()
    print('cap %d  render %s  (job %s, settings %s)'
          % (cap, nombre, job, ok), flush=True)
    pr.StartRendering([job])
    t0 = time.time()
    while pr.IsRenderingInProgress():
        time.sleep(4)
    st = pr.GetRenderJobStatus(job)
    print('   %s  %s  %.0f s' % (st.get('JobStatus'), st.get('CompletionPercentage'),
                                 time.time() - t0), flush=True)
print('RENDER LISTO', flush=True)
