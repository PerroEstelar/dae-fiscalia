# Rinde cada escena visible (1113x448, texto fijo) y mide scroll; resume el JSON de cada escena.
import json, re, sys, os
from playwright.sync_api import sync_playwright
g = json.load(open('/tmp/claude-0/rev/genially_escenas.json', encoding='utf-8'))
BASE = '/tmp/claude-0/rev/sitio_zip/sitio/jp-audiencias-preliminares/derecho-peticion-accion-tutela/'
solo = sys.argv[1:]  # prefijos de archivo (00..15) opcionales
res = {}
JS = r'''() => {
 const out=[]; 
 for (const el of document.querySelectorAll('*')) {
   const cs=getComputedStyle(el); if (!['auto','scroll'].includes(cs.overflowY)) continue;
   if (el.clientHeight<40 || el.offsetParent===null) continue;
   if (el.scrollHeight>el.clientHeight+8) out.push([el.className.toString().slice(0,40), el.clientHeight, el.scrollHeight]);
 }
 const t=(document.body.innerText||'').split(/\s+/).filter(Boolean).length;
 return {scroll: out, palabras_visibles: t};
}'''
def palabras(s): return len(re.sub('<[^>]+>', ' ', s).split())
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1113, 'height': 448})
    for f, v in g.items():
        ll = f[:2]
        if solo and ll not in solo: continue
        u0 = [s['iframes'][0] for s in v['slides'] if s['iframes'] and 'index.html' in s['iframes'][0]][0]
        rel = re.sub(r'^https://estebanioi\.github\.io/jp-audiencias-preliminares/derecho-peticion-accion-tutela/', '', u0).split('?')[0]
        html = open(BASE + rel, encoding='utf-8').read()
        m = re.search(r'<script[^>]*id="contenido"[^>]*>(.*?)</script>', html, re.S)
        datos = json.loads(m.group(1))
        lec = {'titulo_genially': v['titulo'], 'heading': datos.get('heading'), 'escenas': []}
        for s in v['slides']:
            if s['oculta'] or not s['iframes']: continue
            mm = re.search(r'escena=(\d+)', s['iframes'][0])
            if not mm: continue
            n = int(mm.group(1)); sc = datos['scenes'][n - 1]
            segs = sc.get('segmentos', [])
            items = []
            for bl in sc.get('bloques', []):
                for it in bl.get('items', []) or []:
                    ws = sum(palabras(segs[i]) for i in it.get('segs', []) if isinstance(i, int) and i < len(segs))
                    items.append({'tipo': bl.get('tipo'), 'label': it.get('label'), 'palabras': ws, 'ilus': it.get('ilus')})
            url = 'http://localhost:8765/jp-audiencias-preliminares/derecho-peticion-accion-tutela/' + rel + '?escena=%d' % n
            pg.goto(url, wait_until='load'); pg.wait_for_timeout(600)
            try:
                bt = pg.get_by_text('Clic para texto fijo', exact=False)
                if bt.count(): bt.first.click(timeout=1500); pg.wait_for_timeout(400)
            except Exception: pass
            pg.wait_for_timeout(1200)
            pg.screenshot(path='/tmp/claude-0/rev/escenas/%s_E%02d.png' % (ll, n))
            met = pg.evaluate(JS)
            lec['escenas'].append({'n': n, 'nombre': s['nombre'], 'layout': sc.get('layout'),
                'titulo': sc.get('titulo_genially'), 'mediacion': (sc.get('mediacion') or '')[:120],
                'guia': (sc.get('guia') or '')[:90], 'palabras': sum(palabras(x) for x in segs),
                'parrafos': len(segs), 'bloques': [bl.get('tipo') for bl in sc.get('bloques', [])], 'items': items,
                'ilustracion': sc.get('ilustracion'), 'scroll': met['scroll'], 'audio': 'audio' in json.dumps(sc).lower()})
        res[ll] = lec
        print(ll, len(lec['escenas']), flush=True)
    b.close()
prev = {}
if os.path.exists('/tmp/claude-0/rev/escenas.json'): prev = json.load(open('/tmp/claude-0/rev/escenas.json', encoding='utf-8'))
prev.update(res)
json.dump(prev, open('/tmp/claude-0/rev/escenas.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('LISTO')
