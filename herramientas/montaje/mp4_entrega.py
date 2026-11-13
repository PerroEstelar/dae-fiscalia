# -*- coding: utf-8 -*-
r"""Entrega en MP4 de cualquier línea de Resolve, con la receta de
`Entrega_MP4_Fiscalia_Receta.md` (23 oct 2026). Es `ic_mp4.py` sin plan: la
línea, la carpeta y el nombre van por argumento.

1. **Máster de archivo** desde Resolve:
   - MP4 / H.264 NVIDIA, `VideoQuality` 80000 (~32 Mb/s), con audio AAC;
   - va a `<carpeta>/05 EXPORTS/_master/<nombre>_master_32mbps.mp4`;
   - si ya existe, se usa ese.
2. **Entrega** con x264:
   - CRF 18, preset slow, tune animation, High L4.0, keyint 48;
   - faststart y Rec.709 etiquetado;
   - va a `<carpeta>/05 EXPORTS/<nombre>.mp4`.
   - El audio se copia (`-c:a copy`) si el pico del máster queda en −1 dBTP o
     menos. El AAC de Resolve sobrepasa unos 2,5 dB en los transitorios
     (entrevista TE, 11 nov). Si el pico pasa de −1, el audio se rehace con el
     limitador de `te_limita`: −2,5 dBFS sobremuestreado a 192 kHz, en AAC a
     320 kb/s.
3. **Verificación:**
   - cuadros = línea y audio presente;
   - sonoridad y pico de la entrega y del máster;
   - PSNR de la entrega contra el máster.

    python mp4_entrega.py "SRPA - CURSO - PRESENTACION" "E:/.../PRESENTACION DEL CURSO" "srpa - CURSO - PRESENTACION-v3"
"""
import glob
import json
import os
import re
import subprocess
import sys
import time

FB = glob.glob(os.path.expanduser('~') + '/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin')[0]
VIDEO = ['-c:v', 'libx264', '-crf', '18', '-preset', 'slow', '-tune', 'animation',
         '-pix_fmt', 'yuv420p', '-profile:v', 'high', '-level', '4.0',
         '-x264-params', 'keyint=48:min-keyint=24:scenecut=40',
         '-movflags', '+faststart',
         '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']
TECHO_COPIA = -1.0           # dBTP: por encima de esto el audio se limita
LIMITE = 10 ** (-2.5 / 20)   # el limitador de te_limita


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


def master(linea, carpeta, nombre):
    import DaVinciResolveScript as dvr
    resolve = dvr.scriptapp('Resolve')
    pr = resolve.GetProjectManager().GetCurrentProject()
    tl = None
    for i in range(1, int(pr.GetTimelineCount()) + 1):
        t = pr.GetTimelineByIndex(i)
        if t.GetName() == linea:
            tl = t
    if tl is None:
        raise SystemExit('no está la línea ' + linea)
    largo = tl.GetEndFrame() - tl.GetStartFrame()
    dst = '%s/05 EXPORTS/_master' % carpeta
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


def entrega(linea, carpeta, nombre):
    m, largo = master(linea, carpeta, nombre)
    if cuadros(m) != largo:
        raise SystemExit('el máster mide %d y la línea %d' % (cuadros(m), largo))
    sm = medir(m)
    if 'I' not in sm:
        raise SystemExit('el máster no tiene audio')
    f = '%s/05 EXPORTS/%s.mp4' % (carpeta, nombre)
    if os.path.exists(f):
        raise SystemExit('ya existe ' + f)
    if float(sm.get('Peak', 0)) <= TECHO_COPIA:
        audio = ['-c:a', 'copy']
        w('audio copiado del máster (pico %s dBTP)' % sm.get('Peak'))
    else:
        audio = ['-af', 'aresample=192000,alimiter=limit=%.4f:attack=1:release=50:level=false,aresample=48000'
                 % LIMITE, '-c:a', 'aac', '-b:a', '320k']
        w('audio limitado: el máster llega a %s dBTP' % sm.get('Peak'))
    subprocess.run([FB + '/ffmpeg.exe', '-y', '-v', 'error', '-i', m] + VIDEO + audio + ['-f', 'mp4', f + '.parcial'],
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
    w('sonido entrega', medir(f), ' máster', sm)
    r = subprocess.run([FB + '/ffmpeg.exe', '-hide_banner', '-nostats', '-i', f, '-i', m, '-lavfi',
                        '[0:v][1:v]psnr', '-f', 'null', '-'], capture_output=True, text=True, errors='replace').stderr
    w('psnr', (re.findall(r'PSNR.*', r) or ['?'])[-1])
    w('LISTO')


if __name__ == '__main__':
    entrega(sys.argv[1], sys.argv[2], sys.argv[3])
