# -*- coding: utf-8 -*-
"""Gerencia judicial, videos de profe (27 nov 2026): subtitulos de cada entrega en cuanto sale.
Mira lote_entrega.log; cuando una entrega queda bien ("entrega plan_<clave> rc 0 True") corre stt_final.py (Scribe sobre
el video final) y srt_de_stt.py con correcciones.json; deja el .srt junto al video en 05 EXPORTS y una copia en la carpeta
de paso de Drive. Termina cuando el lote de entregas termina ("ENTREGAS LISTAS"). Log: subtitulos.log"""
import json, os, shutil, subprocess, sys, time
sys.path.insert(0, 'D:/DAE/_repo/herramientas/entrega')
from subir_exclusivo import copiar_exclusivo
H = 'D:/DAE/_repo/herramientas/subtitulos/'
S = 'D:/DAE/_repo/cursos/gerencia_judicial/subtitulos/'
T = 'D:/DAE/_tmp/gj_p/'
JS, SRT = T + 'stt_final', T + 'srt'
PASO = 'G:/My Drive/_MA subidas/'
MAN = json.load(open(S + 'manifiesto.json', encoding='utf-8'))
log = open(T + 'subtitulos.log', 'a', encoding='utf-8')


def w(*a):
    print(time.strftime('%H:%M:%S'), *a, file=log, flush=True)


hechos = set()
w('subtitulos: arranca')
while True:
    s = open(T + 'lote_entrega.log', encoding='utf-8', errors='replace').read()
    s = s[s.rfind('entrega_ffmpeg: arranca'):] if 'ENTREGAS LISTAS' in s[s.rfind('entrega_ffmpeg: arranca'):] else s
    listos = [m for m in MAN if m['clave'] not in hechos and ('entrega plan_%s rc 0 True' % m['clave']) in s and os.path.exists(m['video'])]
    for m in listos:
        c = m['clave']
        hechos.add(c)
        r = subprocess.run([sys.executable, H + 'stt_final.py', S + 'manifiesto.json', JS, c], capture_output=True, text=True, errors='replace')
        if r.returncode or not os.path.exists('%s/%s.json' % (JS, c)):
            w('STT FALLO', c, r.stderr[-400:]); continue
        r = subprocess.run([sys.executable, H + 'srt_de_stt.py', S + 'manifiesto.json', JS, SRT, S + 'correcciones.json', c],
                           capture_output=True, text=True, errors='replace')
        w('srt', c, r.returncode, r.stdout.strip()[-300:], r.stderr[-300:] if r.returncode else '')
        f = '%s/%s.srt' % (SRT, m['nombre'])
        if r.returncode or not os.path.exists(f):
            continue
        dst = os.path.join(os.path.dirname(m['video']), m['nombre'] + '.srt')
        shutil.copyfile(f, dst)
        nb, md5 = copiar_exclusivo(f, PASO + m['nombre'] + '.srt')
        w('copiado|%s.srt|%d|%s' % (m['nombre'], nb, md5))
    if 'ENTREGAS LISTAS' in s.split('entrega_ffmpeg: arranca')[-1] and not [m for m in MAN if m['clave'] not in hechos and ('entrega plan_%s rc 0 True' % m['clave']) in s]:
        break
    time.sleep(20)
w('SUBTITULOS LISTOS', sorted(hechos))
