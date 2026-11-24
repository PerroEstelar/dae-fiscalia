import json, re, sys
exec(open('/tmp/claude-0/rev/scripts/cobertura_di.py').read().split("res = {}")[0])
keys = list(g.keys())
def seccion(ll, pref, n=420):
    i = [k[:2] for k in keys].index(ll)
    sec = txt[heads[i]:heads[i + 1]]
    m = re.search(r'^' + re.escape(pref) + r'.*$', sec, re.M)
    if not m: return '(no está «%s»)' % pref
    resto = sec[m.start():]
    return re.sub(r'\s+', ' ', resto[:n])
def escena(ll, n, k=420):
    v = g[[x for x in keys if x.startswith(ll)][0]]
    u0 = [s['iframes'][0] for s in v['slides'] if s['iframes'] and 'index.html' in s['iframes'][0]][0]
    rel = re.sub(r'^https://estebanioi\.github\.io/jp-audiencias-preliminares/derecho-peticion-accion-tutela/', '', u0).split('?')[0]
    datos = json.loads(re.search(r'<script[^>]*id="contenido"[^>]*>(.*?)</script>', open(BASE + rel, encoding='utf-8').read(), re.S).group(1))
    sc = datos['scenes'][n - 1]
    return re.sub(r'\s+', ' ', ' | '.join(sc.get('segmentos', [])))[:k]
for a in sys.argv[1:]:
    ll, rest = a.split(':', 1)
    if rest.startswith('E'):
        print('== GEN', ll, rest, ':', escena(ll, int(rest[1:])))
    else:
        print('== DI ', ll, rest, ':', seccion(ll, rest))
