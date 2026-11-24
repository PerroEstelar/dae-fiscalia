# -*- coding: utf-8 -*-
"""Un HTML autocontenido por lección: el Genially (portada, índice, una diapositiva por escena, fin) y las mediaciones,
todo dentro de un solo archivo, sin depender de Genially ni de GitHub. Para subir a la plataforma de la Fiscalía.

python3 armar.py ta|dp [1.1 …]   ->  out/<curso>/<archivo>.html

Cómo está hecho
- El marco sale del mismo buffer con que se armó el Genially nativo (genially/lUL.json): cada elemento (texto, SVG,
  imagen, grupo, contenido enriquecido) se dibuja en su sitio sobre un lienzo de 1200 × 675 que se escala a la ventana.
  Flechas, menú e índice usan las mismas interactividades (siguiente, anterior, ir a la diapositiva).
- Cada contenido enriquecido (iframe de Pages) pasa a un iframe «srcdoc» con la página del motor en línea (CSS, fuentes,
  objetos.js y app.js parcheado): ?escena=N, instrucciones.html?modo=boton y fin.html.
- Los archivos (ilustraciones, PDF, PNG, audios, videos, subtítulos, pósteres) van en base64 dentro del HTML y se vuelven
  Blob URL solo cuando se piden (window.__ovaR). app.js pide cada ruta por __R(), que sube por los marcos hasta el lector.
- El lector publica window.ovaLeccion (pantallaCompleta, enPantallaCompleta, ventana, cerrarVentana): el contrato que
  app.js e instrucciones.html ya traen para el SCORM dibujado desde Genially.
"""
import base64, glob, html, json, mimetypes, os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(AQUI, 'assets')
CURSOS = {
    'ta': dict(sitio='/home/claude/ta/out/sitio/', videos=os.path.join(AQUI, 'videos'), prefijo='TA',
               carpeta='Terminaciones anticipadas', curso='Terminaciones anticipadas del proceso penal'),
    'dp': dict(sitio='/home/claude/dp2/out/sitio/derecho-peticion/', videos=None, prefijo='DP',
               carpeta='Derecho de peticion', curso='Derecho de petición y acción de tutela'),
}
RE_CONT = re.compile(r'(<script type="application/json"[^>]*id="contenido"[^>]*>)(.*?)(</script>)', re.S)
MIME = {'.webp': 'image/webp', '.png': 'image/png', '.jpg': 'image/jpeg', '.svg': 'image/svg+xml', '.pdf': 'application/pdf',
        '.mp4': 'video/mp4', '.vtt': 'text/vtt', '.mp3': 'audio/mpeg', '.woff2': 'font/woff2', '.ttf': 'font/ttf',
        '.html': 'text/html'}


def b64(p):
    return base64.b64encode(open(p, 'rb').read()).decode('ascii')


def data_uri(p):
    return 'data:%s;base64,%s' % (MIME.get(os.path.splitext(p)[1].lower(), 'application/octet-stream'), b64(p))


def sin_cierre(js):
    """Un </script> dentro de un script en línea cortaría el bloque."""
    return js.replace('</script', '<\\/script').replace('<!--', '<\\!--')


# ---------------------------------------------------------------- páginas del motor en línea
def css_en_linea(ruta):
    t = open(ruta, encoding='utf-8').read()
    base = os.path.dirname(ruta)

    def rep(m):
        u = m.group(2)
        if u.startswith('data:') or u.startswith('#'):
            return m.group(0)
        p = os.path.normpath(os.path.join(base, u.split('?')[0].split('#')[0]))
        if not os.path.exists(p):
            return 'url("")'   # fuentes alternativas (.ttf) que el sitio no trae: el navegador usa la woff2
        return 'url("%s")' % data_uri(p)
    return re.sub(r'url\((["\']?)([^)"\']+)\1\)', rep, t)


def pagina_en_linea(ruta, parche_js=None):
    """HTML del sitio con sus <link> y <script src> en línea. Deja <!--Q--> al principio del <head> para el lector."""
    t = open(ruta, encoding='utf-8').read()
    base = os.path.dirname(ruta)

    def link(m):
        href = re.search(r'href="([^"]+)"', m.group(0)).group(1).split('?')[0]
        return '<style>%s</style>' % css_en_linea(os.path.normpath(os.path.join(base, href)))
    t = re.sub(r'<link rel="stylesheet" href="[^"]+">', link, t)

    def script(m):
        src = m.group(1).split('?')[0]
        js = open(os.path.normpath(os.path.join(base, src)), encoding='utf-8').read()
        if parche_js:
            js = parche_js(os.path.basename(src), js)
        return '<script>%s</script>' % sin_cierre(js)
    t = re.sub(r'<script src="([^"]+)"></script>', script, t)
    # url(...) sueltos en <style> de la página (fuentes de fin.html e instrucciones.html)
    def url_rel(m):
        u = m.group(1)
        p = os.path.normpath(os.path.join(base, u.split('?')[0]))
        return "url('%s')" % data_uri(p) if (not u.startswith('data:') and os.path.exists(p)) else m.group(0)
    t = re.sub(r"url\('([^')]+)'\)", url_rel, t)
    t = re.sub(r'src="(\.\./comun/fin-leccion/[^"]+)"', lambda m: 'src="%s"' % data_uri(os.path.normpath(os.path.join(base, m.group(1)))), t)
    t = t.replace('location.search', '(window.__Q||location.search)')
    t = t.replace('<head>', '<head>\n<!--Q-->', 1)
    return t


R_GLOBAL = ('function __R(u){try{var w=window;for(var i=0;i<8&&w;i++){if(w.__ovaR)return w.__ovaR(u);'
            'if(w.parent===w)break;w=w.parent;}}catch(e){}return u;}\n'
            # páginas que el motor abre en un iframe (el caso con audio): en línea con srcdoc, que hereda el origen
            'function __F(u){try{var w=window;for(var i=0;i<8&&w;i++){if(w.__ovaDoc){var h=w.__ovaDoc(u);'
            'if(h)return \'srcdoc="\'+h.replace(/&/g,"&amp;").replace(/"/g,"&quot;")+\'"\';break;}'
            'if(w.parent===w)break;w=w.parent;}}catch(e){}return \'src="\'+String(u).replace(/"/g,"&quot;")+\'"\';}\n')


def parche_app(nombre, js):
    if nombre != 'app.js':
        return js
    n0 = js.count('location.search')
    js = js.replace('location.search', '(window.__Q||location.search)')
    cambios = [
        ("function srcImagen(t) { return BASE + (datos.ilustraciones ? datos.ilustraciones + '/' + t : 'assets/contexto/' + t + '.webp'); }",
         "function srcImagen(t) { return __R(BASE + (datos.ilustraciones ? datos.ilustraciones + '/' + t : 'assets/contexto/' + t + '.webp')); }"),
        ("esc(escena.video.poster)", "esc(__R(escena.video.poster))"),
        ("esc(escena.video.src)", "esc(__R(escena.video.src))"),
        ("esc(escena.video.vtt)", "esc(__R(escena.video.vtt))"),
        ("esc(v.src)", "esc(__R(v.src))"),
        ("esc(v.vtt)", "esc(__R(v.vtt))"),
        ("esc(escena.descargaMapa.archivo)", "esc(__R(escena.descargaMapa.archivo))"),
        ("'<iframe src=\"' + esc(c.url) + '\" title=\"'", "'<iframe ' + __F(c.url) + ' title=\"'"),
        ("'<p class=\"escena-descarga\"><a class=\"boton-descarga\" href=\"' + esc(escena.descarga.href) + '\" download>'",
         "'<p class=\"escena-descarga\"><a class=\"boton-descarga\" href=\"' + esc(__R(escena.descarga.href)) + '\" download=\"' + "
         "esc(String(escena.descarga.href).split('/').pop()) + '\">'"),
    ]
    for a, b in cambios:
        if a in js:
            js = js.replace(a, b)
        elif a.startswith('esc(escena.video.poster)'):
            pass   # el motor de DP no trae póster
        else:
            raise SystemExit('parche de app.js sin destino: ' + a[:60])
    assert n0 >= 3
    return R_GLOBAL + js


# ---------------------------------------------------------------- recursos de la lección
def recursos_de(sitio, u, l, d, videos):
    """{clave tal como la pide el motor: ruta en disco}."""
    lec = os.path.join(sitio, 'unidad-%02d' % u, 'leccion-%02d' % l)
    comun = os.path.join(sitio, 'unidad-%02d' % u, 'comun')
    out = {}
    ilus = d.get('ilustraciones')
    vistos = set()

    def walk(o):
        if isinstance(o, dict):
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
        elif isinstance(o, str) and len(o) < 200:
            vistos.add(o)
    walk(d)
    for s in vistos:
        if s.startswith('documentos/'):
            p = os.path.join(lec, s)
            if os.path.exists(p):
                out[s] = p
            else:
                print('   falta', s)
        elif s.startswith('../comun/videos/'):
            n = os.path.basename(s)
            p = os.path.join(videos, n) if (videos and n.endswith('.mp4')) else os.path.join(comun, 'videos', n)
            if os.path.exists(p):
                out[s] = p
            else:
                print('   falta', s)
        elif s.startswith('../comun/casos/index.html?caso='):
            out[s] = '#caso'
        elif ilus and re.search(r'\.(webp|png|jpg|svg)$', s) and os.path.exists(os.path.join(comun, ilus, s)):
            out['../comun/%s/%s' % (ilus, s)] = os.path.join(comun, ilus, s)
    # todo lo de documentos/ (los PDF de las listas se piden con la ruta de la escena; por si acaso, la carpeta entera)
    for p in glob.glob(os.path.join(lec, 'documentos', '*')):
        out.setdefault('documentos/' + os.path.basename(p), p)
    return out


def casos_de(sitio, u, d):
    """Los casos con audio de la lección: {id: {titulo, texto, audio}} con el audio como clave del lector."""
    ids = set()
    for e in d['scenes']:
        for s in [e] + (e.get('pestanas') or []):
            for c in s.get('casosAudio') or []:
                ids.add(c['id'] if 'id' in c else c['url'].split('caso=')[1])
    if not ids:
        return {}, {}
    todos = json.load(open(os.path.join(sitio, 'unidad-%02d' % u, 'comun', 'casos', 'casos.json'), encoding='utf-8'))
    datos, rec = {}, {}
    for i in sorted(ids):
        c = dict(todos[i])
        clave = '../comun/casos/' + c['audio']
        p = os.path.join(sitio, 'unidad-%02d' % u, 'comun', 'casos', c['audio'])
        if os.path.exists(p):
            rec[clave] = p
        else:
            print('   falta audio', i)
        c['audio'] = clave
        datos[i] = c
    return datos, rec


# ---------------------------------------------------------------- diapositivas del Genially
def html_de_content(c):
    """Genially dibuja el texto desde Content (ProseMirror), no desde TextMessage (que puede quedar con el texto de la
    plantilla: «Soy un subtítulo…» en el rótulo «Curso»)."""
    out = []
    for p in (c or {}).get('content', []):
        a = p.get('attrs') or {}
        st = []
        if a.get('nodeTextAlignment'):
            st.append('text-align:%s' % a['nodeTextAlignment'])
        if a.get('nodeLineHeight'):
            st.append('line-height:%s' % a['nodeLineHeight'])
        h = ''
        for t in p.get('content', []):
            s = html.escape(t.get('text', ''), quote=False)
            css = []
            bold = False
            for m in t.get('marks', []):
                if m['type'] == 'textColor':
                    css.append('color:%s' % m['attrs']['color'])
                elif m['type'] == 'lineHeight':
                    css.append('line-height:%s' % m['attrs']['lineHeight'])
                elif m['type'] == 'bold':
                    bold = True
                elif m['type'] == 'italic':
                    css.append('font-style:italic')
                elif m['type'] == 'underline':
                    css.append('text-decoration:underline')
            if css:
                s = '<span style="%s">%s</span>' % (';'.join(css), s)
            if bold:
                s = '<strong>' + s + '</strong>'
            h += s
        out.append('<p%s>%s</p>' % (' style="%s"' % ';'.join(st) if st else '', h or '<br>'))
    return ''.join(out)


FUENTES = {'Montserrat-ExtraBold': 'g-mont-xb', 'Montserrat-Bold': 'g-mont-b'}


def px(v):
    try:
        return round(float(str(v).replace('px', '')), 2)
    except ValueError:
        return 0


def diapositivas(buf, ruta_svg):
    I = buf['importData']
    IA = I['interactivityActions']
    slides = I['slides']
    idx = {s['Id']: k for k, s in enumerate(slides)}
    out = []

    def accion(x):
        it = x.get('interactivities') or {}
        aid = it.get('click')
        if not aid or aid not in IA:
            return None
        t = IA[aid].get('target', {})
        if t.get('smartLink') == 'nextPage':
            return 'n'
        if t.get('smartLink') == 'previousPage':
            return 'p'
        if t.get('slideId') in idx:
            return idx[t['slideId']]
        return None
    for s in slides:
        els = []
        for arr in ('svgs', 'images', 'texts', 'groups', 'richContents'):
            for x in s[arr]:
                e = {'i': x['Id'], 'g': x.get('IdGroup'), 'z': int(x.get('ZIndex') or 0), 'x': px(x['Position']['PositionLeft']),
                     'y': px(x['Position']['PositionTop']), 'w': px(x['Size']['Width']), 'h': px(x['Size']['Height'])}
                rot = (x.get('Rotation') or {}).get('Rotatione')
                if rot and rot != 'rotate(0deg)':
                    e['r'] = rot
                if str(x.get('Opacity', '1')) not in ('1', '1.0'):
                    e['o'] = x['Opacity']
                if x.get('IsHidden'):
                    continue
                a = accion(x)
                if a is not None:
                    e['a'] = a
                if (x.get('EffectIn') or 'none') != 'none':
                    e['fx'] = x['EffectIn']
                if arr == 'texts':
                    e.update(t='t', h_=html_de_content(x.get('Content')) if x.get('Content') else x['TextMessage'], ff=x.get('FontFamily') or 'Montserrat', fs=x.get('FontSize'), c=x.get('Color'),
                             lh=x.get('LineHeight'), ls=x.get('LetterSpacing'), va=x.get('VerticalAlign') or 'top',
                             pad=x.get('Padding') or '0px', bg=x.get('Background') or '')
                    e['txt'] = html.unescape(re.sub(r'<[^>]+>', ' ', e['h_'])).strip()
                    if x.get('Classes'):
                        e['cls'] = ' '.join(x['Classes'])
                elif arr == 'svgs':
                    ref = x['SourceSvg'].replace('https://$task/', '')
                    e.update(t='s', s=ruta_svg(ref, I), col=x.get('Colors') or [])
                elif arr == 'images':
                    e.update(t='i', src=x['Source'])
                elif arr == 'groups':
                    e.update(t='g')
                elif arr == 'richContents':
                    m = re.search(r'src="([^"]+)"', x.get('Source') or '')
                    u = m.group(1) if m else ''
                    if 'index.html?escena=' in u:
                        e.update(t='e', n=int(u.split('escena=')[1].split('&')[0]))
                    elif 'instrucciones.html' in u:
                        e.update(t='ins')
                    elif 'fin.html' in u:
                        e.update(t='fin')
                    else:
                        continue
                    tm = re.search(r'title="([^"]*)"', x.get('Source') or '')
                    e['ti'] = html.unescape(tm.group(1)) if tm else ''
                els.append(e)
        els.sort(key=lambda e: e['z'])
        out.append({'id': s['Id'], 'n': s['Name'], 'bg': s.get('BackgroundColor') or '#FFFFFF', 'els': els})
    return out


def main():
    curso = sys.argv[1]
    C = CURSOS[curso]
    sitio = C['sitio']
    solo = set(sys.argv[2:])
    dst = os.path.join(AQUI, 'out', curso)
    os.makedirs(dst, exist_ok=True)
    lector = open(os.path.join(AQUI, 'lector.html'), encoding='utf-8').read()
    fuentes_css = ''.join([
        "@font-face{font-family:'g-mont-xb';src:url(%s) format('woff2');font-weight:100 900}" % data_uri(os.path.join(ASSETS, 'mont-extrabold.woff2')),
        "@font-face{font-family:'g-mont-b';src:url(%s) format('woff2');font-weight:100 900}" % data_uri(os.path.join(ASSETS, 'mont-bold-b.woff2')),
    ])
    resumen = []
    for idx in sorted(glob.glob(sitio + 'unidad-0*/leccion-0*/index.html')):
        h = open(idx, encoding='utf-8').read()
        d = json.loads(RE_CONT.search(h).group(2))
        u, l = d['unit'], d['lesson']
        clave = '%d.%d' % (u, l)
        if solo and clave not in solo:
            continue
        lec = os.path.dirname(idx)
        comun = os.path.join(sitio, 'unidad-%02d' % u, 'comun')
        fuentes_motor = css_en_linea(os.path.join(comun, 'base.css'))
        mont = re.findall(r"@font-face\{[^}]*Montserrat[^}]*\}|@font-face\{[^}]*Roboto[^}]*\}", fuentes_motor)
        buf = json.load(open(os.path.join(sitio, 'genially', 'l%d%d.json' % (u, l)), encoding='utf-8'))
        svgs = {}

        def ruta_svg(ref, I):
            if ref not in svgs:
                svgs[ref] = 's%d' % len(svgs)
            return svgs[ref]
        diap = diapositivas(buf, ruta_svg)
        svg_src = {v: buf['importData']['tasks'][k]['value'] for k, v in svgs.items()}
        imgs = {}
        for s in diap:
            for e in s['els']:
                if e['t'] == 'i':
                    src = e['src']
                    if 'cad36bc82324' in src:
                        imgs.setdefault(src, data_uri(os.path.join(ASSETS, 'logos.webp')))
                    elif '0ba28a40' in src:
                        imgs.setdefault(src, data_uri(os.path.join(ASSETS, 'portada.webp')))
                    elif '914118b6' in src:
                        imgs.setdefault(src, data_uri(os.path.join(ASSETS, 'bombillo.svg')))
                    else:
                        raise SystemExit('imagen de Genially sin copia local: ' + src)
        # páginas del motor
        motor = pagina_en_linea(idx, parche_app)
        fin = pagina_en_linea(os.path.join(lec, 'fin.html'))
        ins = pagina_en_linea(os.path.join(lec, 'instrucciones.html'))
        rec = recursos_de(sitio, u, l, d, C['videos'])
        casos, rec_casos = casos_de(sitio, u, d)
        rec.update(rec_casos)
        casos_html = ''
        if casos:
            casos_html = pagina_en_linea(os.path.join(comun, 'casos', 'index.html'))
            viejo = "var d = (await (await fetch('casos.json')).json())[id];"
            assert viejo in casos_html
            casos_html = casos_html.replace(viejo, "var d = (window.__CASOS || {})[id];")
            casos_html = casos_html.replace("a.src = d.audio;", "a.src = __R(d.audio);")
            casos_html = casos_html.replace('<!--Q-->', '<!--Q--><script>' + R_GLOBAL + '</script>')
        rec = {k: v for k, v in rec.items() if v != '#caso'}
        # bloques de recursos en base64
        bloques, indice, peso = [], {}, 0
        for n, (k, p) in enumerate(sorted(rec.items())):
            rid = 'r%d' % n
            indice[k] = [rid, MIME.get(os.path.splitext(p)[1].lower(), 'application/octet-stream')]
            b = b64(p)
            peso += os.path.getsize(p)
            bloques.append('<script type="text/plain" id="%s">%s</script>' % (rid, b))
        titulo = '%s · U%d L%d · %s' % (C['prefijo'], u, l, re.sub(r'^Lección \d\.\d\.\s*', '', d['heading']))
        meta = {'curso': C['curso'], 'clave': clave, 'titulo': titulo, 'heading': d['heading'], 'total': len(d['scenes'])}
        js = lambda o: sin_cierre(json.dumps(o, ensure_ascii=False, separators=(',', ':')))
        pagina = (lector
                  .replace('/*FUENTES*/', fuentes_css + ''.join(mont))
                  .replace('<!--TITULO-->', html.escape(titulo))
                  .replace('/*META*/null', js(meta))
                  .replace('/*DIAP*/null', js(diap))
                  .replace('/*SVG*/null', js(svg_src))
                  .replace('/*IMG*/null', js(imgs))
                  .replace('/*IDX*/null', js(indice))
                  .replace('/*CASOS*/null', js(casos))
                  .replace('<!--RECURSOS-->', '\n'.join(bloques))
                  .replace('<!--PLANTILLAS-->', ''.join(
                      '<script type="text/plain" id="%s">%s</script>' % (k, base64.b64encode(v.encode('utf-8')).decode('ascii'))
                      for k, v in (('p-motor', motor), ('p-fin', fin), ('p-ins', ins), ('p-casos', casos_html)))))
        nombre = '%s_U%d_L%d.html' % (C['prefijo'], u, l)
        open(os.path.join(dst, nombre), 'w', encoding='utf-8').write(pagina)
        mb = os.path.getsize(os.path.join(dst, nombre)) / 1e6
        resumen.append({'clave': clave, 'archivo': nombre, 'mb': round(mb, 1), 'diapositivas': len(diap), 'recursos': len(rec),
                        'titulo': titulo})
        print('%s  %-16s %3d diap.  %3d recursos  %6.1f MB' % (clave, nombre, len(diap), len(rec), mb))
    json.dump(resumen, open(os.path.join(dst, '_resumen.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
