# -*- coding: utf-8 -*-
r"""Cartones verbatim de Justicia restaurativa.

    python cartones_jr.py              calcula, comprueba y escribe el json
    python cartones_jr.py --quemar     ademas quema los .mov en 02 CARTONES
    python cartones_jr.py T4 --quemar  uno solo

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
    tiempos POR PALABRA de Scribe (`stt_jr.py`). El carton entra en el
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

from guion_jr import VIDEOS, bloques            # noqa: E402
import rutas_jr as R                            # noqa: E402

CUERPO = 52
SALTO = int(round(CUERPO * 1.36))
FPS = 24000 / 1001.0
CABEZA = 182 + 119
RESPIRO = 24
COMODO = 10.0
TOPE_RENGLONES = 3

SALIDA = r'D:\DAE\_tmp\jr\cartones_jr.json'

ELEGIDOS = {
 'C1': [
  ('c02_el_hospital', 'El joven Juan se exalta, al punto, que golpea con '
   'sus manos en tres oportunidades a Ana;'),
  ('c03_le_corresponde', 'le corresponde a usted este caso en su condición '
   'de fiscal local radicado/a.'),
  ('c04_el_legista', 'determina una incapacidad definitiva para trabajar, '
   'sin secuelas, de 65 días.'),
  ('c05_la_mediacion', 'el decidido interés de acudir al mecanismo de '
   'justicia restaurativa (JR) de la mediación,'),
  ('c05_la_mediacion', 'han intentado dialogar con la víctima de manera '
   'directa, pero han sido rechazados.'),
 ],
 'C2': [
  ('n02_los_hechos', 'Una noche de mediados de 2026, en una de las '
   'localidades de Bogotá se presentó una riña múltiple frente a una tienda '
   'de barrio.'),
  ('n04_por_la_espalda', 'Ferreira fue agredido por la espalda con un arma '
   'cortopunzante'),
  ('n05_de_nuevo', 'aprovechando su condición de indefensión, lo alcanzaron '
   'y lo agredieron de nuevo con arma blanca,'),
  ('n06_flagrancia', 'Los dos agresores fueron capturados en flagrancia.'),
  ('n06_flagrancia', 'La víctima no tenía ningún conflicto previo con los '
   'dos procesados:'),
  ('n07_perfil_victima', 'Perfil de la víctima. Nombre en el caso, '
   'ficticio: Camilo Andrés Ferreira Buitrago.'),
  ('n08_lesiones', 'Lesiones sufridas: herida por arma cortopunzante en '
   'tórax posterior izquierdo con hemoneumotórax'),
  ('n08_lesiones', 'Incapacidad médico-legal: 30 días, con carácter '
   'provisional.'),
  ('n09_delito_imputado', 'Delito imputado por estos hechos: homicidio '
   'agravado (arts. 103 y 104, num. 7, CP) en grado de tentativa (art. 27 '
   'CP).'),
  ('n10_perfil_procesados', 'Procesado 1: Jairo Ortiz Cuéllar, 21 años, '
   'conductor de servicio público.'),
  ('n10_perfil_procesados', 'Procesado 2: Jaime Rincón Sepúlveda, 39 años, '
   'comerciante independiente.'),
  ('n11_situacion', 'Antecedentes: sin antecedentes relevantes '
   'documentados.'),
  ('n12_condiciones', 'Capacidad económica: limitada; el pago pactado con '
   'la víctima se estructuró en cuotas.'),
  ('n12_condiciones', 'Aceptación formal de cargos: ninguno de los dos '
   'aceptó cargos.'),
  ('n13_disposicion', 'suscribieron con la víctima un acuerdo privado de '
   'indemnización y un compromiso de no agresión futura,'),
  ('n14_acusacion', 'La Fiscalía imputó inicialmente tentativa de homicidio '
   'agravado en concurso con hurto calificado y agravado,'),
  ('n15_la_pena', 'retiró el cargo de hurto por falta de elementos '
   'probatorios,'),
  ('n15_la_pena', 'con una pena imponible, en caso de condena, de entre 200 '
   'y 450 meses de prisión.'),
  ('n16_el_acuerdo', 'la víctima manifestó estar «a paz y salvo» y '
   'renunciar a cualquier reclamación.'),
  ('n17_la_solicitud', 'el defensor solicitó formalmente a la Fiscalía '
   'adelantar un principio de oportunidad'),
  ('n17_la_solicitud', '«de acuerdo con los postulados de justicia '
   'restaurativa».'),
 ],
 'U1': [
  ('u01_inicio', 'Inicio: el encuentro en la carretera.'),
  ('u02_el_bloqueo', 'Al intentar adelantar a un viejo automóvil, el otro '
   'conductor (Mario) lo bloquea.'),
  ('u03_escalada', 'Escalada: el orgullo entra en juego.'),
  ('u04_el_pinchazo', 'Diego logra adelantar a Mario y lo insulta, '
   'siguiendo su camino.'),
  ('u05_mario_aparece', 'Mario aparece… y reconoce al hombre que lo '
   'insultó. Hay ofensas mutuas.'),
  ('u06_confrontacion', 'Confrontación directa.'),
  ('u08_explosion', 'Explosión: punto sin retorno.'),
  ('u09_la_violencia', 'destruyen los vehículos, se golpean brutalmente, '
   'se hieren gravemente.'),
  ('u11_desenlace', 'Desenlace: destrucción mutua.'),
  ('u12_calcinado', 'Encuentran el auto completamente calcinado.'),
 ],
 'U2': [
  ('a02_impunidad', '«Juanito Lagunas me recomendó acudir a la justicia '
   'restaurativa para el caso de mi primo…,'),
  ('a02_impunidad', 'la justicia restaurativa me suena como a impunidad…, '
   'además, ¿eso no es solo para delitos menores?»'),
  ('a03_tolstoi', 'recuerda una frase que leyó en Guerra y Paz de Tolstói'),
  ('a04_la_mirada', '«Se miraron mutuamente durante un minuto. Esa mirada '
   'salvó a Pierre.'),
  ('a04_la_mirada', 'entre esas dos personas se establecieron relaciones '
   'humanas.'),
  ('a05_hijos_del_planeta', 'los dos eran hijos de este planeta, los dos '
   'tenían o habían tenido una madre que les quería y a la que querían,'),
  ('a05_hijos_del_planeta', 'los dos hacían el bien y el mal y se '
   'enorgullecían, envanecían y arrepentían».'),
  ('a06_encontrarse', 'En la posibilidad, sobre todo, de encontrarse con '
   'el otro, sea quien sea…'),
  ('a08_como_aplicar', '«¿Cómo aplicar la justicia restaurativa en el '
   'proceso penal?»…'),
 ],
 'U3': [
  ('b03_el_perdon', '«¿Pero usted en verdad cree que una víctima va a '
   'terminar pidiendo perdón por lo que le hicieron?'),
  ('b04b_pie_de_foto', 'Cansado. Vincent van Gogh. 1882. Lápiz sobre '
   'papel.'),
  ('b05_rubiano', 'recuerda una historia escrita por el director Fabio '
   'Rubiano'),
  ('b06_el_jardin', 'Una madre juega con su hijo en el jardín que tienen '
   'frente a su casa.'),
  ('b07_debo_raptar', '«Perdón, señora, debo raptar a su hijo.'),
  ('b08_perdoneme', 'para que su hijo valore el hecho de tener una madre '
   'cariñosa, me lo llevo'),
  ('b10_te_perdono', 'lo que acabas de hacer es comprensible, te '
   'perdono».'),
  ('b15_a_la_fuerza', 'exigir el perdón a la fuerza sería un gesto o un '
   'actuar irresponsable.'),
  ('b16_encontrarse', 'Lo fundamental en la justicia restaurativa es la '
   'posibilidad de encontrarse con el otro,'),
  ('b16_encontrarse', 'Pero también, la posibilidad de encontrarse con uno '
   'mismo.'),
  ('b17_no_tiene_que', 'No hay que perdonar a quien hace el daño, quien '
   'quiera perdonar, pues lo hace…'),
  ('b17_no_tiene_que', 'La justicia restaurativa ofrece, sobre todo, la '
   'posibilidad de reconciliarse con lo sucedido'),
  ('b18_lea_esto', '«La frase», usted le explica, «es de James Hillman, un '
   'psicoanalista norteamericano»:'),
  ('b19_hillman_1', 'El perdón, como la humildad, es sólo un término'),
  ('b19_hillman_1', 'a menos que uno haya sido totalmente humillado o '
   'totalmente agraviado.'),
  ('b19_hillman_1', 'El perdón sólo tiene sentido cuando uno no puede ni '
   'olvidar ni perdonar.'),
  ('b20_hillman_2', 'Cualquiera puede olvidar un insulto insignificante, '
   'una afrenta personal.'),
  ('b21_hillman_3', 'Puede muy bien ser que la traición no tenga otro '
   'resultado positivo que el perdón,'),
  ('b22_la_sal', 'Ese perdón es un perdón que no es un olvido, sino el '
   'recuerdo del mal transformado en un contexto más amplio'),
  ('b22_la_sal', 'la sal de la amargura transformada en la sal de la '
   'sabiduría.'),
  ('b23_silencio', 'Juana termina de leer y se queda pensativa… Ambos '
   'hacen silencio…'),
 ],
 'U4': [
  ('d05_mi_primo', '«¿por qué le resultaría mejor a mi primo acudir a la '
   'justicia restaurativa?»'),
  ('d06_thiebaut', 'El libro se titula «Daño y silencio» de Carlos '
   'Thiebaut.'),
  ('d07_nombrarlo', 'Aprender el sufrimiento y aprender a atenderlo al '
   'concebir esa conducta, precisamente, como doliente'),
  ('d08_una_imagen', 'Dar una imagen, un nombre, a algo que todavía no lo '
   'tenía'),
  ('d08_una_imagen', 'quienes están junto al doliente pueden llegar a verse '
   'concernidos por ese dolor'),
  ('d09_las_palabras', 'Las palabras, pues, permiten nombrar los dolores y '
   'las penas y permiten comprenderlas como daños,'),
  ('d11_a_punta', '«¿Cómo es que a punta de palabras la justicia '
   'restaurativa puede ayudar a mi primo?»'),
  ('d13_acciones', 'Pero el daño no solo reclama palabras. Demanda también '
   'acciones.'),
  ('d13_acciones', 'Atender al reclamo de un dolor, sanarlo o paliarlo, es '
   'hacer algo en el mundo;'),
  ('d15_el_silencio', 'El silencio, por ejemplo, dice que en algunos casos '
   'no hay ya cura posible para un daño que se sufrió'),
  ('d16_no_reiteracion', 'El silencio pone una marca que recuerda que ya no '
   'hay sutura en el daño o en la pérdida sufridos,'),
  ('d16_no_reiteracion', 'la de un deseo o un imperativo de no reiteración '
   'del daño.'),
  ('d18_escarbar', '«Me parece muy fuerte someter a mi primo a todo eso. '
   '¿Para qué cavar y cavar y escarbar en el dolor?»'),
  ('d19_voluntariedad', 'lo fundamental en la justicia restaurativa es la '
   'voluntariedad.'),
  ('d20_nadie_obligado', '«Nadie está obligado a avanzar por ese camino. '
   'Pero quien emprende ese camino tampoco está solo.'),
  ('d20_nadie_obligado', 'De ahí la importancia de las personas mediadoras '
   'o facilitadoras.'),
  ('d21_divina_comedia', '¿Usted leyó la Divina Comedia?», le pregunta a '
   'Juana.'),
  ('d23_nueve_circulos', 'Dante recorre los nueve círculos del Infierno, '
   'viendo las imágenes y los horrores más atroces…»'),
  ('d27_virgilio', 'Dante logra regresar del Infierno gracias a que va '
   'acompañado por Virgilio.'),
  ('d27_virgilio', 'Virgilio es su guía, lo orienta, le advierte, le '
   'muestra el camino.'),
  ('d27_virgilio', 'Eso, señora Juana, es lo que hace un mediador».'),
  ('d30_muchas_gracias', '«Lo comentaré con mi primo y le cuento, '
   'doctor(a). Muchas gracias»'),
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
    rej = json.load(open(os.path.join(v, 'JR_%s_rejilla.json' % clave),
                         encoding='utf-8'))
    tr = {t['bloque']: t for t in rej['tramos']}[bloque]
    f = glob.glob(os.path.join(v, 'stt', 'JR_%s_*_%s.json' % (clave, bloque)))[0]
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
    rej = json.load(open(os.path.join(R.voces(clave), 'JR_%s_rejilla.json'
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
    cierre = json.load(open(os.path.join(R.voces(clave), 'JR_%s_ranuras.json' % clave),
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
        p['archivo'] = 'JR_%s_p%02d_carton.mov' % (clave, n)
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
        import jr_pieza as GP
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
        pieza = json.load(open(os.path.join(R.voces(c), 'JR_%s_ranuras.json'
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
