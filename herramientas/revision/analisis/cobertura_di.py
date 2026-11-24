# Compara el texto del DI de cada lección con el texto de sus escenas visibles: frases del DI que no aparecen.
import json, re, unicodedata
g = json.load(open('/tmp/claude-0/rev/genially_escenas.json', encoding='utf-8'))
BASE = '/tmp/claude-0/rev/sitio_zip/sitio/jp-audiencias-preliminares/derecho-peticion-accion-tutela/'
di = open('/tmp/claude-0/rev/di.txt', encoding='utf-8').read().split('\n')
limpio = [l for l in di if not l.startswith('######## PAGINA') and 'Ficha para la escritura' not in l
          and 'Proyecto Fiscalía General de la Nación - Universidad' not in l and 'Formato basado' not in l
          and 'virtuales en el marco del contrato' not in l]
txt = '\n'.join(limpio)
heads = [m.start() for m in re.finditer(r'^Lección [1-4]\.[1-4]\. ', txt, re.M)]
heads.append(len(txt))
def norm(s):
    s = unicodedata.normalize('NFKD', s.lower()); s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()
res = {}
for i, (f, v) in enumerate(g.items()):
    ll = f[:2]
    sec = txt[heads[i]:heads[i + 1]]
    corte = re.search(r'^\s*\d\.\d+\.?\s*Recursos académicos', sec, re.M)
    if corte: sec = sec[:corte.start()]
    sec = sec.replace('-\n', '').replace('\n', ' ')
    u0 = [s['iframes'][0] for s in v['slides'] if s['iframes'] and 'index.html' in s['iframes'][0]][0]
    rel = re.sub(r'^https://estebanioi\.github\.io/jp-audiencias-preliminares/derecho-peticion-accion-tutela/', '', u0).split('?')[0]
    datos = json.loads(re.search(r'<script[^>]*id="contenido"[^>]*>(.*?)</script>', open(BASE + rel, encoding='utf-8').read(), re.S).group(1))
    vis = set()
    for s in v['slides']:
        if s['oculta'] or not s['iframes']: continue
        m = re.search(r'escena=(\d+)', s['iframes'][0])
        if m: vis.add(int(m.group(1)))
    esc = ' '.join(norm(json.dumps(datos['scenes'][n - 1], ensure_ascii=False)) for n in sorted(vis))
    frases = [x.strip() for x in re.split(r'(?<=[.:;?])\s+', sec) if len(x.split()) >= 7]
    faltan = []
    for fr in frases:
        nf = norm(fr)
        w = nf.split()
        # presente si algún tramo de 7 palabras seguidas está en las escenas
        ok = any(' '.join(w[j:j + 7]) in esc for j in range(0, max(1, len(w) - 6), 3))
        if not ok: faltan.append(fr)
    res[ll] = {'frases': len(frases), 'faltan': faltan}
    print(ll, 'frases DI', len(frases), 'no aparecen', len(faltan))
json.dump(res, open('/tmp/claude-0/rev/cobertura.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
