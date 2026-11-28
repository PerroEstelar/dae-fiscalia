
import os, subprocess, glob
FB = glob.glob(os.path.expanduser('~') + '/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin')[0]
R = 'E:/DAE MASTER/PRIORIDAD 2/CURSO - GERENCIA JUDICIAL/VIDEOS PROFE/CURSO/INICIO/01 VIDEO/'
P = R + '_partes/'
V1 = R + 'VIDEO 1 GERENCIA JUDICIAL TOMA1.mp4'
log = open('D:/DAE/_tmp/gj_p/pegar2.out', 'w')
for i in range(1, 5):
    v = P + 'gj_ci_parte%d_video.mp4' % i
    if not os.path.exists(v):
        subprocess.run([FB + '/ffmpeg.exe', '-y', '-v', 'error', '-i', P + 'gj_ci_parte%d.mp4' % i, '-map', '0:v', '-c', 'copy', v], check=True)
open(P + 'lista_video.txt', 'w').write(''.join("file '%sgj_ci_parte%d_video.mp4'\n" % (P, i) for i in range(1, 5)))
dst = R + 'gj_curso_inicio_recortado.mp4'
subprocess.run([FB + '/ffmpeg.exe', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', P + 'lista_video.txt', '-i', V1, '-map', '0:v', '-map', '1:a',
                '-c', 'copy', '-movflags', '+faststart', dst + '.parcial.mp4'], check=True)
os.replace(dst + '.parcial.mp4', dst)
r = subprocess.run([FB + '/ffprobe.exe', '-v', 'error', '-count_packets', '-show_entries', 'stream=codec_type,duration,nb_read_packets', '-of', 'csv', dst], capture_output=True, text=True)
print('LISTO', r.stdout, file=log, flush=True)
