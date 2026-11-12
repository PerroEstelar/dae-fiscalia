# Remux final de la introducción al curso (es te_limita.py con plan_ic): video del export de Resolve copiado tal cual y audio con un limitador.
# El AAC de Resolve dejó picos de -0,4 dBTP donde el compuesto tenía -2,9; aquí se limita y se mide.
import glob, os, re, shutil, subprocess, sys, time
sys.path.insert(0, r'D:\DAE\_repo\cursos\medio-ambiente\introduccion_curso')
import plan_ic as P
LOG = open(P.TMP + '/ic_limita.log', 'w', encoding='utf-8', buffering=1)
def log(*a):
    print(*a, file=LOG, flush=True)
FB = glob.glob(os.path.expanduser('~') + '/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin')[0]
V = int(sys.argv[1]) if len(sys.argv) > 1 else 1
f = '%s/05 EXPORTS/%s.mov' % (P.R, P.EXPORT % V)
crudo = '%s/05 EXPORTS/_descartes/%s_resolve_sin_limitar.mov' % (P.R, P.EXPORT % V)
log('fuente', os.path.getsize(f) if os.path.exists(f) else None)
os.makedirs(os.path.dirname(crudo), exist_ok=True)
if not os.path.exists(crudo):
    for _ in range(60):
        try:
            os.rename(f, crudo)
            break
        except PermissionError:
            time.sleep(10)
    else:
        log('NO SE PUDO MOVER (copia en curso?)'); sys.exit(1)

def medir(x):
    r = subprocess.run([FB + '/ffmpeg.exe', '-hide_banner', '-nostats', '-i', x, '-vn', '-af', 'ebur128=peak=true', '-f', 'null', '-'],
                       capture_output=True, text=True, errors='replace').stderr
    return dict(re.findall(r'(I|LRA|Peak):\s+(-?[\d.]+)', r[r.rfind('Summary'):]))

for lim in (0.75, 0.68, 0.6):
    tmp = f + '.parcial.mov'
    subprocess.run([FB + '/ffmpeg.exe', '-y', '-v', 'error', '-i', crudo, '-map', '0:v', '-map', '0:a', '-c:v', 'copy',
                    '-af', 'aresample=192000,alimiter=limit=%s:attack=1:release=50:level=false,aresample=48000' % lim,
                    '-c:a', 'aac', '-b:a', '320k', '-movflags', '+faststart', '-f', 'mov', tmp], check=True)
    m = medir(tmp)
    log('limite', lim, m)
    if float(m['Peak']) <= -1.0:
        os.replace(tmp, f)
        break
else:
    os.replace(tmp, f)
    log('OJO: no bajó de -1')
n = subprocess.run([FB + '/ffprobe.exe', '-v', 'error', '-count_packets', '-select_streams', 'v', '-show_entries',
                    'stream=nb_read_packets,profile', '-of', 'csv=p=0', f], capture_output=True, text=True).stdout
log('video', n.strip(), os.path.getsize(f) // 1000000, 'MB')
log('LISTO')
