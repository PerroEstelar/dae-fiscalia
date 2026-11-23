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

Un cuarto argumento opcional manda el máster a otra carpeta (el cierre de Bienes, de
43 min, da un máster de ~10 GB que no entra en E:). En `05 EXPORTS/_master` queda un
`LEER - <máster>.txt` que dice dónde está.
"""
import glob
import json
import os
import re
import subprocess
import sys
import time

FB = glob.glob(os.path.expanduser('~') + '/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin')[0]


def _preset():
    """El preset de x264 de la entrega: `slow`, el de la receta. Una entrega **provisional** puede pedir otro
    con `PRESET_ENTREGA` en su plan (el plan llega por `DAE_PLAN`) o con `DAE_PRESET` en el entorno. Los ocho
    videos de unidad de Terminaciones anticipadas (17 nov 2026, «para que salgan más rápido») van con `medium`:
    mismo CRF 18 y mismo formato, archivo algo más grande y casi la mitad de tiempo en un i7 de cuatro núcleos."""
    p = os.environ.get('DAE_PRESET')
    plan = os.environ.get('DAE_PLAN')
    if not p and plan:
        for r, _d, fs in os.walk(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'cursos')):
            if plan + '.py' in fs:
                sys.path.insert(0, r)
                try:
                    p = getattr(__import__(plan), 'PRESET_ENTREGA', None)
                except Exception:
                    p = None
                break
    return p if p in ('medium', 'fast', 'slower', 'slow', 'veryfast', 'nvenc') else 'slow'


PRESET = _preset()
COLOR = ['-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']


def _video(preset):
    if preset == 'nvenc':
        # Entrega URGENTE (cierres de unidad de Bienes, 17 nov 2026: «please hurry, we need to have this before
        # 10 pm», con cuatro videos de 20 a 26 min en cola): H.264 por la placa NVIDIA en calidad constante, que
        # rinde un video de 25 min en pocos minutos y deja el procesador libre para los compuestos. Sigue siendo
        # MP4 H.264 High L4.0 con GOP de 48; no es la receta (x264 CRF 18). Si la placa falla, cae a veryfast.
        # OJO: en el equipo de Sebastián (GTX 970, controlador 582.28) `h264_nvenc` de ffmpeg NO abre («Required:
        # 13.1 Found: 13.0»), así que hoy esta opción siempre cae a veryfast. Los cierres de Bienes salieron al
        # final por Resolve, que sí usa la placa: `cursos/bienes-proceso-penal/unidades/lote/urgente.py`.
        return ['-c:v', 'h264_nvenc', '-preset', 'p6', '-tune', 'hq', '-rc', 'vbr', '-cq', '19', '-b:v', '0',
                '-maxrate', '20M', '-bufsize', '40M', '-g', '48', '-bf', '2',
                '-pix_fmt', 'yuv420p', '-profile:v', 'high', '-level', '4.0', '-movflags', '+faststart'] + COLOR
    return ['-c:v', 'libx264', '-crf', '18', '-preset', preset, '-tune', 'animation',
            '-pix_fmt', 'yuv420p', '-profile:v', 'high', '-level', '4.0',
            '-x264-params', 'keyint=48:min-keyint=24:scenecut=40',
            '-movflags', '+faststart'] + COLOR


VIDEO = _video(PRESET)
URGENTE = PRESET in ('nvenc', 'veryfast')     # sin la pasada de PSNR, que vuelve a decodificar los dos archivos
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


def master(linea, carpeta, nombre, mdir=None):
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
    # NADA OFFLINE (23 nov 2026). La línea del caso 3 de Bienes tenía el intro y el outro sin medio en el pool
    # (`GetMediaPoolItem()` da None): Resolve los rinde como «Media Offline», rojo y en silencio, y el resto del
    # chequeo (cuadros, audio presente) pasa igual. Se vio comparando contra la entrega anterior, ya subida.
    t0l, sin = tl.GetStartFrame(), []
    for k in ('video', 'audio'):
        for n in range(1, tl.GetTrackCount(k) + 1):
            for it in tl.GetItemListInTrack(k, n) or []:
                m = it.GetMediaPoolItem()
                ruta = m.GetClipProperty('File Path') if m else ''
                # un título, un generador o un compuesto no tienen medio: solo cuenta lo que se llama como un archivo
                archivo = os.path.splitext(it.GetName() or '')[1].lower() in (
                    '.mp4', '.mov', '.mxf', '.wav', '.mp3', '.aif', '.aiff', '.m4a', '.png', '.jpg', '.tif', '.tiff')
                if (m is None and archivo) or (ruta and not os.path.exists(ruta)):
                    sin.append('%s%d %s en %d' % (k[0].upper(), n, it.GetName(), it.GetStart() - t0l))
    if sin:
        raise SystemExit('MEDIOS OFFLINE en la línea: ' + '; '.join(sin))
    dst = '%s/05 EXPORTS/_master' % carpeta
    os.makedirs(dst, exist_ok=True)
    nm = nombre + '_master_32mbps'
    if mdir:
        open('%s/LEER - %s.txt' % (dst, nm), 'w', encoding='utf-8').write(
            'El máster %s.mp4 está en\n%s\n(no entra en E:).\n' % (nm, mdir))
        dst = mdir
        os.makedirs(dst, exist_ok=True)
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


def entrega(linea, carpeta, nombre, mdir=None):
    m, largo = master(linea, carpeta, nombre, mdir)
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
    usado = PRESET
    r = subprocess.run([FB + '/ffmpeg.exe', '-y', '-v', 'error', '-i', m] + VIDEO + audio + ['-f', 'mp4', f + '.parcial'])
    if r.returncode and PRESET == 'nvenc':
        usado = 'veryfast'
        w('la placa NVIDIA no pudo (rc %d): va x264 veryfast' % r.returncode)
        r = subprocess.run([FB + '/ffmpeg.exe', '-y', '-v', 'error', '-i', m] + _video('veryfast') + audio
                           + ['-f', 'mp4', f + '.parcial'])
    if r.returncode:
        raise SystemExit('ffmpeg falló (rc %d)' % r.returncode)
    os.replace(f + '.parcial', f)
    j = json.loads(subprocess.run([FB + '/ffprobe.exe', '-v', 'error', '-show_streams', '-of', 'json', f],
                                  capture_output=True, text=True).stdout)
    v_ = [s for s in j['streams'] if s['codec_type'] == 'video'][0]
    a_ = [s for s in j['streams'] if s['codec_type'] == 'audio']
    n = cuadros(f)
    w('preset x264' if usado != 'nvenc' else 'codificador', usado)
    w('entrega %s  %s %s L%s %dx%d %s  cuadros %d / línea %d %s  audio %s  %d MB (máster %d MB)' % (
        os.path.basename(f), v_['codec_name'], v_.get('profile'), v_.get('level'), v_['width'], v_['height'],
        v_.get('color_space'), n, largo, 'OK' if n == largo else 'FALLA',
        ('%s %s Hz %s' % (a_[0]['codec_name'], a_[0]['sample_rate'], a_[0]['channels'])) if a_ else 'FALTA',
        os.path.getsize(f) >> 20, os.path.getsize(m) >> 20))
    w('sonido entrega', medir(f), ' máster', sm)
    if URGENTE:
        w('psnr omitido (entrega urgente)')
    else:
        r = subprocess.run([FB + '/ffmpeg.exe', '-hide_banner', '-nostats', '-i', f, '-i', m, '-lavfi',
                            '[0:v][1:v]psnr', '-f', 'null', '-'], capture_output=True, text=True, errors='replace').stderr
        w('psnr', (re.findall(r'PSNR.*', r) or ['?'])[-1])
    w('LISTO')


if __name__ == '__main__':
    entrega(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else None)
