# -*- coding: utf-8 -*-
r"""Cartones verbatim del curso Delitos contra el medio ambiente (es
`cartones_ei`, que es `cartones_ed`).

    python cartones_da.py              calcula, comprueba y escribe el json
    python cartones_da.py --quemar     ademas quema los .mov en 02 CARTONES
    python cartones_da.py V01 --quemar uno solo

Escogidos a mano; la maquina pone el tiempo (Scribe, palabra por palabra),
comprueba el verbatim y los renglones. Las reglas de EI rigen igual (ver
cartones_ei). Lo propio de este curso:

    - LAS CIFRAS NO VAN EN CARTON: van en los motion graphics de V5
      (`mg_da.py`), con la cifra literal de la fuente. Un carton no puede
      pisar la ventana de un grafico: si empieza antes, se corta donde el
      grafico entra (como el rotulo en EI); si empieza dentro, es FALLA.
    - La voz lee las cifras en letras («ciento dieciocho mil...»): NUM_PAL
      lleva las de este curso para que la busqueda en Scribe las salte.
"""
import glob
import json
import os
import re
import sys
import unicodedata

H = r'D:\DAE\_repo\herramientas'
for sub in ('cartones', 'montaje', 'prompts', os.path.join('voz', 'textos')):
    sys.path.insert(0, os.path.join(H, sub))

from guion_da import VIDEOS, bloques            # noqa: E402
import rutas_da as R                            # noqa: E402

CUERPO = 52
SALTO = int(round(CUERPO * 1.36))
FPS = 24000 / 1001.0
CABEZA = 182 + 119
RESPIRO = 24
N_RESPIRO = 48          # el respiro de la pieza (da_pieza.N_RESPIRO)
COMODO = 10.0
TOPE_RENGLONES = 3

SALIDA = r'D:\DAE\_tmp\da\cartones_da.json'

# Delitos ambientales V01 (7 nov): la frase que el espectador tiene que
# llevarse de cada bloque. Sin carton: la cifra de d03, d05 y d08, los seis
# motores de d06 y la cadena de d12 los cubre el grafico (el eslabon visible
# es el primer nodo de la cadena: con carton se decia dos veces y dejaba a
# «Son fuentes de financiacion...» en 77 cuadros); d13 es la despedida y la
# cubre el rio limpio.
ELEGIDOS = {
 'V01': [
  ('d01_techo', 'avanza un daño que no siempre se ve desde arriba.'),
  ('d02_draga', 'El oro se separa con mercurio'),
  ('d02_draga', 'llega a la mesa de las comunidades ribereñas.'),
  ('d04_fosas', 'pozos de agua estancada y montañas de arena, donde antes había '
   'bosque.'),
  ('d05_bosque', 'el bosque se tala, se quema y se convierte en potrero.'),
  ('d07_dinero', 'Nada de esto ocurre por azar.'),
  ('d07_dinero', 'donde se mueve dinero ilícito aparece quien lo controla.'),
  ('d08_grupos', 'grupos armados organizados regulan estas economías'),
  ('d09_lavado', 'Las ganancias se mezclan con negocios lícitos a través de '
   'testaferros y empresas fachada'),
  ('d10_intervencion', 'si la investigación se queda en la máquina, el negocio '
   'sigue intacto.'),
  ('d11_infracciones', 'Son fuentes de financiación de estructuras criminales.'),
 ],
 # V02 (7 nov): nada sobre las seis ranuras de grafico (r03 pilar, r05
 # niveles, r10 enfoques, r13 programa, r16 articulo 6, r20 consecuencias);
 # e03 y e10 quedan enteros en su grafico. «Las consecuencias de investigar
 # mal» no va: es el antetitulo del grafico que entra un segundo despues.
 'V02': [
  ('e01_proposito', 'no puede investigar todos los hechos al mismo tiempo ni con '
   'la misma intensidad.'),
  ('e02_pilar', 'cada región identifica los fenómenos criminales que más la '
   'afectan'),
  ('e04_ambiente', 'no son hechos aislados: tienen patrones, rutas y '
   'financiadores.'),
  ('e05_enfoques', 'buscando los capitales ilícitos y las economías con '
   'apariencia de legalidad.'),
  ('e06_programa', 'Priorizar exige método.'),
  # 7 nov: «trabajando sobre el mismo caso.» quedaba en 55 cuadros (el p07
  # entra con la voz); desde «peritos» son 103 cuadros a 14,7 car/s
  ('e07_equipo', 'peritos y autoridades ambientales trabajando sobre el '
   'mismo caso.'),
  ('e08_disciplinario', 'Dirigir la investigación es una función pública, y '
   'quien la ejerce responde por ella.'),
  ('e09_disciplinario_b', 'puede dar lugar a una investigación disciplinaria '
   'contra quien la dirigió.'),
  ('e11_dano', 'mientras el proceso fracasa, el daño continúa.'),
  ('e11_dano', 'la estructura que lo financia sigue intacta.'),
  ('e12_cierre', 'es la manera de que la acción penal llegue a tiempo.'),
 ],
 # V03-V06 (7 nov): nada dentro de un gráfico (rótulos-enlace del V03, las
 # preguntas del V05, los pasos del V06); sin siglas en mayúscula (GPS, IP).
 'V03': [
  ('g01_casa', 'no basta con lo que se ve desde afuera.'),
  ('g02_control', 'Como interfieren con derechos fundamentales, como la intimidad y '
   'el secreto de las comunicaciones'),
  ('g05_cosas', 'que se sospecha que se usan para planear delitos, ocultar '
   'evidencia o almacenar lo que producen.'),
  ('g06_analisis', 'su estructura, su jerarquía, su forma de operar y sus '
   'conexiones.'),
  ('g07_encubierto', 'pero nunca provocar el delito: en Colombia, el agente '
   'provocador está prohibido.'),
  ('g08_entrega', 'para identificar a toda la red: desde quien la produce hasta '
   'quien la recibe y la financia.'),
  ('g10_interceptacion', 'y debe someterse a control de legalidad ante un juez '
   'dentro de las 24 horas siguientes.'),
  ('g12_bases', 'Esta técnica exige siempre la autorización previa del juez.'),
  ('g13_exclusion', 'es nula de pleno derecho y no puede usarse en el juicio.'),
  ('g14_porras', 'Escuchemos la experiencia del doctor Jairo Porras.'),
 ],
 'V04': [
  ('h01_empresa', 'desviando sus aguas residuales, sin tratamiento previo, '
   'directamente hacia un río local.'),
  ('h02_pasivo', 'La empresa se niega a reparar el río.'),
  ('h02_pasivo', 'por los relaves de una antigua mina de oro abandonada río '
   'arriba.'),
  ('h04_limites', 'La Fiscalía no puede imputar responsabilidad penal basándose '
   'únicamente en la violación de la norma administrativa'),
  ('h04_limites', 'ni obligar a la empresa a limpiar la contaminación histórica '
   'de la mina.'),
  ('h05_peritaje', 'La prueba clave es un peritaje'),
  ('h06_medicion', 'y que desaparecieron dos especies de peces que aún '
   'sobrevivían a la contaminación minera.'),
  ('h07_aislar', 'la Fiscalía logra aislar la responsabilidad de la empresa del '
   'pasivo ambiental histórico.'),
  ('h08_preacuerdo', 'Se suspende la etapa de juicio oral a cambio de un plan de '
   'reparación estrictamente proporcional al daño causado.'),
 ],
 'V05': [
  ('k01_empresa', 'Una empresa fachada, vinculada a una red de criminalidad '
   'organizada'),
  ('k03_oportunidad', 'los procesados buscan acogerse a un principio de '
   'oportunidad reparando el daño.'),
  ('k04_cabildo', 'deben coordinarse con el Cabildo Gobernador, la autoridad '
   'indígena'),
  ('k05_quienes', 'que dependen del río para su consumo de agua y su pesca.'),
  ('k06_sabedores', 'que perdieron el acceso a un área del bosque considerada '
   'sagrada para sus rituales de sanación.'),
  ('k07_como', 'El daño no es solo ecológico o económico; es un daño a su '
   'cosmovisión.'),
  ('k08_ninos', 'El río contaminado enfermó a los niños y alteró su seguridad '
   'alimentaria.'),
  ('k08_ninos', 'los sabedores ya no tienen dónde enseñar a los jóvenes la '
   'botánica tradicional.'),
  ('k11_semillas', 'sino con especies endémicas y con las plantas medicinales que '
   'exigen los sabedores.'),
  ('k11_semillas', 'los rituales de armonización y limpieza espiritual del '
   'territorio.'),
  # 7 nov: «ellos serán los veedores directos.» no va: entre el grafico de la
  # cuarta pregunta y el carton de las firmas le quedaban 45 cuadros
  ('k13_firmas', 'Y para que el juez declare cumplido el acuerdo y se cierre el '
   'caso penal'),
 ],
 'V06': [
  ('m01_noticia', 'El origen y la fuente son claros: el informe policial de '
   'vigilancia.'),
  ('m01_noticia', 'Se sorprende a Francisco cortando un árbol, rodeado de seis '
   'tablas de madera'),
  ('m02_norma', 'La norma seleccionada es el aprovechamiento ilícito.'),
  ('m02_norma', 'pero... ¿es la respuesta adecuada para este actor en '
   'particular?'),
  ('m03_hipotesis', 'Francisco no es el gran determinador.'),
  ('m03_hipotesis', 'contratado por un empresario maderero que opera en las '
   'sombras.'),
  ('m05_utilidad', 'El elemento material probatorio más valioso es la '
   'caracterización de la situación vital de Francisco.'),
  ('m06_legalidad', 'la Fiscalía de Medio Ambiente trabajando de la mano con la '
   'Unidad de Justicia Restaurativa'),
  ('m07_suficiencia', 'El objetivo ya no es castigar, sino reparar el tejido '
   'social y ambiental.'),
  ('m08_viabilidad', 'Francisco, apoyado por la Fiscalía y Corpoamazonia, asume '
   'compromisos de reparación con su entorno.'),
  ('m08_viabilidad', 'El juez de control de garantías avala este acuerdo.'),
  # 7 nov: la frase entera eran cuatro renglones; queda el cierre
  ('m09_precedente', 'un precedente de justicia restaurativa, sanación y '
   'protección del Amazonas.'),
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
           'cuatrocientos', 'mil', 'veintiseis',
           # Delitos ambientales: las cifras del V01, como las dice la voz
           'dieciocho', 'diecinueve', 'cuatrocientas', 'ochenta', 'veinticinco',
           'trescientos', 'trescientas', 'doscientas', 'quinientos', 'quinientas',
           'seiscientos', 'setecientos', 'ochocientos', 'novecientos'}


def palabras_stt(clave, bloque):
    """[(t_master, palabra_normalizada)] del bloque, con Scribe."""
    v = R.voces(clave)
    rej = json.load(open(os.path.join(v, 'DA_%s_rejilla.json' % clave),
                         encoding='utf-8'))
    tr = {t['bloque']: t for t in rej['tramos']}[bloque]
    f = glob.glob(os.path.join(v, 'stt', 'DA_%s_*_%s.json' % (clave, bloque)))[0]
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


def graficos(clave):
    """[{archivo, ini, cuadros}] de 09 MOTION GRAPHICS/DA_<V>_mg.json."""
    p = os.path.join(R.sub(clave, '09 MOTION GRAPHICS'), 'DA_%s_mg.json' % clave)
    return json.load(open(p, encoding='utf-8')) if os.path.exists(p) else []


def calcula(clave):
    rej = json.load(open(os.path.join(R.voces(clave), 'DA_%s_rejilla.json'
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
        # 7 nov: todo carton abre con mayuscula (el arreglo permitido), tambien
        # un relevo a mitad de oracion: «Llega a la mesa...», «Donde se mueve...»
        frase = presentar(trozo, True, empieza)
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
    ran = json.load(open(os.path.join(R.voces(clave), 'DA_%s_ranuras.json' % clave),
                         encoding='utf-8'))
    cierre = ran['pieza'] - (182 + 119)
    # 7 nov: las ventanas de los motion graphics (V5), en cuadros de la linea
    rotulos = [(d['ini'], d['ini'] + d['cuadros']) for d in graficos(clave)]
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
        # grafico y carton no conviven: un carton que empieza antes de un
        # grafico se corta donde el grafico entra.
        for a, b in rotulos:
            assert not (a <= p['ini'] < b), (clave, p['frase'], 'empieza sobre un grafico')
            if p['ini'] < a < fin:
                fin = a
        p['cuadros'] = fin - p['ini']
        p['densidad'] = round(len(p['frase']) / (p['cuadros'] / FPS), 1)
    for n, p in enumerate(piezas, 1):
        p['archivo'] = RENOMBRA.get(clave, {}).get(n, 'DA_%s_p%02d_carton.mov' % (clave, n))
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
        import da_pieza as GP
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
        pieza = json.load(open(os.path.join(R.voces(c), 'DA_%s_ranuras.json'
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
