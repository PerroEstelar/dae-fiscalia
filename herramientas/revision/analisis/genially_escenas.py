# Lista por lección: título del Genially, diapositivas en orden (nombre, oculta), y el iframe de cada una.
import json, re, glob, sys, os
res = {}
for f in sorted(glob.glob('/tmp/claude-0/rev/sitio_zip/genially/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    raw = open(f, encoding='utf-8').read()
    S = sorted(d['Slides'], key=lambda s: float(s['BigOrder']))
    rc = {}
    for k in ('RichContents',):
        for r in d.get(k, []) or []:
            s = json.dumps(r, ensure_ascii=False).replace('\\/', '/').replace('&amp;', '&')
            m = re.search(r'https://estebanioi\.github\.io/[^"\\\s<>]+', s)
            if m:
                rc.setdefault(r.get('IdSlide') or r.get('SlideId'), []).append(m.group(0))
    titulo = d.get('Title') or d.get('Name') or (d.get('Genially') or {}).get('Name')
    sl = []
    for s in S:
        sl.append({'id': s['Id'], 'nombre': s.get('Name'), 'oculta': bool(s.get('Hidden') or s.get('IsHidden')),
                   'iframes': rc.get(s['Id'], [])})
    res[os.path.basename(f)] = {'titulo': titulo, 'claves': [k for k in d.keys()][:30], 'slides': sl}
json.dump(res, open('/tmp/claude-0/rev/genially_escenas.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for k, v in res.items():
    print(k, '|', v['titulo'], '|', len(v['slides']), 'slides,', sum(1 for s in v['slides'] if s['iframes']), 'con iframe')
