# -*- coding: utf-8 -*-
"""Gerencia judicial, videos de profe (27 nov 2026): escribe los planes (plan_gj*.py) a partir de los cortes medidos
(gj_cortes.py -> cortes_*.json, en cuadros de la grabacion original) y de los rangos de cada _fuente.mp4
(fuentes_piezas.json). Cada corte de diferencia de imagen grande (> 4,5) cambia de plano hasta la primera pausa
(>= 0,35 s) que caiga al menos 2,5 s despues; los chicos van con SUAVE."""
import json, os
T = 'D:/DAE/_tmp/gj_p/'
D = 'D:/DAE/_repo/cursos/gerencia_judicial/profe/'
W = {k: [w for w in json.load(open(T + 'stt_fuente/' + k + '.json', encoding='utf-8'))['words'] if w['type'] == 'word'] for k in ('gjv1', 'gjv2', 'gjv3')}
FP = json.load(open(T + 'fuentes_piezas.json', encoding='utf-8'))
C = {}
for f in ('cortes_ci.json', 'cortes_ci_b.json', 'cortes_u.json'):
    for p in json.load(open(T + f, encoding='utf-8')):
        C.setdefault(p['clave'], []).append(p)


def corte(clave, nota):
    for p in C[clave]:
        for c in p['cortes']:
            if c['nota'] == nota:
                return c
    raise KeyError(clave + ' ' + nota)


def dato(clave, k):
    return [p for p in C[clave] if k in p][0][k]


def pausa(src, k_in, k_lim, minimo=0.35, tras=2.5):
    ws = W[src]
    for i in range(1, len(ws)):
        g0, g1 = ws[i - 1]['end'], ws[i]['start']
        m = (g0 + g1) / 2 * 30
        if g1 - g0 >= minimo and m >= k_in + tras * 30:
            return int(round(m)) if m < k_lim else None
    return None


def tramos(src, k_ini, k_fin, cortes):
    """[(k0, k1, 'CERRADO'|None)] en cuadros de la grabacion original."""
    tr, ini, win = [], k_ini, None
    cortes = sorted(cortes, key=lambda c: c['k_out'])
    for j, c in enumerate(cortes):
        tr.append([ini, c['k_out'], win])
        lim = cortes[j + 1]['k_out'] if j + 1 < len(cortes) else k_fin
        if c['dif'] > 4.5:
            nuevo = None if win else 'CERRADO'
            if nuevo:
                p = pausa(src, c['k_in'], lim)
                if p:
                    tr.append([c['k_in'], p, 'CERRADO']); ini, win = p, None; continue
            ini, win = c['k_in'], nuevo
        else:
            ini = c['k_in']
    tr.append([ini, k_fin, win])
    return tr


def txt(src, k0, k1):
    return ' '.join(w['text'] for w in W[src] if k0 / 30 <= w['start'] < k1 / 30)


def doc_cortes(src, cs, off):
    out = []
    for c in sorted(cs, key=lambda c: c['k_out']):
        t = (c['k_out'] - 0) / 30
        out.append('- %d:%04.1f de la grabación, «…%s [%s] %s…»: salen los cuadros %d a %d de la fuente (%.2f s); energía en los bordes %.0f y %.0f dB bajo la voz; '
                   'diferencia de imagen %.1f%s.' % (t // 60, t % 60, c['antes'][-40:], c['quita'], c['despues'][:30], c['k_out'] - off, c['k_in'] - off - 1,
                                                       (c['k_in'] - c['k_out']) / 30, -c['db_out'], -c['db_in'], c['dif'], ' (plano cerrado después)' if c['dif'] > 4.5 else ' (SUAVE)'))
    return '\n'.join(out)


def fmt_tr(tr, off):
    s = []
    for a, b, w in tr:
        s.append('(%d, %d%s)' % (a - off, b - off, ', CERRADO' if w else ''))
    return '[' + ', '.join(s) + ']'


CAB = '# -*- coding: utf-8 -*-\nr"""%s\n"""\nimport os\nimport sys\n\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\nfrom base_gj_profe import *  # noqa: E402,F401,F403\nfrom base_gj_profe import %s, PROFE, CERRADO  # noqa: E402\n\n'


def escribir(nombre, doc, arma, llamada, tr, off, lt):
    s = CAB % (doc, arma) + 'globals().update(%s, %s))\n\nSUAVE = 3            # cuadros de mezcla en un corte sin cambio de plano\n\nITEMS = [\n    (\'lt01\', \'lt\', %.2f, %.2f, PROFE),\n]\n' % (llamada, fmt_tr(tr, off), lt, lt + 8)
    compile(s, nombre, 'exec')
    open(D + nombre, 'w', encoding='utf-8').write(s)
    return s


res = {}
# bienvenida al curso
sel = ['rotulo leido: es la leccion', 'aqui nos--', 'rotulo leido: competencias e icono', 'la eficacia-- perdon,', 'el mole--',
       'este-- segun (variante)', 'pretender una,', 'rotulo leido: cuatro circulos', 'rotulo leido: tres items',
       'rotulo leido: evaluacion recursos tiempo', 'rotulo leido: dos tipos de evaluacion', 'perdon.',
       'trans-- la (var)', 'que la-- (var)', 'puede-- le (var)', 'car-- del (var)', 'la integracion--', 'placa-- la (var)']
cs = [corte('gjci_b', n) if n in [c['nota'] for p in C['gjci_b'] for c in p['cortes']] else corte('gjci', n) for n in sel]
ki, kf = dato('gjci', 'k_ini'), dato('gjci', 'k_fin')
tr = tramos('gjv1', ki, kf, cs)
res['gjci'] = tr
doc = ('Bienvenida al curso «Gerencia judicial» (27 nov 2026). **Entrega provisional** (ver `base_gj_profe`).\n\n'
       '**Fuente.** `CURSO/INICIO/01 VIDEO/VIDEO 1 GERENCIA JUDICIAL TOMA1.mp4` (866.926.595 bytes, 44.876 cuadros, 24:56), recortada entera sobre el\n'
       'fondo de la Fiscalía. Entra del cuadro %d (medio segundo antes de «Reciban») al %d (0,8 s después de «unidad.»).\n\n'
       '**%d cortes**, cada uno medido (`lote/cortes.py`):\n%s\n\n'
       '**Qué se deja.** Los tropiezos sin silencio donde cortar («entraremos— entendemos», «dese— deje», «quien le— se lo»,\n'
       '«incorproan— incorporando», «inste— instituciones», «la fiscalí— la Fiscalía», «discrecio— de discrecionalidad», «epi— equipo»,\n'
       '«experie— experiencial», «pri— privilegian»). **Para revisar:** en 16:31 dice «Esta sensación es un problema de esfuerzo, es un\n'
       'problema de método» (en el inicio de la U3 lo dice bien: «no es un problema de esfuerzo»). Dura casi 25 minutos (la ficha pide\n'
       'hasta 8 para el video de presentación): se entrega completo.\n\n'
       'El lower third entra cuando dice su nombre («Mi nombre es Jairo Ignacio Acosta Aristizábal», 1:05) y dura 8 s.'
       % (ki, kf, len(cs), doc_cortes('gjv1', cs, 0)))
escribir('plan_gjci.py', doc, 'armar_curso', "armar_curso('INICIO'", tr, 0, 65.3)

# unidades de VIDEO 3
NOM = {'u1c': (1, 'CIERRE'), 'u2i': (2, 'INICIO'), 'u2c': (2, 'CIERRE'), 'u3i': (3, 'INICIO'), 'u3c': (3, 'CIERRE'), 'u4i': (4, 'INICIO'), 'u4c': (4, 'CIERRE')}
SEL = {'u1c': [], 'u2i': ['rotulo: Las cinco lecciones.'], 'u2c': ['rotulo: Tratar a todos igual...', 'la re--'],
       'u3i': ['rotulo: A proposito de la evaluacion integradora'], 'u3c': ['La vel--', 'en que, (repetido)', 'rotulo: Tres indicadores para mi tablero.'],
       'u4i': ['rotulo: Frente a este actor... Influencia?'], 'u4c': ['con la que solo hay coordinacion, (repetido)', 'rotulo: Diagnostico de entrada versus respuesta final.']}
NOTA = {'u1c': 'Empieza en «Llegamos al final de la unidad primera»: sale el rótulo leído «Cierre de la unidad primera.». Se deja «se exige en los\nacuerdos— en algunos acuerdos» (no hay silencio donde cortar).',
        'u2i': 'Se deja «a las disposiciones— a la disposición» (el borde de salida queda en la «s» de «adaptarlos»).',
        'u2c': '', 'u3i': 'Empieza en «Bienvenidas, bienvenidos a la unidad tres»: sale el rótulo leído «Unidad tres. Gestión de servicios, planeación y\nseguimiento.» (el cartón de título ya lo dice).',
        'u3c': '**Para revisar:** «Un buen objetivo en clave de Drucker nos dice: "Mejoraremos la investigación de delitos complejos"» queda como se oye.',
        'u4i': '', 'u4c': 'Termina en «Muchas gracias.»; después dice «Aquí terminamos», fuera de la pieza.'}
for k, (u, pz) in NOM.items():
    cs = [corte(k, n) for n in SEL[k]]
    ki, kf = dato(k, 'k_ini'), dato(k, 'k_fin')
    if k == 'u1c':
        ki = int(round((181.46 - 0.5) * 30))
    f0 = FP[k]['cuadro0']
    tr = tramos('gjv3', ki, kf, cs)
    res[k] = [[a - f0, b - f0, w] for a, b, w in tr]
    w0 = [w for w in W['gjv3'] if w['start'] >= ki / 30 - 0.01][0]
    lt = w0['start'] + 1.2 - f0 / 30
    doc = ('%s de la unidad %d, «%s», de «Gerencia judicial» (27 nov 2026). **Entrega provisional** (ver `base_gj_profe`).\n\n'
           '**Fuente.** `01 VIDEO/gj_%s_fuente.mp4`, sacada de `00 FUENTES/VIDEO 3 … apertura y cierre.mp4` (cuadros %d a %d de esa\n'
           'grabación; los tramos de abajo ya están en cuadros del _fuente). Entra medio segundo antes de «%s» y sale 0,8 s después de «%s».\n\n'
           '%s%s\n\nEl lower third entra 1,2 s después de la primera palabra y dura 8 s.'
           % ('Inicio' if pz == 'INICIO' else 'Cierre', u, {1: 'Contexto estratégico y política criminal', 2: 'Liderazgo y gestión del talento humano', 3: 'Gestión de servicios, planeación y seguimiento', 4: 'Articulación interinstitucional y territorial'}[u],
              k, FP[k]['cuadro0'], FP[k]['cuadro1'], w0['text'], dato(k, 'ultima'),
              ('**%d cortes**:\n%s\n\n' % (len(cs), doc_cortes('gjv3', cs, f0))) if cs else '**Sin cortes.**\n\n', NOTA[k]))
    escribir('plan_gju%d%s.py' % (u, pz[0].lower()), doc, 'armar_unidad', "armar_unidad(%d, '%s'" % (u, pz), [[a, b, w] for a, b, w in tr], f0, lt)

# inicio de la U1: VIDEO 2 + la frase de VIDEO 3
fp = FP['u1i']; a0, a1 = fp['a']; b0, b1 = fp['b']; off_b = a1 - a0
ca = corte('u1ia', 'sale la frase de la evaluacion de VIDEO 2')
cb_in = corte('u1ib', 'entrada de la frase de VIDEO 3 (antes de Tendra)')['k_in']
cb_out = corte('u1ib', 'salida de la frase de VIDEO 3 (despues de temas.)')['k_out']
ki, kf = dato('u1ia', 'k_ini'), dato('u1ia', 'k_fin')
tr = [[ki - a0, ca['k_out'] - a0, None], [off_b + cb_in - b0, off_b + cb_out - b0, 'CERRADO'], [ca['k_in'] - a0, kf - a0, None]]
res['u1i'] = tr
doc = ('Inicio de la unidad 1, «Contexto estratégico y política criminal», de «Gerencia judicial» (27 nov 2026). **Entrega provisional**\n'
       '(ver `base_gj_profe`). **Compuesto entre dos tomas.**\n\n'
       '**Fuente.** `01 VIDEO/gj_u1i_fuente.mp4` = VIDEO 2 (cuadros %d a %d: la toma completa, después del arranque en falso «voy a volver a\n'
       'comenzar…») seguida de VIDEO 3 (cuadros %d a %d: la frase de la evaluación de la otra toma), en cuadros del _fuente desde %d.\n\n'
       '**El cambio.** En VIDEO 2 dice «Tendrá chequeos formativos sin nota y una evaluación calificada al cierre de cada unidad de los\n'
       'tres temas»; en VIDEO 3, «Tendrá chequeos formativos sin nota, una evaluación calificada al cierre de cada uno de los tres temas»,\n'
       'que es lo que dice la ficha (evaluación al cierre de cada tema en las unidades 1 y 2). Sale la de VIDEO 2 (%.2f s, con la pausa\n'
       'de 3,9 s de antes) y entra la de VIDEO 3 en plano cerrado; después vuelve VIDEO 2 en plano entero en «Mi recomendación».\n'
       'Bordes: %.0f y %.0f dB bajo la voz en VIDEO 2; %.0f y %.0f en VIDEO 3.\n\n'
       'La toma de VIDEO 3 entera no se usa: lee los rótulos («Los temas, uno a uno», «La evaluación calificada al cierre de cada tema.\n'
       'Chequeos formativos sin nota.») y tiene más tropiezos.\n\nEl lower third entra 1,2 s después de la primera palabra y dura 8 s.'
       % (a0, a1, b0, b1, off_b, (ca['k_in'] - ca['k_out']) / 30, -ca['db_out'], -ca['db_in'],
          -corte('u1ib', 'entrada de la frase de VIDEO 3 (antes de Tendra)')['db_in'], -corte('u1ib', 'salida de la frase de VIDEO 3 (despues de temas.)')['db_out']))
lt = 45.32 + 1.2 - a0 / 30
s = CAB % (doc, 'armar_unidad') + "globals().update(armar_unidad(1, 'INICIO', %s))\n\nSUAVE = 3\n\nITEMS = [\n    ('lt01', 'lt', %.2f, %.2f, PROFE),\n]\n" % (fmt_tr(tr, 0), lt, lt + 8)
compile(s, 'plan_gju1i.py', 'exec')
open(D + 'plan_gju1i.py', 'w', encoding='utf-8').write(s)
json.dump(res, open(T + 'tramos.json', 'w', encoding='utf-8'), indent=1)
for k, v in res.items():
    print(k, len(v), 'tramos', sum(b - a for a, b, w in v) / 30, 's', sum(1 for a, b, w in v if w), 'cerrados')
print('LISTO')
