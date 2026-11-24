# -*- coding: utf-8 -*-
"""Derecho de petición revisado: piezas comunes (lectura de escenas, cambios generales de la revisión, publicación).

Fuente: el sitio de JP (espejo del 23 nov) y la revisión entregada (REVISION DERECHOS DE PETICION NOV 23.xlsx).
La línea visual y de recursos es la de DP: mismo motor, misma paleta, mismas ilustraciones; solo cambia lo que pidió la revisión.
"""
import copy, json, os, re, shutil, sys
sys.path.insert(0, '/home/claude/dp2')
sys.path.insert(0, '/home/claude/ta')
from base import leer, LECC, DP, RE
_cwd = os.getcwd(); os.chdir('/home/claude/ta')
import maqueta as M
os.chdir(_cwd)

OUT = '/home/claude/dp2/out/sitio/derecho-peticion/'
BASE_URL = 'https://zwaard88-source.github.io/prueba-terminaciones-anticipadas/derecho-peticion/'
GUIA_MAPA = 'Recorra el mapa conceptual: haga clic en cada concepto para leer su texto.'
MED_MAPA = 'Mapa conceptual: la idea de la escena arriba y sus conceptos unidos debajo; cada uno abre su texto.'
GUIA_RUTA = 'Recorra la ruta paso a paso.'
DI = open('/tmp/claude-0/rev/di.txt', encoding='utf-8').read().split('\n')


# ---------------------------------------------------------------- lectura y escritura de una escena
def textos(e, it):
    return [e['segmentos'][i] for i in it.get('segs', [])]


def items(e, tipo=None):
    for b in e['bloques']:
        if tipo is None or b.get('tipo') == tipo:
            return b.get('items', [])
    return []


def seg_nuevo(e, t):
    e['segmentos'].append(t)
    e.setdefault('parrafo', []).append(len(e['segmentos']) - 1)
    return len(e['segmentos']) - 1


def flujo(e):
    for b in e['bloques']:
        if b.get('tipo') == 'compacta':
            return b
    return None


def esc(e):
    """Escena como dict simple (las de maqueta son Escena con atributos sueltos)."""
    return dict(e)


# ---------------------------------------------------------------- cambios generales (hoja «Generales - revisión»)
def a_mapa(e, u, l, n, titulo=None):
    """Camino de paradas -> mapa conceptual de nodos con ramas (modelo 3.2 E07), con su descarga en PNG."""
    e['layout'] = 'esquema'
    e.pop('escenario', None)
    e['guia'] = GUIA_MAPA
    e['mediacion'] = MED_MAPA
    t = titulo or e['titulo_genially']
    e['descarga'] = {'href': 'documentos/mapa-u%d-l%d-p%02d.png' % (u, l, n), 'rotulo': 'Clic para descargar el mapa',
                     'nombre': 'Mapa conceptual: %s (imagen PNG)' % t, 'lamina': True}
    return e


def pdf(e, archivo, rotulo, nombre):
    e['descarga'] = {'href': 'documentos/' + archivo, 'rotulo': rotulo, 'nombre': nombre}
    return e


def generales(d, u, l):
    for n, e in enumerate(d['scenes'], 1):
        # 1. todo camino de paradas pasa a mapa conceptual con descarga
        if e['layout'] == 'esquema' and e.get('escenario'):
            a_mapa(e, u, l, n)
        # 3. listas de verificación: dos columnas (CSS) y botón para descargarla en PDF
        b = next((b for b in e['bloques'] if b.get('tipo') == 'compacta'), None)
        if b and any(z['t'] == 'chequeo' for z in b.get('flujo', [])) and not e.get('descarga'):
            ii = [i for z in b['flujo'] if z['t'] == 'chequeo' for i in z['i']]
            e['descarga'] = {'href': 'documentos/lista-u%d-l%d-p%02d.pdf' % (u, l, n), 'rotulo': 'Clic para descargar la lista',
                             'nombre': '%s (PDF)' % e['titulo_genially']}
            e['_pdf'] = {'titulo': e['titulo_genially'], 'parrafos': [e['segmentos'][j] for i in ii for j in b['items'][i]['segs']], 'lista': True}
        # 2. rejillas: un ícono propio por caja, no la misma ilustración repetida
        if e['layout'] == 'rejilla':
            for it in items(e):
                it.pop('ilus', None)
    return d


# ---------------------------------------------------------------- parches del motor y del tema (copia DP revisada)
CSS_DP = '''
/* DP revisado (revisión del 23 nov, hoja de generales) */
/* Avisos del juego en la esquina de abajo, no en la mitad de la lectura */
.j-aviso{left:auto;right:14px;top:auto;bottom:12px;transform:none;font-size:14px;padding:8px 16px;border-width:2px;animation:j-aviso-esq 2.6s ease both}
.j-aviso.nivel{top:auto;bottom:58px}
@keyframes j-aviso-esq{0%{opacity:0;transform:translateY(10px)}12%,80%{opacity:1;transform:none}100%{opacity:0;transform:translateY(-6px)}}
/* Pantallas de lectura sin la columna de íconos decorativos (el texto gana ancho) */
.compacta.sin-tips:not(.con-ilus):not(.cmp-esc){grid-template-columns:minmax(0,1fr)}
.compacta.sin-tips:not(.con-ilus):not(.cmp-esc)>.cmp-lado{display:none}
/* Listas de verificación en dos columnas, para verlas sin scroll */
.cmp-chq-lista{display:grid;grid-template-columns:1fr 1fr;gap:6px 14px}
@container ova (max-width:640px){.cmp-chq-lista{grid-template-columns:minmax(0,1fr)}}
'''


def parche_app(ruta):
    a = open(ruta, encoding='utf-8').read()
    # el confeti cae solo sobre el encabezado, no sobre el texto de la escena
    viejo = "p.style.setProperty('--y', (caja.height * (0.35 + Math.random() * 0.6)) + 'px');"
    nuevo = "p.style.setProperty('--y', (30 + Math.random() * 40) + 'px');"
    if nuevo not in a:
        assert viejo in a
        a = a.replace(viejo, nuevo)
    # texto fijo por escena (revisión 1.1 E01: «que el objetivo salga completo de una, sin animación»)
    viejo = "if (!escrituraAnimada() || escritos.indexOf(huella(t)) >= 0) {"
    nuevo = "if (!escrituraAnimada() || (escena && escena.textoFijo) || escritos.indexOf(huella(t)) >= 0) {"
    if nuevo not in a:
        assert viejo in a
        a = a.replace(viejo, nuevo)
    open(ruta, 'w', encoding='utf-8').write(a)


def preparar_comun(u):
    dst = OUT + 'unidad-%02d/comun' % u
    if not os.path.isdir(dst):
        shutil.copytree(DP + 'unidad-%02d/comun' % u, dst)
        with open(dst + '/tema-curso.css', 'a', encoding='utf-8') as f:
            f.write(CSS_DP)
        parche_app(dst + '/app.js')
        os.makedirs(dst + '/casos', exist_ok=True)
        shutil.copy('/home/claude/dp2/casos.html', dst + '/casos/index.html')
    return dst


def juego_max(esc):
    return sum(25 + sum(10 * sum(len(b['items']) if b.get('items') else 2 for b in s['bloques']) for s in (e.get('pestanas') or [e])) for e in esc)


def publicar(u, l, d):
    preparar_comun(u)
    src = DP + 'unidad-%02d/leccion-%02d/' % (u, l)
    out = OUT + 'unidad-%02d/leccion-%02d/' % (u, l)
    os.makedirs(out + 'documentos', exist_ok=True)
    h = open(src + 'index.html', encoding='utf-8').read()
    js = json.dumps(d, ensure_ascii=False).replace('</', '<\\/')
    m = RE.search(h)
    open(out + 'index.html', 'w', encoding='utf-8').write(h[:m.start(2)] + js + h[m.end(2):])
    for f in ('fin.html', 'instrucciones.html'):
        t = open(src + f, encoding='utf-8').read()
        if f == 'fin.html':
            t = re.sub(r'MAX=\d+', 'MAX=%d' % juego_max(d['scenes']), t)
            t = re.sub(r'TOTAL=\d+', 'TOTAL=%d' % len(d['scenes']), t)
        open(out + f, 'w', encoding='utf-8').write(t)
    return out


# ---------------------------------------------------------------- DI
def di_buscar(frase, desde=0):
    for i in range(desde, len(DI)):
        if frase in DI[i]:
            return i
    raise KeyError(frase)


RUIDO = re.compile(r'^(Formato basado en el documento|virtuales en el marco del contrato|######## PAGINA|Proyecto Fiscalía General de la Nación - Universidad|Ficha para la escritura de cursos)')


def di_parrafos(a, b):
    """Párrafos del DI entre los renglones a y b (excluido b). El texto viene del PDF: sin renglones en blanco, con encabezado
    y pie de página en medio; un renglón corto que cierra con punto (o dos puntos) termina el párrafo."""
    out, cur = [], ''
    for t in DI[a:b]:
        s = t.strip()
        if not s or RUIDO.match(s):
            continue
        cur = (cur + ' ' + s) if cur else s
        if len(s) < 96 and re.search(r'[.:;?!”"]$', s):
            out.append(cur)
            cur = ''
    if cur:
        out.append(cur)
    return [re.sub(r'\s+', ' ', x).strip() for x in out]
