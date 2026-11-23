# -*- coding: utf-8 -*-
"""Saca la presentación de la docente (nombre y credenciales) de las introducciones de unidad U1-U5 de Medio
ambiente (23 nov 2026). Pedido: «la profe Diana debe presentarse una única vez, en el video de inicio».

Sobre el máster de cada línea (rinde_masters.py), en cuadros de la línea (23,976):
  - se quitan los cuadros [fA, fB): de la pausa después de «…recursos naturales.» a justo antes de la frase que
    sigue (U1, U2: «En este video…», «En esta oportunidad…»; U3-U5: «y en esta oportunidad…», que queda «Y en esta
    oportunidad…»). Los bordes van en silencio o en el valle de energía antes de la palabra (RMS de 10 ms);
  - después del corte va un plano cerrado (recorte 1664x936 desde (36, 30), x1,154, con el panel DAE/Fiscalía
    entero) hasta el cuadro en que entra el cartón de la unidad, fC; ahí vuelve el plano abierto;
  - el audio se corta en los mismos cuadros (1 cuadro = 2002 muestras a 48 kHz) con fundidos de 12 ms.
El lower third termina en el 569, antes de todos los cortes. Receta de entrega (ic_mp4): x264 CRF 18 slow, tune
animation, High L4.0, keyint 48, AAC 320k, faststart. Log: D:/DAE/_tmp/ma/sinpres/corta.log

    python ma_corta.py [u ...]"""
import glob, json, os, subprocess, sys, time
FB = glob.glob(os.path.expanduser('~') + '/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin')[0]
T = 'D:/DAE/_tmp/ma/sinpres/'
M = os.path.expanduser('~').replace('\\', '/') + '/AppData/Local/Temp/dae_rindiendo/ma_sinpres/'
C = 'E:/DAE MASTER/CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE/'
CORTES = {1: (618, 1293, 1384, 4), 2: (588, 760, 818, 3), 3: (607, 667, 740, 3), 4: (576, 633, 700, 3),
          5: (614, 680, 740, 3)}     # fA, fB, fC, versión nueva
CERRADO = 'crop=1664:936:36:30,scale=1920:1080:flags=lanczos:in_color_matrix=bt709:out_color_matrix=bt709'
FIS = ['-c:v', 'libx264', '-crf', '18', '-preset', 'slow', '-tune', 'animation', '-pix_fmt', 'yuv420p',
       '-profile:v', 'high', '-level', '4.0', '-x264-params', 'keyint=48:min-keyint=24:scenecut=40',
       '-c:a', 'aac', '-b:a', '320k', '-ar', '48000', '-movflags', '+faststart',
       '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']
log = open(T + 'corta.log', 'a', encoding='utf-8')


def w(*a):
    print(time.strftime('%H:%M:%S'), *a, file=log, flush=True)


def cuadros(f):
    r = subprocess.run([FB + '/ffprobe.exe', '-v', 'error', '-count_packets', '-select_streams', 'v:0', '-show_entries',
                        'stream=nb_read_packets', '-of', 'csv=p=0', f], capture_output=True, text=True)
    return int((r.stdout.split() or ['0'])[0])     # ffprobe repite el valor en otra línea (con .mov)


def medir(f):
    r = subprocess.run([FB + '/ffmpeg.exe', '-hide_banner', '-nostats', '-i', f, '-map', '0:a:0', '-af', 'ebur128=peak=true',
                        '-f', 'null', '-'], capture_output=True, text=True, errors='replace')
    s = r.stderr[r.stderr.rfind('Summary:'):]
    out = {}
    for k in ('I:', 'LRA:', 'Peak:'):
        i = s.find(k)
        if i >= 0:
            out[k[:-1]] = s[i + len(k):].split()[0]
    return out


for u in [int(x) for x in sys.argv[1:]] or sorted(CORTES):
    fA, fB, fC, v = CORTES[u]
    src = M + 'MA_U%d_master.mov' % u
    n = cuadros(src)
    out = C + 'UNIDAD %d/05 EXPORTS/delitosambientales - U%d - INTRODUCCION-v%d.mp4' % (u, u, v)
    if os.path.exists(out):
        w('ya existe', out); continue
    sA, sB = fA * 2002, fB * 2002
    g = ('[0:v]trim=start_frame=0:end_frame=%d,setpts=PTS-STARTPTS[v0];'
         '[0:v]trim=start_frame=%d:end_frame=%d,setpts=PTS-STARTPTS,%s[v1];'
         '[0:v]trim=start_frame=%d,setpts=PTS-STARTPTS[v2];'
         '[v0][v1][v2]concat=n=3:v=1:a=0[v];'
         '[0:a]atrim=end_sample=%d,asetpts=PTS-STARTPTS,afade=t=out:st=%.4f:d=0.012[a0];'
         '[0:a]atrim=start_sample=%d,asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.012[a1];'
         '[a0][a1]concat=n=2:v=0:a=1[a]') % (fA, fB, fC, CERRADO, fC, sA, sA / 48000.0 - 0.012, sB)
    t0 = time.time()
    r = subprocess.run([FB + '/ffmpeg.exe', '-y', '-v', 'error', '-i', src, '-filter_complex', g, '-map', '[v]', '-map', '[a]']
                       + FIS + ['-f', 'mp4', out + '.parcial'], capture_output=True, text=True, errors='replace')
    if r.returncode:
        w('FALLO', u, r.stderr[-600:]); continue
    k = cuadros(out + '.parcial')
    esperado = n - (fB - fA)
    son = medir(out + '.parcial')
    if k != esperado:
        w('CUADROS MAL', u, k, esperado); continue
    os.replace(out + '.parcial', out)
    w('LISTO', u, os.path.basename(out), 'cuadros %d = %d - %d' % (k, n, fB - fA), 'sonido', son,
      '%d MB' % (os.path.getsize(out) >> 20), '%.0f s' % (time.time() - t0))
w('CORTES LISTOS')
