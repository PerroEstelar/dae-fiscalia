# -*- coding: utf-8 -*-
"""Máster de las introducciones de unidad de Medio ambiente (U1-U5) tal como están en Resolve, para sacarles la
presentación de la docente (23 nov 2026). H.264 NVIDIA a VideoQuality 80000 y audio PCM 24 bits en .mov (el corte
de audio se hace sobre PCM). Log: D:/DAE/_tmp/ma/sinpres/masters.log"""
import os, sys, time
import DaVinciResolveScript as dvr
T = 'D:/DAE/_tmp/ma/sinpres/'
OUT = os.path.expanduser('~').replace('\\', '/') + '/AppData/Local/Temp/dae_rindiendo/ma_sinpres'
os.makedirs(OUT, exist_ok=True)
log = open(T + 'masters.log', 'a', encoding='utf-8')


def w(*a):
    print(time.strftime('%H:%M:%S'), *a, file=log, flush=True)


resolve = dvr.scriptapp('Resolve')
pr = resolve.GetProjectManager().GetCurrentProject()
unidades = [int(x) for x in sys.argv[1:]] or [1, 2, 3, 4, 5]
for u in unidades:
    nombre = 'MA - U%d - INTRODUCCION' % u
    tl = None
    for i in range(1, int(pr.GetTimelineCount()) + 1):
        t = pr.GetTimelineByIndex(i)
        if t.GetName() == nombre:
            tl = t
    if tl is None:
        w('NO HAY LINEA', nombre); continue
    while pr.IsRenderingInProgress():
        time.sleep(2)
    largo = tl.GetEndFrame() - tl.GetStartFrame()
    pr.SetCurrentTimeline(tl)
    resolve.OpenPage('deliver')
    pr.DeleteAllRenderJobs()
    pr.SetCurrentRenderFormatAndCodec('mov', 'H264_NVIDIA')
    pr.SetRenderSettings({'SelectAllFrames': True, 'TargetDir': os.path.normpath(OUT), 'CustomName': 'MA_U%d_master' % u,
                          'FormatWidth': 1920, 'FormatHeight': 1080, 'FrameRate': 23.976, 'VideoQuality': 80000,
                          'EncodingProfile': 'High', 'AudioCodec': 'lpcm', 'AudioBitDepth': 24, 'AudioSampleRate': 48000,
                          'ExportVideo': True, 'ExportAudio': True})
    job = pr.AddRenderJob()
    t0 = time.time()
    pr.StartRendering([job])
    while pr.IsRenderingInProgress():
        time.sleep(2)
    time.sleep(10)
    w('master', u, 'largo', largo, pr.GetRenderJobStatus(job), '%.0f s' % (time.time() - t0))
# los ajustes son del proyecto: se devuelven los de la entrega normal
pr.SetCurrentRenderFormatAndCodec('mp4', 'H264_NVIDIA')
pr.SetRenderSettings({'AudioCodec': 'aac', 'SelectAllFrames': True, 'ExportVideo': True, 'ExportAudio': True})
resolve.OpenPage('edit')
w('MASTERS LISTOS')
