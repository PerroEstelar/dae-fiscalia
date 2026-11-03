# -*- coding: utf-8 -*-
r"""Cartones verbatim del curso Ley 1826 (es `cartones_dh`).

    python cartones_lp.py              calcula, comprueba y escribe el json
    python cartones_lp.py --quemar     ademas quema los .mov en 02 CARTONES
    python cartones_lp.py T4 --quemar  uno solo

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
    tiempos POR PALABRA de Scribe (`stt_lp.py`). El carton entra en el
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

from guion_lp import VIDEOS, bloques            # noqa: E402
import rutas_lp as R                            # noqa: E402

CUERPO = 52
SALTO = int(round(CUERPO * 1.36))
FPS = 24000 / 1001.0
CABEZA = 182 + 119
RESPIRO = 24
COMODO = 10.0
TOPE_RENGLONES = 3

SALIDA = r'D:\DAE\_tmp\lp\cartones_lp.json'

# Ley 1826 (3 nov): escogidos a mano con las voces ya medidas (frases VERBATIM
# de `guion_lp`, la que se oye encima). Lo que va: los datos (fechas,
# nombres, placas, articulos, formatos, cifras), la frase del agresor entre
# comillas (U2 C2) y la tesis de cada caso. Fuera: la ranura del rotulo
# (U2 C1 r05, U2 C2 r02).
# Primera corrida (3 nov): densidad 76/69/74/85/75 % y tres fallas de lectura.
# Fuera «una caida atipica...» (U2 C1: el plano del grafico ya lo dice) y «En
# el curso de un proceso por lesiones...» (U4 C2: el cruce lo muestra; 85 %
# era demasiado lleno). Recortados: el radicado de U2 C1 (4 renglones -> 3,
# desde «se radico»), la recusacion de U4 C1 (16,6 car/s: sin «en la
# audiencia concentrada») y los dos de U4 C3 que se pisaban (el de desistir
# salia a 19,4 car/s: ahora desde «desea», y el del archivo desde «un
# acuerdo», que le da el aire).
# Y fuera «Durante los ultimos tres anos, en vivienda conyugal ubicada en
# Medellin,» (U2 C2): iba de 303 a 627 y la r02 (470-639) es la del rotulo de
# Maria Elena. Rotulo y carton no conviven; el nombre pesa mas, y la ladera
# de la r01 ya dice Medellin.
ELEGIDOS = {
 'U2C1': [
  ('a01_cali', 'El 15 de agosto de 2023, en el barrio Industrial de la ciudad '
   'de Cali,'),
  ('a01_cali', 'Mario Alberto Gómez Parra (contratista activo de la '
   'distribuidora) y a Pedro Antonio Morales Rincón (extransportador)'),
  ('a02_transbordo', 'realizando el transbordo clandestino de 45 botellas con '
   'etiquetas de la marca protegida Kombucha Valle'),
  ('a02_transbordo', 'desde un vehículo particular (Placa KTH412) hacia el '
   'camión repartidor oficial de la compañía (Placa WXN445).'),
  ('a06_sin_captura', 'La investigación se adelantó sin captura,'),
  ('a07_radicado', 'se radicó bajo las reglas del procedimiento penal '
   'especial abreviado (Ley 1826 de 2017) el 4 de febrero de 2026.'),
 ],
 'U2C2': [
  ('b02_episodio', 'El episodio más grave ocurrió el 10 de enero de 2026,'),
  ('b02_episodio', 'una incapacidad médico-legal definitiva de 25 días con '
   'deformidad física transitoria,'),
  ('b03_la_mato', '«si me denuncia o habla en un juzgado, la mato a usted y '
   'a su mamá».'),
  ('b05_armados', 'ha enviado a familiares y terceros armados al lugar donde '
   'María Elena se encuentra refugiada'),
  ('b06_riesgo', 'la red de protección a víctimas de VBG (Ley 1257 de 2008),'),
  ('b08_prueba_anticipada', 'la Fiscalía acude ante el juez de control de '
   'garantías para solicitar la práctica anticipada de su testimonio.'),
 ],
 'U4C1': [
  ('c01_noticia', 'un delito de inasistencia alimentaria (art. 233 del CP),'),
  ('c01_noticia', 'un ciudadano de 35 años de edad contra su hijo menor de '
   'edad.'),
  ('c02_conciliacion', 'fijar fecha para diligencia de conciliación '
   'utilizando el formato FGN-MP02-F-10.'),
  ('c03_recusacion', 'una solicitud de recusación contra el fiscal y '
   'posterior solicitud de nulidad'),
  ('c04_no_querellable', 'la inasistencia alimentaria no es un delito '
   'querellable y que exigir conciliación obligatoria vulnera el debido '
   'proceso.'),
 ],
 'U4C2': [
  ('d02_mediador', 'remitiendo el conflicto a un mediador del distrito '
   'judicial mediante el formato FGN-MP02-F-132.'),
  ('d03_exceso', 'el indiciado acepta expresamente que conducía con exceso de '
   'velocidad,'),
  ('d03_exceso', 'se ofrece a pagar la suma de 10 millones de pesos como '
   'indemnización total.'),
  ('d04_sin_acuerdo', 'se suscribe el formato FGN-MP02-F-133, certificando '
   'que no hubo acuerdo.'),
  ('d05_audio', 'el fiscal pretende introducir el audio de la sesión de '
   'mediación'),
  ('d06_exclusion', 'El defensor formula oposición solicitando la regla de '
   'exclusión.'),
 ],
 'U4C3': [
  ('e01_denuncia', 'Una ciudadana de 28 años presenta denuncia por el delito '
   'de VIF sistemática'),
  ('e02_desistir', 'desea desistir de la denuncia,'),
  ('e03_archivo', 'un acuerdo de mediación y posterior archivo de la carpeta '
   'penal,'),
  ('e04_terapia', 'y que ella depende económicamente de él.'),
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
    rej = json.load(open(os.path.join(v, 'LP_%s_rejilla.json' % clave),
                         encoding='utf-8'))
    tr = {t['bloque']: t for t in rej['tramos']}[bloque]
    f = glob.glob(os.path.join(v, 'stt', 'LP_%s_*_%s.json' % (clave, bloque)))[0]
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
    rej = json.load(open(os.path.join(R.voces(clave), 'LP_%s_rejilla.json'
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
    cierre = json.load(open(os.path.join(R.voces(clave), 'LP_%s_ranuras.json' % clave),
                            encoding='utf-8'))['pieza'] - (182 + 119)
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
        p['cuadros'] = fin - p['ini']
        p['densidad'] = round(len(p['frase']) / (p['cuadros'] / FPS), 1)
    for n, p in enumerate(piezas, 1):
        p['archivo'] = 'LP_%s_p%02d_carton.mov' % (clave, n)
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
        import lp_pieza as GP
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
        pieza = json.load(open(os.path.join(R.voces(c), 'LP_%s_ranuras.json'
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
