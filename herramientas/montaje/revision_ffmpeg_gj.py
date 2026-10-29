# -*- coding: utf-8 -*-
r"""La revision de Gerencia judicial SIN Resolve: compone la linea con ffmpeg
desde la misma media, el mismo `plan` y las mismas `capas` del montaje.

    python revision_ffmpeg_gj.py T1 [T3 T4]

29 oct: el render de Resolve se colgo dos veces en 0 % (no responde a Stop
y hay que reiniciarlo). Esto arma lo mismo que la linea:
    V1 (intro, carton de entrada, ranuras, respiro, cierre, outro) en fila,
    V2 MOVIMIENTO y V3 DETALLE encima (opacos; el fundido de entrada del V2
    viene horneado), V4 cartones, V6 marca y V8 rotulo con su alfa;
    A1 voz desde el cuerpo, A5 cama de musica, A4 el sonido del intro al
    principio y al final. Sin cambios de nivel: la linea no tiene ninguno.
Salida: D:\DAE\_tmp\gj\revision\GJ_<T>_REVISION_FFMPEG.mp4 (x264 crf 18, AAC)
y despues: cuadros, negros, loudness y la hoja de `revisar`.
NO es la entrega: la entrega sale de Resolve con el OK de Sebastian.
"""
import os
import subprocess
import sys
import time

H = r'D:\DAE\_repo\herramientas'
for sub in ('montaje', 'prompts', 'cartones', os.path.join('voz', 'textos')):
    sys.path.insert(0, os.path.join(H, sub))

import gj_pieza as SP                                     # noqa: E402

FPS = '24000/1001'
FPS_N = 24000 / 1001.0
OUT = os.path.join(SP.TMP, 'revision')


def componer(L):
    v1, v4, v6, voz, mus, ini, dur, tot = SP.plan(L)
    v2, v3, v8, faltan = SP.capas(L)
    assert not faltan, faltan
    ins, fil = [], []

    def entrada(p):
        ins.extend(['-i', p])
        return len(ins) // 2 - 1

    # V1 en fila
    cola = []
    for k, (pos, largo, p) in enumerate(v1):
        i = entrada(p)
        fil.append('[%d:v]trim=end_frame=%d,setpts=PTS-STARTPTS,fps=%s,scale=1920:1080,'
                   'setsar=1,format=yuv420p[a%d]' % (i, largo, FPS, k))
        cola.append('[a%d]' % k)
    fil.append('%sconcat=n=%d:v=1:a=0[base0]' % (''.join(cola), len(cola)))
    cur = 'base0'
    capas = [(x, False) for x in v2 + v3] + [(x, True) for x in v4 + v6 + v8]
    for k, ((pos, largo, p), alfa) in enumerate(capas):
        i = entrada(p)
        fmt = 'yuva420p' if alfa else 'yuv420p'
        fil.append('[%d:v]trim=end_frame=%d,setpts=PTS-STARTPTS,fps=%s,scale=1920:1080,'
                   'format=%s,setpts=PTS+%.6f/TB[c%d]' % (i, largo, FPS, fmt, pos / FPS_N, k))
        fil.append('[%s][c%d]overlay=eof_action=pass:format=auto[o%d]' % (cur, k, k))
        cur = 'o%d' % k
    fil.append('[%s]trim=end_frame=%d,format=yuv420p[v]' % (cur, tot))
    # audio
    iv = entrada(voz)
    im = entrada(mus)
    ii = entrada(SP.INTRO)
    ii2 = entrada(SP.INTRO)
    d_in = int(round(ini / FPS_N * 1000))
    d_out = int(round((tot - SP.N_INTRO) / FPS_N * 1000))
    n_in = SP.N_INTRO / FPS_N
    fil.append('[%d:a]aresample=48000,adelay=%d:all=1[av]' % (iv, d_in))
    fil.append('[%d:a]aresample=48000[am]' % im)
    fil.append('[%d:a]aresample=48000,atrim=0:%.4f[ai]' % (ii, n_in))
    fil.append('[%d:a]aresample=48000,atrim=0:%.4f,asetpts=PTS-STARTPTS,adelay=%d:all=1[ao]'
               % (ii2, n_in, d_out))
    fil.append('[av][am][ai][ao]amix=inputs=4:normalize=0:duration=longest,'
               'atrim=0:%.4f[a]' % (tot / FPS_N))
    os.makedirs(OUT, exist_ok=True)
    sal = os.path.join(OUT, 'GJ_%s_REVISION_FFMPEG.mp4' % L)
    if os.path.exists(sal):
        SP.aparta(sal, 'rehecha_%s' % time.strftime('%H%M%S'))
    fg = os.path.join(SP.TMP, 'revision_%s.filtro' % L)
    open(fg, 'w', encoding='utf-8').write(';\n'.join(fil))
    cmd = ['ffmpeg', '-y', '-v', 'error'] + ins + [
        '-/filter_complex', fg, '-map', '[v]', '-map', '[a]',
        '-r', FPS, '-frames:v', str(tot), '-c:v', 'libx264', '-crf', '18', '-preset', 'medium',
        '-tune', 'animation', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k',
        '-movflags', '+faststart', sal]
    t0 = time.time()
    r = subprocess.run(cmd, capture_output=True, text=True)
    SP.w('%s ffmpeg rc %d  %.0f s  %s' % (L, r.returncode, time.time() - t0, r.stderr[-600:]))
    return sal


def chequear(L, f):
    n = SP.cuadros(f)
    SP.w('cuadros %d / pieza %d  %s' % (n, SP.pieza(L), 'OK' if n == SP.pieza(L) else 'FALLA'))
    r = subprocess.run(['ffmpeg', '-v', 'info', '-i', f, '-vf',
                        'blackdetect=d=0.04:pix_th=0.06', '-an', '-f', 'null', '-'],
                       capture_output=True, text=True).stderr
    negros = [l.split('blackdetect')[1].strip() for l in r.splitlines() if 'black_start' in l]
    SP.w('negros: %s' % (negros or 'ninguno'))
    r = subprocess.run(['ffmpeg', '-nostats', '-i', f, '-af', 'ebur128=peak=true',
                        '-vn', '-f', 'null', '-'], capture_output=True, text=True).stderr
    for l in r.splitlines()[-14:]:
        if l.strip().startswith(('I:', 'Peak:', 'LRA:')):
            SP.w('    ' + l.strip())


def hoja(L, f):
    """La hoja de `revisar`: un cuadro a mitad de cada ranura, movimiento,
    detalle y carton, y el rotulo a los 60 cuadros."""
    from PIL import Image, ImageDraw
    v1, v4, v6, voz, mus, ini, dur, tot = SP.plan(L)
    v2, v3, v8, _ = SP.capas(L)
    marcas = [('V1', pos + largo // 2) for pos, largo, _ in v1]
    marcas += [('V2', pos + largo // 2) for pos, largo, _ in v2]
    marcas += [('V3', pos + largo // 2) for pos, largo, _ in v3]
    marcas += [('V4', pos + largo // 2) for pos, largo, _ in v4]
    marcas += [('V8', pos + 60) for pos, largo, _ in v8]
    marcas = sorted(set(marcas), key=lambda x: x[1])
    tw, th = 480, 270
    out = Image.new('RGB', (4 * tw, ((len(marcas) + 3) // 4) * th), (20, 20, 20))
    d = ImageDraw.Draw(out)
    tmp = os.path.join(SP.TMP, '_q_%s.png' % L)
    for i, (k, q) in enumerate(marcas):
        subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', '%.3f' % ((q + 0.5) / FPS_N),
                        '-i', f, '-frames:v', '1', '-vf', 'scale=%d:%d' % (tw, th), tmp],
                       check=True)
        x, y = (i % 4) * tw, (i // 4) * th
        out.paste(Image.open(tmp), (x, y))
        s = q / FPS_N
        d.rectangle([x, y, x + tw, y + 16], fill=(0, 0, 0))
        d.text((x + 4, y + 2), '%s %d  %d:%05.2f' % (k, q, int(s // 60), s % 60),
               fill=(255, 255, 0))
    hp = os.path.join(SP.TMP, 'revision_ffmpeg_%s.jpg' % L)
    out.save(hp, quality=84)
    SP.w('hoja %s' % hp)


if __name__ == '__main__':
    for L in [a.upper() for a in sys.argv[1:] if not a.startswith('--')]:
        f = os.path.join(OUT, 'GJ_%s_REVISION_FFMPEG.mp4' % L)
        if '--solo-hoja' not in sys.argv:
            SP.w('=== %s revision ffmpeg' % L)
            f = componer(L)
        if os.path.exists(f):
            chequear(L, f)
            hoja(L, f)
    SP.w('LISTO')
