# -*- coding: utf-8 -*-
r"""Entrega en MP4 de la introducción al curso de Delitos ambientales.

Es la receta de `Entrega_MP4_Fiscalia_Receta.md` (23 oct 2026). Es la misma de
`sr_pieza.exportar` + `entregas`, y la que pide Sebastián: MP4 sin pérdida
visible, no .mov.

1. **Máster de archivo** desde Resolve:
   - MP4 / H.264 NVIDIA, `VideoQuality` 80000 (~32 Mb/s), con audio AAC;
   - va a `05 EXPORTS/_master/<nombre>_master_32mbps.mp4`.
2. **Entrega** con x264:
   - CRF 18, preset slow, tune animation, High L4.0, keyint 48;
   - audio copiado (`-c:a copy`, una sola pasada de AAC), faststart;
   - Rec.709 etiquetado;
   - va a `05 EXPORTS/<nombre>.mp4`.
3. **Verificación:**
   - cuadros = línea, audio presente, sonoridad y pico;
   - PSNR de la entrega contra el máster.

    python ic_mp4.py 1            versión 1
"""
import glob
import json
import os
import re
import subprocess
import sys
import time

sys.path.insert(0, r'D:\DAE\_repo\cursos\medio-ambiente\introduccion_curso')
import plan_ic as P  # noqa: E402

FB = glob.glob(os.path.expanduser('~') + '/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin')[0]
FISCALIA = ['-c:v', 'libx264', '-crf', '18', '-preset', 'slow', '-tune', 'animation',
            '-pix_fmt', 'yuv420p', '-profile:v', 'high', '-level', '4.0',
            '-x264-params', 'keyint=48:min-keyint=24:scenecut=40',
            '-c:a', 'copy', '-movflags', '+faststart',
            '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']


def w(*a):
    print(*a, flush=True)


def cuadros(p):
    r = subprocess.run([FB + '/ffprobe.exe', '-v', 'error', '-count_packets', '-select_streams', 'v',
                        '-show_entries', 'stream=nb_read_packets', '-of', 'csv=p=0', p],
                       capture_output=True, text=True)
    return int((r.stdout.split() or ['0'])[0])     # ffprobe repite el valor en otra línea


def medir(p):
    r = subprocess.run([FB + '/ffmpeg.exe', '-hide_banner', '-nostats', '-i', p, '-vn', '-af',
                        'ebur128=peak=true', '-f', 'null', '-'], capture_output=True, text=True,
                       errors='replace').stderr
    return dict(re.findall(r'(I|LRA|Peak):\s+(-?[\d.]+)', r[r.rfind('Summary'):]))


def master(nombre):
    import DaVinciResolveScript as dvr
    resolve = dvr.scriptapp('Resolve')
    pr = resolve.GetProjectManager().GetCurrentProject()
    tl = None
    for i in range(1, int(pr.GetTimelineCount()) + 1):
        t = pr.GetTimelineByIndex(i)
        if t.GetName() == P.NOMBRE_LINEA:
            tl = t
    if tl is None:
        raise SystemExit('no está la línea ' + P.NOMBRE_LINEA)
    largo = tl.GetEndFrame() - tl.GetStartFrame()
    dst = '%s/05 EXPORTS/_master' % P.R
    os.makedirs(dst, exist_ok=True)
    nm = nombre + '_master_32mbps'
    if os.path.exists('%s/%s.mp4' % (dst, nm)):
        w('el máster ya está: se usa ese (%s)' % nm)
        return '%s/%s.mp4' % (dst, nm), largo
    pr.SetCurrentTimeline(tl)
    resolve.OpenPage('deliver')
    pr.DeleteAllRenderJobs()
    ok_fmt = pr.SetCurrentRenderFormatAndCodec('mp4', 'H264_NVIDIA')
    ok = pr.SetRenderSettings({'SelectAllFrames': True, 'TargetDir': os.path.normpath(dst), 'CustomName': nm,
                               'FormatWidth': 1920, 'FormatHeight': 1080, 'FrameRate': 23.976,
                               'VideoQuality': 80000, 'AudioCodec': 'aac', 'AudioSampleRate': 48000,
                               'ExportVideo': True, 'ExportAudio': True})
    w('formato', ok_fmt, pr.GetCurrentRenderFormatAndCodec(), 'ajustes', ok)
    job = pr.AddRenderJob()
    pr.StartRendering([job])
    t0 = time.time()
    while pr.IsRenderingInProgress():
        time.sleep(3)
    st = pr.GetRenderJobStatus(job)
    w('máster', st.get('JobStatus'), st.get('CompletionPercentage'), '%.0f s' % (time.time() - t0))
    resolve.OpenPage('edit')
    time.sleep(20)          # el máster recién terminado puede no tener todavía el moov
    return '%s/%s.mp4' % (dst, nm), largo


def entrega(v):
    nombre = P.EXPORT % v
    m, largo = master(nombre)
    if cuadros(m) != largo:
        raise SystemExit('el máster mide %d y la línea %d' % (cuadros(m), largo))
    f = '%s/05 EXPORTS/%s.mp4' % (P.R, nombre)
    if os.path.exists(f):
        raise SystemExit('ya existe ' + f)
    subprocess.run([FB + '/ffmpeg.exe', '-y', '-v', 'error', '-i', m] + FISCALIA + ['-f', 'mp4', f + '.parcial'],
                   check=True)
    os.replace(f + '.parcial', f)
    j = json.loads(subprocess.run([FB + '/ffprobe.exe', '-v', 'error', '-show_streams', '-of', 'json', f],
                                  capture_output=True, text=True).stdout)
    v_ = [s for s in j['streams'] if s['codec_type'] == 'video'][0]
    a_ = [s for s in j['streams'] if s['codec_type'] == 'audio']
    n = cuadros(f)
    w('entrega %s  %s %s L%s %dx%d %s  cuadros %d / línea %d %s  audio %s  %d MB (máster %d MB)' % (
        os.path.basename(f), v_['codec_name'], v_.get('profile'), v_.get('level'), v_['width'], v_['height'],
        v_.get('color_space'), n, largo, 'OK' if n == largo else 'FALLA',
        ('%s %s Hz %s' % (a_[0]['codec_name'], a_[0]['sample_rate'], a_[0]['channels'])) if a_ else 'FALTA',
        os.path.getsize(f) >> 20, os.path.getsize(m) >> 20))
    w('sonido entrega', medir(f), ' máster', medir(m))
    r = subprocess.run([FB + '/ffmpeg.exe', '-hide_banner', '-nostats', '-i', f, '-i', m, '-lavfi',
                        '[0:v][1:v]psnr', '-f', 'null', '-'], capture_output=True, text=True, errors='replace').stderr
    w('psnr', (re.findall(r'PSNR.*', r) or ['?'])[-1])
    w('LISTO')


if __name__ == '__main__':
    entrega(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
