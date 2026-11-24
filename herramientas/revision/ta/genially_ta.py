# -*- coding: utf-8 -*-
"""Genially nativo de Terminaciones anticipadas, calcado del de Derecho de petición (DP).

python3 genially_ta.py  ->  en out/sitio/:
  · unidad-0U/leccion-0L/fin.html e instrucciones.html (de los de DP, con los datos de TA)
  · genially/lUL.json: «copyBuffer» del editor de Genially con todas las diapositivas de la lección
    (portada, índice, una por escena, fin), listo para $geniallyDebug.pasteSlidesFromBuffer()
  · genially/carga.html?l=UL: lo abre el editor en un iframe oculto y le pasa el JSON por postMessage
Molde: la lección 1.1 de DP (JSON del visor de Genially) y sus páginas fin/instrucciones.
"""
import copy, html, importlib, json, math, os, random, re, string, sys, uuid
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import maqueta as M
from sitio import BASE, LECC

AQUI = os.path.dirname(os.path.abspath(__file__))
SITIO = os.path.join(AQUI, 'out', 'sitio')
DPG = '/tmp/claude-0/rev/sitio_zip/genially/00_6aece52f70e58f4344320b6f.json'
DPL = M.DP + 'unidad-01/leccion-01/'
NIVELES = ['Observador', 'Investigador', 'Fiscal en formación', 'Referente en terminaciones']
DP_NIV = ['Observador', 'Analista', 'Garante del derecho', 'Referente en tutela']
DP_CURSO = 'Derecho de petición y acción de tutela'
DP_UNI = 'Derecho de petición: fundamentos, modalidades y términos'
TIPOS = {'Texts': 'text', 'Svgs': 'svg', 'Images': 'image', 'Groups': 'group', 'RichContents': 'rich-content'}
ARR = {'Texts': 'texts', 'Svgs': 'svgs', 'Images': 'images', 'Groups': 'groups', 'RichContents': 'richContents'}
ARRAYS = ['widgetsAudio', 'widgetsVideo', 'containerBoxes', 'baseWidgets', 'activities', 'areas', 'arrows', 'audios', 'videos',
          'richContents', 'pins', 'images', 'svgs', 'texts', 'groups', 'charts']

D = json.load(open(DPG, encoding='utf-8'))
SL = {s['Name']: s for s in D['Slides']}
IA = D['interactivityActions']


def nano(n=21):
    return ''.join(random.choice(string.ascii_letters + string.digits + '_-') for _ in range(n))


def corto(heading):
    return re.sub(r'^Lección \d\.\d\.\s*', '', heading)


def elementos(nombre):
    sid = SL[nombre]['Id']
    out = []
    for k in TIPOS:
        for x in D[k]:
            if x['IdSlide'] == sid:
                out.append((k, x))
    return out


# ---------------------------------------------------------------- textos
def _html_parrafo(p):
    al = (p.get('attrs') or {}).get('nodeTextAlignment')
    st = ' style="text-align: %s;"' % al if al else ' style=""'
    pre = ' data-node-text-align="%s"' % al if al else ''
    h = ''
    for t in p.get('content', []):
        s = html.escape(t.get('text', ''), quote=False)
        for m in t.get('marks', []):
            if m['type'] == 'textColor':
                c = m['attrs']['color']
                s = '<span data-text-color-mark="%s" style="color: %s;">%s</span>' % (c, c, s)
        if any(m['type'] == 'bold' for m in t.get('marks', [])):
            s = '<strong>' + s + '</strong>'
        h += s
    return '<p%s dir="ltr"%s>%s</p>' % (pre, st, h)


def texto(x, nuevo, size=None, alto=None, ancho=None, top=None, valign=None, alinear=None):
    """Cambia el texto de un elemento de texto (Content de ProseMirror y TextMessage) conservando sus marcas."""
    c = x['Content']
    p = c['content'][0]
    t0 = p['content'][0] if p.get('content') else {'type': 'text', 'marks': []}
    p = copy.deepcopy(p)
    p['content'] = [dict(t0, text=nuevo)]
    if alinear is not None:
        p.setdefault('attrs', {})['nodeTextAlignment'] = alinear
    x['Content'] = {'type': 'doc', 'content': [p]}
    x['TextMessage'] = _html_parrafo(p)
    x['Name'] = (nuevo[:8] + '...') if len(nuevo) > 8 else nuevo
    if size:
        x['FontSize'] = '%spx' % size
    if alto is not None:
        x['Size']['Height'] = '%spx' % alto
    if ancho is not None:
        x['Size']['Width'] = '%spx' % ancho
    if top is not None:
        x['Position']['PositionTop'] = '%spx' % top
    if valign:
        x['VerticalAlign'] = valign
    return x


def txt_de(x):
    return ''.join(t.get('text', '') for p in x['Content'].get('content', []) for t in p.get('content', []))


def ajusta(n_chars, ancho, alto, tams, k=0.56, lh=1.15):
    """Mayor tamaño de letra con el que n caracteres caben en la caja (estimación por ancho medio de Montserrat)."""
    for fs in tams:
        cpl = max(1, int(ancho / (k * fs)))
        lineas = math.ceil(n_chars * 1.12 / cpl)
        if lineas * fs * lh <= alto:
            return fs
    return tams[-1]


# ---------------------------------------------------------------- diapositiva
class Diapo:
    def __init__(self, molde, nombre, color='#E5F1F1'):
        s = copy.deepcopy(SL[molde])
        self.id = str(uuid.uuid4())
        self.s = {k: v for k, v in s.items() if k not in ('IdSlide',)}
        self.s.update(Id=self.id, Name=nombre, BackgroundColor=color)
        for a in ARRAYS:
            self.s[a] = []
        self.els = []                     # (coleccion, elemento) con ids nuevos
        grupos = {}
        crudos = elementos(molde)
        for k, x in crudos:
            if k == 'Groups':
                grupos[x['Id']] = str(uuid.uuid4())
        for k, x in crudos:
            y = copy.deepcopy(x)
            y['Id'] = grupos.get(x['Id']) or str(uuid.uuid4())
            y['IdSlide'] = self.id
            if y.get('IdGroup'):
                y['IdGroup'] = grupos[y['IdGroup']]
            y['_orig'] = x['Id']
            self.els.append((k, y))

    def por_z(self, k, z):
        r = [y for kk, y in self.els if kk == k and int(y['ZIndex']) == z]
        assert len(r) == 1, (self.s['Name'], k, z, len(r))
        return r[0]

    def quitar(self, pred):
        self.els = [(k, y) for k, y in self.els if not pred(k, y)]


def acciones_de(d, destinos, acciones):
    """Rehace las interactividades: smartLink tal cual; ir a diapositiva -> destinos[id_original_del_elemento]."""
    for k, y in d.els:
        if not y.get('interactivities'):
            continue
        nuevas = {}
        for ev, aid in y['interactivities'].items():
            a = IA[aid]
            t = a.get('target', {})
            if 'smartLink' in t:
                tgt = {'smartLink': t['smartLink']}
            else:
                dest = destinos.get(y['_orig'])
                if dest is None:
                    continue
                tgt = {'slideId': dest}
            nid = nano()
            acciones[nid] = {'refId': nano(), 'type': a['type'], 'target': tgt}
            nuevas[ev] = nid
        y['interactivities'] = nuevas


def iframe(y, url, titulo, w=None, h=None):
    w = w or int(float(y['Size']['Width'][:-2]))
    h = h or int(float(y['Size']['Height'][:-2]))
    t = html.escape(titulo, quote=True)
    ifr = '<iframe src="%s" title="%s" width="%d" height="%d" style="border:0" allowfullscreen></iframe>' % (url, t, w, h)
    y['Source'] = '<div class="card-iframe">%s</div>' % ifr
    y['originalUrl'] = ifr


# ---------------------------------------------------------------- piezas comunes del marco
def marco_comun(d, u, l, heading, z):
    """z: dict con los ZIndex del molde para: chip_l, tit_l, curso, uni, nuni."""
    texto(d.por_z('Texts', z['chip_l']), 'Lección %d' % l)
    h = corto(heading)
    texto(d.por_z('Texts', z['tit_l']), h, size=ajusta(len(h), 476, 50, [14, 13, 12]))
    texto(d.por_z('Texts', z['curso']), M.CURSO)
    texto(d.por_z('Texts', z['uni']), 'Unidad %d' % u)
    nu = M.UNIDADES[u]
    texto(d.por_z('Texts', z['nuni']), nu, size=ajusta(len(nu), 175, 46, [13, 12, 11]), valign='center')


def entradas_indice(escenas):
    tit = [e['titulo_genially'] for e in escenas]
    lab = lambda i: re.sub(r'^[a-h]\.\s*', '', tit[i])
    if len(tit) <= 11:
        return [(lab(i), i) for i in range(len(tit))]
    sec = [i for i, t in enumerate(tit) if re.match(r'^[a-h]\. ', t)]
    if not sec:   # sin apartados: las claves y, del resto, una muestra pareja hasta 11 filas
        clave = re.compile(r'^(Cierre de la lección|Síntesis de la unidad|Finalización|Cierre del curso)')
        k = [i for i in range(len(tit)) if clave.match(tit[i])]
        o = [i for i in range(len(tit)) if i not in k]
        cupo = 11 - len(k)
        o = [o[round(j * (len(o) - 1) / (cupo - 1))] for j in range(cupo)] if cupo < len(o) else o
        return [(lab(i), i) for i in sorted(set(o + k))]
    clave = re.compile(r'^(Presentación del curso|Introducción a la unidad|Pregunta orientadora|Ruta de la lección|Síntesis de la unidad|Cierre de la lección|Cierre del curso|Finalización)')
    ini = [i for i, t in enumerate(tit) if clave.match(t) and (not sec or i < sec[0])]
    fin = [i for i, t in enumerate(tit) if clave.match(t) and sec and i > sec[-1]]
    idx = sorted(set(ini + sec + fin))
    while len(idx) > 11 and ini:
        idx.remove(ini.pop(0))
    return [(lab(i), i) for i in idx]


def leccion(clave, esc=None, heading=None, base=None, sigla='TA'):
    """esc/heading/base/sigla: para usar el mismo armado con otro curso (DP revisado: herramientas/revision/dp2)."""
    u, l = map(int, clave.split('.'))
    if esc is None:
        esc = importlib.import_module('lecciones.l%d%d' % (u, l)).ESCENAS
    heading = heading or M.HEADINGS[clave]
    url = (base or BASE) + 'unidad-%02d/leccion-%02d/' % (u, l)
    pref = '%s · U%d-L%d' % (sigla, u, l)
    acciones = {}

    # --- portada
    por = Diapo('DPT · U1-L1 · Portada', pref + ' · Portada')
    h = corto(heading)
    texto(por.por_z('Texts', 3), h, size=ajusta(len(h), 532, 288, [38, 34, 31, 28]))
    texto(por.por_z('Texts', 18), 'Lección %d' % l, ancho=215, alto=41)   # a 179 px «Lección 4» partía en dos renglones (también en el DP original)
    texto(por.por_z('Texts', 15), M.CURSO)
    texto(por.por_z('Texts', 14), 'Unidad %d' % u)
    nu = M.UNIDADES[u]
    texto(por.por_z('Texts', 16), nu, size=ajusta(len(nu), 175, 46, [13, 12, 11]), valign='center')
    # --- índice
    ind = Diapo('DPT · U1-L1 · Índice', pref + ' · Índice')
    marco_comun(ind, u, l, heading, dict(chip_l=10, tit_l=11, curso=7, uni=15, nuni=16))
    iframe(ind.por_z('RichContents', 87), url + 'instrucciones.html?modo=boton', 'Ver instrucciones de navegación')
    # --- escenas
    escs = []
    for n, e in enumerate(esc, 1):
        d = Diapo('DPT · U1-L1-E01', '%s-E%02d' % (pref, n))
        marco_comun(d, u, l, heading, dict(chip_l=11, tit_l=12, curso=8, uni=16, nuni=17))
        t = e['titulo_genially']
        texto(d.por_z('Texts', 13), t, size=ajusta(len(t), 1030, 37, [16, 15, 14]), ancho=1030)
        iframe(d.por_z('RichContents', 3), url + 'index.html?escena=%d' % n, t)
        escs.append(d)
    # --- fin
    fin = Diapo('DPT · U1-L1 · Fin', pref + ' · Fin')
    texto(fin.por_z('Texts', 10), 'Lección %d' % l)
    texto(fin.por_z('Texts', 11), h, size=ajusta(len(h), 476, 50, [14, 13, 12]))
    texto(fin.por_z('Texts', 3), h, size=ajusta(len(h), 407, 279, [31, 28, 25]))
    texto(fin.por_z('Texts', 5), 'Lección %d' % l)
    iframe(fin.por_z('RichContents', 16), url + 'fin.html', 'Fin de la lección')
    fin.quitar(lambda k, y: k == 'Images' and int(y['ZIndex']) == 14)

    # --- filas del índice: molde = grupo 30 (fila numerada) y 85 (fin); 25 = inicio
    ent = entradas_indice(esc)
    g_fila = [y for k, y in ind.els if k == 'Groups' and int(y['ZIndex']) == 30][0]
    hijos_fila = [(k, y) for k, y in ind.els if y.get('IdGroup') == g_fila['Id']]
    g_fin = [y for k, y in ind.els if k == 'Groups' and int(y['ZIndex']) == 85][0]
    hijos_fin = [(k, y) for k, y in ind.els if y.get('IdGroup') == g_fin['Id']]
    filas_molde = {int(y['ZIndex']) for k, y in ind.els if k == 'Groups' and int(y['ZIndex']) not in (13, 25)}
    ids_filas = {y['Id'] for k, y in ind.els if k == 'Groups' and int(y['ZIndex']) in filas_molde}
    ind.quitar(lambda k, y: y['Id'] in ids_filas or y.get('IdGroup') in ids_filas)
    total = len(ent) + 1
    por_col = math.ceil(total / 2)
    z = 200
    destinos = {}
    nuevas = []
    for i in range(total):
        col, fila = divmod(i, por_col)
        x0, y0 = (43 if col == 0 else 606), 253 + 57 * fila
        es_fin = i == len(ent)
        g = copy.deepcopy(g_fin if es_fin else g_fila)
        hijos = copy.deepcopy(hijos_fin if es_fin else hijos_fila)
        gid = str(uuid.uuid4())
        g.update(Id=gid, ZIndex=z, BigZIndex=z, ReadingOrder=z)
        g['Position'] = {'PositionLeft': '%dpx' % x0, 'PositionTop': '%dpx' % y0}
        g['_orig'] = 'fila%d' % i
        z += 1
        nuevas.append(('Groups', g))
        for k, y in sorted(hijos, key=lambda kv: int(kv[1]['ZIndex'])):
            y = copy.deepcopy(y)
            y.update(Id=str(uuid.uuid4()), IdGroup=gid, ZIndex=z, BigZIndex=z, ReadingOrder=z)
            z += 1
            if k == 'Texts':
                tx = txt_de(y)
                if tx.strip().isdigit():
                    texto(y, str(i + 1))
                elif not es_fin:
                    lab = ent[i][0]
                    fs = ajusta(len(lab), 474, 44, [15, 14, 13, 12], k=0.6)
                    texto(y, lab, size=fs, top=3, alto=44, valign='center')
            nuevas.append((k, y))
        destinos['fila%d' % i] = fin.id if es_fin else escs[ent[i][1]].id
    ind.els += nuevas
    # inicio de la lección -> portada (como en DP)
    g_ini = [y for k, y in ind.els if k == 'Groups' and int(y['ZIndex']) == 25][0]
    destinos[g_ini['_orig']] = por.id

    # menú (botón redondo) -> índice; «Ver lección» de la portada -> índice
    def menu_a(d, dest):
        for k, y in d.els:
            if y.get('interactivities'):
                for aid in y['interactivities'].values():
                    if 'slideId' in IA[aid].get('target', {}):
                        destinos.setdefault(y['_orig'], dest)
    for d in [por, fin] + escs:
        menu_a(d, ind.id)
    # en el índice, el menú vuelve a la portada (como en DP)
    for k, y in ind.els:
        if k == 'Svgs' and y.get('interactivities') and int(y['ZIndex']) == 86:
            destinos[y['_orig']] = por.id

    todas = [por, ind] + escs + [fin]
    tasks = {}
    slides = []
    for o, d in enumerate(todas, 1):
        acciones_de(d, destinos, acciones)
        s = dict(d.s, Order=o, BigOrder=str(o))
        for k, y in d.els:
            y = {kk: vv for kk, vv in y.items() if kk != '_orig'}
            y['type'] = TIPOS[k]
            if k == 'Svgs':
                ref = y['SourceSvg']
                tasks[ref] = {'value': D['svgRefs'][ref], 'finished': True}
                y['SourceSvg'] = 'https://$task/' + ref
            s[ARR[k]].append(y)
        slides.append(s)
    buf = {'type': 'slides', 'importData': {'weave': None, 'slides': slides, 'interactivityActions': acciones,
                                             'dragAndDropRelationships': [], 'tasks': tasks, 'version': 24, 'config': {}},
           'slideIds': [s['Id'] for s in slides]}
    meta = {'leccion': clave, 'titulo_genially': '%s · U%d L%d · %s' % (sigla, u, l, corto(heading)), 'diapositivas': len(slides), 'indice': [e[0] for e in ent]}
    return buf, meta, esc


def paginas(clave, esc):
    """fin.html e instrucciones.html de la lección, desde las de DP."""
    u, l = map(int, clave.split('.'))
    dst = os.path.join(SITIO, 'unidad-%02d' % u, 'leccion-%02d' % l)
    mx = sum(25 + sum(10 * sum(len(b['items']) if b.get('items') else 2 for b in s['bloques']) for s in (e.get('pestanas') or [e])) for e in esc)
    for f in ('fin.html', 'instrucciones.html'):
        t = open(DPL + f, encoding='utf-8').read()
        t = t.replace(DP_CURSO + ' · Unidad 1. ' + DP_UNI, M.CURSO + ' · Unidad %d. %s' % (u, M.UNIDADES[u]))
        t = t.replace(DP_CURSO, M.CURSO).replace(DP_UNI, M.UNIDADES[u])
        for a, b in zip(DP_NIV[1:], NIVELES[1:]):
            t = t.replace(a, b)
        t = t.replace('Unidad 1 · Lección 1', 'Unidad %d · Lección %d' % (u, l)).replace('Lección 1', 'Lección %d' % l).replace('Unidad 1', 'Unidad %d' % u)
        t = t.replace('dpt-juego-u1-l1', 'ta-juego-u%d-l%d' % (u, l))
        t = re.sub(r'MAX=\d+', 'MAX=%d' % mx, t)
        t = re.sub(r'TOTAL=\d+', 'TOTAL=%d' % len(esc), t)
        open(os.path.join(dst, f), 'w', encoding='utf-8').write(t)


CARGA = '''<!doctype html><meta charset="utf-8"><title>carga</title>
<script>
(async function () {
  var l = new URLSearchParams(location.search).get('l');
  try {
    var r = await fetch('l' + l + '.json', {cache: 'no-store'});
    var d = await r.json();
    parent.postMessage({tipo: 'ta-genially', l: l, datos: d}, 'https://app.genially.com');
  } catch (e) { parent.postMessage({tipo: 'ta-genially', l: l, error: String(e)}, 'https://app.genially.com'); }
})();
</script>'''


def main():
    random.seed(20261124)
    os.makedirs(os.path.join(SITIO, 'genially'), exist_ok=True)
    resumen = []
    for k in LECC:
        buf, meta, esc = leccion(k)
        paginas(k, esc)
        u, l = map(int, k.split('.'))
        json.dump(buf, open(os.path.join(SITIO, 'genially', 'l%d%d.json' % (u, l)), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
        resumen.append(meta)
        print(k, meta['diapositivas'], 'diapositivas ·', len(meta['indice']), 'filas de índice:', ' | '.join(meta['indice']))
    open(os.path.join(SITIO, 'genially', 'carga.html'), 'w', encoding='utf-8').write(CARGA)
    json.dump(resumen, open(os.path.join(SITIO, 'genially', 'lecciones.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
