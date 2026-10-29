# -*- coding: utf-8 -*-
r"""Cartones verbatim de Gerencia judicial.

    python cartones_gj.py              calcula, comprueba y escribe el json
    python cartones_gj.py --quemar     ademas quema los .mov en 02 CARTONES
    python cartones_gj.py T4 --quemar  uno solo

ESCOGIDOS A MANO, COMO EN LAS SITUACIONES
    El proponedor automatico fallo en Desaparicion Forzada de cuatro maneras
    (cortaba citas, cortaba en «Art.», se comia nombres y atribuciones, y
    cubria 68-77 % del cuerpo). Aqui se escogen a mano y la maquina pone el
    tiempo y comprueba el verbatim y los renglones.

LO QUE SE ESCOGE Y LO QUE NO
    - Los datos que el espectador tiene que poder leer: 2.000 casos (va en
      el rotulo de la r01 del T1), el articulo 349 de la Ley 906 de 2004, el
      Auto 456 de 2024.
    - Las DOS citas del T4, enteras, partidas en su punto.
    - La pregunta que el caso plantea (T3: unilateral o negociacion; T4: las
      dos situaciones).
    - Una atribucion no se salta: «la defensa sostiene que», «algunos
      testigos afirman que», «el investigador ... considera que».
    - La presentacion (primer bloque de cada caso) va sin carton: la primera
      placa es la persona y el rotulo dice quien es.
    - El hecho de violencia sexual del T4 NO va a carton: esta en la voz,
      verbatim, y ni la imagen ni la letra lo repiten.

EL TIEMPO SALE DE LA VOZ, NO DE LA PROPORCION DE CARACTERES
    En las situaciones el carton entraba en el cuadro que daba repartir los
    caracteres del bloque sobre su duracion. Aqui hay algo mejor: los
    tiempos POR PALABRA de Scribe (`stt_gj.py`). El carton entra en el
    cuadro en que se oye su primera palabra. Un relevo termina 24 cuadros
    antes del siguiente; el ultimo de cada bloque se estira hasta leerse
    comodo (10 car/s) sin pasar el respiro del que viene.

ARREGLOS PERMITIDOS, Y SOLO ESOS
    Mayuscula inicial cuando el trozo abre a mitad de oracion, y cerrar o
    abrir la comilla angular de una cita partida. `comprobar_arreglo`
    verifica que ninguna palabra cambie.
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

from guion_gj import VIDEOS, bloques            # noqa: E402
import rutas_gj as R                            # noqa: E402

CUERPO = 52
SALTO = int(round(CUERPO * 1.36))
FPS = 24000 / 1001.0
CABEZA = 182 + 119
RESPIRO = 24
COMODO = 10.0
TOPE_RENGLONES = 3

SALIDA = r'D:\DAE\_tmp\gj\cartones_gj.json'

ELEGIDOS = {
 'T1': [
  ('p02_el_orden_de_llegada', 'su equipo atiende las denuncias en el '
   'estricto orden en que llegan,'),
  ('p02_el_orden_de_llegada', 'gastando tiempo importante en casos menores '
   'mientras los delitos graves se quedan sin investigar.'),
 ],
 'T3': [
  ('t02_ordenes_ficticias', 'algunos de sus directivos habrían utilizado '
   'órdenes de pedido ficticias y contratos simulados'),
  ('t04_el_incremento', 'La Fiscalía le atribuye conductas que produjeron un '
   'importante incremento patrimonial ilícito.'),
  ('t05_aceptar', 'el procesado manifiesta que desea aceptar '
   'responsabilidad.'),
  ('t06_interrogantes', 'si se encuentra ante una aceptación unilateral de '
   'cargos o ante una verdadera negociación.'),
  ('t07_la_distincion', 'el tratamiento del reintegro previsto en el '
   'artículo 349 de la Ley 906 de 2004 (en adelante CPP).'),
  # t08 entero: «apenas una parte...» solo entraba tarde y quedaba a 17,8
  # car/s. t09: «Las victimas reclaman reparacion» solo eran 55 cuadros (no
  # se lee); queda lo que la defensa sostiene, con su atribucion.
  ('t08_restituida', 'Además, durante la actuación se advierte que apenas '
   'una parte reducida de los recursos ha sido restituida.'),
  ('t09_victimas_y_defensa', 'la defensa sostiene que el procesado no fue '
   'destinatario final de la totalidad del incremento patrimonial.'),
 ],
 'T4': [
  ('c03_dos_situaciones', 'Al comenzar la semana se presentan dos (2) '
   'situaciones que, en apariencia, pertenecen a ámbitos completamente '
   'distintos:'),
  # «La primera ocurre dentro del equipo.» solo duraba 62 cuadros y le
  # quitaba lectura a c03 (16,6 car/s): fuera. c03 se sostiene hasta la
  # servidora.
  ('c04_dentro_del_equipo', 'Una servidora informa que tiene una '
   'discapacidad visual'),
  ('c05_lo_que_pide', 'Pide que determinados documentos se remitan también '
   'en un formato accesible'),
  ('c05_lo_que_pide', 'se establezca un mecanismo que le permita participar '
   'en igualdad de condiciones.'),
  ('c06_cita_coordinador', '«Aquí todos debemos trabajar con las mismas '
   'herramientas.'),
  ('c06_cita_coordinador', 'Si empezamos a hacer excepciones, dejamos de '
   'tratar a las personas por igual».'),
  ('c07_ese_mismo_dia', 'La actuación continuará ante la jurisdicción '
   'ordinaria.'),
  ('c08_la_joven', 'el equipo advierte que la joven vive en una zona rural '
   'distante, que su lengua materna no es el castellano'),
  ('c09_auto_456', 'Una situación semejante fue examinada por la Corte '
   'Constitucional en el Auto 456 de 2024,'),
  ('c09_auto_456', 'no elimina la obligación de incorporar los enfoques '
   'étnico y de género'),
  ('c09_auto_456', 'ni de evitar que factores geográficos, económicos, '
   'culturales o lingüísticos se conviertan en barreras de acceso a la '
   'justicia.'),
  ('c10_cita_investigador', '«El procedimiento penal es el mismo para todo '
   'el mundo.'),
  ('c10_cita_investigador', 'Lo más objetivo es no hacer ninguna '
   'diferencia».'),
  ('c11_tercer_dato', 'algunos testigos afirman que, durante la agresión, el '
   'presunto responsable utilizó expresiones despectivas'),
  ('c11_tercer_dato', 'asociadas con la identidad y la expresión de género '
   'que él atribuía a la víctima.'),
  ('c12_irrelevantes', 'El investigador que recibió inicialmente el asunto '
   'considera que esas expresiones son irrelevantes'),
  ('c12_irrelevantes', 'porque, a su juicio, basta establecer si existió o '
   'no la agresión.'),
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


def palabras_stt(clave, bloque):
    """[(t_master, palabra_normalizada)] del bloque, con Scribe."""
    v = R.voces(clave)
    rej = json.load(open(os.path.join(v, 'GJ_%s_rejilla.json' % clave),
                         encoding='utf-8'))
    tr = {t['bloque']: t for t in rej['tramos']}[bloque]
    f = glob.glob(os.path.join(v, 'stt', 'GJ_%s_*_%s.json' % (clave, bloque)))[0]
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
    q = [x for x in norm(trozo) if not x.isdigit()][:3]
    toks = [t for _, t in ws]
    pos = texto.find(trozo)
    est = len(norm(texto[:pos]))
    mejor = None
    for k in range(len(toks) - len(q) + 1):
        if toks[k:k + len(q)] == q:
            if mejor is None or abs(k - est) < abs(mejor - est):
                mejor = k
    if mejor is not None:
        return CABEZA + int(round(ws[mejor][0] * FPS)), 'stt'
    return CABEZA + int(round((tr['entra'] + tr['dur'] * pos / len(texto))
                              * FPS)), 'proporcion'


def calcula(clave):
    rej = json.load(open(os.path.join(R.voces(clave), 'GJ_%s_rejilla.json'
                                      % clave), encoding='utf-8'))
    tr = {t['bloque']: t for t in rej['tramos']}
    tx = {b[0]: ' '.join(b[2].split()) for b in bloques(clave)}
    piezas = []
    for k, (bl, trozo) in enumerate(ELEGIDOS[clave]):
        texto = tx[bl]
        pos = texto.find(trozo)
        assert pos >= 0, '%s: el trozo no esta VERBATIM en %s:\n  %s' % (
            clave, bl, trozo)
        ini, como = entra(clave, bl, texto, trozo)
        fin_bloque = CABEZA + int(round(tr[bl]['sale'] * FPS))
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
    cierre = json.load(open(os.path.join(R.voces(clave), 'GJ_%s_ranuras.json' % clave),
                            encoding='utf-8'))['pieza'] - (182 + 119)
    for k, p in enumerate(piezas):
        sig = piezas[k + 1]['ini'] if k + 1 < len(piezas) else None
        mismo = sig is not None and piezas[k + 1]['bloque'] == p['bloque']
        if mismo:
            fin = sig - RESPIRO
        else:
            comodo = p['ini'] + int(round(len(p['frase']) / COMODO * FPS))
            fin = max(p['fin_bloque'], comodo)
            fin = min(fin, p['fin_bloque'] + 90)
            if sig is not None:
                fin = min(fin, sig - RESPIRO)
        # 29 oct: el ultimo carton de cada tema se estiraba hasta 90 cuadros
        # despues de la voz y se metia ~28 cuadros en el carton de cierre
        # (T1 903 > 875). Puede sostenerse sobre el respiro, nunca pasar al
        # cierre.
        fin = min(fin, cierre)
        p['cuadros'] = fin - p['ini']
        p['densidad'] = round(len(p['frase']) / (p['cuadros'] / FPS), 1)
    for n, p in enumerate(piezas, 1):
        p['archivo'] = 'GJ_%s_p%02d_carton.mov' % (clave, n)
    return piezas


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
        import gj_pieza as GP
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
        pieza = json.load(open(os.path.join(R.voces(c), 'GJ_%s_ranuras.json'
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
