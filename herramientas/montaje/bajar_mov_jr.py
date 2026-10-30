# -*- coding: utf-8 -*-
r"""Baja los crudos de Kling de Justicia restaurativa a D:\DAE\_tmp\jr\mov\crudos.

    python bajar_mov_jr.py crudos.json

crudos.json = {"JR_U2_r01_juana_entra": {"url": "...", "hasta": 3.7}, ...}
`hasta` (segundos, opcional) recorta el crudo por el final ANTES del
conformado: Kling a veces mete algo en el ultimo segundo (30 oct, U2 r01:
la mano del fiscal entra por abajo a los 3,8 s a tomar la taza) y
`mov_jr.kling` hace el retime sobre el largo del crudo, asi que con cortar
el archivo basta. El entero se guarda en crudos\_enteros\ por si acaso.
No pisa un crudo que ya exista.
"""
import json
import os
import subprocess
import sys
import time
import urllib.request

CRUDOS = r'D:\DAE\_tmp\jr\mov\crudos'


def bajar(url, ruta):
    err = None
    for _ in range(4):
        try:
            with urllib.request.urlopen(url, timeout=180) as r:
                data = r.read()
            with open(ruta + '.part', 'wb') as f:
                f.write(data)
            os.replace(ruta + '.part', ruta)
            return 'ok %d' % len(data)
        except Exception as e:                                # noqa: BLE001
            err = e
            time.sleep(3)
    return 'FALLA %s' % err


if __name__ == '__main__':
    os.makedirs(os.path.join(CRUDOS, '_enteros'), exist_ok=True)
    for nm, s in sorted(json.load(open(sys.argv[1], encoding='utf-8')).items()):
        dst = os.path.join(CRUDOS, nm + '.mp4')
        if os.path.exists(dst):
            print(nm, 'ya', flush=True)
            continue
        hasta = s.get('hasta')
        ent = os.path.join(CRUDOS, '_enteros', nm + '.mp4')
        print(nm, bajar(s['url'], ent), flush=True)
        if not os.path.exists(ent):
            continue
        if hasta:
            subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', ent, '-t', '%.3f' % hasta,
                            '-c:v', 'libx264', '-crf', '12', '-preset', 'medium',
                            '-pix_fmt', 'yuv420p', '-an', dst], check=True)
            print(nm, 'recortado a %.2f s' % hasta, flush=True)
        else:
            import shutil
            shutil.copyfile(ent, dst)
    print('LISTO')
