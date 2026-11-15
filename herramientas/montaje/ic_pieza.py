# -*- coding: utf-8 -*-
r"""Introducción al curso de Delitos ambientales (12 nov 2026). Es `te_pieza` con
el plan de `DAE_PLAN`: `introduccion_curso/plan_ic.py` (por defecto) o
`cierre_curso/plan_cc.py`.

- la composición (ventana, Rec.709) y el audio v2 de los profes en un solo paso
  (ecualizado, comprimido, −16 LUFS con techo −3 dBTP: el AAC de Resolve sobrepasa);
- el cartón de título (`titulo_dema` sobre u1v2, subtítulo «Introducción al curso»);
- los cartones de caja y el lower third (`cartones_srpa`);
- las listas de After Effects (`mg_srpa`, en `MA_intros_mg.aep`).

    python ic_pieza.py prueba 20     un cuadro compuesto en el segundo 20 de la fuente
    python ic_pieza.py componer      clip compuesto (video + audio v2)
    python ic_pieza.py reimagen <compuesto anterior>   solo la imagen; el audio, del anterior
    python ic_pieza.py titulo        cartón de entrada y salida
    python ic_pieza.py medir         alto, cima y car/s de cada cartón, sin rendir
    python ic_pieza.py cartones      cartones y lower third
    python ic_pieza.py mg_armar      composiciones de AE (AE con MA_intros_mg.aep abierto)
    python ic_pieza.py mg_render     aerender de las composiciones

La línea de Resolve se arma con `ic_linea.py` (dentro de run_inline).
"""
import json
import math
import os
import shutil
import subprocess
import sys
import time

sys.path.insert(0, r'D:\DAE\_repo\herramientas\montaje')
sys.path.insert(0, r'D:\DAE\_repo\herramientas\cartones')
sys.path.insert(0, r'D:\DAE\_repo\herramientas\motion')
import importlib as _il  # noqa: E402
# el plan sale de DAE_PLAN (plan_ic, plan_cc, plan_bi, plan_bc, plan_u4l1…): se busca en cursos/
_plan = os.environ.get('DAE_PLAN', 'plan_ic')
for _r, _ds, _fs in os.walk(r'D:\DAE\_repo\cursos'):
    if _plan + '.py' in _fs:
        sys.path.insert(0, _r)
        break
P = _il.import_module(_plan)  # noqa: E402


def escala(K, x, y, w, h):
    """El recorte y la subida a 1080 de `srpa_composicion`. Las grabaciones de Teams vienen
    en BT.601; una fuente que ya es un export en HD (U3 L5) viene en BT.709 (`MATRIZ_FUENTE`)."""
    m = getattr(P, 'MATRIZ_FUENTE', 'bt601')
    return K.escala(x, y, w, h).replace('in_color_matrix=bt601', 'in_color_matrix=' + m)


def fps_compuesto():
    # 30 para las grabaciones de Teams; una fuente a 23,976 se compone a 23,976 (sin duplicar cuadros)
    return str(getattr(P, 'FPS_COMPUESTO', '30'))


def prueba(t):
    import srpa_composicion as K
    w, h = P.VENTANA
    x, y = P.XY
    out = '%s/prueba_%s.png' % (P.TMP, t)
    subprocess.run([K.FB + '/ffmpeg.exe', '-y', '-v', 'error', '-ss', str(t), '-i', P.ORIGINAL,
                    '-vf', escala(K, x, y, w, h), '-frames:v', '1', out], check=True)
    print(out, flush=True)


def tramos_vf(K, fin):
    """Video y audio de los tramos de P.TRAMOS (cortes de tomas falsas), cada uno con su
    ventana (x, y, w, h) o la del plan. Devuelve el grafo hasta [vc] y [ac] (el audio
    crudo, antes de la cadena v2); los cortes de audio llevan fundidos de 15 ms."""
    w, h = P.VENTANA
    x, y = P.XY
    tr = getattr(P, 'TRAMOS', None) or [(0.0, None, None)]
    # CONGELA [(a, b)]: sobre [a, b) se ve quieto el cuadro de b (una transición horneada en la
    # fuente); el audio sigue corrido. Los bordes se llevan a la rejilla de la fuente.
    fq = getattr(P, 'FPS_FUENTE', 30)
    cong = [(math.floor(c0 * fq + 1e-6) / fq, math.ceil(c1 * fq - 1e-6) / fq) for c0, c1 in getattr(P, 'CONGELA', [])]
    v, a = [], []
    for i, (t0, t1, win) in enumerate(tr):
        t1 = fin if t1 is None else t1
        esc = escala(K, *(win or (x, y, w, h)))
        dentro = [(c0, c1) for c0, c1 in cong if t0 - 1e-6 <= c0 < c1 < t1]
        if not dentro:
            v.append('[0:v]trim=start=%.3f:end=%.3f,setpts=PTS-STARTPTS,%s[v%d]' % (t0, t1, esc, i))
        else:
            ps, t = [], t0
            pre = []
            for j, (c0, c1) in enumerate(dentro):
                if c0 - t > 1e-3:       # un congelado al arranque del tramo no tiene «antes»
                    ps.append('[0:v]trim=start=%.4f:end=%.4f,setpts=PTS-STARTPTS,%s[v%dn%d]' % (t, c0, esc, i, j))
                    pre.append('[v%dn%d]' % (i, j))
                ps.append('[0:v]trim=start=%.4f,setpts=PTS-STARTPTS,trim=end_frame=1,%s,'
                          'tpad=stop_mode=clone:stop_duration=%.4f,trim=duration=%.4f,setpts=PTS-STARTPTS[v%dq%d]'
                          % (c1, esc, c1 - c0, c1 - c0, i, j))
                pre.append('[v%dq%d]' % (i, j))
                t = c1
            ps.append('[0:v]trim=start=%.4f:end=%.3f,setpts=PTS-STARTPTS,%s[v%dz]' % (t, t1, esc, i))
            et = ''.join(pre) + '[v%dz]' % i
            ps.append('%sconcat=n=%d:v=1:a=0[v%d]' % (et, len(pre) + 1, i))
            v.extend(ps)
        af = 'atrim=start=%.3f:end=%.3f,asetpts=PTS-STARTPTS' % (t0, t1)
        if (i > 0 and tr[i - 1][1] != t0) or (i == 0 and t0 > 0):
            af += ',afade=t=in:d=0.015'
        if (i < len(tr) - 1 and tr[i + 1][0] != t1) or (i == len(tr) - 1 and t1 < fin - 0.05):
            af += ',afade=t=out:st=%.3f:d=0.015' % (t1 - t0 - 0.015)
        a.append('[0:a]%s[a%d]' % (af, i))
    n = len(tr)
    return ';'.join(v + a) + ';%sconcat=n=%d:v=1:a=1[vc][ac]' % (''.join('[v%d][a%d]' % (i, i) for i in range(n)), n)


def componer():
    import srpa_composicion as K
    import srpa_audio as A
    if os.path.exists(P.COMPUESTO):
        raise SystemExit('ya existe ' + P.COMPUESTO)
    fin = K.duracion(P.ORIGINAL)
    g = tramos_vf(K, fin)
    base = '[ac]aresample=48000,' + A.CADENA
    r = subprocess.run([K.FB + '/ffmpeg.exe', '-hide_banner', '-nostats', '-i', P.ORIGINAL, '-filter_complex',
                        g + ';' + base + ',loudnorm=%s:print_format=json[a];[vc]nullsink' % P.AUDIO_META,
                        '-map', '[a]', '-f', 'null', '-'],
                       capture_output=True, text=True, errors='replace').stderr
    m = json.loads(r[r.rfind('{'):r.rfind('}') + 1])
    ln = ('loudnorm=%s:measured_I=%s:measured_TP=%s:measured_LRA=%s:measured_thresh=%s:offset=%s:linear=true'
          % (P.AUDIO_META, m['input_i'], m['input_tp'], m['input_lra'], m['input_thresh'], m['target_offset']))
    subprocess.run([K.FB + '/ffmpeg.exe', '-y', '-v', 'error', '-i', P.ORIGINAL, '-filter_complex',
                    g + ';[vc]format=yuv420p[v];%s,%s,aresample=48000[a]' % (base, ln),
                    '-map', '[v]', '-map', '[a]', '-r', fps_compuesto(),
                    '-c:v', 'libx264', '-crf', '16', '-preset', 'fast', '-pix_fmt', 'yuv420p',
                    '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709',
                    '-c:a', 'aac', '-b:a', '256k', '-movflags', '+faststart', '-f', 'mp4',
                    P.COMPUESTO + '.parcial'], check=True)
    os.replace(P.COMPUESTO + '.parcial', P.COMPUESTO)
    r = subprocess.run([K.FB + '/ffmpeg.exe', '-hide_banner', '-nostats', '-i', P.COMPUESTO, '-vn', '-af',
                        'ebur128=peak=true', '-f', 'null', '-'], capture_output=True, text=True, errors='replace').stderr
    print('COMPUESTO  original I %s LRA %s  ->' % (m['input_i'], m['input_lra']),
          ' '.join(r[r.rfind('Summary'):].split())[:300], flush=True)


def reimagen(previo):
    """Recompone solo la imagen, con las ventanas de `P.TRAMOS`, y toma el audio de un
    compuesto anterior del mismo corte. Sirve cuando solo cambia una ventana: el audio v2
    (dos pasadas de loudnorm) ya estaba hecho y no depende de la imagen.

    En el cierre de Bienes el plano cerrado de la frase repetida duraba hasta 2507,9 y en
    su último segundo el profe baja la cabeza: el mentón se salía del cuadro. Se acortó a
    2503,35 y se rehízo la imagen así."""
    import srpa_composicion as K
    if os.path.exists(P.COMPUESTO):
        raise SystemExit('ya existe ' + P.COMPUESTO)
    fin = K.duracion(P.ORIGINAL)
    g = tramos_vf(K, fin)
    os.makedirs(P.TMP, exist_ok=True)
    tmp = '%s/%s_imagen.mp4' % (P.TMP, os.path.splitext(os.path.basename(P.COMPUESTO))[0])
    subprocess.run([K.FB + '/ffmpeg.exe', '-y', '-v', 'error', '-i', P.ORIGINAL, '-filter_complex',
                    g + ';[vc]format=yuv420p[v];[ac]anullsink', '-map', '[v]', '-r', fps_compuesto(),
                    '-c:v', 'libx264', '-crf', '16', '-preset', 'fast', '-pix_fmt', 'yuv420p',
                    '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709',
                    '-f', 'mp4', tmp], check=True)
    subprocess.run([K.FB + '/ffmpeg.exe', '-y', '-v', 'error', '-i', tmp, '-i', previo,
                    '-map', '0:v', '-map', '1:a', '-c', 'copy', '-movflags', '+faststart', '-f', 'mp4',
                    P.COMPUESTO + '.parcial'], check=True)
    os.replace(P.COMPUESTO + '.parcial', P.COMPUESTO)

    def cuenta(x, sel):
        r = subprocess.run([K.FB + '/ffprobe.exe', '-v', 'error', '-count_packets', '-select_streams', sel,
                            '-show_entries', 'stream=nb_read_packets,duration', '-of', 'csv=p=0', x],
                           capture_output=True, text=True).stdout.split()
        return r[0] if r else '?'
    print('REIMAGEN  imagen %s (antes %s)  audio %s (antes %s)' % (
        cuenta(P.COMPUESTO, 'v'), cuenta(previo, 'v'), cuenta(P.COMPUESTO, 'a'), cuenta(previo, 'a')), flush=True)


def titulo():
    if getattr(P, 'CURSO_LINEAS', None):
        # otro curso: el nombre del curso se reescribe (titulo_srpa sobre el mismo fondo u1v2)
        import titulo_srpa as TS
        TS.rendir_fijo(P.CURSO_LINEAS, P.SUB, P.TITULO)
        return
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


def aep_iconos():
    """El proyecto de AE y la carpeta de íconos del plan; por defecto los de Delitos ambientales."""
    import mg_srpa as G
    return getattr(P, 'AEP', G.M.AEP), getattr(P, 'ICONOS', G.M.ICONOS)


def mg_armar():
    import mg_srpa as G
    M = G.M
    AEP, ICONOS = aep_iconos()
    info = M.cmd('getProjectInfo', {})
    if os.path.normcase(os.path.normpath(info.get('path') or '')) != os.path.normcase(os.path.normpath(AEP)):
        raise SystemExit('AE tiene abierto %r y no %s' % (info.get('path'), AEP))
    r = M.cmd('getProjectItems', {})
    existentes = {it['name'] for it in (r['items'] if isinstance(r, dict) else r)}
    usados = set()
    for _c, tipo, _a, _b, d in P.ITEMS:
        if tipo == 'mg_act':
            usados.add(d['icono'])
        elif tipo == 'mg_lista':
            usados |= {f[0] for f in d['filas']}
    os.makedirs(ICONOS, exist_ok=True)
    for ico in sorted(usados):
        dst = '%s/%s.png' % (ICONOS, ico)
        if not os.path.exists(dst):
            src = '%s/%s.png' % (G.ICONOS, ico)                    # íconos de SRPA
            shutil.copy2(src if os.path.exists(src) else '%s/%s.png' % (M.ICONOS, ico), dst)
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
    M.cmd('saveProject', {'path': AEP})
    print('ARMADO', flush=True)


def mg_render():
    import mg_srpa as G
    M = G.M
    AEP = aep_iconos()[0]
    for clave, tipo, t0, t1, d in P.ITEMS:
        if tipo not in ('mg_act', 'mg_lista'):
            continue
        out = '%s/09 MOTION GRAPHICS/%s.mov' % (P.R, nombre_comp(clave))
        if os.path.exists(out) and os.path.getsize(out) > 0:
            continue
        t = time.time()
        subprocess.run([M.AERENDER, '-project', AEP.replace('/', '\\'), '-comp', nombre_comp(clave),
                        '-OMtemplate', M.OM, '-output', out.replace('/', '\\')], capture_output=True)
        print('%-18s %s %.0f s' % (clave, 'OK' if os.path.exists(out) else 'FALLA', time.time() - t), flush=True)
    print('RENDER LISTO', flush=True)


def ajustes():
    """Anchos propios del plan. En la introducción de Bienes el profe está centrado y bajo
    (la cara llega a y≈990 de salida): la columna de cartones y listas se angosta
    (`P.MAXW`) y el lower third lleva el nombre más chico y el cargo más angosto
    (`P.LT` = (px del nombre, ancho del cargo)), para no tapar la cara."""
    if getattr(P, 'MAXW', None):
        import cartones_ma as C0
        import mg_ma as M0
        C0.MAXW = M0.MAXW = P.MAXW
    if getattr(P, 'LT', None):
        import cartones_srpa as CS
        CS.LT_NOMBRE, CS.LT_ANCHO = P.LT


if __name__ == '__main__':
    ajustes()
    if sys.argv[1] == 'cartones':
        cartones(sys.argv[2:])
    elif sys.argv[1] == 'prueba':
        prueba(sys.argv[2])
    elif sys.argv[1] == 'reimagen':
        reimagen(sys.argv[2])
    else:
        {'componer': componer, 'titulo': titulo, 'medir': medir, 'mg_armar': mg_armar,
         'mg_render': mg_render}[sys.argv[1]]()
