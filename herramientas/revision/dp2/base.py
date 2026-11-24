# -*- coding: utf-8 -*-
"""Base de Derecho de petición (sitio de JP, 23 nov): leer y escribir el JSON de cada lección."""
import json, re
DP = '/tmp/claude-0/rev/sitio_zip/sitio/jp-audiencias-preliminares/derecho-peticion-accion-tutela/'
RE = re.compile(r'(<script type="application/json" id="contenido">)(.*?)(</script>)', re.S)

def ruta(u, l):
    return DP + 'unidad-%02d/leccion-%02d/index.html' % (u, l)

def leer(u, l):
    h = open(ruta(u, l), encoding='utf-8').read()
    return json.loads(RE.search(h).group(2))

LECC = [(u, l) for u in range(1, 5) for l in range(1, 5)]
