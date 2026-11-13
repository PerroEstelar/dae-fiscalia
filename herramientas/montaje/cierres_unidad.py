# -*- coding: utf-8 -*-
r"""Cierres de unidad de Delitos ambientales con la intro y el outro de la serie (13 nov 2026).

Pedido de Sebastián: a cada «cierre» (los videos de diapositivas animadas de las
5 unidades) ponerle nuestra intro y nuestro outro, nada más, y entregarlo en
nuestro MP4 sin pérdida visible.

Se hace con ffmpeg en una sola codificación, sin pasar por Resolve: así hay una
generación menos que con el máster de 32 Mb/s.

**Intro y outro:** `FGN_intro_version7.mp4`, sus primeros 194 cuadros (8,09 s), al
principio y al final, igual que en las líneas de Resolve.

**El cierre:**

- Viene en 1280×720 a 24 fps.
- Termina con una tarjeta de «Gemini Notebook», 3,5–4 s en silencio. Sebastián
  pidió quitarla («sí, quítala de las 5»). `inicio_tarjeta` encuentra el corte
  seco a esa tarjeta, y el cierre termina un cuadro antes.
- Se escala a 1920×1080 con lanczos (Rec.709 de entrada y de salida).
- Se pasa a 23,976 con `fps`, que descarta un cuadro cada ~42 s; en diapositivas
  no se nota y el sonido no se mueve.
- El audio, AAC 44,1 kHz mono, pasa a 48 kHz estéreo (el mismo canal a los dos
  lados). Se deja en el nivel en que vino: Sebastián pidió «solo eso».
- Video y audio se cortan al mismo largo exacto: un cuadro a 23,976 son 2002
  muestras a 48 kHz.

**Codificación:** la receta de `Entrega_MP4_Fiscalia_Receta.md`:

- x264 CRF 18, preset slow, tune animation;
- High L4.0, keyint 48, faststart;
- Rec.709 etiquetado;
- el audio en AAC 256k: hay que recodificarlo porque se empalma.

**Verificación:**

- cuadros = 194 + cierre + 194;
- largo del audio igual al del video;
- sonoridad y pico;
- PSNR del tramo del cierre contra la fuente escalada con la misma cadena.

    python cierres_unidad.py 1 2 3 4 5     las unidades que se pidan (por defecto, todas)
"""
import glob
import json
import os
import re
import subprocess
import sys
import time

FB = glob.glob(os.path.expanduser('~') + '/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin')[0]
CURSO = 'E:/DAE MASTER/CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE'
INTRO = 'E:/DAE MASTER/00 COMUNES/INTRO/FGN_intro_version7.mp4'
N_INTRO = 194                      # cuadros de la intro que se usan, al principio y al final
MUESTRAS = 2002                    # muestras a 48 kHz por cuadro a 24000/1001
FPS = '24000/1001'
ESCALA = ('scale=1920:1080:flags=lanczos:in_color_matrix=bt709:out_color_matrix=bt709:'
          'in_range=tv:out_range=tv,setsar=1')
FISCALIA = ['-c:v', 'libx264', '-crf', '18', '-preset', 'slow', '-tune', 'animation',
            '-pix_fmt', 'yuv420p', '-profile:v', 'high', '-level', '4.0',
            '-x264-params', 'keyint=48:min-keyint=24:scenecut=40',
            '-c:a', 'aac', '-b:a', '256k', '-ar', '48000', '-movflags', '+faststart',
            '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709',
            '-color_range', 'tv']


def w(*a):
    print(*a, flush=True)


def fuente(u):
    return '%s/UNIDAD %d/CIERRE DE UNIDAD/01 VIDEO/UNIDAD %d - CIERRE.mp4' % (CURSO, u, u)


def destino(u):
    return '%s/UNIDAD %d/CIERRE DE UNIDAD/05 EXPORTS/unidad %d cierre intro-outro.mp4' % (CURSO, u, u)


def sonda(p):
    return json.loads(subprocess.run([FB + '/ffprobe.exe', '-v', 'error', '-show_streams', '-show_format',
                                      '-of', 'json', p], capture_output=True, text=True).stdout)


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


def inicio_tarjeta(p, dur):
    """Segundo en que entra la tarjeta final de «Gemini Notebook».

    Es un corte seco desde la última diapositiva a una tarjeta clara y quieta
    (luma media ~227) que dura hasta el final. El score de escena del corte va
    de 0,15 (U3, diapositiva casi blanca) a 0,38: el umbral es 0,08 y vale el
    último corte, siempre que lo que sigue sea la tarjeta quieta.
    """
    t0 = max(0.0, dur - 12)
    r = subprocess.run([FB + '/ffmpeg.exe', '-hide_banner', '-ss', '%.3f' % t0, '-i', p, '-an', '-vf',
                        "select='gte(scene,0)',signalstats,metadata=print:file=-", '-f', 'null', '-'],
                       capture_output=True, text=True, errors='replace').stdout
    filas = []
    for linea in r.splitlines():
        if linea.startswith('frame:'):
            filas.append({'t': t0 + float(linea.split('pts_time:')[1]), 's': 0.0, 'y': 0.0})
        elif 'scene_score' in linea:
            filas[-1]['s'] = float(linea.split('=')[1])
        elif 'YAVG' in linea:
            filas[-1]['y'] = float(linea.split('=')[1])
    cortes = [i for i, f in enumerate(filas) if f['s'] > 0.08]
    if not cortes:
        raise SystemExit('no encuentro la tarjeta final en ' + p)
    i = cortes[-1]
    yf = filas[-1]['y']
    if yf < 215 or any(abs(f['y'] - yf) > 4 for f in filas[i:]):
        raise SystemExit('lo que sigue al último corte no es la tarjeta quieta (%s)' % p)
    return filas[i]['t']


def largo_cierre(p):
    """Cuadros del cierre a 23,976, sin la tarjeta final de Gemini Notebook.

    Termina un cuadro (de 24) antes de la tarjeta, para que el `fps` no la
    alcance al redondear al cuadro más cercano.
    """
    j = sonda(p)
    v = [s for s in j['streams'] if s['codec_type'] == 'video'][0]
    a = [s for s in j['streams'] if s['codec_type'] == 'audio'][0]
    dur = min(float(v['duration']), float(a['duration']))
    fin = inicio_tarjeta(p, dur) - 1.0 / 24
    return int(fin * 24000 / 1001), fin, dur


def cadena_cierre(n):
    return ('[1:v]%s,fps=%s,trim=end_frame=%d,setpts=PTS-STARTPTS,format=yuv420p[cv];'
            '[1:a]aresample=48000,pan=stereo|c0=c0|c1=c0,apad,atrim=end_sample=%d,asetpts=PTS-STARTPTS[ca]'
            % (ESCALA, FPS, n, n * MUESTRAS))


def armar(u):
    src, dst = fuente(u), destino(u)
    if os.path.exists(dst):
        w('U%d ya existe %s' % (u, dst))
        return
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    n, fin, dur = largo_cierre(src)
    w('U%d  la tarjeta de Gemini Notebook entra en el %.3f s de %.3f: se quitan %.2f s' % (
        u, fin + 1.0 / 24, dur, dur - fin))
    intro =('[{i}:v]trim=end_frame=%d,setpts=PTS-STARTPTS,setsar=1,format=yuv420p[{k}v];'
             '[{i}:a]aresample=48000,apad,atrim=end_sample=%d,asetpts=PTS-STARTPTS[{k}a]'
             % (N_INTRO, N_INTRO * MUESTRAS))
    fc = ';'.join([intro.format(i=0, k='i0'), cadena_cierre(n), intro.format(i=2, k='i2'),
                   '[i0v][i0a][cv][ca][i2v][i2a]concat=n=3:v=1:a=1[v][a]'])
    t = time.time()
    w('U%d  cierre %d cuadros a 23,976 -> total %d' % (u, n, n + 2 * N_INTRO))
    subprocess.run([FB + '/ffmpeg.exe', '-y', '-v', 'error', '-i', INTRO, '-i', src, '-i', INTRO,
                    '-filter_complex', fc, '-map', '[v]', '-map', '[a]', '-r', FPS] + FISCALIA +
                   ['-f', 'mp4', dst + '.parcial'], check=True)
    os.replace(dst + '.parcial', dst)
    w('U%d  codificado en %.0f s' % (u, time.time() - t))
    verificar(u, n)


def verificar(u, n):
    src, dst = fuente(u), destino(u)
    j = sonda(dst)
    v = [s for s in j['streams'] if s['codec_type'] == 'video'][0]
    a = [s for s in j['streams'] if s['codec_type'] == 'audio']
    total = cuadros(dst)
    esperado = n + 2 * N_INTRO
    dv = esperado * 1001 / 24000
    da = float(a[0]['duration']) if a else 0
    w('U%d  %s %s L%s %dx%d %s %s  cuadros %d / %d %s  audio %s (%.3f s, video %.3f s) %s  %d MB' % (
        u, v['codec_name'], v.get('profile'), v.get('level'), v['width'], v['height'], v.get('r_frame_rate'),
        v.get('color_space'), total, esperado, 'OK' if total == esperado else 'FALLA',
        ('%s %s Hz %sch' % (a[0]['codec_name'], a[0]['sample_rate'], a[0]['channels'])) if a else 'FALTA',
        da, dv, 'OK' if abs(da - dv) < 0.05 else 'DESFASE', os.path.getsize(dst) >> 20))
    w('U%d  sonido entrega %s  fuente %s' % (u, medir(dst), medir(src)))
    fc = ('[0:v]trim=start_frame=%d:end_frame=%d,setpts=PTS-STARTPTS[e];'
          '[1:v]%s,fps=%s,trim=end_frame=%d,setpts=PTS-STARTPTS,format=yuv420p[f];[e][f]psnr'
          % (N_INTRO, N_INTRO + n, ESCALA, FPS, n))
    r = subprocess.run([FB + '/ffmpeg.exe', '-hide_banner', '-nostats', '-i', dst, '-i', src,
                        '-filter_complex', fc, '-f', 'null', '-'], capture_output=True, text=True,
                       errors='replace').stderr
    w('U%d  psnr del cierre contra la fuente escalada: %s' % (u, (re.findall(r'PSNR.*', r) or ['?'])[-1]))


if __name__ == '__main__':
    for u in [int(x) for x in sys.argv[1:]] or [1, 2, 3, 4, 5]:
        armar(u)
    w('LISTO')
