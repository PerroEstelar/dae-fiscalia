# -*- coding: utf-8 -*-
"""Derecho de petición revisado: la revisión del 23 nov aplicada escena por escena (16 lecciones).

python3 revisar.py  ->  publica en out/sitio/derecho-peticion/ y escribe out/casos.json y out/escenas_dp.json
Cada escena lleva «_o» = número de escena en el Genially original (o «n…» si es nueva), para ubicar las celdas del Excel.
Regla de texto: el texto es el del DI; solo se parte, se ordena y se cambia el recurso. Lo nuevo sale del DI vigente.
"""
import copy, json, os, re, sys
sys.path.insert(0, '/home/claude/dp2')
from nucleo import *

CASOS = {}
U = {}


def S(d, n):
    """Escena por su número en el Genially original."""
    for e in d['scenes']:
        if e.get('_o') == n:
            return e
    raise KeyError(n)


def pos(d, n):
    return d['scenes'].index(S(d, n))


def nueva(e, tag):
    e = dict(e)
    e['_o'] = tag
    return e


def caso_audio(e, u, l, k, titulo, paras):
    cid = 'u%dl%dc%d' % (u, l, k)
    CASOS[cid] = {'titulo': titulo, 'texto': [p for p in paras if p], 'audio': 'audio/%s.mp3' % cid}
    e['casosAudio'] = [{'id': cid, 'titulo': titulo, 'url': '../comun/casos/index.html?caso=' + cid}]


def lista_dos(e):
    for b in e['bloques']:
        for z in b.get('flujo', []):
            if z['t'] == 'lista':
                z['dos'] = True
    return e


def con_pestanas(titulo, subs, tag):
    """subs: [(rótulo de pestaña, escena)]."""
    hijos = []
    for rot, s in subs:
        s = dict(s)
        s['pestana'] = rot
        s['titulo_genially'] = titulo
        hijos.append(s)
    p = dict(hijos[0])
    p['pestanas'] = hijos
    p['titulo_genially'] = titulo
    p['_hijos'] = True
    p['guia'] = 'Abra cada pestaña para leer su contenido.'
    p['_o'] = tag
    return p


def celda_txt(e, rotulo):
    b = flujo(e)
    for it in b['items']:
        if it.get('label') == rotulo:
            return [e['segmentos'][i] for i in it['segs']]
    raise KeyError(rotulo)


def ruta_de(titulo, pasos, intro=None, tag=None, objs=('lupa', 'documento', 'carpetas', 'reloj', 'personas', 'escudo', 'libros', 'expediente', 'telefono', 'balanza')):
    e = dict(M.ruta(titulo, [(rot, txt, objs[i % len(objs)]) for i, (rot, txt) in enumerate(pasos)]))
    if intro:
        e['lead'] = [seg_nuevo(e, intro)]
    e['guia'] = GUIA_RUTA
    e['_o'] = tag
    return e


def sin_num(t):
    return re.sub(r'^\d+\.\s*', '', t)


# =================================================================== UNIDAD 1
def L11(d, u=1, l=1):
    S(d, 1)['textoFijo'] = True                                       # E01: el objetivo completo, sin animación
    # E03: caja 1 como línea de tiempo 2011 → 2015; actuaciones del art. 13 en viñetas (ícono propio por caja: general)
    e = S(d, 3)
    t0 = e['segmentos'][0]
    e['segmentos'][0] = ('2011 → Ley 1437: expidió el Código de Procedimiento Administrativo y de lo Contencioso Administrativo (CPACA).\n'
                         '2015 → Ley Estatutaria 1755: sustituyó el Título II de la Parte Primera del CPACA (derecho de petición) y modificó los artículos 13 a 33.\n'
                         'Hoy → el régimen aplicable se lee en el CPACA en su texto vigente, esto es, con las modificaciones introducidas por la Ley 1755 de 2015.')
    t3 = e['segmentos'][3]
    cab, resto = t3.split(': ', 1)
    acts, cierre = resto.split('. La enumeración', 1)
    acts = [a.strip().rstrip('.') for a in re.split(r';\s*(?:e\s+)?', acts)]
    e['segmentos'][3] = cab + ':\n' + '\n'.join('• ' + a[0].upper() + a[1:] for a in acts) + '\nLa enumeración' + cierre
    # E04: viñetas en lo que revelan las peticiones (tercera columna)
    e = S(d, 4)
    t = e['segmentos'][2]
    a, b = t.split('Pueden revelar ', 1)
    lst, c = b.split('. Por ello', 1)
    partes = [x.strip() for x in re.split(r',\s*|\s+o\s+', lst)]
    e['segmentos'][2] = a + 'Pueden revelar:\n' + '\n'.join('• ' + p for p in partes if p) + '\nPor ello' + c
    # E05: dos bloques sin scroll y una franja de límites abajo
    e0 = S(d, 5)
    s = e0['segmentos']
    p1b = s[1].split(' Sin embargo, ', 1)
    n = dict(M.compacta(e0['titulo_genially'], [
        ('malla', [[('Se conecta con…', [s[0], p1b[0]], 'personas'), ('Pero no reemplaza…', ['Sin embargo, ' + p1b[1]], 'carpetas')]]),
        ('p', s[2], 'alerta')], guia='Abra cada recuadro; abajo, los límites.'))
    d['scenes'][pos(d, 5)] = nueva(n, 5)
    # E06: escenario con a, b y c en ventana; en c) los plazos de 15, 10 y 30 días en tablita
    e0 = S(d, 6)
    s = e0['segmentos']
    n = dict(M.compacta(e0['titulo_genially'], [
        ('p', s[0]),
        ('malla', [[('a) Facultad de presentar una solicitud respetuosa', s[1], 'personas'), ('b) Deber de trámite y respuesta', s[2], 'expediente'),
                    ('c) Oportunidad de la decisión', s[3], 'reloj')]]),
        ('tabla', ['Petición general', 'Documentos e información', 'Consultas'], [['15 días', '10 días', '30 días']])],
        ilus=e0.get('ilustracion'), guia='Abra a), b) y c); abajo, los plazos.'))
    d['scenes'][pos(d, 6)] = nueva(n, 6)
    # E07: tres pestañas (Orientar, Trasladar, Enfoque diferencial), el traslado como flujo de 5 días y PDF con el texto completo
    e0 = S(d, 7)
    s = e0['segmentos']
    tr = s[1]
    i_tr = tr.index('Sin embargo, ')
    orientar = s[0] + '\n\n' + tr[:i_tr].strip()
    trasl = tr[i_tr:]
    pasos = [('Recibe y verifica', 'La solicitud escrita llega a una dependencia o a un servidor que no es competente para resolverla: no basta con orientar al usuario.'),
             ('Remite en 5 días', 'Debe efectuarse el traslado al competente (artículo 21 de la Ley 1437 de 2011, sustituido por el artículo 1 de la Ley Estatutaria 1755 de 2015), dentro de los cinco (5) días siguientes a la recepción.'),
             ('Copia al peticionario', 'Con envío de copia del oficio remisorio al peticionario. Si la solicitud es verbal, se informa de inmediato la falta de competencia; si no existe autoridad competente, también se comunica.'),
             ('Corre el término', 'Los términos para resolver o responder se cuentan a partir del día siguiente a la recepción de la petición por la autoridad competente.')]
    t_or = dict(M.compacta('Orientar', [('p', s[0]), ('p', tr[:i_tr].strip(), 'clave')]))
    t_tr = dict(M.compacta('Trasladar', [('p', 'Sin embargo, cuando la solicitud escrita sea recibida por una dependencia o servidor que no sea competente para resolverla, no basta con brindar orientación al usuario:'),
                                          ('flechas', [p[0] for p in pasos], [[p[1] for p in pasos]])]))
    t_ed = dict(M.compacta('Enfoque diferencial', [('p', s[2])]))
    p = con_pestanas(e0['titulo_genially'], [('Orientar', t_or), ('Trasladar', t_tr), ('Enfoque diferencial', t_ed)], 7)
    pdf(p, 'u1-l1-participacion-y-atencion.pdf', 'Clic para descargar el texto completo', 'Participación ciudadana y atención al usuario (PDF)')
    p['_pdf'] = {'titulo': e0['titulo_genially'], 'parrafos': s}
    d['scenes'][pos(d, 7)] = p
    # E08: el escudo de la tarjeta 3 tapa «Cerrar» (objeto distinto) y chips de quiénes llegan a la Fiscalía
    e = S(d, 8)
    it = items(e)[2]
    it['obj'] = 'personas'
    # E09: sin «baje con la barra»; la frase fuerza arriba; PDF opcional
    e0 = S(d, 9)
    s = e0['segmentos']
    n = dict(M.compacta(e0['titulo_genially'], [('p', s[2], 'clave'), ('p', s[0]), ('p', s[1])], guia='Lea el contenido.'))
    pdf(n, 'u1-l1-calidad-institucional.pdf', 'Clic para descargar el texto (PDF)', 'Derecho de petición y calidad institucional (PDF)')
    n['_pdf'] = {'titulo': e0['titulo_genially'], 'parrafos': s}
    d['scenes'][pos(d, 9)] = nueva(n, 9)
    # E10: «Caso de aplicación», reflexión como guía en PDF, idea clave visible sin clic, audio de la situación
    e0 = S(d, 10)
    s = e0['segmentos']
    n = dict(M.compacta('Caso de aplicación', [
        ('malla', [[('Situación', s[0], 'expediente'), ('Análisis', [s[1], s[2]], 'lupa')]]),
        ('p', s[9], 'clave')], ilus=e0.get('ilustracion'), guia='Escuche la situación y abra el análisis; la idea clave queda a la vista.'))
    pdf(n, 'u1-l1-guia-de-reflexion.pdf', 'Clic para descargar la guía de reflexión', 'Actividad de reflexión (PDF para responder)')
    n['_pdf'] = {'titulo': 'Actividad de reflexión', 'parrafos': s[3:9], 'responder': True}
    caso_audio(n, u, l, 1, 'Caso de aplicación: la asociación comunitaria y los canales de atención', [s[0]])
    d['scenes'][pos(d, 10)] = nueva(n, 10)
    # E11: viene así del DI (anuncia la Política de Atención para la 1.2): no se cambia, se avisa en el Excel


def L12(d, u=1, l=2):
    # E03 (modalidades): el caso práctico de la petición particular (§2.2 del DI) destacado en la caja 2, con audio
    i = di_buscar('Caso práctico diferenciador de la petición particular')
    j = di_buscar('2.3. Solicitudes de información y copias', i)
    ps = di_parrafos(i, j)
    titulo_caso = 'Dos solicitudes a la Fiscalía, dos trámites diferentes'
    ps[0] = ps[0].split(titulo_caso, 1)[1].strip()
    e = S(d, 3)
    it = items(e)[1]
    it['label'] = 'Peticiones de interés particular · con caso práctico'
    it['segs'] = it['segs'] + [seg_nuevo(e, 'Caso práctico: ' + titulo_caso + '.\n' + ps[0])] + [seg_nuevo(e, p) for p in ps[1:]]
    caso_audio(e, u, l, 1, 'Caso práctico: dos solicitudes en un mismo escrito', [ps[0]])
    # E04: tres cajas arriba, sin columna de íconos (CSS general)
    # E05: mapa conceptual (general)
    # E06: términos en tablita + mapa descargable
    e0 = S(d, 6)
    s = e0['segmentos']
    n = dict(M.compacta(e0['titulo_genially'], [
        ('tabla', ['Regla general', 'Documentos e información', 'Consultas', 'Prórroga excepcional'],
         [['15 días', '10 días', '30 días', 'Hasta el doble del plazo inicial, avisando antes del vencimiento']]),
        ('malla', [[(items(e0)[0]['label'], s[0], 'reloj'), (items(e0)[1]['label'], s[1], 'escudo'),
                    (items(e0)[2]['label'], s[2], 'telefono'), (items(e0)[3]['label'], s[3], 'expediente')]])],
        guia='Mire los plazos y abra cada recuadro.'))
    n['descarga'] = {'href': 'documentos/mapa-u1-l2-p06.png', 'rotulo': 'Clic para descargar el mapa', 'nombre': 'Mapa: %s (imagen PNG)' % e0['titulo_genially'], 'lamina': True}
    d['scenes'][pos(d, 6)] = nueva(n, 6)
    # E07: el traslado como ruta (verificar competencia → remitir en 5 días con copia → término desde el competente)
    e0 = S(d, 7)
    s = e0['segmentos']
    n = ruta_de(e0['titulo_genially'], [
        ('Verificar la competencia', s[0].split(' Dentro de ese mismo término')[0]),
        ('Remitir en 5 días, con copia', 'Dentro de ese mismo término' + s[0].split(' Dentro de ese mismo término')[1]),
        ('Contar el término desde el competente', s[1]),
        ('Si la competencia es parcial', s[2])], tag=7)
    d['scenes'][pos(d, 7)] = n
    # E08: guía en secuencia -> ruta paso a paso (como 2.1 E06)
    e0 = S(d, 8)
    s = e0['segmentos']
    rots = [it['label'] for it in items(e0, 'compacta')[1:]] if False else [it['label'] for it in flujo(e0)['items'][1:]]
    d['scenes'][pos(d, 8)] = ruta_de(e0['titulo_genially'], [(sin_num(r), sin_num(t)) for r, t in zip(rots, s[1:])], intro=s[0], tag=8)
    # E09: caso de aplicación con audio
    e = S(d, 9)
    caso_audio(e, u, l, 2, 'Caso de aplicación: una comunicación con cuatro solicitudes', [celda_txt(e, 'Situación')[0]])


def L13(d, u=1, l=3):
    b0 = di_buscar('Lección 1.3.')
    # E02: mapa conceptual con las cuatro exigencias y los párrafos «en palabras sencillas» del DI vigente
    i = di_buscar('2. La respuesta debe ser clara, precisa y congruente', b0)
    j = di_buscar('3. La respuesta debe ser oportuna y comunicada', i)
    ps = di_parrafos(i + 1, j)
    U['L13_E02_DI'] = ps
    def par(ini):
        return [p for p in ps if p.startswith(ini)][0]
    e0 = S(d, 2)
    n = dict(M.esquema(e0['titulo_genially'], 'lupa', [
        ('De fondo: resuelve, no solo anuncia', par('De fondo'), 'documento'),
        ('Clara: se entiende', par('Clara'), 'personas'),
        ('Precisa: va al punto', par('Precisa'), 'lupa'),
        ('Congruente y completa', par('Congruente'), 'balanza')]))
    n['lead'] = [seg_nuevo(n, x) for x in (par('La Corte Constitucional'), par('Estas exigencias excluyen'), par('En palabras'), par('Ejemplo común'))]
    n['segmentos'][n['lead'][2]] = n['segmentos'][n['lead'][2]].replace('En palabras imples', 'En palabras simples')
    n['tail'] = [seg_nuevo(n, par('Estos criterios se complementan'))]
    a_mapa(n, u, l, 2)
    d['scenes'][pos(d, 2)] = nueva(n, 2)
    # E07: el caso del DI vigente (la carta de la ciudadana), con audio y escenario con ventanas
    i = di_buscar('7.1. Situación', b0)
    k = di_buscar('7.2. Análisis', i)
    j = di_buscar('8. Conclusión', k)
    lin = [t.strip() for t in DI[i + 1:k] if t.strip() and not RUIDO.match(t.strip())]
    txt = ' '.join(lin)
    intro, carta = txt.split('Señores ', 1)
    carta = 'Señores ' + carta
    U['L13_caso'] = [intro, carta]
    sit = [intro.strip(), 'Señores, Fiscalía General de la Nación. Asunto: Información sobre mi solicitud de protección y amenazas recientes.',
           carta.split('amenazas recientes ', 1)[1].split(' Atentamente,')[0].strip(),
           'Atentamente, Elena Robles Salcedo.',
           carta.split('Elena Robles Salcedo ', 1)[1].strip()]
    ana = di_parrafos(k + 1, j)
    e0 = S(d, 7)
    n = dict(M.compacta('Caso de aplicación', [('malla', [[('Situación', sit, 'expediente'), ('Análisis', ana, 'lupa')]])],
                        ilus=e0.get('ilustracion'), guia='Escuche la situación y abra el análisis.'))
    caso_audio(n, u, l, 1, 'Caso de aplicación: la carta de la ciudadana', sit[1:])
    d['scenes'][pos(d, 7)] = nueva(n, 7)


def L14(d, u=1, l=4):
    # E02: mapa conceptual (problema arriba, los cuatro deberes como ramas) con descarga: el general ya lo pasa a mapa
    e = S(d, 2)
    its = items(e)
    e['lead'] = its[0]['segs']                    # el problema arriba, como intro del mapa
    its.pop(0)


# =================================================================== UNIDAD 2
def a_4x2(e):
    for z in flujo(e)['flujo']:
        if z['t'] == 'malla':
            cs = [c for f in z['filas'] for c in f['celdas']]
            z['filas'] = [{'rot': None, 'celdas': cs[k:k + 4]} for k in range(0, len(cs), 4)]
            z['columnas'] = 4


def audio_situacion(d, n, u, l, k, titulo):
    e = S(d, n)
    caso_audio(e, u, l, k, titulo, celda_txt(e, 'Situación'))


def L21(d, u=2, l=1):
    # E01: el objetivo de la lección resaltado arriba; el resto debajo
    e0 = S(d, 1)
    s = e0['segmentos']
    n = dict(M.compacta(e0['titulo_genially'], [('sub', 'Objetivo de la lección'), ('p', s[4], 'clave'), ('p', s[0]), ('p', s[1]), ('p', s[2]), ('p', s[3])], guia='Lea el contenido.'))
    d['scenes'][pos(d, 1)] = nueva(n, 1)
    # E03 y E07: mapa (general). E04: los 7 valores en 4 × 2
    a_4x2(S(d, 4))
    # E08: audio de la situación
    audio_situacion(d, 8, u, l, 1, 'Caso de aplicación: la persona mayor que no usa canales virtuales')
    # E09: persona presentando con pestañas (Idea clave | Conclusión)
    e0 = S(d, 9)
    s = e0['segmentos']
    a1 = dict(M.compacta('Idea clave', [('p', s[0], 'clave')], ilus=e0.get('ilustracion')))
    a2 = dict(M.compacta('Conclusión', [('p', s[1]), ('p', s[2]), ('p', s[3])], ilus=e0.get('ilustracion')))
    d['scenes'][pos(d, 9)] = con_pestanas(e0['titulo_genially'], [('Idea clave', a1), ('Conclusión', a2)], 9)


def L22(d, u=2, l=2):
    # E03: mapa (general). E06: audio de la situación
    audio_situacion(d, 6, u, l, 1, 'Caso de aplicación: una petición con tres solicitudes')
    # E07: modelo de oficio, como documento, con botón para descargarlo como plantilla en PDF
    e = S(d, 7)
    e['guia'] = 'Este es un modelo de respuesta: léalo y descárguelo como plantilla.'
    pdf(e, 'u2-l2-plantilla-de-respuesta.pdf', 'Clic para descargar la plantilla', 'Plantilla de respuesta a una petición (PDF)')
    e['_pdf'] = {'titulo': 'Plantilla de respuesta a una petición', 'parrafos': e['segmentos'], 'oficio': True}
    for z in flujo(e)['flujo']:
        if z['t'] == 'p':
            z['c'] = 'oficio'


def L23(d, u=2, l=3):
    # E03: mapa (general)
    # E04 y E05: once categorías agrupadas (pública, datos personales, restringida, cómo se entrega)
    e4, e5 = S(d, 4), S(d, 5)
    def it(e, k):
        x = items(e)[k]
        return (x['label'], textos(e, x), x['obj'])
    g = {'pub': [it(e4, 0), it(e4, 1)], 'per': [it(e4, 2), it(e4, 3), it(e4, 4), it(e5, 0)],
         'res': [it(e5, 1), it(e5, 2), it(e5, 4)], 'ent': [it(e5, 3), it(e5, 5)]}
    objs = ['documento', 'carpetas', 'personas', 'escudo', 'lupa', 'huella', 'carpetas', 'documento', 'expediente', 'lupa', 'balanza']
    k = [0]
    def mm(lst):
        out = []
        for (r, t, o) in lst:
            out.append((r, t, objs[k[0] % len(objs)]))
            k[0] += 1
        return out
    n4 = dict(M.compacta(e4['titulo_genially'].replace(': de la información pública', ''), [
        ('sub', 'Información pública'), ('malla', [mm(g['pub'])]),
        ('sub', 'Datos personales'), ('malla', [mm(g['per'])])], guia='Abra cada recuadro: van agrupados por tipo de información.'))
    n4['titulo_genially'] = 'Categorías de información: pública y datos personales'
    n5 = dict(M.compacta('Categorías de información: restringida y cómo se entrega', [
        ('sub', 'Información restringida'), ('malla', [mm(g['res'])]),
        ('sub', 'Cómo se entrega'), ('malla', [mm(g['ent'])])], guia='Abra cada recuadro: van agrupados por tipo de información.'))
    d['scenes'][pos(d, 4)] = nueva(n4, 4)
    d['scenes'][pos(d, 5)] = nueva(n5, 5)
    # E06 (nueva, después de las reglas jurisprudenciales): la 4.4 del DI, texto inicial, una pestaña por medida y su caso con audio
    b0 = di_buscar('Lección 2.3.')
    i = di_buscar('4.4. Eliminación, anonimización y ocultamiento', b0)
    j = di_buscar('5. Criterios para resolver solicitudes de información', i)
    t = ' '.join(x.strip() for x in DI[i + 1:j] if x.strip() and not RUIDO.match(x.strip()))
    t = re.sub(r'\s+', ' ', t)
    intro, resto = t.split('Eliminación: retirar el dato', 1)
    resto = 'Eliminación: retirar el dato' + resto
    elim, resto = resto.split('Anonimización: impedir', 1)
    anon, resto = ('Anonimización: impedir' + resto).split('Ocultamiento: restringir', 1)
    ocul, comun = ('Ocultamiento: restringir' + resto).split('Criterio común para responder', 1)
    def partes(x):
        a, rest = x.split('Caso práctico — datos ficticios', 1)
        caso, trat = rest.split('Tratamiento del caso.', 1)
        caso = caso.lstrip('.: ').strip()
        return a.strip(), caso, 'Tratamiento del caso. ' + trat.strip()
    intro_ps = [x.strip() for x in re.split(r'(?<=\.) (?=Las explicaciones siguientes)', intro.strip())]
    subs = []
    for kk, (rot, x, obj) in enumerate([('Eliminación', elim, 'carpetas'), ('Anonimización', anon, 'huella'), ('Ocultamiento', ocul, 'escudo')], 1):
        a, caso, trat = partes(x)
        def_, cons = (a.split('Consecuencia jurídica y técnica', 1) + [''])[:2]
        sub = dict(M.compacta(rot, [('p', def_.strip()), ('p', ('Consecuencia jurídica y técnica' + cons).replace('técnica:', 'técnica.').strip(), 'regla'),
                                    ('malla', [[('Caso %d' % kk, caso, 'expediente'), ('Tratamiento del caso', trat.replace('Tratamiento del caso. ', ''), 'lupa')]])]))
        caso_audio(sub, u, l, kk + 1, 'Caso %d: %s' % (kk, rot.lower()), [caso])
        subs.append((rot, sub))
    ini = dict(M.compacta('Para empezar', [('p', intro_ps[0]), ('p', intro_ps[1], 'alerta')] if len(intro_ps) > 1 else [('p', intro_ps[0])]))
    cm = dict(M.compacta('Criterio común', [('p', comun.strip(), 'clave')]))
    p = con_pestanas('Eliminación, anonimización y ocultamiento: tres medidas con efectos distintos', [('Para empezar', ini)] + subs + [('Criterio común', cm)], 'n6')
    d['scenes'].insert(pos(d, 6) + 1, p)
    # E08: audio de la situación
    audio_situacion(d, 8, u, l, 1, 'Caso de aplicación: la copia de una carpeta de indagación')


def L24(d, u=2, l=4):
    # E02: en cada paso solo lo clave; el texto completo en PDF
    e = S(d, 2)
    full = list(e['segmentos'])
    for it in items(e):
        it['segs'] = it['segs'][:1] if len(it['segs']) < 4 else [it['segs'][0], it['segs'][2]]
    pdf(e, 'u2-l4-del-problema-al-control-de-terminos.pdf', 'Clic para descargar el texto completo', 'Del problema jurídico-operativo al control de términos (PDF)')
    e['_pdf'] = {'titulo': e['titulo_genially'], 'parrafos': full}
    # E03: mapa (general; el detalle queda en las ventanas). E04: audio
    audio_situacion(d, 4, u, l, 1, 'Caso de aplicación: la ciudadana que pide una respuesta anterior')


# =================================================================== UNIDAD 3
def di_sec(leccion, a, b):
    i = di_buscar(a, di_buscar(leccion))
    j = di_buscar(b, i)
    return di_parrafos(i + 1, j)


def clave_arriba(e, frase_ini):
    """Pasa a «Elemento clave», arriba, la oración del texto que empieza con frase_ini."""
    b = flujo(e)
    for i, t in enumerate(e['segmentos']):
        k = t.find(frase_ini)
        if k >= 0:
            fin = t.find('. ', k)
            ora = t[k:fin + 1] if fin > 0 else t[k:]
            j = seg_nuevo(e, ora)
            b['flujo'].insert(0, {'t': 'p', 's': [j], 'c': 'clave', 'n': 0})
            b['items'][0]['segs'].insert(0, j)
            return e
    raise KeyError(frase_ini)


def L31(d, u=3, l=1):
    # E01 + E02: una sola lámina (introducción y objetivo con el mismo escudo)
    e1, e2 = S(d, 1), S(d, 2)
    e2['segmentos'][0] = e1['segmentos'][0] + '\n\n' + e2['segmentos'][0]
    e2['textoFijo'] = True
    e2['_o'] = 1
    e2['_tambien'] = [2]
    d['scenes'].remove(e1)
    # E03: mapa (general). E07: audio de la situación. E08: lista (general)
    audio_situacion(d, 7, u, l, 1, 'Caso de aplicación: la petición sin respuesta que llega a tutela')


def L32(d, u=3, l=2):
    L = 'Lección 3.2.'
    # E03: las tres cajas del mapa, con el texto del DI vigente (quién la presenta, agente oficioso, sin abogado)
    ps = di_sec(L, '3. Legitimación por activa', '4. Legitimación por pasiva')
    e0 = S(d, 3)
    n = dict(M.rejilla(e0['titulo_genially'], [('Quién puede presentar la tutela', ps[0], 'personas'), ('Lo que dice el artículo 10 del Decreto 2591', ps[1], 'libros'),
                                              ('Un interés cierto, directo y particular', ps[2], 'lupa')]))
    for it in items(n):
        it.pop('ilus', None)
    d['scenes'][pos(d, 3)] = nueva(n, 3)
    # E04: pasiva, con el ejemplo de la persona que no obtuvo respuesta a su petición
    ps = di_sec(L, '4. Legitimación por pasiva', '5. Inmediatez')
    e0 = S(d, 4)
    n = dict(M.compacta(e0['titulo_genially'], [('p', ps[0]), ('p', ps[1], 'clave'), ('malla', [[('Para el servidor que recibe la comunicación', ps[2], 'escudo')]])],
                        guia='Lea el contenido y abra el recuadro.'))
    d['scenes'][pos(d, 4)] = nueva(n, 4)
    # E05: inmediatez con el texto vigente (¿por qué importa el tiempo?) y el ejemplo destacado
    ps = di_sec(L, '5. Inmediatez', '6. Subsidiariedad')
    e0 = S(d, 5)
    n = dict(M.compacta(e0['titulo_genially'], [('sub', ps[0][0].upper() + ps[0][1:]), ('p', ps[1]), ('p', ps[3], 'clave'),
                                                ('malla', [[('No hay un término fijo', ps[2], 'reloj'), ('No es el plazo del requerimiento', ps[4], 'documento'),
                                                            ('Lo que ha dicho la Corte', ps[5:8], 'libros')]])],
                        guia='Lea el ejemplo y abra cada recuadro.'))
    d['scenes'][pos(d, 5)] = nueva(n, 5)
    # E06: subsidiariedad como el mapa conceptual de la E07, con el texto vigente
    ps = di_sec(L, '6. Subsidiariedad', '7. Tutela como mecanismo transitorio')
    e0 = S(d, 6)
    n = dict(M.esquema(e0['titulo_genially'], 'balanza', [('No reemplaza todos los procesos', ps[0], 'libros'), ('Tres situaciones', ps[1], 'carpetas'),
                                                          ('Idóneo, eficaz y perjuicio irremediable', ps[2], 'lupa'), ('Para quien no hace la defensa', ps[3], 'personas')]))
    a_mapa(n, u, l, 6)
    d['scenes'][pos(d, 6)] = nueva(n, 6)


def L33(d, u=3, l=3):
    L = 'Lección 3.3.'
    # E04: mapa conceptual con los 7 requisitos generales a la vista; los defectos específicos en su pantalla
    rq = di_sec(L, '4.1. Requisitos generales', '4.2. Defectos específicos')
    rq = [x for x in rq if re.match(r'^\d\. ', x)]
    e0 = S(d, 4)
    intro = textos(e0, items(e0)[0]) + textos(e0, items(e0)[1])
    objs = ['personas', 'balanza', 'escalones', 'reloj', 'documento', 'lupa', 'tribunal']
    n = dict(M.esquema('Tutela contra providencias judiciales: requisitos generales', 'tribunal',
                       [(sin_num(x).split('. ')[0], sin_num(x).split('. ', 1)[1], objs[k]) for k, x in enumerate(rq)]))
    n['lead'] = [seg_nuevo(n, t) for t in intro]
    a_mapa(n, u, l, 4)
    d['scenes'][pos(d, 4)] = nueva(n, 4)
    df = di_sec(L, '4.2. Defectos específicos', '5. Personas de especial')
    nd = dict(M.compacta('Tutela contra providencias judiciales: defectos específicos', [('p', df[1]), ('p', df[0], 'alerta'), ('p', df[2])]))
    d['scenes'].insert(pos(d, 4) + 1, nueva(nd, 'n4'))
    # E05 (cosa juzgada), E06 (temeridad) y E08 (implicaciones) no están en el DI vigente de la 3.3 (van en la 3.4): salen
    for k in (5, 6, 8):
        d['scenes'].remove(S(d, k))
    # Cierre de la lección (§8 del DI), antes del caso
    ci = di_sec(L, '8. Cierre de la lección', '9. Caso de aplicación')
    nc = dict(M.compacta('Cierre de la lección', [('p', x) for x in ci]))
    d['scenes'].insert(pos(d, 9), nueva(nc, 'n8'))
    # E09: el caso del DI (la grabación judicial) con sus 4 preguntas y el audio
    sit = di_sec(L, '9.1. Situación', '9.2. Análisis')
    ana = di_sec(L, '9.2. Análisis', '9.3. Preguntas')
    pq = di_sec(L, '9.3. Preguntas', '9. Conclusión')
    n = dict(M.compacta('Caso de aplicación: una nueva solicitud de acceso a una grabación judicial', [
        ('malla', [[('Situación', sit, 'expediente'), ('Análisis del caso', ana + [pq[4]], 'lupa')]]),
        ('sub', 'Preguntas para resolver el ejercicio'), ('lista', pq[:4], True)],
        ilus=S(d, 9).get('ilustracion'), guia='Escuche la situación, piense en las preguntas y abra el análisis.'))
    caso_audio(n, u, l, 1, 'Caso de aplicación: la grabación judicial', sit)
    d['scenes'][pos(d, 9)] = nueva(n, 9)


def L34(d, u=3, l=4):
    L = 'Lección 3.4.'
    # E02: el problema con el texto vigente (qué es la improcedencia y qué no significa), como mapa con ramas
    ps = di_sec(L, '2. Problema jurídico-institucional', '3. Marco normativo')
    e0 = S(d, 2)
    n = dict(M.esquema(e0['titulo_genially'], 'balanza', [('Qué es la improcedencia', ps[0], 'documento'), ('Improcedencia no es negar el amparo', ps[1], 'balanza'),
                                                          ('Las causales del artículo 6', ps[2], 'libros'), ('Ejemplo', ps[3], 'lupa'), ('Lo que el servidor sí debe hacer', ps[4], 'escudo')]))
    a_mapa(n, u, l, 2)
    d['scenes'][pos(d, 2)] = nueva(n, 2)
    # E03: intro corta y una ventana por causal; el texto completo en PDF
    e = S(d, 3)
    b = flujo(e)
    full = list(e['segmentos'])
    ps_ = [z for z in b['flujo'] if z['t'] == 'p']
    for z in ps_[1:]:
        b['flujo'].remove(z)
    e['guia'] = 'Lea la introducción y abra cada causal.'
    pdf(e, 'u3-l4-articulo-6-decreto-2591.pdf', 'Clic para descargar el texto completo', 'Causales de improcedencia: artículo 6 del Decreto 2591 de 1991 (PDF)')
    e['_pdf'] = {'titulo': e['titulo_genially'], 'parrafos': full}
    # E04 y E05: sin la ilustración que se come el lienzo; la idea clave arriba
    for k in (4, 5, 7):
        e = S(d, k)
        e.pop('ilustracion', None)
        flujo(e).pop('escenario', None)
    e = S(d, 4)
    b = flujo(e)
    primera = e['segmentos'][0].split('. ')[0] + '.'
    j = seg_nuevo(e, primera)
    b['flujo'].insert(0, {'t': 'p', 's': [j], 'c': 'clave', 'n': 0})
    e = S(d, 5)
    t = ' '.join(e['segmentos'])
    m = re.search(r'[^.]*(término|plazo)[^.]*razonable[^.]*\.', t) or re.search(r'[^.]*término[^.]*\.', t)
    j = seg_nuevo(e, m.group(0).strip())
    flujo(e)['flujo'].insert(0, {'t': 'p', 's': [j], 'c': 'clave', 'n': 0})
    # E07: arriba, que la tutela no es una instancia adicional ni reemplaza los recursos ordinarios
    e = S(d, 7)
    t = ' '.join(e['segmentos'])
    j = seg_nuevo(e, e['segmentos'][0].split('. ')[0] + '.')
    flujo(e)['flujo'].insert(0, {'t': 'p', 's': [j], 'c': 'clave', 'n': 0})
    e.pop('ilustracion', None)
    # E10: audio de la situación (caso de temeridad, sí es el del DI)
    audio_situacion(d, 10, u, l, 1, 'Caso de aplicación: la tutela contra el juzgado penal')
    # E11: la lista del DI de la 3.4 (reconocimiento y canalización de comunicaciones relacionadas con tutela)
    ls = di_sec(L, '11. Lista de reconocimiento', '12. Conclusión')
    ult, nota = ls[-1].split('? ', 1)
    n = dict(M.compacta('Lista de reconocimiento y canalización de comunicaciones relacionadas con tutela',
                        [('p', ls[0]), ('chequeo', ls[1:-1] + [ult + '?']), ('p', nota, 'alerta')]))
    d['scenes'][pos(d, 11)] = nueva(n, 11)
    # E12: conclusión con la síntesis del DI vigente
    cc = di_sec(L, '12. Conclusión', '3.6 Recursos académicos')
    n = dict(M.compacta('Conclusión', [('p', cc[0], 'clave'), ('p', cc[1]), ('p', cc[2]), ('p', cc[3])]))
    d['scenes'][pos(d, 12)] = nueva(n, 12)


# =================================================================== UNIDAD 4
def malla_a_ruta(d, n, intro_extra=True):
    """Compacta con «p … malla(pasos) … p» -> ruta paso a paso con la intro arriba (y el cierre como último paso)."""
    e0 = S(d, n)
    b = flujo(e0)
    ps = [e0['segmentos'][i] for z in b['flujo'] if z['t'] == 'p' for i in z['s']]
    celdas = [b['items'][c[0]] for z in b['flujo'] if z['t'] == 'malla' for f in z['filas'] for c in f['celdas']]
    pasos = [(sin_num(it['label']), ' '.join(sin_num(e0['segmentos'][i]) for i in it['segs'])) for it in celdas]
    corte = [z['t'] for z in b['flujo']].index('malla')
    antes = [e0['segmentos'][i] for z in b['flujo'][:corte] if z['t'] == 'p' for i in z['s']]
    despues = [e0['segmentos'][i] for z in b['flujo'][corte:] if z['t'] == 'p' for i in z['s']]
    r = ruta_de(e0['titulo_genially'], pasos, intro=' '.join(antes) if antes else None, tag=n)
    if despues:
        r['tail'] = [seg_nuevo(r, t) for t in despues]
    d['scenes'][pos(d, n)] = r
    return r


def numerar(e):
    for z in flujo(e)['flujo']:
        if z['t'] == 'lista':
            z['num'] = True


def L41(d, u=4, l=1):
    # E03: los plazos del trámite en un recuadro aparte
    e = S(d, 3)
    b = flujo(e)
    j = seg_nuevo(e, 'Plazos del trámite: procedimiento preferente y sumario; el juez debe fallar dentro de los diez (10) días siguientes a la presentación de la solicitud (Decreto 2591 de 1991).')
    b['flujo'].insert(0, {'t': 'p', 's': [j], 'c': 'regla', 'n': 0})
    b['items'][0]['segs'].insert(0, j)
    # E06: la rejilla de los 7 elementos del informe -> ruta paso a paso con la intro arriba
    malla_a_ruta(d, 6)
    # E08: audio de la situación. E09: lista (general)
    audio_situacion(d, 8, u, l, 1, 'Caso de aplicación: la tutela de la ciudadana y el informe')


def L42(d, u=4, l=2):
    # E03 y E06: mapa (general). E04: la rejilla de 8 campos -> ruta paso a paso
    malla_a_ruta(d, 4)
    # E07: la matriz de seguimiento, que pide scroll, como tabla descargable
    e = S(d, 7)
    full = list(e['segmentos'])
    b = flujo(e)
    tb = [z for z in b['flujo'] if z['t'] == 'tabla'][0]
    filas = [[e['segmentos'][c] for c in f] for f in tb['filas']]
    cab = [e['segmentos'][c] for c in tb['cols']]
    n = dict(M.compacta(e['titulo_genially'], [('p', full[0]), ('p', 'La matriz básica tiene ocho campos: ' + ', '.join(f[0].lower() for f in filas[:-1]) + ' y ' + filas[-1][0].lower() + '. Descárguela para usarla.', 'clave'), ('p', full[20])]))
    pdf(n, 'u4-l2-matriz-de-seguimiento.pdf', 'Clic para descargar la matriz', 'Matriz de seguimiento institucional (PDF)')
    n['_pdf'] = {'titulo': e['titulo_genially'], 'parrafos': [full[0], full[1]], 'tabla': [cab] + filas, 'pie': [full[20]]}
    d['scenes'][pos(d, 7)] = nueva(n, 7)
    # E08: audio
    audio_situacion(d, 8, u, l, 1, 'Caso de aplicación: la orden de contactar a una mujer mayor')


def L43(d, u=4, l=3):
    L = 'Lección 4.3.'
    # E03: la rejilla de 7 elementos de la orden -> ruta paso a paso
    malla_a_ruta(d, 3)
    # nueva, después de la E05: el caso práctico de la impugnación y el cumplimiento en paralelo (§5 del DI), con audio
    ps = di_sec(L, '5. Impugnación y cumplimiento', '6. Hecho superado')
    sit = [re.sub(r'^Situación\s+', '', ps[4]), ps[5]]
    ana = [re.sub(r'^Análisis y actuación que corresponde\s+', '', ps[6]), ps[7], ps[8]]
    adv = re.sub(r'^Advertencia para recordar\s+', '', ps[9])
    nc = dict(M.compacta('Caso práctico: la impugnación y el cumplimiento deben avanzar en paralelo', [
        ('p', ps[3].split('Caso práctico ', 1)[1], ''),
        ('malla', [[('Situación', sit, 'expediente'), ('Análisis y actuación que corresponde', ana, 'lupa')]]),
        ('p', 'Advertencia para recordar: ' + adv, 'alerta')], guia='Escuche la situación y abra el análisis.'))
    caso_audio(nc, u, l, 2, 'Caso práctico: Mariana Ríos y la certificación', sit)
    d['scenes'].insert(pos(d, 5) + 1, nueva(nc, 'n5'))
    # E07: 530 palabras -> dos pestañas (cumplimiento del fallo / incidente de desacato)
    dz = di_sec(L, '7. Incumplimiento y desacato', '8. Lineamientos jurisprudenciales')
    e0 = S(d, 7)
    t1 = dict(M.compacta('Cumplimiento del fallo', [('p', dz[0])]))
    t2 = dict(M.compacta('Incidente de desacato', [('p', dz[1]), ('p', dz[16]), ('p', dz[17])]))
    d['scenes'][pos(d, 7)] = con_pestanas(e0['titulo_genially'], [('Cumplimiento del fallo', t1), ('Incidente de desacato', t2)], 7)
    # nueva: el cuadro comparativo (cumplimiento frente a desacato) y la advertencia pedagógica en ventana
    T = [('Finalidad', 'Lograr que la orden se ejecute y se restablezca el derecho protegido.', 'Inducir el cumplimiento mediante un trámite que puede conducir a una sanción personal, si se demuestra la responsabilidad exigida.'),
         ('Pregunta central', '¿Se realizó lo que ordenó el juez, en su alcance y plazo?', '¿Hubo incumplimiento y puede atribuirse a una conducta dolosa o culposa de la persona obligada?'),
         ('Naturaleza del examen', 'Objetivo: se verifica la ejecución material de la orden. No exige probar culpa o dolo para adoptar medidas de cumplimiento.', 'Objetivo y subjetivo: además del incumplimiento, exige establecer la responsabilidad personal y su relación con el resultado.'),
         ('Qué debe verificarse', 'Contenido de la orden, destinatario, plazo, acciones realizadas, resultado y medidas pendientes para ejecutarla integralmente.', 'Claridad y conocimiento de la orden, identificación del obligado, posibilidades reales de cumplir, conducta desplegada, obstáculos y dolo o culpa atribuibles.'),
         ('Papel de los obstáculos', 'Deben identificarse y acreditarse para adoptar medidas efectivas que permitan superar la dificultad. Alegarlos no equivale a cumplir.', 'Deben valorarse para determinar si el incumplimiento es atribuible a la persona. No toda dificultad excluye su responsabilidad ni toda demora demuestra culpa.'),
         ('Pruebas relevantes', 'Providencia y notificación, cronología, documentos de ejecución y evidencia de que el resultado ordenado se produjo.', 'Además de esos soportes, comunicaciones, gestiones, decisiones y pruebas de las circunstancias que permitan valorar la conducta personal del obligado.'),
         ('Resultado posible', 'Órdenes y medidas judiciales dirigidas a obtener la ejecución efectiva. La actividad de seguimiento no se agota en recibir informes.', 'Sanción si se prueba responsabilidad subjetiva, con respeto del debido proceso; o decisión sin sanción cuando no se acreditan sus presupuestos.'),
         ('Garantías procesales', 'El juez verifica la ejecución de la orden dentro de sus competencias y con respeto de las garantías aplicables.', 'La persona investigada debe conocer el trámite, ejercer su defensa, controvertir las pruebas y aportar o solicitar las pertinentes.'),
         ('Relación entre los mecanismos', 'Puede adelantarse sin esperar a que se solicite o decida un incidente de desacato.', 'No reemplaza el cumplimiento. La falta de sanción no convierte en ejecutada una orden pendiente.'),
         ('Actuación institucional', 'Continuar la ejecución, coordinar responsables, resolver obstáculos y acreditar resultados ante el juez.', 'Atender el incidente con información individualizada y soportes, garantizar la defensa y continuar simultáneamente las actuaciones de cumplimiento.')]
    intro = dz[2].split('Cumplimiento del fallo e incidente de desacato ', 1)[1]
    adv = dz[15].replace('Advertencia pedagógica ', '')
    fuente = dz[14].replace('C- 367', 'C-367')
    ncc = dict(M.compacta('Cuadro comparativo: cumplimiento del fallo e incidente de desacato', [
        ('p', intro), ('malla', [[('Advertencia pedagógica', adv, 'escudo')]]),
        ('tabla', ['Aspecto', 'Cumplimiento del fallo', 'Incidente de desacato'], [list(x) for x in T]), ('p', fuente)],
        guia='Abra la advertencia y recorra el cuadro.'))
    pdf(ncc, 'u4-l3-cuadro-cumplimiento-y-desacato.pdf', 'Clic para descargar el cuadro', 'Cuadro comparativo: cumplimiento del fallo e incidente de desacato (PDF)')
    ncc['_pdf'] = {'titulo': ncc['titulo_genially'], 'parrafos': [intro], 'tabla': [['Aspecto', 'Cumplimiento del fallo', 'Incidente de desacato']] + [list(x) for x in T], 'pie': ['Advertencia pedagógica: ' + adv, fuente]}
    d['scenes'].insert(pos(d, 7) + 1, nueva(ncc, 'n7'))
    # E08: mapa (general). E09: audio
    audio_situacion(d, 9, u, l, 1, 'Caso de aplicación: la orden de responder en 48 horas')


def L44(d, u=4, l=4):
    # E03: la rejilla de 8 criterios -> ruta paso a paso
    malla_a_ruta(d, 3)
    # Casos 1 a 5: audio de la situación y actuaciones numeradas
    for k, (n, m) in enumerate([(4, 5), (6, 7), (8, 9), (10, 11), (12, 13)], 1):
        e = S(d, n)
        caso_audio(e, u, l, k, e['titulo_genially'].split('. ', 1)[0] + ': ' + e['titulo_genially'].split('. ', 1)[1].lower(), celda_txt(e, 'Situación'))
        numerar(S(d, m))
    # E14: la matriz con botón para descargarla en PDF
    e = S(d, 14)
    tb = [z for z in flujo(e)['flujo'] if z['t'] == 'tabla'][0]
    pdf(e, 'u4-l4-matriz-de-analisis-de-casos.pdf', 'Clic para descargar la matriz', 'Matriz de análisis de casos (PDF)')
    e['_pdf'] = {'titulo': e['titulo_genially'], 'parrafos': [e['segmentos'][0]],
                 'tabla': [[e['segmentos'][c] for c in tb['cols']]] + [[e['segmentos'][c] for c in f] for f in tb['filas']]}


# =================================================================== armado
def cargar(u, l):
    d = leer(u, l)
    for n, e in enumerate(d['scenes'], 1):
        e['_o'] = n
    return d


REV = {(1, 1): L11, (1, 2): L12, (1, 3): L13, (1, 4): L14, (2, 1): L21, (2, 2): L22, (2, 3): L23, (2, 4): L24, (3, 1): L31, (3, 2): L32, (3, 3): L33, (3, 4): L34, (4, 1): L41, (4, 2): L42, (4, 3): L43, (4, 4): L44}


def main(solo=None):
    res = {}
    for u, l in LECC:
        if solo and (u, l) not in solo:
            continue
        d = cargar(u, l)
        generales(d, u, l)
        if (u, l) in REV:
            REV[(u, l)](d)
        res['%d.%d' % (u, l)] = [{'n': i + 1, 'o': e.get('_o'), 'titulo': e['titulo_genially'], 'layout': e['layout'],
                                  'pdf': e.get('_pdf'), 'descarga': (e.get('descarga') or {}).get('href'),
                                  'tambien': e.get('_tambien', [])} for i, e in enumerate(d['scenes'])]
        for e in d['scenes']:
            if e.get('pestanas') and e.get('descarga'):
                for h in e['pestanas']:
                    h['descarga'] = e['descarga']
        limpio = copy.deepcopy(d)
        for e in limpio['scenes']:
            for k in [k for k in e if k.startswith('_')]:
                e.pop(k)
        publicar(u, l, limpio)
    os.makedirs('/home/claude/dp2/out', exist_ok=True)
    json.dump(res, open('/home/claude/dp2/out/escenas_dp.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(CASOS, open('/home/claude/dp2/out/casos.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for uu in range(1, 5):
        sub = {k: v for k, v in CASOS.items() if k.startswith('u%d' % uu)}
        if os.path.isdir(OUT + 'unidad-%02d/comun/casos' % uu):
            json.dump(sub, open(OUT + 'unidad-%02d/comun/casos/casos.json' % uu, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return res


if __name__ == '__main__':
    solo = [tuple(map(int, a.split('.'))) for a in sys.argv[1:]] or None
    r = main(solo)
    for k, v in r.items():
        print(k, len(v), 'escenas')
