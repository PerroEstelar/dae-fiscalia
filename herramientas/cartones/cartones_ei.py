# -*- coding: utf-8 -*-
r"""Cartones verbatim del curso Estándares interamericanos (es `cartones_ed`).

    python cartones_ei.py              calcula, comprueba y escribe el json
    python cartones_ei.py --quemar     ademas quema los .mov en 02 CARTONES
    python cartones_ei.py T4 --quemar  uno solo

ESCOGIDOS A MANO, COMO EN LAS SITUACIONES
    El proponedor automatico fallo en Desaparicion Forzada de cuatro maneras
    (cortaba citas, cortaba en «Art.», se comia nombres y atribuciones, y
    cubria 68-77 % del cuerpo). Aqui se escogen a mano y la maquina pone el
    tiempo y comprueba el verbatim y los renglones.

LO QUE SE ESCOGE Y LO QUE NO (Justicia restaurativa, 30 oct)
    - Los datos que el espectador tiene que poder leer: fechas, dias de
      incapacidad, articulos, nombres, edades, la pena (200 a 450 meses).
    - Las tablas del C2, renglon por renglon («Procesado 1: ...»).
    - Las citas literarias (Tolstoi, Hillman, Thiebaut, Rubiano, Dante),
      partidas en su punto o en la coma donde deja de caber en tres
      renglones; y los parlamentos de Juana, que son lo que el curso
      discute.
    - Los titulos de fase de la U1 («Inicio:», «Escalada:», ...) van
      enteros aunque sean cortos: son la estructura de la fabula.
    - Fuera por tiempo (30 oct, primera corrida): «Ambos conductores se
      enfrentan fisicamente» y «El auto se incendia...» de la U1 (los
      titulos de fase se los comian, 33 y 54 cuadros); «recuerda una
      pintura de Van Gogh» (43 cuadros, el pie de foto lo cubre); «Es una
      broma, no?» (48); «el perdon adquiere un gran significado» (52); «es,
      en un grado cero, aprender a nombrarlo» y «transitar de la pragmatica
      de los silencios a su etica» (dejaban a 18 car/s al anterior). Fuera
      por densidad del C2 (81 %): la nota metodologica, «Edad y ocupacion»
      (lo dice el rotulo), «capturado en flagrancia; imputado...» y el
      primer renglon del acuerdo.
    - La presentacion (primer bloque de la U2, U3 y U4) va sin carton: la
      primera placa es Juana y el rotulo dice quien es. El pie de foto de la
      pintura («Cansado. Vincent van Gogh...») si va: es su razon de ser.
    - Las PREGUNTAS del documento no estan en la voz ni en los cartones:
      van a Moodle.

EL TIEMPO SALE DE LA VOZ, NO DE LA PROPORCION DE CARACTERES
    En las situaciones el carton entraba en el cuadro que daba repartir los
    caracteres del bloque sobre su duracion. Aqui hay algo mejor: los
    tiempos POR PALABRA de Scribe (`stt_ei.py`). El carton entra en el
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

from guion_ei import VIDEOS, bloques            # noqa: E402
import rutas_ei as R                            # noqa: E402

CUERPO = 52
SALTO = int(round(CUERPO * 1.36))
FPS = 24000 / 1001.0
CABEZA = 182 + 119
RESPIRO = 24
N_RESPIRO = 48          # el respiro de la pieza (ei_pieza.N_RESPIRO)
COMODO = 10.0
TOPE_RENGLONES = 3

SALIDA = r'D:\DAE\_tmp\ei\cartones_ei.json'

# Estándares interamericanos (5 nov): escogidos a mano con las voces ya
# medidas, un cartón por bloque (dos en el S04 d04, la enumeración de las
# fuentes). Lo que va: lo que la situación pone a decidir -quién, qué fuente,
# qué versión, qué inconsistencia- y la frase final de cada caso. Fuera, como
# en Enfoque diferencial: las agresiones del S08 h02 («había sufrido
# agresiones durante su detención» lo dice la voz; el cartón no lo subraya).
ELEGIDOS = {
 'S01': [
  ('a01_el_lider', 'se denuncia la desaparición de un líder comunitario'),
  ('a02_las_amenazas', 'habían puesto en conocimiento de distintas autoridades '
   'las amenazas recibidas.'),
  ('a03_la_investigacion', 'La Fiscalía inicia una investigación penal'),
  ('a04_varios_anos', 'la familia considera que sus derechos no han sido '
   'garantizados adecuadamente'),
  ('a05_la_pregunta', 'si es posible presentar el caso ante una autoridad '
   'internacional.'),
  # 5 nov: entero quedaba a 17,1 car/s en tres renglones (es el último y lo
  # corta el cuerpo); se queda en lo que la familia sostiene.
  ('a06_condenar', 'un tribunal internacional debería condenar penalmente a los '
   'responsables'),
 ],
 'S04': [
  ('d01_la_investigacion', 'la presunta desaparición forzada de una persona.'),
  ('d02_la_revision', 'disposiciones constitucionales y penales relacionadas '
   'con la conducta investigada.'),
  # 5 nov, primera corrida: «la Convención Americana sobre Derechos Humanos,»
  # solo quedaba 54 cuadros (20,9 car/s): el bloque d03 termina en esa coma y
  # el d04 sigue la enumeración sin pausa. Las dos convenciones van en UN
  # cartón que cruza la frontera de bloque (el texto es continuo en el
  # documento; la partición es solo de la voz).
  ('d03_la_convencion+d04_las_decisiones', 'la Convención Americana sobre '
   'Derechos Humanos, a la Convención Interamericana sobre Desaparición Forzada '
   'de Personas'),
  ('d04_las_decisiones', 'y a diferentes decisiones de la Corte Interamericana.'),
  ('d05_determinar', 'qué fuentes internacionales pueden resultar relevantes'),
 ],
 'S06': [
  ('f01_la_informacion', 'la muerte de dos jóvenes durante una operación '
   'militar'),
  ('f02_el_informe', 'los jóvenes pertenecían a una organización armada y '
   'murieron durante un enfrentamiento.'),
  ('f03_la_entrevista', 'habían salido de sus viviendas para asistir a una '
   'entrevista de trabajo.'),
  ('f04_el_testigo', 'Un testigo afirma haberlos visto ingresar a un vehículo '
   'militar'),
  ('f05_las_lesiones', 'podrían resultar incompatibles con algunos aspectos de '
   'la versión operacional.'),
  ('f06_el_fiscal', 'determinar las actuaciones que orientarán la '
   'investigación.'),
 ],
 'S07': [
  ('g01_la_desaparicion', 'la desaparición de varias personas después de un '
   'operativo militar'),
  ('g02_la_fosa', 'la posible existencia de una fosa clandestina.'),
  ('g03_los_restos', 'restos humanos y algunas prendas de vestir.'),
  ('g04_las_redes', 'fotografías y videos publicados en redes sociales'),
  ('g05_la_publicacion', 'personas que podrían corresponder a las víctimas.'),
  ('g06_el_fiscal', 'las actuaciones de obtención y conservación de los '
   'elementos identificados.'),
 ],
 'S08': [
  ('h01_la_custodia', 'la muerte de una persona que permanecía bajo custodia '
   'policial.'),
  ('h03_el_video', 'un video publicado en redes sociales,'),
  ('h04_las_inconsistencias', 'inconsistencias entre la información registrada '
   'por las autoridades policiales y los hallazgos médico-legales.'),
  ('h05_el_fiscal', 'qué instrumentos internacionales pueden orientar las '
   'actuaciones investigativas.'),
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
    rej = json.load(open(os.path.join(v, 'EI_%s_rejilla.json' % clave),
                         encoding='utf-8'))
    tr = {t['bloque']: t for t in rej['tramos']}[bloque]
    f = glob.glob(os.path.join(v, 'stt', 'EI_%s_*_%s.json' % (clave, bloque)))[0]
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
    rej = json.load(open(os.path.join(R.voces(clave), 'EI_%s_rejilla.json'
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
    ran = json.load(open(os.path.join(R.voces(clave), 'EI_%s_ranuras.json' % clave),
                         encoding='utf-8'))
    cierre = ran['pieza'] - (182 + 119)
    # 3 nov: las ranuras con rotulo, en cuadros de la linea
    import lowerthirds_ei as LTS
    rotulos = []
    for e in LTS.LOWERS.get(clave, []):
        r = ran['ranuras'][e[1] - 1]
        # 4 nov (C4): el rotulo de Yaneth entra cuando la voz dice su nombre,
        # no al abrir la ranura; la ventana que no puede pisar un carton es la
        # del rotulo en pantalla (entra .. entra + cuadros), no la ranura entera
        a = CABEZA + r['ini'] + (e[3] if len(e) > 3 else LTS.OFF)
        rotulos.append((a, a + e[2].get('cuadros', LTS.N)))
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
        p['archivo'] = RENOMBRA.get(clave, {}).get(n, 'EI_%s_p%02d_carton.mov' % (clave, n))
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
DESPLAZA = {('S06', 4): 36, ('S04', 4): 24}


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
        import ei_pieza as GP
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
        pieza = json.load(open(os.path.join(R.voces(c), 'EI_%s_ranuras.json'
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
