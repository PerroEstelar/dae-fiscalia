# -*- coding: utf-8 -*-
"""Corre una lista de pasos en orden, cada uno con su log. Uso:
    python cadena.py pasos.json
pasos.json = [["log", [args...]], ...]   (args sin el python)"""
import json
import subprocess
import sys
import time

for log, args in json.load(open(sys.argv[1], encoding='utf-8')):
    with open(log, 'a', encoding='utf-8') as f:
        f.write('\n### %s  %s\n' % (time.strftime('%H:%M:%S'), ' '.join(args)))
        f.flush()
        r = subprocess.run([sys.executable, '-u'] + args, stdout=f, stderr=subprocess.STDOUT,
                           cwd=r'D:\DAE\_tmp\sit')
        f.write('### fin %s codigo %d\n' % (time.strftime('%H:%M:%S'), r.returncode))
