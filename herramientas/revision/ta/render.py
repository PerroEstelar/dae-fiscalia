# -*- coding: utf-8 -*-
"""Rinde las escenas de una lección TA (motor en localhost:8765) y las monta en el marco Genially.
    python3 render.py 1.1 [n …]"""
import importlib, json, os, sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import maqueta as M
from playwright.sync_api import sync_playwright

AQUI = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(AQUI, 'out')
URL = 'http://localhost:8765/jp-audiencias-preliminares/terminaciones-anticipadas/unidad-%02d/leccion-%02d/index.html?escena=%d'
FONTS = M.DP + 'unidad-01/comun/assets/fonts/'
FA = M.DP + 'unidad-01/comun/assets/vendor/'

MARCO = r'''<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="file://%(fa)sfontawesome.min.css"><link rel="stylesheet" href="file://%(fa)ssolid.min.css">
<style>
@font-face{font-family:M;src:url(file://%(fonts)smontserrat-latin.woff2) format('woff2');font-weight:100 900}
@font-face{font-family:M;src:url(file://%(fonts)smontserrat-latin-ext.woff2) format('woff2');font-weight:100 900;unicode-range:U+0100-024F}
*{box-sizing:border-box;margin:0}
body{width:1112px;height:625px;background:#E5F1F1;font-family:M,sans-serif;position:relative;overflow:hidden}
.cab{position:absolute;left:0;top:0;width:1112px;height:93px;background:#002F46}
.logos{position:absolute;left:36px;top:8px;width:230px;height:76px}
.lec{position:absolute;left:343px;top:0;height:93px;width:540px;display:flex;align-items:center;gap:10px}
.chip{flex:none;height:30px;padding:0 9px;border-radius:5px 5px 5px 0;background:#EE616B;color:#fff;font-size:15.5px;font-weight:400;line-height:30px}
.tit{color:#fff;font-weight:700;font-size:13.4px;line-height:15.4px}
.flecha{position:absolute;top:28px;width:37px;height:37px;border-radius:50%%;background:#fff;color:#002F46;display:flex;align-items:center;justify-content:center;font-size:17px}
.menu{position:absolute;left:1026px;top:18px;width:56px;height:56px;border-radius:50%%;background:#F2F8F8;box-shadow:0 2px 6px rgba(0,0,0,.35);display:flex;align-items:center;justify-content:center;color:#002F46;font-size:24px}
.barra{position:absolute;left:40px;top:100px;width:1030px;height:42px;background:#fff;border-radius:18px 18px 0 0;display:flex;align-items:center}
.barra i{color:#2f4a55;font-size:22px;margin:0 20px 0 18px}
.barra span{color:#002F46;font-weight:700;font-size:%(ts)spx}
.esc{position:absolute;left:40px;top:142px;width:1030px;height:415px;background:#fff;border-radius:0 0 14px 14px;overflow:hidden;border:2px solid #E5F1F1;border-top:0}
.esc img{position:absolute;left:0;top:0;width:1029px;height:414px}
.curso{position:absolute;left:41px;top:572px;height:26px;padding:0 9px;border-radius:5px 5px 5px 0;background:#343434;color:#fff;font-size:16px;line-height:26px}
.ncurso{position:absolute;left:116px;top:575px;color:#002F46;font-weight:700;font-size:15px}
.pie{position:absolute;right:41px;top:557px;height:50px;display:flex;align-items:center;gap:10px}
.uni{flex:none;height:26px;padding:0 8px;border-radius:5px 5px 5px 0;background:#002F46;color:#fff;font-size:15.5px;line-height:26px}
.nuni{max-width:175px;text-align:right;color:#002F46;font-weight:700;font-size:12.6px;line-height:14px}
</style></head><body>
<div class="cab"><img class="logos" src="file://%(logos)s"><div class="lec"><span class="chip">Lección %(l)d</span><div class="tit">%(tit)s</div></div>
<span class="flecha" style="left:908px"><i class="fas fa-chevron-left"></i></span><span class="flecha" style="left:960px"><i class="fas fa-chevron-right"></i></span>
<span class="menu"><i class="fas fa-bars"></i></span></div>
<div class="barra"><i class="fas fa-lightbulb"></i><span>%(etit)s</span></div>
<div class="esc"><img src="file://%(png)s"></div>
<span class="curso">Curso</span><span class="ncurso">%(curso)s</span>
<div class="pie"><span class="uni">Unidad %(u)d</span><div class="nuni">%(nuni)s</div></div>
</body></html>'''

JS_PREP = r'''([poster, pagina]) => {
  document.querySelectorAll('.j-aviso, .confeti, [class*="confet"]').forEach(e => e.remove());
  const v = document.querySelector('video');
  if (v && poster) { v.setAttribute('poster', poster); v.removeAttribute('src'); }
  if (pagina !== null && pagina !== undefined) {
    const ps = document.querySelectorAll('.act-pagina');
    ps.forEach((p, i) => p.hidden = i !== pagina);
    document.querySelectorAll('.act-punto').forEach((p, i) => p.classList.toggle('activo', i === pagina));
  }
}'''


def escena_png(pg, u, l, n, e):
    pg.goto(URL % (u, l, n), wait_until='load')
    pg.wait_for_timeout(700)
    try:
        bt = pg.get_by_text('Clic para texto fijo', exact=False)
        if bt.count():
            bt.first.click(timeout=1500)
            pg.wait_for_timeout(300)
    except Exception:
        pass
    pg.wait_for_timeout(900)
    poster = None
    if getattr(e, 'poster', None):
        poster = '../comun/videos/%s.jpg' % e.poster
    pg.evaluate(JS_PREP, [poster, getattr(e, 'pagina', None)])
    for acc in getattr(e, 'meta', {}).get('clic', []):
        try:
            pg.locator(acc[0]).nth(acc[1] if len(acc) > 1 else 0).click(timeout=2500, force=True)
            pg.wait_for_timeout(900)
        except Exception as ex:
            print('   clic falló', acc, str(ex)[:80])
    pg.add_style_tag(content='.j-aviso,.confeti{display:none!important}')
    pg.wait_for_timeout(400)
    p = os.path.join(OUT, 'escenas', 'L%d.%d_E%02d.png' % (u, l, n))
    pg.screenshot(path=p)
    return p


def marco_png(pg, u, l, n, e, png):
    head = M.HEADINGS['%d.%d' % (u, l)].split('. ', 1)[1]
    nuni = M.UNIDADES[u]
    lineas = 1 if len(head) < 62 else 2 if len(head) < 124 else 3
    d = dict(fa=FA, fonts=FONTS, logos=os.path.join(AQUI, 'logos.png'), l=l, u=u, tit=html.escape(head), etit=html.escape(e['titulo_genially']),
             png=png, curso=html.escape(M.CURSO), nuni=html.escape(nuni), tt={1: 39, 2: 31, 3: 24}[lineas],
             ts='15' if len(e['titulo_genially']) < 95 else '13', ux=1071 - 180 - 82 if len(nuni) > 26 else 1071 - 160 - 82,
             nt=564 if len(nuni) > 26 else 572)
    f = os.path.join(OUT, 'marco.html')
    open(f, 'w', encoding='utf-8').write(MARCO % d)
    pg.goto('file://' + f)
    pg.wait_for_timeout(250)
    p = os.path.join(OUT, 'final', 'L%d.%d_E%02d.png' % (u, l, n))
    pg.screenshot(path=p)
    return p


def lecc(clave):
    u, l = map(int, clave.split('.'))
    mod = importlib.import_module('lecciones.l%d%d' % (u, l))
    importlib.reload(mod)
    return u, l, mod.ESCENAS


def main(clave, solo=None):
    u, l, escenas = lecc(clave)
    M.publicar(u, l, escenas)
    os.makedirs(os.path.join(OUT, 'escenas'), exist_ok=True)
    os.makedirs(os.path.join(OUT, 'final'), exist_ok=True)
    meta = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': 1113, 'height': 448}, device_scale_factor=2)
        pm = b.new_page(viewport={'width': 1112, 'height': 625}, device_scale_factor=2)
        for n, e in enumerate(escenas, 1):
            if solo and n not in solo:
                continue
            png = escena_png(pg, u, l, n, e)
            fin = marco_png(pm, u, l, n, e, png)
            print('ok', os.path.basename(fin), e['layout'], e['titulo_genially'][:60], flush=True)
        b.close()
    meta = [{'n': n, 'titulo': e['titulo_genially'], 'layout': e['layout'], 'com': getattr(e, 'meta', {}).get('com', '')}
            for n, e in enumerate(escenas, 1)]
    json.dump(meta, open(os.path.join(OUT, 'meta_L%d.%d.json' % (u, l)), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main(sys.argv[1], [int(x) for x in sys.argv[2:]] or None)
