# -*- coding: utf-8 -*-
"""Miniaturas de revisión hechas con plantillas: cada celda trae un dict {"tpl": ..., ...} y sale un SVG 400×170.

    python3 plantillas.py <specs.json> <carpeta_svg>

specs.json: {"<clave>": {"tpl": "mapa", "titulo": "E02 · ...", ...}, ...}. Se usa la clase S de
dp_u1l1/miniaturas.py (paleta, etiqueta PROPUESTA, chips, botón PDF).

Plantillas y campos:
  mapa        centro, sub?, nodos[2-5], chips?[], nota?, pdf?(etiqueta)
  cajas       cajas[{t, items?[], chips?[]}] (2-6), nota?
  pestanas    tabs[2-4], activa, pasos?[] | items?[], nota?, pdf?
  linea       pasos[3-8], activa, panel_t?, panel?[], nota?, pdf?
  dos_bloques izq{t, chips?[], items?[]}, der{t, items[], alerta?}, franja?{t, chips[]}
  texto_pdf   frase, nota?, pdf?
  escenario   botones[2-6], panel_t, panel[], nota?
  columnas    cols[2-5], abierta, items[], frase?
  tarjetas    cards[{t, chips?[], items?[]}] (2-4)
  tabla       cols[2-3], filas[[..]], nota?, pdf?
  checklist   t, items[≤8], marcados
  acordeon    items[2-6], abierto, lineas?[], nota?
  caso        situacion?, audio?, cajas[], idea?, pdf?
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dp_u1l1'))
from miniaturas import C, CR, G, H, M, N, O, T, W, S  # noqa: E402


def corta(s, n):
    return s if len(s) <= n else s[:n - 1].rstrip() + '…'


def chips_en(s, x0, y, ancho, chips, size=6.8, fill=W, stroke=T, color=M, max_filas=3):
    x, fila = x0, 0
    for c in chips:
        w = len(c) * size * 0.56 + 10
        if x + w > x0 + ancho and x > x0:
            fila += 1
            x = x0
            y += size + 10
            if fila >= max_filas:
                break
        s.chip(x, y, c, size, fill, stroke, color)
        x += w + 4
    return y + size + 10


def items_en(s, x, y, items, size=7.3, n=40, gap=11, bullet=C, maxi=8):
    for i, it in enumerate(items[:maxi]):
        s.add('<circle cx="%s" cy="%s" r="2" fill="%s"/>' % (x + 2, y + i * gap - 2.5, bullet))
        s.text(x + 8, y + i * gap, corta(it, n), size, M, 500)
    return y + min(len(items), maxi) * gap


def nota(s, d, y=162):
    if d.get('nota'):
        s.text(14, y, corta(d['nota'], 70), 7.2, T, 500, italic=True)


def pdf(s, d, x=None, y=145):
    if d.get('pdf'):
        lab = d['pdf'] if isinstance(d['pdf'], str) else 'Descargar (PDF)'
        w = len(lab) * 7.5 * 0.56 + 26
        s.pdf(x if x is not None else 386 - w, y, lab)


def t_mapa(s, d):
    s.rect(120, 27, 160, 32, M, None, rx=8)
    s.text(200, 41 if d.get('sub') else 47, corta(d['centro'], 30), 9.5, W, 700, 'middle')
    if d.get('sub'):
        s.text(200, 53, corta(d['sub'], 42), 7, CR, 500, 'middle')
    ns = d['nodos']
    k = len(ns)
    ancho = (372 - (k - 1) * 8) / k
    for i, nd in enumerate(ns):
        x = 14 + i * (ancho + 8)
        cx = x + ancho / 2
        s.line(200, 59, cx, 74, T, 1.1)
        s.rect(x, 74, ancho, 30, W, T, rx=6)
        s.text(cx, 93, corta(nd, int(ancho / 4.6)), 7.6, M, 700, 'middle')
        s.add('<circle cx="%s" cy="74" r="5" fill="%s"/><text x="%s" y="77" font-family="Poppins, Arial" '
              'font-size="7.5" font-weight="700" fill="%s" text-anchor="middle">+</text>' % (x + ancho - 6, C, x + ancho - 6, W))
    if d.get('chips'):
        chips_en(s, 14, 112, 372, d['chips'], 6.6)
    nota(s, d, 160 if not d.get('pdf') else 132)
    pdf(s, d)


def t_cajas(s, d):
    cs = d['cajas'][:8]
    k = len(cs)
    cols = 2 if k == 4 else (4 if k > 6 else min(k, 3))
    filas = (k + cols - 1) // cols
    alto_total = 132 if not d.get('nota') else 120
    h = (alto_total - (filas - 1) * 6) / filas
    w = (372 - (cols - 1) * 6) / cols
    for i, c in enumerate(cs):
        x, y = 14 + (i % cols) * (w + 6), 27 + (i // cols) * (h + 6)
        s.rect(x, y, w, h, W, T, rx=7)
        s.add('<circle cx="%s" cy="%s" r="7" fill="%s"/><text x="%s" y="%s" font-family="Poppins, Arial" '
              'font-size="8" font-weight="700" fill="%s" text-anchor="middle">%d</text>'
              % (x + 12, y + 12, C, x + 12, y + 15, W, i + 1))
        s.text(x + 23, y + 15, corta(c['t'], int((w - 28) / 4.4)), 7.8, M, 700)
        yy = y + 27
        if c.get('chips'):
            yy = chips_en(s, x + 8, yy - 4, w - 14, c['chips'], 6.3, max_filas=2 if filas > 1 else 4)
        if c.get('items'):
            items_en(s, x + 8, yy + 4, c['items'], 6.8, int((w - 20) / 3.8), 10,
                     maxi=2 if filas > 1 else 6)
        if not c.get('chips') and not c.get('items'):
            s.lines(x + 8, yy, w - 16, 2 if filas > 1 else 4, gap=7)
    nota(s, d)
    pdf(s, d, y=150)


def t_pestanas(s, d):
    tabs = d['tabs'][:4]
    x = 14
    for i, t in enumerate(tabs):
        w = len(t) * 8 * 0.58 + 20
        act = i == d.get('activa', 0)
        s.rect(x, 27, w, 18, M if act else N, None if act else T, rx=5)
        s.text(x + w / 2, 39.5, t, 8, W if act else M, 700, 'middle')
        x += w + 4
    s.rect(14, 47, 372, 112, W, T, rx=7)
    if d.get('pasos'):
        ps = d['pasos'][:4]
        w = (352 - (len(ps) - 1) * 14) / len(ps)
        for i, p in enumerate(ps):
            x = 24 + i * (w + 14)
            s.rect(x, 62, w, 36, N if i % 2 == 0 else CR, None, rx=6)
            palabras = p.split()
            a, b = ' '.join(palabras[:len(palabras) // 2 + 1]), ' '.join(palabras[len(palabras) // 2 + 1:])
            s.text(x + w / 2, 77, corta(a, int(w / 4.2)), 7.2, M, 700, 'middle')
            s.text(x + w / 2, 89, corta(b, int(w / 4.2)), 7.2, M, 500, 'middle')
            if i < len(ps) - 1:
                s.arrow(x + w + 1, 80, x + w + 12, 80)
        y = 112
    else:
        y = items_en(s, 26, 66, d.get('items', []), 7.6, 70, 12) + 4
    if d.get('nota'):
        s.text(24, max(y + 6, 120), corta(d['nota'], 72), 7.2, T, 500, italic=True)
    pdf(s, d, y=138)


def t_linea(s, d):
    ps = d['pasos'][:8]
    k = len(ps)
    s.line(30, 50, 370, 50, T, 2)
    paso = 340 / max(k - 1, 1)
    for i, p in enumerate(ps):
        x = 30 + i * paso
        act = i == d.get('activa', 0)
        s.add('<circle cx="%s" cy="50" r="%s" fill="%s" stroke="%s" stroke-width="1.5"/>'
              % (x, 9 if act else 7.5, C if act else W, C if act else T))
        s.text(x, 53, str(i + 1), 8, W if act else M, 700, 'middle')
        anc = 'start' if i == 0 else ('end' if i == k - 1 else 'middle')
        xt = x - 8 if i == 0 else (x + 8 if i == k - 1 else x)
        tam = 6.4 if k < 7 else 5.7
        s.text(xt, 70, corta(p, int(paso / (4.2 if k < 7 else 3.9)) if k > 3 else 22), tam, M, 600, anc)
    ax = 30 + d.get('activa', 0) * paso
    s.rect(14, 80, 372, 80, W, C, rx=7, sw=1.2)
    s.add('<path d="M%s 80 l6 -7 l6 7 z" fill="%s"/>' % (ax - 6, C))
    s.text(24, 96, corta(d.get('panel_t', ps[d.get('activa', 0)]), 60), 8.5, M, 700)
    if d.get('panel'):
        items_en(s, 24, 110, d['panel'], 7.2, 64, 11, maxi=4)
    else:
        s.lines(24, 106, 350, 3, gap=8)
    pdf(s, d, y=140)


def t_dos_bloques(s, d):
    iz, de = d['izq'], d['der']
    h = 98 if d.get('franja') else 132
    s.rect(14, 27, 182, h, W, T, rx=7)
    s.text(24, 42, corta(iz['t'], 34), 8.6, M, 700)
    y = 50
    if iz.get('chips'):
        y = chips_en(s, 24, y, 166, iz['chips'], 6.6)
    if iz.get('items'):
        items_en(s, 24, y + 8, iz['items'], 7.1, 34, 11, maxi=5 if h > 100 else 4)
    s.rect(204, 27, 182, h, W, O if de.get('alerta') else T, rx=7)
    x0 = 216
    if de.get('alerta'):
        s.add('<path d="M218 36 l7 12 h-14 z" fill="%s"/><text x="218" y="46.5" font-family="Poppins, Arial" '
              'font-size="8" font-weight="700" fill="%s" text-anchor="middle">!</text>' % (C, W))
        x0 = 232
    s.text(x0, 46 if de.get('alerta') else 42, corta(de['t'], 30), 8.6, O if de.get('alerta') else M, 700)
    items_en(s, 216, 62, de.get('items', []), 7.1, 34, 11, maxi=5 if h > 100 else 4)
    if d.get('franja'):
        f = d['franja']
        s.rect(14, 131, 372, 28, N, None, rx=6)
        s.text(24, 148, f['t'], 7.8, M, 700)
        chips_en(s, 24 + len(f['t']) * 4.6 + 8, 139, 340 - len(f['t']) * 4.6, f.get('chips', []), 6.5, max_filas=1)


def t_texto_pdf(s, d):
    s.rect(14, 27, 372, 30, CR, None, rx=6)
    s.text(200, 46, corta(d['frase'], 62), 9.3, O, 700, 'middle')
    s.lines(24, 68, 352, 3, last=0.85)
    s.lines(24, 94, 352, 3, last=0.7)
    s.lines(24, 120, 352, 1, last=0.5)
    nota(s, d, 152)
    pdf(s, d, y=140)


def t_escenario(s, d):
    s.rect(14, 27, 372, 132, CR, None, rx=7)
    s.rect(14, 120, 372, 39, '#F4D9DC', None, rx=0)
    s.rect(36, 92, 128, 30, T, None, rx=3)
    s.persona(66, 66, 1.5, M)
    s.persona(130, 66, 1.5, O)
    bs = d['botones'][:6]
    for i, b in enumerate(bs):
        x = 34 + i * (140 / max(len(bs) - 1, 1)) if len(bs) > 1 else 100
        y = 46 + (i % 2) * 10
        s.add('<circle cx="%s" cy="%s" r="8" fill="%s" stroke="%s" stroke-width="2"/>' % (x, y, C, W))
        s.text(x, y + 3.2, b, 8, W, 700, 'middle')
    s.rect(190, 34, 188, 118, W, T, rx=7, sw=1.4)
    s.text(200, 50, corta(d['panel_t'], 40), 8.4, M, 700)
    items_en(s, 200, 66, d['panel'], 7.1, 40, 12, maxi=6)


def t_columnas(s, d):
    cols = d['cols'][:5]
    ab = d.get('abierta', len(cols) - 1)
    cerr = len(cols) - 1
    wc = 48
    wa = 372 - cerr * (wc + 6)
    x = 14
    for i, c in enumerate(cols):
        if i == ab:
            s.rect(x, 27, wa, 132, W, T, rx=7, sw=1.6)
            s.text(x + 12, 44, corta(c, int(wa / 5)), 8.8, M, 700)
            y = items_en(s, x + 12, 62, d.get('items', []), 7.4, int(wa / 4.2), 11, maxi=6)
            if d.get('frase'):
                s.rect(x + 10, 132, wa - 20, 20, CR, None, rx=5)
                s.text(x + wa / 2, 145, corta(d['frase'], int(wa / 4.3)), 7.8, O, 700, 'middle')
            x += wa + 6
        else:
            s.rect(x, 27, wc, 132, N, T, rx=7)
            s.add('<text transform="translate(%s 93) rotate(-90)" font-family="Poppins, Arial" font-size="7.5" '
                  'font-weight="700" fill="%s" text-anchor="middle">%s</text>' % (x + wc / 2 + 3, M, corta(c, 22)))
            x += wc + 6


def t_tarjetas(s, d):
    cs = d['cards'][:4]
    k = len(cs)
    w = (372 - (k - 1) * 6) / k
    for i, c in enumerate(cs):
        x = 14 + i * (w + 6)
        s.rect(x, 27, w, 132, W if i % 2 == 0 else CR, T if i % 2 == 0 else C, rx=7)
        s.text(x + w / 2, 44, corta(c['t'], int(w / 4.4)), 8.2, M, 700, 'middle')
        y = 54
        if c.get('chips'):
            y = chips_en(s, x + 8, y, w - 14, c['chips'], 6.4, max_filas=4)
        if c.get('items'):
            items_en(s, x + 8, y + 8, c['items'], 6.8, int((w - 16) / 3.7), 11, maxi=6)
        if not c.get('chips') and not c.get('items'):
            s.lines(x + 10, y + 4, w - 20, 5, gap=8)


def t_tabla(s, d):
    cols = d['cols'][:3]
    filas = d['filas'][:5]
    w = 372 / len(cols)
    s.rect(14, 27, 372, 18, M, None, rx=4)
    for i, c in enumerate(cols):
        s.text(14 + i * w + 8, 39.5, corta(c, int(w / 4.8)), 7.8, W, 700)
    hf = (110 if not d.get('pdf') else 92) / max(len(filas), 1)
    for j, f in enumerate(filas):
        y = 47 + j * hf
        s.rect(14, y, 372, hf - 2, W if j % 2 == 0 else N, None, rx=3)
        for i, v in enumerate(f[:len(cols)]):
            s.text(14 + i * w + 8, y + hf / 2 + 2.5, corta(v, int(w / 4.1)), 7, M, 600 if i == 0 else 500)
    pdf(s, d, y=145)
    nota(s, d)


def t_checklist(s, d):
    s.rect(14, 27, 372, 132, W, T, rx=7)
    s.text(26, 44, corta(d['t'], 60), 9, M, 700)
    its = d['items'][:8]
    mk = d.get('marcados', 3)
    for i, it in enumerate(its):
        col, fila = i // 4 if len(its) > 4 else 0, i % 4 if len(its) > 4 else i
        x, y = 26 + col * 180, 60 + fila * 22
        s.rect(x, y - 9, 11, 11, C if i < mk else W, T, rx=2, sw=1)
        if i < mk:
            s.add('<path d="M%s %s l2.5 3 l5 -6" stroke="%s" stroke-width="1.6" fill="none"/>' % (x + 2, y - 3.5, W))
        s.text(x + 17, y, corta(it, 34 if len(its) > 4 else 70), 7.3, M, 500)
    s.rect(26, 144, 120, 8, N, None, rx=4)
    s.rect(26, 144, 120 * mk / max(len(its), 1), 8, T, None, rx=4)
    s.text(152, 151, '%d de %d' % (mk, len(its)), 7, T, 600)


def t_acordeon(s, d):
    its = d['items'][:6]
    ab = d.get('abierto', 0)
    y = 27
    for i, it in enumerate(its):
        if i == ab:
            s.rect(14, y, 372, 52, W, C, rx=6, sw=1.3)
            s.text(24, y + 14, corta(it, 64), 8.2, M, 700)
            s.text(376, y + 14, '–', 10, C, 700, 'end')
            if d.get('lineas'):
                items_en(s, 24, y + 28, d['lineas'], 7, 70, 10, maxi=2)
            else:
                s.lines(24, y + 24, 340, 3, gap=7)
            y += 56
        else:
            s.rect(14, y, 372, 18, N, None, rx=5)
            s.text(24, y + 12.5, corta(it, 70), 7.8, M, 600)
            s.text(376, y + 13, '+', 9, T, 700, 'end')
            y += 21
    nota(s, d)


def t_caso(s, d):
    s.rect(14, 27, 130, 106, W, T, rx=7)
    s.text(24, 42, 'Situación', 8.5, M, 700)
    if d.get('audio'):
        s.rect(24, 50, 110, 22, M, None, rx=11)
        s.add('<path d="M36 55 v12 l9 -6 z" fill="%s"/>' % W)
        for i in range(12):
            hh = 3 + (i * 37 % 9)
            s.rect(52 + i * 6.5, 61 - hh / 2, 3, hh, CR, None, rx=1)
        s.text(79, 86, 'audio del caso', 6.8, T, 500, 'middle', True)
        s.lines(28, 96, 100, 3, gap=8, last=0.5)
    else:
        s.rect(28, 50, 102, 74, H, M, rx=2, sw=1)
        s.text(34, 61, corta(d.get('situacion', 'Documento del caso'), 22), 6.6, O, 700)
        s.lines(34, 67, 88, 6, gap=8, last=0.5)
    cs = d.get('cajas', ['Análisis', 'Actividad'])[:3]
    h = (106 - (len(cs) - 1) * 6) / len(cs)
    for i, c in enumerate(cs):
        y = 27 + i * (h + 6)
        s.rect(152, y, 234, h, W, T, rx=7)
        s.text(162, y + 15, corta(c, 44), 8.2, M, 700)
        if d.get('pdf') and i == len(cs) - 1:
            s.pdf(162, y + h - 21, d['pdf'] if isinstance(d['pdf'], str) else 'Guía (PDF)')
        elif h > 26:
            s.lines(162, y + 24, 210, 1 if h < 40 else 2, gap=8, last=0.6)
    s.rect(14, 139, 372, 20, M, None, rx=5)
    s.text(24, 152.5, 'Idea clave', 8, CR, 700)
    s.text(76, 152.5, corta(d.get('idea', 'visible siempre, sin clic'), 60), 7.5, W, 500)


TPL = {k[2:]: v for k, v in globals().items() if k.startswith('t_')}


def hacer(clave, d):
    s = S(clave, d['titulo'])
    TPL[d['tpl']](s, d)
    return s.svg()


if __name__ == '__main__':
    specs = json.load(open(sys.argv[1], encoding='utf-8'))
    out = sys.argv[2]
    os.makedirs(out, exist_ok=True)
    for k, d in specs.items():
        open(os.path.join(out, k + '.svg'), 'w', encoding='utf-8').write(hacer(k, d))
    print(len(specs), 'miniaturas')
