# -*- coding: utf-8 -*-
"""Maquetas de Terminaciones anticipadas sobre el motor de las mediaciones (el de Derecho de petición).

Cada lección es un módulo lecciones/lUL.py con ESCENAS = [ ... ] armadas con las funciones de aquí.
El texto sale del DI (cuerpo.txt, solo el cuerpo a 12 pt: sin notas al pie ni encabezados de página),
por número de renglón: T(392) es el párrafo que empieza en el renglón 392; T(392, 2), sus dos primeras oraciones.
"""
import copy, json, os, re, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parrafos import parrafos

DP = '/tmp/claude-0/rev/sitio_zip/sitio/jp-audiencias-preliminares/derecho-peticion-accion-tutela/'
TA = '/tmp/claude-0/rev/sitio_zip/sitio/jp-audiencias-preliminares/terminaciones-anticipadas/'
FRAMES = '/mnt/user-data/uploads/DAE/_tmp/rev_ta/frames/'

_P = {ini: t for ini, t, h in parrafos(1, 5897)}
UNIDADES = {1: 'Archivo de la indagación', 2: 'La preclusión en el proceso penal',
            3: 'Aplicación del principio de oportunidad', 4: 'Preacuerdos y negociaciones en el sistema penal'}
CURSO = 'Terminaciones anticipadas del proceso penal'

ABREV = r'(?<!\bart\.)(?<!\bArt\.)(?<!\bNo\.)(?<!\bRad\.)(?<!\bExp\.)(?<!\binc\.)(?<!M\.P\.)(?<!\bp\.)(?<!\bpp\.)(?<!\bnum\.)(?<!\bnúm\.)(?<!\bCfr\.)(?<!\bSent\.)(?<!\bLit\.)(?<!\bNum\.)(?<!\bS\.)(?<!\bA\.)'
_ORA = re.compile(ABREV + r'(?<=[.?!”])\s+(?=[A-ZÁÉÍÓÚÑ¿«“(])')


def limpia(t):
    t = re.sub(r'\[\d+\.\d+\]', '', t)
    t = re.sub(r'^Veamos un ejemplo…\s*', '', t)
    t = re.sub(r'^VIDEO\s+', '', t)
    t = re.sub(r'^[●·•]\s*', '', t)
    t = re.sub(r'\s+([,.;:])', r'\1', t)
    t = re.sub(r'\s{2,}', ' ', t).replace('detal les', 'detalles').replace('proposiión', 'proposición').replace('argumenta ndo', 'argumentando').replace('mismo s hechos', 'mismos hechos').replace('falta d e ', 'falta de ').replace('N o procede', 'No procede').replace('C- 1154', 'C-1154').replace('AP- 6797', 'AP-6797')
    return t.strip()


def oraciones(t):
    return [x.strip() for x in _ORA.split(t) if x.strip()]


def T(ini, n=None, desde=0):
    """Párrafo del DI que empieza en el renglón ini (o lo contiene). n: cuántas oraciones; desde: a partir de cuál."""
    if ini not in _P:
        k = max(i for i in _P if i <= ini)
        t = _P[k]
    else:
        t = _P[ini]
    t = limpia(t)
    if n is None and not desde:
        return t
    o = oraciones(t)
    return ' '.join(o[desde:(desde + n) if n else None])


def J(*partes):
    return ' '.join(p for p in partes if p)


# ---------------------------------------------------------------- escenas
class Escena(dict):
    pass


def _base(layout, titulo, segs, bloques, guia=None, **k):
    e = Escena(layout=layout, segmentos=segs, parrafo=list(range(len(segs))), vineta=[], lead=[], titulo=[], tail=[], chips=[],
               bloques=bloques, rotulo=None, seccion=titulo, grupo=None, titulos_fuente=[titulo], encabezados=[], mediacion='',
               rotulos=[titulo], titulo_genially=titulo, complemento_genially='', apartado=titulo)
    if guia:
        e['guia'] = guia
    for a, b in k.items():
        if b is not None:
            e[a] = b
    return e


def _items(items, segs, extra=None):
    out = []
    for it in items:
        label, textos, obj = it[0], it[1], it[2] if len(it) > 2 else 'documento'
        if isinstance(textos, str):
            textos = [textos]
        idx = []
        for t in textos:
            segs.append(t)
            idx.append(len(segs) - 1)
        d = {'label': label, 'segs': idx, 'obj': obj}
        if len(it) > 3 and it[3]:
            d['ilus'] = it[3]
        if extra:
            d.update(extra)
        out.append(d)
    return out


def lamina(titulo, texto, obj='escudo', acomp=('personas', 'documento'), ilus='norma-competencia.webp', rotulo=None, **meta):
    e = _base('lamina', titulo, [texto], [{'tipo': 'lamina', 'items': [{'label': rotulo or titulo, 'segs': [0], 'obj': obj, 'acomp': list(acomp)}]}],
              ilustracion=ilus, relleno='dialogo-autoridades.webp')
    e.meta = meta
    return e


def esquema(titulo, raiz, items, descarga=True, raices=None, **meta):
    segs = []
    its = _items(items, segs)
    e = _base('esquema', titulo, segs, [{'tipo': 'esquema', 'items': its}], objeto_raiz=raiz,
              objetos_raiz=list(raices or [raiz, 'personas', 'documento']), guia='Recorra el mapa conceptual.')
    if descarga:
        e['descarga'] = {'href': 'documentos/mapa.png', 'rotulo': 'Clic para descargar el mapa',
                         'nombre': 'Mapa conceptual: %s (imagen PNG)' % titulo, 'lamina': True}
    e.meta = meta
    return e


ILUS = ['norma-competencia.webp', 'radicacion-terminos.webp', 'dialogo-autoridades.webp', 'comunidad-interes-general.webp']


def _con_ilus(items):
    return [(list(it) + [None] * (4 - len(it)))[:3] + [it[3] if len(it) > 3 and it[3] else ILUS[i % 4]] for i, it in enumerate(items)]


def rejilla(titulo, items, **meta):
    segs = []
    e = _base('rejilla', titulo, segs, [{'tipo': 'rejilla', 'items': _items(_con_ilus(items), segs)}],
              guia='Haga clic en cada recuadro para leer su texto completo.')
    e.meta = meta
    return e


def compara(titulo, items, **meta):
    segs = []
    e = _base('compara', titulo, segs, [{'tipo': 'compara', 'items': _items(_con_ilus(items), segs)}],
              guia='Haga clic en cada imagen: se despliega con su texto completo.')
    e.meta = meta
    return e


def giro(titulo, items, **meta):
    segs = []
    e = _base('giro', titulo, segs, [{'tipo': 'giro', 'items': _items(items, segs)}],
              guia='Pase el cursor o toque cada tarjeta para leer su contenido.')
    e.meta = meta
    return e


def ruta(titulo, items, **meta):
    segs = []
    e = _base('ruta', titulo, segs, [{'tipo': 'ruta', 'items': _items(items, segs)}], guia='Recorra la ruta paso a paso.')
    e.meta = meta
    return e


def fichas(titulo, items, **meta):
    segs = []
    e = _base('fichas', titulo, segs, [{'tipo': 'fichas', 'items': _items(items, segs)}], guia='Elija cada ficha para leer su contenido.')
    e.meta = meta
    return e


def compacta(titulo, flujo, ilus=None, objetos=('libros', 'personas', 'huella'), video=None, guia=None, escenario=False, **meta):
    """flujo: ('p', texto[, clase]) · ('sub', texto) · ('malla', [[(rot, textos, obj), …], …], cols) ·
    ('lista', [textos], num) · ('chequeo', [textos]) · ('tabla', [cab…], [[celda…], …]) · ('flechas', [cab…], [[…]])"""
    segs, items, fl = [], [], []
    principal = {'label': titulo, 'segs': [], 'clase': 'flujo', 'obj': 'documento'}
    items.append(principal)

    def seg(t):
        segs.append(t)
        return len(segs) - 1

    for z in flujo:
        t = z[0]
        if t == 'p':
            i = seg(z[1])
            principal['segs'].append(i)
            fl.append({'t': 'p', 's': [i], 'c': z[2] if len(z) > 2 else '', 'n': 0})
        elif t == 'sub':
            fl.append({'t': 'sub', 'x': z[1]})
        elif t == 'malla':
            filas = []
            for fila in z[1]:
                celdas = []
                for (rot, textos, obj) in fila:
                    textos = [textos] if isinstance(textos, str) else textos
                    items.append({'label': rot, 'segs': [seg(x) for x in textos], 'clase': 'celda', 'obj': obj})
                    celdas.append([len(items) - 1])
                filas.append({'rot': None, 'celdas': celdas})
            fl.append({'t': 'malla', 'cols': list(z[2]) if len(z) > 2 and z[2] else [], 'filas': filas, 'repetidos': [], 'columnas': max(len(f['celdas']) for f in filas)})
        elif t == 'lista':
            ss = [seg(x) for x in z[1]]
            principal['segs'] += ss
            d = {'t': 'lista', 's': ss, 'n': [0] * len(ss)}
            if len(z) > 2 and z[2]:
                d['num'] = True
            fl.append(d)
        elif t == 'chequeo':
            ii = []
            for x in z[1]:
                items.append({'label': x[:40], 'segs': [seg(x)], 'clase': 'chequeo', 'obj': 'documento'})
                ii.append(len(items) - 1)
            fl.append({'t': 'chequeo', 'i': ii})
        elif t in ('tabla', 'flechas'):
            cols = [seg(x) for x in z[1]]
            filas = [[seg(x) for x in f] for f in z[2]]
            principal['segs'] += cols + [x for f in filas for x in f]
            fl.append({'t': t, 'cols': cols, 'filas': filas})
    b = {'tipo': 'compacta', 'flujo': fl, 'items': items, 'lado': [], 'roles': {'repetidos': []}, 'objetos': list(objetos)}
    if escenario:
        b['escenario'] = True
    e = _base('compacta', titulo, segs, [b], guia=guia or 'Lea el contenido.', ilustracion=ilus)
    if video:
        e['video'] = {'src': '../comun/videos/%s.mp4' % video[0], 'vtt': '../comun/videos/%s.vtt' % video[0],
                      'poster': '../comun/videos/%s.jpg' % video[0], 'titulo': video[1]}
        e.poster = video[0]
    e.meta = meta
    return e


def actividad(titulo, preguntas, intro=(), cierre=(), modo='preguntas', ilus='dialogo-autoridades.webp', pagina=None, **meta):
    """preguntas: [{'enunciado': [textos], 'contexto': [textos]?, 'opciones': [(letra, texto, ok, retro)], 'retro': [...]}]"""
    segs = []

    def seg(t):
        segs.append(t)
        return len(segs) - 1

    qs = []
    for q in preguntas:
        d = {'cab': None, 'enunciado': [seg(x) for x in q['enunciado']], 'caption': None,
             'opciones': [{'letra': o[0], 'seg': seg(o[1]), 'ok': bool(o[2]), 'retro': [seg(o[3])] if len(o) > 3 and o[3] else []} for o in q['opciones']],
             'retro': [seg(x) for x in q.get('retro', [])]}
        if q.get('contexto'):
            d['contexto'] = [seg(x) for x in q['contexto']]
        qs.append(d)
    b = {'tipo': 'actividad', 'modo': modo, 'intro': [seg(x) for x in intro], 'preguntas': qs, 'cierre': [seg(x) for x in cierre],
         'items': [{'label': titulo, 'segs': list(range(len(segs))), 'obj': 'expediente'}]}
    e = _base('compacta', titulo, segs, [b], guia='Responda cada pregunta; si se equivoca, lea la explicación y vuelva a intentarlo.', ilustracion=ilus)
    e.meta = meta
    e.pagina = pagina
    return e


def VF(enunciado, verdadero, retro, contexto=None):
    q = {'enunciado': [enunciado], 'opciones': [('V', 'Verdadero', verdadero, retro), ('F', 'Falso', not verdadero, retro)]}
    if contexto:
        q['contexto'] = contexto if isinstance(contexto, list) else [contexto]
    return q


def MC(enunciado, opciones, correcta, retros, contexto=None):
    q = {'enunciado': [enunciado], 'opciones': [(l, t, l == correcta, retros.get(l)) for l, t in opciones]}
    if contexto:
        q['contexto'] = contexto if isinstance(contexto, list) else [contexto]
    return q


# ---------------------------------------------------------------- lección
def publicar(u, l, escenas):
    h = open(DP + 'unidad-01/leccion-01/index.html', encoding='utf-8').read()
    m = re.search(r'(<script type="application/json" id="contenido">)(.*?)(</script>)', h, re.S)
    d = json.loads(m.group(2))
    heading = HEADINGS['%d.%d' % (u, l)]
    d.update(heading=heading, unit=u, lesson=l, leccion_rotulo='Lección %d' % l, clave_curso='ta')
    d['juego'] = {'clave': 'ta-juego-u%d-l%d' % (u, l), 'niveles': ['Observador', 'Investigador', 'Fiscal en formación', 'Referente en terminaciones']}
    d['retro'] = dict(d['retro'], rotulo='Unidad %d · Lección %d' % (u, l))
    d['scenes'] = [dict(e) for e in escenas]
    # cada mapa con su propia lámina para descargar (antes todos apuntaban a «documentos/mapa.png», que no existía)
    for n, e in enumerate(d['scenes'], 1):
        if (e.get('descarga') or {}).get('href') == 'documentos/mapa.png':
            e['descarga'] = dict(e['descarga'], href='documentos/mapa-u%d-l%d-p%02d.png' % (u, l, n))
    dirc = TA + 'unidad-%02d/' % u
    if not os.path.isdir(dirc + 'comun'):
        shutil.copytree(DP + 'unidad-01/comun', dirc + 'comun')
        os.makedirs(dirc + 'comun/videos', exist_ok=True)
        with open(dirc + 'comun/tema-curso.css', 'a', encoding='utf-8') as f:
            f.write(CSS_TA)
    _parche_app(dirc + 'comun/app.js')
    for f in os.listdir(FRAMES):
        if f.endswith('_700.jpg'):
            shutil.copy(FRAMES + f, dirc + 'comun/videos/' + f.replace('_700', ''))
    out = dirc + 'leccion-%02d/' % l
    os.makedirs(out, exist_ok=True)
    js = json.dumps(d, ensure_ascii=False).replace('</', '<\\/')
    h2 = h[:m.start(2)] + js + h[m.end(2):]
    h2 = re.sub(r'<title>.*?</title>', '<title>%s · Mediación</title>' % heading, h2)
    h2 = h2.replace('aria-label="Mediación de la unidad 1, lección 1"', 'aria-label="Mediación de la unidad %d, lección %d"' % (u, l))
    open(out + 'index.html', 'w', encoding='utf-8').write(h2)
    return out


def _parche_app(ruta):
    """Copia TA del motor: el video de la escena lleva «poster» (cuadro fijo mientras no se reproduce). Idempotente."""
    a = open(ruta, encoding='utf-8').read()
    viejo = "'<figure class=\"escena-video\"><video controls preload=\"metadata\" playsinline src=\"' + esc(escena.video.src) + '\">'"
    nuevo = "'<figure class=\"escena-video\"><video controls preload=\"metadata\" playsinline' + (escena.video.poster ? ' poster=\"' + esc(escena.video.poster) + '\"' : '') + ' src=\"' + esc(escena.video.src) + '\">'"
    if nuevo not in a:
        assert viejo in a, 'app.js: no encuentro el <video> de la escena'
        open(ruta, 'w', encoding='utf-8').write(a.replace(viejo, nuevo))


# Ajuste de tema del curso (propuesta): sin la columna de íconos decorativos en las pantallas de lectura.
CSS_TA = '''
/* Terminaciones anticipadas: pantallas de lectura sin columna de íconos decorativos (el texto gana ancho) */
.compacta.sin-tips:not(.con-ilus):not(.cmp-esc){grid-template-columns:minmax(0,1fr)}
.compacta.sin-tips:not(.con-ilus):not(.cmp-esc)>.cmp-lado{display:none}
'''

HEADINGS = {
    '1.1': 'Lección 1.1. Fundamentos jurídicos, causales y procedencia del archivo de la indagación',
    '1.2': 'Lección 1.2. Diferencias entre archivo, inadmisión de denuncia y preclusión',
    '1.3': 'Lección 1.3. Desarchivo de las diligencias, reactivación de la investigación y derechos de las víctimas',
    '2.1': 'Lección 2.1. Causales de preclusión, oportunidades procesales para su solicitud y efectos',
    '2.2': 'Lección 2.2. Audiencia de preclusión: estructura, argumentación y actividad probatoria',
    '3.1': 'Lección 3.1. Fundamentos constitucionales y legales',
    '3.2': 'Lección 3.2. Causales de aplicación del principio de oportunidad',
    '3.3': 'Lección 3.3. Procedimiento, participación de las víctimas y control judicial',
    '3.4': 'Lección 3.4. Relación del principio de oportunidad con la justicia restaurativa',
    '4.1': 'Lección 4.1. Marco normativo y jurisprudencial, finalidades y límites de los preacuerdos',
    '4.2': 'Lección 4.2. Técnicas de negociación',
    '4.3': 'Lección 4.3. Dosificación punitiva',
    '4.4': 'Lección 4.4. Control de legalidad',
}


# ---------------------------------------------------------------- ayudas de contenido
def B(a, b):
    """Viñetas (●) del DI entre los renglones a y b."""
    return [limpia(t) for i, t, h in parrafos(a, b) if re.match(r'^\s*[●·•]', t)]


def sin_rotulo(t):
    t = re.sub(r'^(Respuesta correcta:\s*(VERDADERO|FALSO)\.\s*)', '', t)
    t = re.sub(r'^Afirmación \d\.\s*', '', t)
    t = re.sub(r'^Opción [A-D] (in)?correcta:\s*', '', t)
    t = re.sub(r'^(SITUACIÓN|Situación) \d[.:]\s*', '', t)
    t = re.sub(r'^(Análisis de la situación|REFLEXIÓN FINAL):\s*', '', t)
    return t.strip()


MOMENTOS = ('¿Qué permite comprender esta situación?', '¿Qué aspectos debe valorar el fiscal?', '¿Qué debería hacer el fiscal en una situación similar?')
OBJ_MOM = ('lupa', 'balanza', 'escalones')


MOMENTO4 = '¿Qué disposición o criterio normativo debe tener presente?'


def ejemplo(nombre, situacion, lead, preguntas, momentos, clave=None, video=None, com=None, com_analisis=None):
    """Un «Veamos un ejemplo…» del DI. Con video (caso animado ya producido): dos pantallas, el video con las preguntas
    para reflexionar y el análisis. Sin video: una pantalla con la situación en ventana y los tres momentos al mismo nivel."""
    mom = [(MOMENTOS[i], momentos[i], OBJ_MOM[i]) for i in range(3)]
    if len(momentos) > 3:
        mom.append((MOMENTO4, momentos[3], 'libros'))
    filas = [mom] if len(mom) == 3 else [mom[:2], mom[2:]]
    if video:
        pq = preguntas[:5]
        while len(pq) > 2 and sum(len(x.split()) for x in [lead] + pq) > 95:
            pq = pq[:-1]
        flujo_a = [('p', lead), ('lista', pq)]
        if sum(len(x.split()) for x in [lead] + pq) > 95:
            flujo_a = [('sub', 'Para reflexionar'), ('lista', pq)]
        a = compacta('Veamos un ejemplo: ' + nombre, flujo_a, video=video, com=com,
                     guia='Vea el caso y piense en las preguntas antes de pasar al análisis.')
        flujo = [('malla', filas)]
        if clave:
            flujo.append(('p', clave, 'clave'))
        b = compacta('Análisis del caso: ' + nombre, flujo, ilus='dialogo-autoridades.webp', com=com_analisis,
                     guia='Abra cada pregunta para leer el análisis.')
        return [a, b]
    sit = situacion + '\n\n' + lead + ' ' + ' '.join(preguntas)
    flujo = [('malla', [[('Situación', [situacion, lead + '\n' + '\n'.join('• ' + p for p in preguntas)], 'expediente')]]),
             ('sub', 'Análisis'), ('malla', filas)]
    if clave:
        flujo.append(('p', clave, 'clave'))
    return [compacta('Veamos un ejemplo: ' + nombre, flujo, com=com, guia='Lea la situación y abra cada pregunta del análisis.')]
