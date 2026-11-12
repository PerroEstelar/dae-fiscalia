# -*- coding: utf-8 -*-
r"""Introducción al curso de Delitos ambientales (12 nov 2026). Es `te_pieza` con
el plan `cursos/medio-ambiente/introduccion_curso/plan_ic.py`.

- la composición (ventana, Rec.709) y el audio v2 de los profes en un solo paso
  (ecualizado, comprimido, −16 LUFS con techo −3 dBTP: el AAC de Resolve sobrepasa);
- el cartón de título (`titulo_dema` sobre u1v2, subtítulo «Introducción al curso»);
- los cartones de caja y el lower third (`cartones_srpa`);
- las listas de After Effects (`mg_srpa`, en `MA_intros_mg.aep`).

    python ic_pieza.py prueba 20     un cuadro compuesto en el segundo 20 de la fuente
    python ic_pieza.py componer      clip compuesto (video + audio v2)
    python ic_pieza.py titulo        cartón de entrada y salida
    python ic_pieza.py medir         alto, cima y car/s de cada cartón, sin rendir
    python ic_pieza.py cartones      cartones y lower third
    python ic_pieza.py mg_armar      composiciones de AE (AE con MA_intros_mg.aep abierto)
    python ic_pieza.py mg_render     aerender de las composiciones

La línea de Resolve se arma con `ic_linea.py` (dentro de run_inline).
"""
import json
import os
import shutil
import subprocess
import sys
import time

sys.path.insert(0, r'D:\DAE\_repo\cursos\medio-ambiente\introduccion_curso')
sys.path.insert(0, r'D:\DAE\_repo\herramientas\montaje')
sys.path.insert(0, r'D:\DAE\_repo\herramientas\cartones')
sys.path.insert(0, r'D:\DAE\_repo\herramientas\motion')
import plan_ic as P  # noqa: E402


def prueba(t):
    import srpa_composicion as K
    w, h = P.VENTANA
    x, y = P.XY
    out = '%s/prueba_%s.png' % (P.TMP, t)
    subprocess.run([K.FB + '/ffmpeg.exe', '-y', '-v', 'error', '-ss', str(t), '-i', P.ORIGINAL,
                    '-vf', K.escala(x, y, w, h), '-frames:v', '1', out], check=True)
    print(out, flush=True)


def componer():
    import srpa_composicion as K
    import srpa_audio as A
    if os.path.exists(P.COMPUESTO):
        raise SystemExit('ya existe ' + P.COMPUESTO)
    w, h = P.VENTANA
    x, y = P.XY
    fin = K.duracion(P.ORIGINAL)
    base = '[0:a]aresample=48000,' + A.CADENA
    r = subprocess.run([K.FB + '/ffmpeg.exe', '-hide_banner', '-nostats', '-i', P.ORIGINAL, '-filter_complex',
                        base + ',loudnorm=%s:print_format=json[a]' % P.AUDIO_META, '-map', '[a]', '-f', 'null', '-'],
                       capture_output=True, text=True, errors='replace').stderr
    m = json.loads(r[r.rfind('{'):r.rfind('}') + 1])
    ln = ('loudnorm=%s:measured_I=%s:measured_TP=%s:measured_LRA=%s:measured_thresh=%s:offset=%s:linear=true'
          % (P.AUDIO_META, m['input_i'], m['input_tp'], m['input_lra'], m['input_thresh'], m['target_offset']))
    subprocess.run([K.FB + '/ffmpeg.exe', '-y', '-v', 'error', '-i', P.ORIGINAL, '-filter_complex',
                    '[0:v]%s,format=yuv420p[v];%s,%s,aresample=48000[a]' % (K.escala(x, y, w, h), base, ln),
                    '-map', '[v]', '-map', '[a]', '-r', '30', '-t', '%.3f' % fin,
                    '-c:v', 'libx264', '-crf', '16', '-preset', 'fast', '-pix_fmt', 'yuv420p',
                    '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709',
                    '-c:a', 'aac', '-b:a', '256k', '-movflags', '+faststart', '-f', 'mp4',
                    P.COMPUESTO + '.parcial'], check=True)
    os.replace(P.COMPUESTO + '.parcial', P.COMPUESTO)
    r = subprocess.run([K.FB + '/ffmpeg.exe', '-hide_banner', '-nostats', '-i', P.COMPUESTO, '-vn', '-af',
                        'ebur128=peak=true', '-f', 'null', '-'], capture_output=True, text=True, errors='replace').stderr
    print('COMPUESTO  original I %s LRA %s  ->' % (m['input_i'], m['input_lra']),
          ' '.join(r[r.rfind('Summary'):].split())[:300], flush=True)


def titulo():
    import titulo_dema as TD
    TD.SUB = P.SUB
    TD.SRC = P.TITULO_BASE
    TD.DST = P.TITULO
    TD.rendir()


def destino_carton(clave):
    return '%s/02 CARTONES/%s_%s.mov' % (P.R, P.PREFIJO, clave)


def medir():
    import cartones_srpa as CS
    C = CS.C
    for clave, tipo, t0, t1, cont in P.ITEMS:
        if tipo != 'carton':
            continue
        _c, _b, total, off = C.componer(cont)
        largo = sum(len(x[0]) for x in cont)
        aviso = '  <-- SE SUBE DE LA ZONA' if off - C.BAR_PAD < C.ZONA[1] else ''
        print('%-18s %5.1f s  %3d car  %4.1f car/s  alto %3d cima %3d%s' % (
            clave, t1 - t0, largo, largo / (t1 - t0), total, off - C.BAR_PAD, aviso), flush=True)


def cartones(solo=None):
    import cartones_srpa as CS
    C = CS.C
    for clave, tipo, t0, t1, cont in P.ITEMS:
        if solo and not any(clave.startswith(x) for x in solo):
            continue
        n = int(round((t1 - t0) * P.FPS))
        if tipo == 'carton':
            total, off = C.render(cont, n, destino_carton(clave))
            aviso = '  <-- SE SUBE DE LA ZONA' if off - C.BAR_PAD < C.ZONA[1] else ''
            print('%-18s %4d f  alto %3d cima %3d%s' % (clave, n, total, off - C.BAR_PAD, aviso), flush=True)
        elif tipo == 'lt':
            fondo = CS.lower_third(destino_carton(clave), n, cont)
            print('%-18s %4d f  lower third, fondo %d' % (clave, n, fondo), flush=True)
    print('LISTO', flush=True)


def nombre_comp(clave):
    return '%s_%s' % (P.PREFIJO, clave)


def mg_armar():
    import mg_srpa as G
    M = G.M
    info = M.cmd('getProjectInfo', {})
    if os.path.normcase(os.path.normpath(info.get('path') or '')) != os.path.normcase(os.path.normpath(M.AEP)):
        raise SystemExit('AE tiene abierto %r y no %s' % (info.get('path'), M.AEP))
    r = M.cmd('getProjectItems', {})
    existentes = {it['name'] for it in (r['items'] if isinstance(r, dict) else r)}
    usados = set()
    for _c, tipo, _a, _b, d in P.ITEMS:
        if tipo == 'mg_act':
            usados.add(d['icono'])
        elif tipo == 'mg_lista':
            usados |= {f[0] for f in d['filas']}
    for ico in sorted(usados):
        dst = '%s/%s.png' % (M.ICONOS, ico)
        if not os.path.exists(dst):
            shutil.copy2('%s/%s.png' % (G.ICONOS, ico), dst)       # íconos de SRPA
        if 'ico_' + ico not in existentes:
            M.cmd('importFootage', {'path': dst, 'name': 'ico_' + ico})
    for clave, tipo, t0, t1, d in P.ITEMS:
        if tipo not in ('mg_act', 'mg_lista'):
            continue
        nm = nombre_comp(clave)
        n = int(round((t1 - t0) * P.FPS))
        if nm in existentes:
            M.cmd('deleteItem', {'itemName': nm})
        if tipo == 'mg_act':
            c, cima = G.mg_act(nm, n, d)
        else:
            c, cima = G.mg_lista(nm, n, [int(round((f[2] - t0) * P.FPS)) for f in d['filas']], d)
        M.batch(c.c)
        print('%-18s %4d f  %3d capas  cima %d%s' % (clave, n, c.k, cima,
                                                    '  <-- SE SUBE DE LA ZONA' if cima < 250 else ''), flush=True)
    M.cmd('saveProject', {'path': M.AEP})
    print('ARMADO', flush=True)


def mg_render():
    import mg_srpa as G
    M = G.M
    for clave, tipo, t0, t1, d in P.ITEMS:
        if tipo not in ('mg_act', 'mg_lista'):
            continue
        out = '%s/09 MOTION GRAPHICS/%s.mov' % (P.R, nombre_comp(clave))
        if os.path.exists(out) and os.path.getsize(out) > 0:
            continue
        t = time.time()
        subprocess.run([M.AERENDER, '-project', M.AEP.replace('/', '\\'), '-comp', nombre_comp(clave),
                        '-OMtemplate', M.OM, '-output', out.replace('/', '\\')], capture_output=True)
        print('%-18s %s %.0f s' % (clave, 'OK' if os.path.exists(out) else 'FALLA', time.time() - t), flush=True)
    print('RENDER LISTO', flush=True)


if __name__ == '__main__':
    if sys.argv[1] == 'cartones':
        cartones(sys.argv[2:])
    elif sys.argv[1] == 'prueba':
        prueba(sys.argv[2])
    else:
        {'componer': componer, 'titulo': titulo, 'medir': medir, 'mg_armar': mg_armar,
         'mg_render': mg_render}[sys.argv[1]]()
