import json, re, unicodedata, sys
exec(open('/tmp/claude-0/rev/scripts/cobertura_di.py').read().split("res = {}")[0])
c = json.load(open('/tmp/claude-0/rev/cobertura.json', encoding='utf-8'))
for i, (f, v) in enumerate(g.items()):
    ll = f[:2]
    if ll not in sys.argv[1:]: continue
    sec = txt[heads[i]:heads[i + 1]]
    corte = re.search(r'^\s*\d\.\d+\.?\s*Recursos académicos', sec, re.M)
    if corte: sec = sec[:corte.start()]
    falt = set(c[ll]['faltan'])
    # recorrer por encabezados numerados
    partes = re.split(r'\n(?=\d+(?:\.\d+)*\.?\s+[A-ZÁÉÍÓÚÑ¿])', sec)
    print('##', ll, v['titulo'][:18])
    for p in partes:
        h = p.split('\n')[0][:70]
        cuerpo = p.replace('-\n', '').replace('\n', ' ')
        fr = [x.strip() for x in re.split(r'(?<=[.:;?])\s+', cuerpo) if len(x.split()) >= 7]
        nf = sum(1 for x in fr if x in falt)
        if nf: print('   %2d/%2d  %s' % (nf, len(fr), h))
