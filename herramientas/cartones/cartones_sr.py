# -*- coding: utf-8 -*-
r"""Cartones verbatim de los CASOS del curso SRPA y justicia restaurativa (es
`cartones_ei`, con los tiempos de Scribe y las reglas de siempre).

    python cartones_sr.py              calcula, comprueba y escribe el json
    python cartones_sr.py --quemar     ademas quema los .mov en 02 CARTONES

CASO NICO (12 nov)
    Un cartón por momento que el caso subraya, con el texto LITERAL del
    documento (dígitos: 15 años, 9:15 a. m., 30 metros, 10 minutos).
    - Sin cartón: n01 (lo lleva el rótulo de Nico), n11, n20, n33 y n37-n40
      (los lleva la lista de After Effects: el desayuno, lo que la policía no
      hizo, lo que el defensor no hizo y la valoración inicial), y el final de
      n26 (la lista de lo que el CAE ofrecía).
    - Fuera, como en Enfoque diferencial y EI: la agresión (n14, n15). La voz
      la dice; el cartón no la subraya.
    - Las palabras del defensor (n28, n29) sí van, entre comillas: son lo que
      el caso discute.
    - Rótulo, lista y cartón no conviven: un cartón que empieza antes de una
      ventana de rótulo o de lista se corta donde ella empieza.
"""
import glob
import json
import os
import re
import sys
import unicodedata

H = r'D:\DAE\_repo\herramientas'
for sub in ('cartones', 'montaje', os.path.join('voz', 'textos')):
    sys.path.insert(0, os.path.join(H, sub))

from guion_sr import VIDEOS, bloques            # noqa: E402
import rutas_sr as R                            # noqa: E402

CUERPO = 52
SALTO = int(round(CUERPO * 1.36))
FPS = 24000 / 1001.0
CABEZA = 182 + 119
RESPIRO = 24
N_RESPIRO = 48          # el respiro de la pieza (sr_pieza.N_RESPIRO)
COMODO = 10.0
TOPE_RENGLONES = 3

SALIDA = r'D:\DAE\_tmp\sr\cartones_sr.json'

# Estándares interamericanos (5 nov): escogidos a mano con las voces ya
# medidas, un cartón por bloque (dos en el S04 d04, la enumeración de las
# fuentes). Lo que va: lo que la situación pone a decidir -quién, qué fuente,
# qué versión, qué inconsistencia- y la frase final de cada caso. Fuera, como
# en Enfoque diferencial: las agresiones del S08 h02 («había sufrido
# agresiones durante su detención» lo dice la voz; el cartón no lo subraya).
ELEGIDOS = {
 'NICO': [
  ('n02_documentos', 'no había sido reconocido legalmente por sus progenitores'),
  ('n03_escuela', 'No figuraba matriculado en ninguna institución educativa'),
  ('n04_puente', 'Desde hacía varios meses habitaba debajo de un puente peatonal'),
  ('n05_alimentacion', 'pequeños alimentos que conseguía sin autorización de sus '
   'propietarios.'),
  ('n06_comerciantes', 'Algunos habían intentado ayudarlo entregándole comida,'),
  ('n06_comerciantes', 'otros manifestaban inconformidad por su presencia constante '
   'en los establecimientos.'),
  ('n07_recurrente', 'Nico se acercaba a las mesas, tomaba los alimentos y salía '
   'corriendo sin pagar.'),
  ('n08_discusiones', 'el adolescente estaba afectando sus ventas'),
  ('n09_reunion', '«esperarlo entre todos, atraparlo y entregarlo a la Policía para '
   'que aprendiera a respetar lo ajeno».'),
  ('n10_domingo', 'El domingo 12 de abril de 2022, aproximadamente a las 9:15 a. m.'),
  ('n12_huida', 'Nico se acercó a la mesa, tomó el tamal y el recipiente con el caldo '
   'y emprendió la huida.'),
  ('n13_persecucion', 'lograron interceptarlo, aproximadamente a 30 metros del '
   'establecimiento.'),
  ('n16_video', 'Un comerciante grabó parcialmente lo ocurrido con su teléfono '
   'celular.'),
  ('n17_patrulla', 'Aproximadamente 10 minutos después llegó una patrulla de la '
   'Policía Nacional.'),
  ('n18_entrega', 'lo habían retenido porque acababa de hurtar alimentos'),
  ('n19_policias', 'escucharon brevemente la versión de algunos comerciantes.'),
  ('n21_quince', 'Nico manifestó que tenía 15 años, que vivía debajo del puente'),
  ('n21_quince', 'no tenía a nadie que pudiera responder por él.'),
  ('n22_cip', 'Centro de Internamiento Preventivo (CIP)'),
  ('n23_defensor', 'se le asignó un defensor público'),
  ('n24_hambre', 'llevaba varios días sin comer y que no tenía dinero para '
   'comprarlos.'),
  ('n25_otras', 'había tomado alimentos de diferentes establecimientos porque tenía '
   'hambre.'),
  ('n26_cae', 'si aceptaba los cargos, probablemente sería enviado a un Centro de '
   'Atención Especializada (CAE),'),
  ('n28_mire', '«Mire, usted no tiene dónde vivir, no tiene familia y está pasando '
   'muchas necesidades.'),
  ('n28_mire', 'Si acepta lo que hizo y no se pone a discutir el proceso, puede '
   'quedarse en un lugar donde le van a dar comida, techo y atención.»'),
  ('n29_afuera', '«Afuera no tiene nada. Piénselo bien, porque tal vez esto sea lo '
   'mejor que le pueda pasar.»'),
  ('n30_pregunta', 'tendría que regresar a vivir debajo del puente.'),
  ('n31_respuesta', 'eso dependería de las decisiones que adoptaran las autoridades'),
  ('n32_dispuesto', 'estaba dispuesto a aceptar todo lo que le imputaran, siempre '
   'que no tuviera que volver a dormir en la calle.'),
  ('n34_consecuencias', 'una comprensión libre, consciente e informada de sus '
   'derechos.'),
  ('n35_ingreso', 'Nico ingresó a un Centro de Atención Especializada (CAE).'),
  ('n36_higiene', 'condiciones de higiene personal considerablemente deterioradas.'),
  ('n41_convivencia', 'podían representar un problema para la convivencia con los '
   'demás jóvenes'),
  ('n42_cabello', 'sin que mediara una valoración médica especializada'),
  ('n42_cabello', 'se ordenó cortarle completamente el cabello para eliminar los '
   'piojos.'),
  ('n43_aislamiento', 'se decidió ubicarlo en un espacio de aislamiento individual.'),
 ],
}


def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.findall(r'[a-z0-9]+', s)


def comprobar_arreglo(crudo, frase):
    """Las palabras tienen que ser las mismas, en el mismo orden. Solo se
    permite la mayuscula inicial y agregar o quitar comillas angulares."""
    a = [w for w in re.findall(r'\w+', crudo)]
    b = [w for w in re.findall(r'\w+', frase)]
    if len(a) != len(b):
        return False, 'cambia el numero de palabras'
    for i, (x, y) in enumerate(zip(a, b)):
        if x == y:
            continue
        if i == 0 and x[:1].upper() + x[1:] == y:
            continue
        return False, 'cambia «%s» por «%s»' % (x, y)
    resto_a = re.sub(r'[\w«»\s]', '', crudo)
    resto_b = re.sub(r'[\w«»\s]', '', frase)
    if resto_a != resto_b:
        return False, 'cambia la puntuacion'
    return True, ''


def presentar(trozo, primero_del_bloque, empieza_oracion):
    t = trozo
    if t.count('»') > t.count('«'):
        t = '«' + t
    if t.count('«') > t.count('»'):
        t = t.rstrip('.') + '»' + ('.' if trozo.endswith('.') else '')
    # el primer carton de un bloque siempre abre con mayuscula, aunque el
    # documento venga de dos puntos («aparece un tercer dato: algunos...»)
    if primero_del_bloque:
        for i, ch in enumerate(t):
            if ch.isalpha():
                t = t[:i] + ch.upper() + t[i + 1:]
                break
            if ch not in '«':
                break
    return t


NUM_PAL = {'uno', 'una', 'un', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete',
           'ocho', 'nueve', 'diez', 'once', 'doce', 'quince', 'veinte', 'veintiun',
           'veintiuno', 'veintisiete', 'treinta', 'cuarenta', 'cincuenta', 'sesenta',
           'setenta', 'ochenta', 'noventa', 'cien', 'ciento', 'doscientos',
           'cuatrocientos', 'mil', 'veintiseis'}


def palabras_stt(clave, bloque):
    """[(t_master, palabra_normalizada)] del bloque, con Scribe."""
    v = R.voces(clave)
    rej = json.load(open(os.path.join(v, 'SR_%s_rejilla.json' % clave),
                         encoding='utf-8'))
    tr = {t['bloque']: t for t in rej['tramos']}[bloque]
    f = glob.glob(os.path.join(v, 'stt', 'SR_%s_*_%s.json' % (clave, bloque)))[0]
    j = json.load(open(f, encoding='utf-8'))
    out = []
    for w in j.get('words', []):
        if w.get('type') != 'word':
            continue
        for tok in norm(w['text']):
            out.append((tr['entra'] + w['start'], tok))
    return out, tr


def entra(clave, bloque, texto, trozo):
    """Cuadro de la linea (desde 0) en que se oye la primera palabra del trozo.
    Busca la secuencia de las primeras palabras (sin numeros) en Scribe; si
    no la encuentra, reparte caracteres como en las situaciones."""
    ws, tr = palabras_stt(clave, bloque)
    # 31 oct (U3 r18, r27): la busqueda se saltaba NUM_PAL en Scribe pero no
    # en el trozo, y «Usted, con UN gesto» o «Pero si UNO ha sido» nunca
    # casaban (caian a proporcion, 13 cuadros antes). Se salta a los dos lados.
    q = [x for x in norm(trozo) if not x.isdigit() and x not in NUM_PAL][:3]
    # 31 oct: el carton dice «Procesado 1» y Scribe oye «procesado uno»; los
    # numeros en letras se saltan igual que los digitos, a los dos lados.
    idx = [k for k, (_, t) in enumerate(ws) if not t.isdigit() and t not in NUM_PAL]
    toks = [ws[k][1] for k in idx]
    pos = texto.find(trozo)
    est = len(norm(texto[:pos]))
    mejor = None
    for k in range(len(toks) - len(q) + 1):
        if toks[k:k + len(q)] == q:
            if mejor is None or abs(k - est) < abs(mejor - est):
                mejor = k
    if mejor is not None:
        return CABEZA + int(round(ws[idx[mejor]][0] * FPS)), 'stt'
    return CABEZA + int(round((tr['entra'] + tr['dur'] * pos / len(texto))
                              * FPS)), 'proporcion'


def calcula(clave):
    rej = json.load(open(os.path.join(R.voces(clave), 'SR_%s_rejilla.json'
                                      % clave), encoding='utf-8'))
    tr = {t['bloque']: t for t in rej['tramos']}
    tx = {b[0]: ' '.join(b[2].split()) for b in bloques(clave)}
    piezas = []
    for k, (bl, trozo) in enumerate(ELEGIDOS[clave]):
        # 5 nov (EI S04): 'a+b' = un carton que cruza la frontera de dos
        # bloques seguidos; entra con la voz del primero y su bloque termina
        # con el segundo
        partes = bl.split('+')
        texto = ' '.join(tx[x] for x in partes)
        pos = texto.find(trozo)
        assert pos >= 0, '%s: el trozo no esta VERBATIM en %s:\n  %s' % (
            clave, bl, trozo)
        assert pos < len(tx[partes[0]]), (clave, bl, 'el trozo empieza en el 2o bloque')
        ini, como = entra(clave, partes[0], texto, trozo)
        ini += DESPLAZA.get((clave, k + 1), 0)
        fin_bloque = CABEZA + int(round(tr[partes[-1]]['sale'] * FPS))
        primero = k == 0 or ELEGIDOS[clave][k - 1][0] != bl
        empieza = pos == 0 or texto[:pos].rstrip().endswith(('.', ':'))
        frase = presentar(trozo, primero, empieza)
        ok, motivo = comprobar_arreglo(trozo, frase)
        assert ok, (clave, motivo, frase)
        piezas.append({'tema': clave, 'bloque': bl, 'ini': ini, 'como': como,
                       'fin_bloque': fin_bloque, 'frase': frase,
                       'frase_cruda': trozo, 'arreglado': frase != trozo,
                       'relevo': not primero})
    for k in range(1, len(piezas)):
        a, b = piezas[k - 1], piezas[k]
        if not b['relevo']:
            continue
        quiere = a['ini'] + int(round(len(a['frase']) / 14.0 * FPS)) + RESPIRO
        sig = piezas[k + 1]['ini'] if k + 1 < len(piezas) else None
        fin_b = b['fin_bloque'] + 90
        if sig is not None and piezas[k + 1]['bloque'] != b['bloque']:
            fin_b = min(fin_b, sig - RESPIRO)
        limite = fin_b - int(round(len(b['frase']) / 16.0 * FPS))
        if quiere > b['ini']:
            b['ini'] = min(quiere, max(b['ini'], limite))
    ran = json.load(open(os.path.join(R.voces(clave), 'SR_%s_ranuras.json' % clave),
                         encoding='utf-8'))
    cierre = ran['pieza'] - (182 + 119)
    # las ventanas que un carton no puede pisar: los rotulos y las listas de
    # After Effects (mg_sr), en cuadros de la linea
    import lowerthirds_sr as LTS
    import mg_sr as MG
    rotulos = [(a, a + n) for a, n, _ in LTS.en_linea(clave)]
    rotulos += [(a, a + n) for a, n, _ in MG.lista(clave)]
    for k, p in enumerate(piezas):
        sig = piezas[k + 1]['ini'] if k + 1 < len(piezas) else None
        mismo = sig is not None and piezas[k + 1]['bloque'] == p['bloque']
        if mismo:
            fin = sig - RESPIRO
        else:
            # 30 oct: un titulo de fase de la U1 («Confrontacion directa.»)
            # se quedaba en 53 cuadros; ningun carton dura menos de 72.
            comodo = p['ini'] + max(72, int(round(len(p['frase']) / COMODO * FPS)))
            fin = max(p['fin_bloque'], comodo)
            fin = min(fin, p['fin_bloque'] + 90)
            if sig is not None:
                fin = min(fin, sig - RESPIRO)
        # 29 oct: el ultimo carton de cada tema se estiraba hasta 90 cuadros
        # despues de la voz y se metia ~28 cuadros en el carton de cierre
        # (T1 903 > 875). Puede sostenerse sobre el respiro, nunca pasar al
        # cierre.
        fin = min(fin, cierre)
        # 3 nov (pase previo, como en Ley 1826): el ultimo carton termina con
        # el CUERPO, no sobre el respiro (Sebastian deja el respiro limpio y
        # funde a negro). Si al cortarlo quedara bajo 72 cuadros, entra lo justo.
        fin = min(fin, max(cierre - N_RESPIRO, p['ini'] + 72))
        # rotulo y carton no conviven: un carton que empieza antes de una
        # ranura con rotulo se corta donde ella empieza.
        for a, b in rotulos:
            assert not (a <= p['ini'] < b), (clave, p['frase'], 'empieza sobre el rotulo')
            if p['ini'] < a < fin:
                fin = a
        p['cuadros'] = fin - p['ini']
        p['densidad'] = round(len(p['frase']) / (p['cuadros'] / FPS), 1)
    for n, p in enumerate(piezas, 1):
        p['archivo'] = RENOMBRA.get(clave, {}).get(n, 'SR_%s_p%02d_carton.mov' % (clave, n))
    return piezas


# 4 nov (C4, revision): un carton que cambia de largo en una linea ya tocada
# va con otro nombre: el media pool cachea la duracion del archivo y un
# carton reescrito en su sitio entraria con el largo viejo. El p01 del C4 se
# corta donde entra el rotulo de Yaneth (236 -> 106 cuadros).
RENOMBRA = {}

# 5 nov (EI S06): cuadros que un carton entra DESPUES de su primera palabra,
# cuando el anterior se queda sin tiempo de leerse. El p03 del S06 («habian
# salido de sus viviendas para asistir a una entrevista de trabajo.») tenia 83
# cuadros a 20,8 car/s porque el p04 («Un testigo afirma...») entra en cuanto
# la voz lo dice; el testigo entra 36 cuadros despues y los dos quedan
# legibles. Clave (video, numero de carton).
# El p04 del S04 («Y a diferentes decisiones...») entra 24 cuadros tarde para
# que las dos convenciones (117 caracteres, tres renglones) bajen de 18,6 a
# ~16 car/s.
DESPLAZA = {}


def renglones(t):
    from PIL import Image, ImageDraw
    import cartones_ta as C
    import apertura_verbatim_p3c5 as V
    f = C.fuente(C.F_BOLD, CUERPO)
    d = ImageDraw.Draw(Image.new('RGBA', (10, 10)))
    return len(V.partir(t, f, d))


def quemar(d):
    import cartones_ta as C
    C.TINTE = (0, 72, 144)
    import apertura_verbatim_p3c5 as V
    dest = os.path.join(R.sub(d['tema'], '02 CARTONES'), d['archivo'])
    if os.path.exists(dest):
        import sr_pieza as GP
        GP.aparta(dest, 'requemado')
    n = d['renglones']
    y0 = int(540 - (n * SALTO) / 2.0) + 20
    V.verbatim([(d['frase'], 0)], d['cuadros'], dest, y0=y0, cuerpo=CUERPO,
               salto=SALTO)
    return dest


def w(x):
    sys.stdout.write(x.encode('ascii', 'replace').decode('ascii') + '\n')
    sys.stdout.flush()


if __name__ == '__main__':
    todo, fallas = [], []
    claves = [x.upper() for x in sys.argv[1:] if not x.startswith('--')] \
        or VIDEOS
    previo = []
    if claves != VIDEOS and os.path.exists(SALIDA):
        previo = [d for d in json.load(open(SALIDA, encoding='utf-8'))
                  if d['tema'] not in claves]
    for c in claves:
        o = calcula(c)
        pieza = json.load(open(os.path.join(R.voces(c), 'SR_%s_ranuras.json'
                                            % c), encoding='utf-8'))['pieza']
        cuerpo = pieza - (182 + 119 + 48 + 119 + 182)
        cub = sum(d['cuadros'] for d in o)
        w('=== %s: %d cartones, %d cuadros = %.0f%% del cuerpo'
          % (c, len(o), cub, 100.0 * cub / cuerpo))
        for d in o:
            d['renglones'] = renglones(d['frase'])
            if d['renglones'] > TOPE_RENGLONES:
                fallas.append((d['archivo'], d['renglones']))
            if d['cuadros'] < 60:
                fallas.append((d['archivo'], 'corto %d' % d['cuadros']))
            w('  %s %5d +%4d  %4.1f car/s  %d ren  %s%s%s'
              % (d['archivo'][6:9], d['ini'], d['cuadros'], d['densidad'],
                 d['renglones'], d['como'], ' relevo' if d['relevo'] else '',
                 ' ARREGLO' if d['arreglado'] else ''))
            w('      ' + d['frase'])
        todo += o
    if fallas:
        w('FALLAS: %s' % fallas)
    os.makedirs(os.path.dirname(SALIDA), exist_ok=True)
    json.dump(previo + todo, open(SALIDA, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    if '--quemar' in sys.argv and not fallas:
        for d in todo:
            p = quemar(d)
            w('quemado %s  %d cuadros' % (os.path.basename(p), d['cuadros']))
    w('LISTO')
