# -*- coding: utf-8 -*-
"""En el equipo de Sebastián: arma D:\\DAE\\_sitios\\terminaciones-anticipadas (repo de GitHub Pages).

python armar_sitio_equipo.py <zip_del_sitio> [videos]
  sin «videos»: descomprime el sitio (sin tocar .git ni los .mp4 ya hechos) y escribe los .vtt desde los .srt finales.
  con «videos»: además pasa cada video final a MP4 web (540p, H.264, +faststart) donde falte. Log en _videos.log.
"""
import glob, json, os, re, shutil, subprocess, sys, zipfile

PY = sys.executable
DST = r'D:\DAE\_sitios\terminaciones-anticipadas'
PROFE = r'D:\DAE MASTER\CURSO 4 - Curso Terminaciones Anticipadas'
CASOS = r'E:\DAE MASTER\CURSO 4 - Curso Terminaciones Anticipadas'
PROF = {'curso_inicio': r'INICIO DEL CURSO', 'curso_cierre': r'CIERRE DEL CURSO',
        'u1_inicio': r'UNIDAD 1\INICIO', 'u1_cierre': r'UNIDAD 1\CIERRE', 'u2_inicio': r'UNIDAD 2\INICIO', 'u2_cierre': r'UNIDAD 2\CIERRE',
        'u3_inicio': r'UNIDAD 3\INICIO', 'u3_cierre': r'UNIDAD 3\CIERRE', 'u4_inicio': r'UNIDAD 4\INICIO', 'u4_cierre': r'UNIDAD 4\CIERRE'}
UNI = {'curso_inicio': 1, 'u1_inicio': 1, 'u1_cierre': 1, 'c06': 1, 'c07': 1, 'c08': 1, 'c09': 1, 'u2_inicio': 2, 'u2_cierre': 2,
       'u3_inicio': 3, 'u3_cierre': 3, 'u4_inicio': 4, 'u4_cierre': 4, 'curso_cierre': 4, 'c01': 4, 'c02': 4, 'c03': 4, 'c04': 4, 'c05': 4}


def fuente(k):
    """(video, srt) finales de cada clave."""
    if k in PROF:
        d = os.path.join(PROFE, PROF[k], '05 EXPORTS')
        vs = glob.glob(os.path.join(d, '*.mp4'))
        v = max(vs, key=lambda f: int(re.search(r'-v(\d+)\.mp4$', f).group(1)))
        return v, v[:-4] + '.srt'
    n = int(k[1:])
    d = glob.glob(os.path.join(CASOS, '*', 'CASO %02d - *' % n, '05 EXPORTS'))[0]
    v = [f for f in glob.glob(os.path.join(d, '*.mov')) if '.drt' not in f]
    assert len(v) == 1, (k, v)
    s = glob.glob(os.path.join(d, '*.srt'))
    assert len(s) == 1, (k, s)
    return v[0], s[0]


def vtt(srt, out):
    t = open(srt, encoding='utf-8-sig').read().replace('\r\n', '\n')
    t = re.sub(r'(\d\d:\d\d:\d\d),(\d\d\d)', r'\1.\2', t)
    open(out, 'w', encoding='utf-8', newline='\n').write('WEBVTT\n\n' + t.strip() + '\n')


def main():
    z, hacer_videos = sys.argv[1], 'videos' in sys.argv[2:]
    os.makedirs(DST, exist_ok=True)
    with zipfile.ZipFile(z) as f:
        f.extractall(DST)
    filas = []
    for k, u in UNI.items():
        v, s = fuente(k)
        dv = os.path.join(DST, 'unidad-%02d' % u, 'comun', 'videos')
        os.makedirs(dv, exist_ok=True)
        vtt(s, os.path.join(dv, k + '.vtt'))
        filas.append((k, u, v, s, os.path.exists(os.path.join(dv, k + '.mp4'))))
    for r in filas:
        print(r[0], r[1], os.path.basename(r[2]), '|', os.path.basename(r[3]), '| mp4 listo' if r[4] else '| mp4 falta')
    if hacer_videos:
        cmds = []
        for k, u, v, s, listo in filas:
            if listo:
                continue
            o = os.path.join(DST, 'unidad-%02d' % u, 'comun', 'videos', k + '.mp4')
            cmds.append([k, v, o])
        json.dump(cmds, open(os.path.join(DST, '..', '_ta_videos_cola.json'), 'w', encoding='utf-8'), ensure_ascii=False)
        log = open(os.path.join(DST, '..', '_ta_videos.log'), 'a', encoding='utf-8')
        subprocess.Popen([PY, os.path.abspath(__file__), '_cola'], stdout=log, stderr=log,
                         creationflags=0x00000008 | 0x00000200, close_fds=True)
        print('cola lanzada:', len(cmds), 'videos')


def cola():
    cmds = json.load(open(os.path.join(DST, '..', '_ta_videos_cola.json'), encoding='utf-8'))
    for k, v, o in cmds:
        p = o[:-4] + '.parcial.mp4'
        r = subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-i', v, '-vf', 'scale=-2:540:flags=lanczos', '-c:v', 'libx264',
                            '-preset', 'medium', '-crf', '26', '-profile:v', 'high', '-pix_fmt', 'yuv420p',
                            '-c:a', 'aac', '-b:a', '96k', '-ac', '2', '-movflags', '+faststart', p])
        if r.returncode == 0:
            os.replace(p, o)
        print(k, 'ok' if r.returncode == 0 else 'ERROR %d' % r.returncode, round(os.path.getsize(o) / 1e6, 1) if os.path.exists(o) else '', flush=True)
    print('FIN', flush=True)


if __name__ == '__main__':
    cola() if sys.argv[1:] == ['_cola'] else main()
