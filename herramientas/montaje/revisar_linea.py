# -*- coding: utf-8 -*-
r"""Revision interna de CUALQUIER linea de Resolve, sin exportar a la carpeta
de entregas: render a una carpeta de trabajo y, sobre ese archivo, cuadros,
negros, loudness y una hoja con un cuadro a mitad de cada clip de V1, V2, V3
y V8.

    python revisar_linea.py "DF C5 LA TIERRA HABLA Y LA MATRIZ DEL SILENCIO" D:\DAE\_tmp\df\revision DF_C5_REVISION_INTERNA
"""
import os
import subprocess
import sys
import time

sys.path.insert(0, r'D:\DAE\_repo\herramientas\montaje')

FPS_N = 24000 / 1001.0


def cuadros(p):
    r = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-count_frames',
                        '-show_entries', 'stream=nb_read_frames', '-of', 'default=nw=1:nk=1', p],
                       capture_output=True, text=True).stdout.split()
    return int(r[0]) if r else -1


def main(nombre, destino, nm):
    import DaVinciResolveScript as dvr
    from PIL import Image, ImageDraw
    import sit_pieza as SP
    resolve = dvr.scriptapp('Resolve')
    pr = resolve.GetProjectManager().GetCurrentProject()
    tl = None
    for i in range(1, int(pr.GetTimelineCount()) + 1):
        t = pr.GetTimelineByIndex(i)
        if t.GetName() == nombre:
            tl = t
    assert tl is not None, nombre
    st = tl.GetStartFrame()
    largo = tl.GetEndFrame() - st
    marcas = []
    for k, pista in ((1, 'V1'), (2, 'V2'), (3, 'V3'), (8, 'V8')):
        if tl.GetTrackCount('video') >= k:
            for it in tl.GetItemListInTrack('video', k):
                a, b = it.GetStart() - st, it.GetEnd() - st
                marcas.append((pista, (a + b) // 2))
    marcas.sort(key=lambda x: x[1])
    os.makedirs(destino, exist_ok=True)
    pr.SetCurrentTimeline(tl)
    pr.DeleteAllRenderJobs()
    m = os.path.join(destino, nm + '.mp4')
    SP.aparta(m, 'rerender_%s' % time.strftime('%H%M%S'))
    pr.SetRenderSettings({'SelectAllFrames': True, 'TargetDir': destino, 'CustomName': nm,
                          'FormatWidth': 1920, 'FormatHeight': 1080, 'VideoQuality': 80000,
                          'AudioCodec': 'lpcm', 'AudioBitDepth': 24, 'AudioSampleRate': 48000})
    pr.SetCurrentRenderFormatAndCodec('mp4', 'H264_NVIDIA')
    job = pr.AddRenderJob()
    pr.StartRendering([job])
    while pr.IsRenderingInProgress():
        time.sleep(3)
    print('render', pr.GetRenderJobStatus(job).get('JobStatus'), flush=True)
    n = cuadros(m)
    print('cuadros %d / linea %d  %s' % (n, largo, 'OK' if n == largo else 'FALLA'), flush=True)
    r = subprocess.run(['ffmpeg', '-v', 'info', '-i', m, '-vf', 'blackdetect=d=0.04:pix_th=0.06',
                        '-an', '-f', 'null', '-'], capture_output=True, text=True).stderr
    print('negros:', [l.split('blackdetect')[1].strip() for l in r.splitlines()
                      if 'black_start' in l] or 'ninguno', flush=True)
    r = subprocess.run(['ffmpeg', '-nostats', '-i', m, '-af', 'ebur128=peak=true', '-vn', '-f',
                        'null', '-'], capture_output=True, text=True).stderr
    for l in r.splitlines()[-14:]:
        if l.strip().startswith(('I:', 'Peak:', 'LRA:')):
            print('   ', l.strip(), flush=True)
    hoja = Image.new('RGB', (4 * 480, ((len(marcas) + 3) // 4) * 270), (20, 20, 20))
    d = ImageDraw.Draw(hoja)
    q = os.path.join(destino, '_q.png')
    for i, (k, f) in enumerate(marcas):
        subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', '%.3f' % ((f + 0.5) / FPS_N), '-i', m,
                        '-frames:v', '1', '-vf', 'scale=480:270', q], check=True)
        x, y = (i % 4) * 480, (i // 4) * 270
        hoja.paste(Image.open(q), (x, y))
        d.text((x + 6, y + 4), '%s %d' % (k, f), fill=(255, 255, 0))
    hp = os.path.join(destino, nm + '_hoja.jpg')
    hoja.save(hp, quality=85)
    print('hoja', hp, flush=True)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
    print('LISTO')
