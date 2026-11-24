# -*- coding: utf-8 -*-
"""PDF descargables de DP revisado (listas, textos completos, plantilla, matrices), con la línea visual del curso."""
import html, json, os
from playwright.sync_api import sync_playwright
OUT = '/home/claude/dp2/out/sitio/derecho-peticion/'
FONTS = OUT + 'unidad-01/comun/assets/fonts/'
CSS = '''@font-face{font-family:M;src:url(file://%smontserrat-latin.woff2) format('woff2');font-weight:100 900}
@font-face{font-family:M;src:url(file://%smontserrat-latin-ext.woff2) format('woff2');font-weight:100 900;unicode-range:U+0100-024F}
@page{size:A4;margin:18mm 16mm 18mm}
body{font-family:M,Arial,sans-serif;color:#002F46;font-size:10.5pt;line-height:1.45}
.cab{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:3px solid #EE616B;padding-bottom:6px;margin-bottom:14px}
.cab .c{font-size:8.5pt;color:#396B83;font-weight:700;text-transform:uppercase;letter-spacing:.04em}
h1{font-size:16pt;margin:0 0 10px;font-weight:800}
p{margin:0 0 8px;text-align:justify}
.chq{list-style:none;padding:0}.chq li{display:flex;gap:8px;margin:0 0 7px}.chq li:before{content:'';flex:none;width:11px;height:11px;border:1.5px solid #396B83;border-radius:3px;margin-top:3px}
.resp{border:1px solid #B9D3DB;border-radius:6px;height:70px;margin:4px 0 12px}
table{border-collapse:collapse;width:100%%;font-size:9pt;margin:6px 0 10px}th{background:#002F46;color:#fff;text-align:left;padding:6px}td{border-bottom:1px solid #D5E5EA;padding:6px;vertical-align:top}
td:first-child{font-weight:700}
.oficio{border:1px solid #B9D3DB;border-radius:6px;padding:16px 18px;background:#fff}
.pie{font-size:8pt;color:#396B83;margin-top:14px}''' % (FONTS, FONTS)


def doc(curso, leccion, d):
    t = html.escape(d['titulo'])
    h = '<div class="cab"><span class="c">%s</span><span class="c">%s</span></div><h1>%s</h1>' % (curso, leccion, t)
    ps = [html.escape(p).replace('\n', '<br>') for p in d.get('parrafos', [])]
    if d.get('lista'):
        h += '<ul class="chq">' + ''.join('<li><span>%s</span></li>' % p for p in ps) + '</ul>'
    elif d.get('responder'):
        h += ''.join('<p>%s</p>' % p + ('<div class="resp"></div>' if p.lstrip()[:2].rstrip('.').isdigit() else '') for p in ps)
    elif d.get('oficio'):
        h += '<div class="oficio">' + ''.join('<p>%s</p>' % p for p in ps) + '</div>'
    else:
        h += ''.join('<p>%s</p>' % p for p in ps)
    if d.get('tabla'):
        tb = d['tabla']
        h += '<table><tr>' + ''.join('<th>%s</th>' % html.escape(c) for c in tb[0]) + '</tr>' + ''.join(
            '<tr>' + ''.join('<td>%s</td>' % html.escape(c) for c in f) + '</tr>' for f in tb[1:]) + '</table>'
    for p in d.get('pie', []):
        h += '<p>%s</p>' % html.escape(p)
    h += '<p class="pie">Material de apoyo del curso. Fiscalía General de la Nación · Dirección de Altos Estudios.</p>'
    return '<!doctype html><html lang="es"><meta charset="utf-8"><style>%s</style><body>%s</body></html>' % (CSS, h)


def main():
    esc = json.load(open('/home/claude/dp2/out/escenas_dp.json', encoding='utf-8'))
    hechos = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        for k, lst in esc.items():
            u, l = map(int, k.split('.'))
            for e in lst:
                if e.get('pdf') and e.get('descarga', '').endswith('.pdf'):
                    f = OUT + 'unidad-%02d/leccion-%02d/' % (u, l) + e['descarga']
                    tmp = '/tmp/claude-0/pdf_tmp.html'
                    open(tmp, 'w', encoding='utf-8').write(doc('Derecho de petición y acción de tutela', 'Unidad %d · Lección %d' % (u, l), e['pdf']))
                    pg.goto('file://' + tmp)
                    pg.wait_for_timeout(200)
                    pg.pdf(path=f, format='A4', print_background=True, margin={'top': '18mm', 'bottom': '18mm', 'left': '16mm', 'right': '16mm'})
                    hechos.append(f.replace(OUT, ''))
        b.close()
    return hechos


if __name__ == '__main__':
    for h in main():
        print(h)
