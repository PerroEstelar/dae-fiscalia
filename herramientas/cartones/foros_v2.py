# -*- coding: utf-8 -*-
"""Cartones de la tarea del foro sin el antetítulo «Tarea del foro» (23 nov 2026), para los casos que todavía lo
muestran: Bienes U1 (Logística C.M.R. del Norte), Bienes U2 (El siniestro vial) y SRPA U5 caso 1 (Los Chapulines).
Mismo método que `c5u3_foro_v2.py`: primero se rinde el cartón viejo con el código de hoy y se compara cuadro a cuadro
con el archivo entregado; después, el nuevo con el mismo largo, al lado, con « v2» en el nombre.
    python foros_v2.py [clave ...]          Log: D:/DAE/_tmp/c5u3/foros.log"""
import glob, os, shutil, subprocess, sys, time
FB = glob.glob(os.path.expanduser('~') + '/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin')[0]
os.environ['PATH'] = FB + os.pathsep + os.environ['PATH']
sys.path.insert(0, r'D:\DAE\_repo\herramientas\cartones')
import cartones_ta as C

B = 'E:/DAE MASTER/CURSO 5 - Bienes en el proceso penal/'
T = 'D:/DAE/_tmp/c5u3/'
LOG = T + 'foros.log'
J = {
    'c5u1': (B + 'UNIDAD 1/CASO 01 - logistica CMR del norte/02 CARTONES/C5U1_p2_foro_v264.mov', 264, {
        "ante": "Tarea del foro",
        "titulo": "Escoja dos de los seis bienes e identifique a qué categoría pertenece cada uno",
        "cuerpo": "y sustente qué medida procede sobre cada uno y en qué momento procesal."}),
    'c5u2': (B + 'UNIDAD 2/CASO 02 - el siniestro vial/02 CARTONES/C5U2_p2_foro.mov', 296, {
        "ante": "Tarea del foro",
        "titulo": "Escoja dos bienes del inventario y diga qué medida procede sobre cada uno",
        "cuerpo": "y en qué momento procesal, contando el término de seis meses y la caución."}),
    'u5c1': ('E:/DAE MASTER/CURSO 1 - SRPA/UNIDAD 1 - PROFE CARLOS HUMBERTO/UNIDAD 5/cASO 1/02 CARTONES/U5C1_p2_foro.mov', 192, {
        "ante": "Tarea del foro",
        "titulo": "Redacte, para uno de los tres adolescentes, el fundamento de la respuesta que considere aplicable",
        "cuerpo": "indicando qué hechos del expediente la sostienen y qué papel juega su edad al momento de los hechos."}),
}


def w(*a):
    with open(LOG, 'a', encoding='utf-8') as f:
        print(time.strftime('%H:%M:%S'), *a, file=f, flush=True)


def md5s(p):
    r = subprocess.run([FB + '/ffmpeg.exe', '-v', 'error', '-i', p, '-map', '0:v', '-f', 'framemd5', '-'],
                       capture_output=True, text=True)
    return [l.split(',')[-1].strip() for l in r.stdout.splitlines() if l and not l.startswith('#')]


for k in sys.argv[1:] or list(J):
    viejo, n, spec = J[k]
    nuevo = os.path.splitext(viejo)[0] + ' v2.mov'
    w('==', k, os.path.basename(viejo), n, 'cuadros')
    C.render_carton(spec, n, None, True, T + k + '_check.mov', con_tinte=True)
    a, b = md5s(viejo), md5s(T + k + '_check.mov')
    dif = sum(1 for x, y in zip(a, b) if x != y) + abs(len(a) - len(b))
    w(k, 'control: entregado %d cuadros, hoy %d, distintos %d' % (len(a), len(b), dif))
    if dif:
        w(k, 'CONTROL DISTINTO: no se rinde el nuevo')
        continue
    if os.path.exists(nuevo):
        w(k, 'ya existe', nuevo)
        continue
    C.render_carton({x: y for x, y in spec.items() if x != 'ante'}, n, None, True, T + k + '_v2.mov', con_tinte=True)
    m = len(md5s(T + k + '_v2.mov'))
    if m == n:
        shutil.copy2(T + k + '_v2.mov', nuevo)
        w(k, 'nuevo', m, 'cuadros ->', nuevo)
    subprocess.run([FB + '/ffmpeg.exe', '-y', '-v', 'error', '-ss', '5', '-i', viejo, '-ss', '5', '-i', nuevo,
                    '-filter_complex', '[0:v]scale=960:540[a];[1:v]scale=960:540[b];[a][b]hstack', '-frames:v', '1',
                    T + k + '_antes_despues.png'])
w('FOROS LISTOS')
