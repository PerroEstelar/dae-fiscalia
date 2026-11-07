# -*- coding: utf-8 -*-
r"""Baja los crudos de Kling de Delitos ambientales a D:\DAE\_tmp\da\mov\crudos.

    python bajar_mov_da.py crudos.json

crudos.json = {"DA_V01_r03_la_draga": {"url": "...", "hasta": 3.7}, ...}
`desde`/`hasta` (segundos, opcionales) recortan; `hasta` recorta el crudo por el final ANTES del
conformado: Kling a veces mete algo en el ultimo segundo (30 oct, U2 r01:
la mano del fiscal entra por abajo a los 3,8 s a tomar la taza) y
`mov_da.kling` hace el retime sobre el largo del crudo, asi que con cortar
el archivo basta. El entero se guarda en crudos\_enteros\ por si acaso.
No pisa un crudo que ya exista.
"""
import json
import os
import subprocess
import sys
import time
import urllib.request

CRUDOS = r'D:\DAE\_tmp\da\mov\crudos'


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
        # 7 nov (V02 r02): `desde` (segundos) corta tambien la cabeza, cuando
        # lo que sirve empieza con el gesto ya hecho (la carpeta ya abierta:
        # el papel no se anima). El clip cubre la ranura entera y entra en
        # corte seco, asi que no tiene que arrancar en la placa.
        desde = s.get('desde') or 0
        if hasta or desde:
            cmd = ['ffmpeg', '-y', '-v', 'error', '-ss', '%.3f' % desde, '-i', ent]
            if hasta:
                cmd += ['-t', '%.3f' % (hasta - desde)]
            subprocess.run(cmd + ['-c:v', 'libx264', '-crf', '12', '-preset', 'medium',
                                  '-pix_fmt', 'yuv420p', '-an', dst], check=True)
            print(nm, 'recortado %.2f-%s s' % (desde, '%.2f' % hasta if hasta else 'fin'),
                  flush=True)
        else:
            import shutil
            shutil.copyfile(ent, dst)
    print('LISTO')
