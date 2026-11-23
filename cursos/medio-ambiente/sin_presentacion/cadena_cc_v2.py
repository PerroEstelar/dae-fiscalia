# -*- coding: utf-8 -*-
"""Cierre del curso DA v2, sin la presentación de la docente (23 nov 2026). Corre en segundo plano:
componer -> lower third lt01_v2 -> aparta la línea y el .drt de la v1 -> línea nueva -> máster y MP4 v2 -> hoja.
    python cadena_cc_v2.py <python del venv de Resolve>
Log: D:/DAE/_tmp/ma/cc/cadena_v2.log"""
import os, shutil, subprocess, sys, time
VENV = sys.argv[1]
M = r'D:\DAE\_repo\herramientas\montaje'
R = 'E:/DAE MASTER/CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE/CIERRE DEL CURSO'
LOG = 'D:/DAE/_tmp/ma/cc/cadena_v2.log'
env = dict(os.environ, DAE_PLAN='plan_cc', PYTHONUTF8='1')
VIEJA = 'MA - CURSO - CIERRE'
APARTADA = 'MA - CURSO - CIERRE (v1, con presentacion)'


def w(*a):
    with open(LOG, 'a', encoding='utf-8') as f:
        print(time.strftime('%H:%M:%S'), *a, file=f, flush=True)


def paso(nombre, args):
    w('>>', nombre)
    t0 = time.time()
    r = subprocess.run([VENV] + args, cwd=M, env=env, capture_output=True, text=True, encoding='utf-8', errors='replace')
    w(r.stdout[-2500:].strip())
    if r.stderr.strip():
        w('stderr:', r.stderr[-2500:].strip())
    w('<<', nombre, 'rc', r.returncode, '%.0f s' % (time.time() - t0))
    if r.returncode:
        w('CADENA FALLO en', nombre)
        sys.exit(1)


APARTAR = r'''
import DaVinciResolveScript as dvr
resolve = dvr.scriptapp('Resolve')
pr = resolve.GetProjectManager().GetCurrentProject()
print('proyecto', pr.GetName())
tls = [pr.GetTimelineByIndex(i) for i in range(1, int(pr.GetTimelineCount()) + 1)]
nombres = [t.GetName() for t in tls]
if %(apartada)r in nombres:
    print('ya estaba apartada')
else:
    t = [t for t in tls if t.GetName() == %(vieja)r]
    if len(t) != 1:
        raise SystemExit('líneas con ese nombre: %%d' %% len(t))
    print('renombrar', t[0].SetName(%(apartada)r), t[0].GetName())
''' % {'vieja': VIEJA, 'apartada': APARTADA}

if __name__ == '__main__':
    w('== cadena del cierre del curso v2')
    paso('componer', ['ic_pieza.py', 'componer'])
    paso('lower third', ['ic_pieza.py', 'cartones', 'lt01_v2'])
    drt = R + '/10 TIMELINE SEBASTIAN/' + VIEJA + '.drt'
    if os.path.exists(drt):
        os.makedirs(R + '/10 TIMELINE SEBASTIAN/_descartes', exist_ok=True)
        dst = R + '/10 TIMELINE SEBASTIAN/_descartes/' + APARTADA + '.drt'
        shutil.move(drt, dst)
        w('drt v1 ->', dst)
    paso('apartar la línea v1', ['-c', APARTAR])
    paso('línea', ['ic_linea_externa.py'])
    paso('mp4', ['ic_mp4.py', '2'])
    paso('revisión', ['ic_revision.py', '2'])
    w('CADENA LISTA')
