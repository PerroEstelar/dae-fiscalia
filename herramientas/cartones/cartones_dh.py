# -*- coding: utf-8 -*-
r"""Cartones verbatim de Derechos humanos (herramienta de Justicia restaurativa).

    python cartones_dh.py              calcula, comprueba y escribe el json
    python cartones_dh.py --quemar     ademas quema los .mov en 02 CARTONES
    python cartones_dh.py T4 --quemar  uno solo

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
    tiempos POR PALABRA de Scribe (`stt_dh.py`). El carton entra en el
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

from guion_dh import VIDEOS, bloques            # noqa: E402
import rutas_dh as R                            # noqa: E402

CUERPO = 52
SALTO = int(round(CUERPO * 1.36))
FPS = 24000 / 1001.0
CABEZA = 182 + 119
RESPIRO = 24
COMODO = 10.0
TOPE_RENGLONES = 3

SALIDA = r'D:\DAE\_tmp\dh\cartones_dh.json'

# Derechos humanos, 31 oct: escogidos a mano con las voces ya medidas (frases
# VERBATIM de `guion_dh`, la que se oye encima). Lo que va: los datos
# (fechas, articulos, tratados, la sentencia Gelman), los tres caminos y los
# cuatro pasos del analisis de convencionalidad (U2), las cuatro marcas (U3),
# las tres cargas, los cuatro hechos y las tres decisiones del juez (U4), el
# epilogo mudo de la U4 (bloque SILENCIO: entra por proporcion) y el cierre
# de la U5. Fuera por el rotulo de nombre (rotulo y carton no conviven en la
# misma ranura): U5 «imputacion vigente...» (r01, Julian) y la lista de
# elementos de prueba (r02, Sandra; la placa ya los pone en la mesa).
ELEGIDOS = {
 'U1': [
  ('a01_noticia_criminal', 'Lo que ocurra con ella en las primeras horas '
   'puede proteger derechos o ponerlos en riesgo.'),
  ('a02_vengo_a_denunciar', 'Desde hace dos semanas me están amenazando.'),
  ('a04_las_cuotas', 'Hace quince días hablé al aire de las cuotas que '
   'están cobrando a los comerciantes del mercado.'),
  ('a05_la_moto', 'dos llamadas de número desconocido diciéndome que me '
   'calle,'),
  ('a05_la_moto', 'el martes una moto me siguió desde la emisora hasta mi '
   'casa.'),
  ('a07_una_vecina', 'Y una vecina vio la moto; está dispuesta a contarlo.'),
  ('a09_mi_mama', 'a otro compañero le dejaron un papel parecido, pero él '
   'no quiere denunciar.'),
  ('a10_los_del_cerro', 'Son «Los del Cerro». Eso también lo dije al aire.'),
  ('a11_detengase', 'Antes de cualquier teoría, registre su primera '
   'decisión.'),
 ],
 'U2': [
  ('b02_vida_privada', 'el artículo 11 de la Convención Americana sobre '
   'Derechos Humanos'),
  ('b02_vida_privada', 'el artículo 17 del Pacto Internacional de Derechos '
   'Civiles y Políticos,'),
  ('b04_camino_a', 'Camino A: «Eso es derecho internacional, aquí aplicamos '
   'la ley colombiana».'),
  ('b06_derecho_extranjero', '«¿La Fiscalía considera que la Convención '
   'Americana es derecho extranjero? ¿Conoce el artículo 93 de la '
   'Constitución?».'),
  ('b08_camino_b', 'Camino B: «Mejor retiremos esa evidencia para evitar '
   'problemas».'),
  ('b10_bastó_invocar', 'bastó invocar un tratado para que la actuación '
   'retrocediera.'),
  ('b11_camino_c', 'Camino C: «Hagamos el análisis de convencionalidad '
   'completo».'),
  ('b12_obliga', '¿El tratado obliga a Colombia y qué rango tiene? (CADH y '
   'PIDCP ratificados; bloque de constitucionalidad, art. 93 CP).'),
  ('b13_estandar', '¿Cuál es el estándar aplicable? (la injerencia en la '
   'vida privada es legítima si es legal, necesaria y proporcional).'),
  ('b14_lo_cumplio', '¿El acto lo cumplió? (los registros se obtuvieron con '
   'orden y control judicial, con fin investigativo legítimo).'),
  ('b15_se_motiva', '¿Cómo se motiva la respuesta? (citando la fuente, el '
   'estándar y su aplicación a los hechos).'),
  ('b17_fortalecida', 'control de convencionalidad, que es tarea de '
   'cualquier autoridad pública (Gelman vs. Uruguay, 2011, párr. 239).'),
  ('b18_ni_rechazo', 'Ni el rechazo automático (camino A) ni la retirada '
   'automática (camino B): el camino C es el del análisis.'),
 ],
 'U3': [
  ('c01_semana_ocho', 'Va a escuchar dos versiones de la misma entrevista.'),
  ('c01_semana_ocho', 'En la primera, algo falla cuatro veces: márquelo '
   'cuando lo escuche.'),
  ('c10_cuatro_marcas', 'Uno: le pidió repetir todo desde el principio sin '
   'consultar lo ya actuado. Dos: la culpó de exponerse.'),
  ('c11_tres_cuatro', 'Tres: redujo la amenaza a un asunto pasional, desde '
   'el prejuicio y no desde los hechos.'),
  ('c11_tres_cuatro', 'Cuatro: la interrumpió por un mensaje justo cuando '
   'iba a decir lo más difícil, y ella se cerró.'),
  ('c12_falta_de_metodo', 'Ninguna fue crueldad: fue falta de método.'),
  ('c20_lo_vamos_a_tomar', 'cambia la valoración del riesgo y las medidas '
   'que vamos a solicitar.'),
  ('c22_no_se_lo_busco', 'Usted no se lo buscó. Informar es su trabajo, y '
   'es un derecho.'),
  ('c22_no_se_lo_busco', 'De estas amenazas responde quien las hace, no '
   'usted.'),
  ('c24_de_metodo', 'La diferencia no fue de amabilidad: fue de método.'),
  ('c25_su_bitacora', 'Anote en su bitácora cuál de las cuatro fallas podría '
   'ocurrir hoy en su propio puesto de trabajo.'),
 ],
 'U4': [
  ('d01_semana_diez', 'Wilmer Acosta fue capturado en flagrancia cuando '
   'dejaba un nuevo panfleto en la emisora, con un arma de fuego sin '
   'permiso.'),
  ('d02_legalizada', 'se le imputaron amenazas agravadas y porte ilegal de '
   'armas.'),
  ('d04_solicita', 'medida de aseguramiento privativa de la libertad en '
   'establecimiento carcelario,'),
  ('d05_tres_cargas', 'Sustento la solicitud en tres cargas.'),
  ('d06_primera_carga', 'Primera carga: la inferencia razonable de autoría.'),
  ('d07_hecho_uno', 'Hecho uno: dejó un panfleto amenazante en la emisora '
   'de la víctima;'),
  ('d08_hecho_dos', 'Hecho dos: portaba un arma de fuego sin permiso; acta '
   'de incautación y cadena de custodia.'),
  ('d09_hecho_tres', 'Hecho tres: el panfleto coincide en diseño y texto con '
   'los que la víctima recibió desde el día cero;'),
  ('d10_hecho_cuatro', 'Hecho cuatro: su teléfono registra mensajes al '
   'número desde el cual se amenazó a la víctima;'),
  ('d12_segunda_carga', 'Segunda carga: los fines.'),
  ('d13_peligro', 'Peligro para la víctima: fue capturado ejecutando una '
   'nueva amenaza contra la misma persona.'),
  ('d14_obstruccion', 'Obstrucción de la justicia: actúa por encargo de una '
   'estructura con presencia en el territorio y capacidad de presionar '
   'testigos.'),
  ('d16_tercera_carga', 'Tercera carga: el tipo de medida.'),
  ('d19_el_costo', 'un sistema que la Corte Constitucional declaró en estado '
   'de cosas inconstitucional.'),
  ('d20_no_desproporcional', 'la medida no es desproporcional en estricto '
   'sentido.'),
  ('d22_menos_gravosa', 'la defensa propone vigilancia electrónica más '
   'prohibición de comunicarse con la víctima:'),
  ('d23_resuelvo', 'Primera: la inferencia razonable existe;'),
  ('d24_deciden_los_hechos', 'Segunda: la calificación jurídica no decide '
   'nada por sí misma; deciden los hechos.'),
  ('d26_tercera', 'Tercera: la detención en establecimiento carcelario es '
   'procedente por la pena mínima del tipo penal.'),
  ('d27_impongo', 'Impongo detención preventiva en establecimiento '
   'carcelario.'),
  ('d28_la_suya', 'Lo que esta unidad evalúa no es la decisión del juez, '
   'sino la sustentación: la suya.'),
  ('d29_la_otra_silla', 'La persona que el juez acaba de enviar aquí se '
   'presume inocente.'),
  ('d29_la_otra_silla', 'Si la medida era necesaria, esto era exactamente lo '
   'que la tercera carga debía justificar.'),
 ],
 'U5': [
  ('e01_estado_del_caso', 'hoy vence el término para definir la acusación.'),
  ('e04_hoy_cerramos', 'Lo que decidamos de un lado no puede deshacer lo del '
   'otro.'),
  ('e06_prueba_de_coherencia', 'ninguna protección vulnera garantías, '
   'ninguna restricción desprotege.'),
  ('e07_se_retracta', 'el comerciante que declaró haber visto a Acosta dejar '
   'el panfleto de la semana ocho se retracta por escrito.'),
  ('e08_otro_mensaje_tel', 'Es de un número distinto. Dice que lo de Acosta '
   'no cambia nada.'),
  ('e10_reponderar', 'Reponderar no es empezar de cero.'),
  ('e12_los_determinadores', 'la nueva amenaza es noticia criminal conexa, y '
   'la línea de los determinadores se abre hoy.'),
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
    rej = json.load(open(os.path.join(v, 'DH_%s_rejilla.json' % clave),
                         encoding='utf-8'))
    tr = {t['bloque']: t for t in rej['tramos']}[bloque]
    f = glob.glob(os.path.join(v, 'stt', 'DH_%s_*_%s.json' % (clave, bloque)))[0]
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
    rej = json.load(open(os.path.join(R.voces(clave), 'DH_%s_rejilla.json'
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
    cierre = json.load(open(os.path.join(R.voces(clave), 'DH_%s_ranuras.json' % clave),
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
        p['archivo'] = 'DH_%s_p%02d_carton.mov' % (clave, n)
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
        import dh_pieza as GP
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
        pieza = json.load(open(os.path.join(R.voces(c), 'DH_%s_ranuras.json'
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
