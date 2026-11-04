# -*- coding: utf-8 -*-
r"""Cartones verbatim del curso Enfoque diferencial (es `cartones_lp`).

    python cartones_ed.py              calcula, comprueba y escribe el json
    python cartones_ed.py --quemar     ademas quema los .mov en 02 CARTONES
    python cartones_ed.py T4 --quemar  uno solo

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
    tiempos POR PALABRA de Scribe (`stt_ed.py`). El carton entra en el
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

from guion_ed import VIDEOS, bloques            # noqa: E402
import rutas_ed as R                            # noqa: E402

CUERPO = 52
SALTO = int(round(CUERPO * 1.36))
FPS = 24000 / 1001.0
CABEZA = 182 + 119
RESPIRO = 24
N_RESPIRO = 48          # el respiro de la pieza (ed_pieza.N_RESPIRO)
COMODO = 10.0
TOPE_RENGLONES = 3

SALIDA = r'D:\DAE\_tmp\ed\cartones_ed.json'

# Enfoque diferencial (3 nov): escogidos a mano con las voces ya medidas
# (frases VERBATIM de `guion_ed`, la que se oye encima). Lo que va: los
# datos (edades, articulos, sentencias, nombres), las frases que el profesor
# subraya y la tesis de cada caso. Fuera:
#   - las ranuras de los rotulos (C1 r01 Molano, C2 r01 Jairo y r22
#     Mauricio, C3 r01 Wilmer, C5 r02 Valentina);
#   - los insultos. «caso de maricones» (C2) y las expresiones racistas del
#     C3 los dice la voz, verbatim; en pantalla no se escriben: el carton
#     del C3 es «comenzaron las expresiones racistas»;
#   - el hecho de violencia sexual del C4 («abuso sexualmente de ella») y
#     los golpes del C2 y del C3: lo dice la voz, el carton no lo subraya.
# Primera corrida (3 nov): densidad 62/62/54/59/50 %. Fuera por velocidad
# de lectura: «los demas pasajeros... grababan» (C3, 19 car/s), «no habia
# sido valorado...» (C3, 19), «punto muerto» (C4: le daba 75 cuadros a la
# remision, que es el error del caso) y la pregunta «¿nombre real o apodo?»
# (C5, 44 cuadros: la dice Julian y la r05 es el primer plano de ella).
# Recortados: la imputacion del C3 desde «les imputo» y el 134B desde «el
# posible».
ELEGIDOS = {
 'C1': [
  ('a02_la_denuncia', 'una mujer de 29 años con discapacidad cognitiva leve,'),
  ('a03_la_historia_clinica', 'encuentra el diagnóstico de discapacidad '
   'cognitiva leve certificado por su EPS.'),
  ('a04_la_imputacion', 'formula la imputación por el delito de acceso carnal '
   'abusivo con incapaz de resistir (artículo 210 del Código Penal),'),
  ('a05_no_ordena', 'No ordena entrevista psicológica forense centrada en la '
   'comprensión y voluntariedad de Yolanda'),
  ('a06_no_indaga', 'no indaga sobre la naturaleza de la relación entre ella y '
   'el procesado,'),
  ('a08_la_defensa', 'la defensa del procesado invoca la Sentencia C-163 de '
   '2021'),
  ('a09_equiparar', 'equiparar automáticamente el diagnóstico de discapacidad '
   'con la incapacidad de resistir,'),
  ('a10_modelo_social', 'Yolanda se presume con plena autonomía para su vida '
   'sexual,'),
  ('a12_el_juez', 'la acusación tiene un vacío probatorio serio:'),
  ('a13_el_vacio', 'y que la sola referencia al diagnóstico no basta.'),
  ('a15_la_valoracion', 'ordena una valoración psicológica forense específica'),
  ('a16_bases_solidas', 'antes de poder sostener nuevamente la acusación sobre '
   'bases sólidas.'),
 ],
 'C2': [
  ('b02_el_activista', 'Era un reconocido defensor de derechos humanos y líder '
   'del activismo LGBTI en su ciudad.'),
  ('b03_las_amenazas', 'había recibido amenazas relacionadas con su labor como '
   'activista.'),
  # 3 nov, pase previo: 27 s sin carton entre el 914 y el 1567 (la manana
  # del crimen). Los datos, no los golpes.
  ('b04_la_manana', 'Una mañana de finales de agosto,'),
  ('b06_el_cumpleanos', 'Su cuerpo fue hallado al día siguiente, coincidiendo con '
   'la fecha de su cumpleaños'),
  ('b07_nada_robado', 'No se sustrajo ningún objeto de valor de la vivienda.'),
  ('b08_el_prejuicio', 'la actuación institucional estuvo marcada por el '
   'prejuicio.'),
  ('b09_el_coronel', 'coronel Hernán Ocampo Rueda,'),
  ('b09_el_coronel', 'lo calificó como un «crimen absolutamente pasional»,'),
  ('b10_antes_de', 'antes de que existiera una sola línea de investigación '
   'seria sobre el móvil del homicidio.'),
  ('b11_la_escena', 'miembros de la Policía ingresaron sin la debida protección '
   'del lugar de los hechos,'),
  ('b12_la_camisa', 'como la camisa que se había comprado para sus cumpleaños '
   'y el pantalón de la víctima,'),
  ('b12_la_camisa', 'el piso de la vivienda fue lavado antes de que se '
   'recogieran muestras.'),
  ('b13_la_custodia', 'que no fueron embalados ni custodiados conforme a la '
   'cadena de custodia,'),
  ('b14_el_despacho', 'fundamentó la hipótesis de «crimen pasional»'),
  ('b16_parte_civil', 'La pareja de Jairo intentó ser reconocida como parte '
   'civil dentro del proceso,'),
  ('b17_negadas', 'Ambas solicitudes fueron negadas o resueltas de manera '
   'extemporánea'),
  ('b18_la_desidia', 'denotaron una permanente desidia frente a la práctica de '
   'interrogatorios»'),
  ('b19_la_vida_sexual', 'en lugar de sobre la evidencia forense disponible.'),
  ('b20_diez_anos', 'Diez años después de los hechos, el caso seguía en etapa '
   'de indagatoria, sin una sola persona imputada.'),
  ('b21_decenas', 'decenas de homicidios y amenazas contra personas LGBTI en la '
   'región,'),
  ('b22_impune', 'El crimen de Jairo Montero Salas permanece impune.'),
 ],
 'C3': [
  ('c02_la_llamada', 'dos pasajeros, en evidente estado de embriaguez, se '
   'negaban a descender'),
  ('c03_la_aeronave', 'les explicó con calma la situación'),
  # 3 nov, pase previo: la primera mitad iba al 35 %; 21 s sin carton entre
  # el 1022 y el 1519 (se negaron) y 24 s entre el 2233 y el 2807 (la
  # captura; los insultos siguen sin escribirse en pantalla).
  ('c04_los_golpes', 'Los dos hombres se negaron y, ante la insistencia de '
   'Wilmer, se resistieron físicamente'),
  ('c06_el_video', 'El video se difundió esa misma noche en redes sociales'),
  ('c08_los_insultos', 'Fue solo entonces, durante el traslado, cuando '
   'comenzaron las expresiones racistas:'),
  # («Los dos agresores...» entero salia a 16,6 car/s: el relevo de «les
  # imputo» no se deja empujar)
  ('c11_la_imputacion', 'fueron capturados por agresión a servidor público,'),
  ('c11_la_imputacion', 'les imputó únicamente el delito de violencia contra '
   'servidor público,'),
  ('c12_sin_considerar', 'la circunstancia de agravación punitiva por móvil '
   'discriminatorio prevista en el artículo 58, numeral 3, del Código Penal,'),
  ('c12_sin_considerar', 'el posible delito autónomo de hostigamiento (art. '
   '134B).'),
  ('c13_en_libertad', 'Esa misma noche quedaron en libertad'),
  ('c16_wilmer', '«lo que más me dolió no fueron los golpes, fue que nadie, al '
   'principio, quiso llamar las cosas por su nombre».'),
  ('c17_la_revision', 'el patrón verbal reiterado documentado durante el '
   'traslado y en la estación'),
  ('c18_la_adicion', 'Mediante una adición a la imputación,'),
  ('c18_la_adicion', 'la circunstancia de agravación del artículo 58.3 como el '
   'delito autónomo de hostigamiento (art. 134B),'),
  ('c19_la_correccion', 'una primera lectura de los hechos invisibilizó su '
   'dimensión racial,'),
 ],
 'C4': [
  ('d01_el_resguardo', 'En un resguardo indígena cercano a Puerto Guzmán, '
   'Putumayo,'),
  ('d02_el_taita', 'autoridad indígena (Taita) de un cabildo con una estructura '
   'política y organizativa débil'),
  # 3 nov, pase previo: 21 s sin carton entre el 777 y el 1289. El nombre y
  # la posicion de autoridad son la tesis del caso; el abuso no se escribe.
  ('d03_la_rutina', 'Jacanamijoy, aprovechando su posición de autoridad y la '
   'confianza que esta le confería ante la familia y la comunidad,'),
  ('d05_la_madre', 'acudió primero ante las autoridades del cabildo para '
   'denunciar.'),
  ('d06_la_reunion', 'no tenían la fuerza política ni los mecanismos internos '
   'para actuar contra el Taita,'),
  ('d08_la_justicia', 'la madre acudió a la justicia occidentalizada.'),
  ('d09_sin_claridad', 'frente a un hecho ocurrido en territorio ancestral y '
   'protagonizado por una autoridad indígena.'),
  ('d10_los_colegas', 'algunos le recomendaron quedarse con el caso y avocar '
   'conocimiento directamente,'),
  ('d10_los_colegas', 'otros insistían en que lo devolviera al resguardo'),
  ('d11_la_mesa', 'una mesa técnica interinstitucional'),
  ('d12_la_recomendacion', 'la recomendación mayoritaria fue devolver el caso '
   'a la jurisdicción indígena,'),
  ('d13_remitio', 'el fiscal remitió el caso de vuelta al resguardo.'),
  ('d16_en_su_cargo', 'Ninguna de las dos jurisdicciones lo asumió,'),
  ('d16_en_su_cargo', 'sin que se activara medida de protección alguna a favor '
   'de la víctima.'),
 ],
 'C5': [
  ('e01_valentina', 'Valentina, mujer trans de 29 años,'),
  # 3 nov, pase previo: 24 s sin carton entre el 521 y el 1107 (la
  # recepcion y la pregunta en voz alta, que es el hecho del caso).
  ('e03_la_recepcion', 'En la recepción, el funcionario le solicitó su documento '
   'de identidad.'),
  ('e04_en_voz_alta', 'le preguntó en voz alta, frente a otras personas que '
   'esperaban de turno'),
  ('e06_su_nombre', 'Valentina explicó que Valentina era su nombre '
   'identitario.'),
  ('e07_el', 'el funcionario se refirió a ella varias veces como «él»,'),
  ('e08_alias', 'escribió «alias Valentina» en el campo de observaciones'),
  ('e09_el_campo', 'el mismo campo que normalmente se usa para registrar apodos '
   'de personas investigadas por un delito, no de víctimas.'),
  ('e11_o_su_amante', '«¿pero su pareja o su amante?»,'),
  ('e13_la_casilla', 'por su orientación sexual en lugar de su identidad de '
   'género'),
  ('e13_la_casilla', 'la única casilla disponible'),
  ('e14_hombre_gay', 'escribió en la casilla «hombre gay»,'),
  ('e16_la_suposicion', 'El funcionario no transcribió la respuesta de la '
   'víctima: la sustituyó por su propia suposición.'),
  ('e17_salio', 'había quedado señalada como si fuera ella la irregular,'),
  ('e18_no_volvio', 'No volvió a insistir en el trámite de la denuncia.'),
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
    rej = json.load(open(os.path.join(v, 'ED_%s_rejilla.json' % clave),
                         encoding='utf-8'))
    tr = {t['bloque']: t for t in rej['tramos']}[bloque]
    f = glob.glob(os.path.join(v, 'stt', 'ED_%s_*_%s.json' % (clave, bloque)))[0]
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
    rej = json.load(open(os.path.join(R.voces(clave), 'ED_%s_rejilla.json'
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
    ran = json.load(open(os.path.join(R.voces(clave), 'ED_%s_ranuras.json' % clave),
                         encoding='utf-8'))
    cierre = ran['pieza'] - (182 + 119)
    # 3 nov: las ranuras con rotulo, en cuadros de la linea
    import lowerthirds_ed as LTS
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
        p['archivo'] = RENOMBRA.get(clave, {}).get(n, 'ED_%s_p%02d_carton.mov' % (clave, n))
    return piezas


# 4 nov (C4, revision): un carton que cambia de largo en una linea ya tocada
# va con otro nombre: el media pool cachea la duracion del archivo y un
# carton reescrito en su sitio entraria con el largo viejo. El p01 del C4 se
# corta donde entra el rotulo de Yaneth (236 -> 106 cuadros).
RENOMBRA = {'C4': {1: 'ED_C4_p01_carton_rotulo.mov'}}


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
        import ed_pieza as GP
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
        pieza = json.load(open(os.path.join(R.voces(c), 'ED_%s_ranuras.json'
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
