# -*- coding: utf-8 -*-
r"""Cartones verbatim de las situaciones en video (A a E).

EL PROPONEDOR AUTOMATICO NO SIRVIO AQUI, Y SE DEJA ESCRITO POR QUE
    Se corrio primero `cartones_pieza_df` tal cual, con un relevo automatico
    encima. Salieron cuatro averias en una pasada:
      - partio la cita de la minuta entre «esperar 72» y «horas para...»;
      - el separador de oraciones corto en «(Art. 165 C.P.)» porque lee el
        punto de «Art.» como fin de oracion;
      - el salto de «relleno» se comio los NOMBRES: «Julian David Morales,»
        y «Manuel Antonio Gomez,» miden menos de 42 caracteres y los tomo
        por un «Ademas,»; y en la A se comio «Pobladores del sector
        senalaron que», que es la atribucion: el carton afirmaba como hecho
        lo que la situacion pone en boca de los pobladores;
      - 68 a 77 % del cuerpo con carton, con trozos de un renglon.

    Asi que los cartones se escogen A MANO, como se hizo con el C4 y el C5
    del caso integrador -que es la ronda que Sebastian prefirio-, y la
    maquina hace lo que hace bien: el TIEMPO de cada trozo, la comprobacion
    de verbatim y la de renglones.

LO QUE SE ESCOGE Y LO QUE NO
    - Los datos que el espectador tiene que poder leer: fechas, horas,
      placas, sumas, articulos.
    - Las citas, enteras: la minuta, la nota, la frase de Julian, lo que
      dijo cada funcionario. Partidas en su punto, nunca a mitad de frase.
    - El hecho violento NO va a carton: el abordaje (A, C) y los disparos y
      el cuerpo (E) estan en la voz, verbatim, y ni la imagen ni la letra
      los repiten. Es la misma regla de la placa.
    - Una atribucion no se salta: si la situacion dice «X senala que», el
      carton o lo dice o no existe.

COMO SE MIDE EL TIEMPO
    Cada trozo entra en el cuadro en que la voz llega a su primera palabra,
    repartiendo los caracteres del bloque sobre su duracion en la rejilla
    -la misma aproximacion del caso integrador-. Un relevo termina 24
    cuadros antes de que entre el siguiente. El ultimo de cada bloque se
    estira hasta leerse comodo (10 car/s), sin pasar el respiro del que
    viene.

LA PRESENTACION NO LLEVA CARTON
    El primer bloque de cada situacion -quien es, cuantos anos, a que se
    dedica- va solo con la voz: la primera placa es la persona, y un carton
    encima le tapa la cara justo cuando el espectador la esta conociendo.
    Con eso, y sin el estadero de la A -que la placa r07 ya cuenta-, la
    cobertura queda entre 55 y 62 %, en la franja del C4 y el C5.

ARREGLOS PERMITIDOS, Y SOLO ESOS
    La mayuscula inicial cuando el trozo salta un arranque adverbial, y
    cerrar o abrir la comilla angular de una cita partida.
    `comprobar_arreglo` verifica que ninguna palabra cambie.

    python cartones_sit.py            calcula y escribe el json
    python cartones_sit.py --quemar   ademas quema los .mov en 02 CARTONES
"""
import json
import os
import sys

sys.path.insert(0, r'D:\DAE\_tmp\df')
sys.path.insert(0, r'D:\DAE\_repo\herramientas\cartones')
sys.path.insert(0, r'D:\DAE\_repo\herramientas\voz\textos')
import cartones_pieza_df as CP                   # noqa: E402
from guion_sit import VIDEOS, bloques            # noqa: E402
import rutas_sit as R                            # noqa: E402

CUERPO = 52
SALTO = int(round(CUERPO * 1.36))
FPS = 23.976
CABEZA = 301
RESPIRO = 24
COMODO = 10.0          # caracteres por segundo
TOPE_RENGLONES = 3

SALIDA = r'D:\DAE\_tmp\sit\cartones_sit.json'

# (bloque, trozo VERBATIM tal como esta en el bloque). Los trozos de un mismo
# bloque, en orden, son un relevo.
ELEGIDOS = {
 'A': [
  ('a02_la_salida', 'El 14 de marzo de 2026, a las 17:00 horas, Carlos '
   'Alberto salió en su camioneta Toyota Hilux (placas XYZ-789)'),
  ('a03_ultima_llamada', 'A las 18:02 horas, el dispositivo móvil de '
   'Carlos registró la última llamada saliente hacia su esposa'),
  ('a04_desconexion', 'A las 18:45 horas, la terminal captó tráfico de '
   'datos en la radio estación «SJP-Sector El Vergel»'),
  ('a04_desconexion', 'y, a las 19:12 horas, se produjo la desconexión '
   'abrupta del teléfono por pérdida de energía o extracción de batería'),
  ('a08_rosa_elena', 'la señora Rosa Elena Morales acudió el 15 de marzo de '
   '2026 a las 08:30 horas a la Subestación de Policía'),
  ('a09_libro_de_poblacion', '«Posible retiro voluntario del hogar por '
   'deudas comerciales o desavenencias personales.'),
  ('a09_libro_de_poblacion', 'Se sugiere a la familia esperar 72 horas para '
   'interponer denuncia formal».'),
 ],
 'B': [
  ('b02_la_nota', '«Me voy de la ciudad a buscar trabajo por mi cuenta. No '
   'me busquen, estoy bien y fue mi decisión».'),
  ('b04_la_presion', 'Allegados señalan que miembros del grupo armado '
   'ilegal Bloque Central Renacer'),
  ('b04_la_presion', 'lo venían presionando e intimidando para que se '
   'vinculara a la estructura criminal como mecánico de su flotilla de '
   'vehículos'),
  ('b05_la_llamada', '«Si no me presento mañana a las 06:00 a.m. en el '
   'cruce de El Vergel, se meten con mi familia».'),
  ('b06_el_funcionario', 'Al acudir a la autoridad receptora, el '
   'funcionario de atención sugiere no abrir noticia criminal'),
  ('b06_el_funcionario', '«hay una nota clara firmada por el joven que '
   'prueba que se fue por su propia voluntad y que es mayor de edad».'),
 ],
 'C': [
  ('c02_el_trayecto', 'El 5 de abril de 2026, a las 14:30 horas, Fernando '
   'transitaba en su vehículo particular por la periferia urbana'),
  ('c04_la_llamada', 'Dos horas después de la interceptación (16:30 '
   'horas), la esposa de Fernando recibe una llamada telefónica'),
  ('c05_la_exigencia', 'Un hombre afirma tener en su poder a Fernando, '
   'exige la suma de $150.000.000 de pesos a cambio de respetarle la vida'),
  ('c05_la_exigencia', 'aporta un detalle específico de las prendas que '
   'vestía la víctima como prueba de supervivencia'),
  ('c05_la_exigencia', 'y fija un plazo de 24 horas para la entrega del '
   'dinero en un punto rural.'),
  ('c07_el_analista', 'el analista de denuncias duda si ingresar la noticia '
   'criminal bajo el delito de Desaparición Forzada (Art. 165 C.P.)'),
  ('c07_el_analista', 'o remitiendo inmediatamente la carpeta al grupo '
   'GAULA por el delito de Secuestro Extorsivo (Art. 169 C.P.)'),
 ],
 'D': [
  ('d02_la_tormenta', 'Manuel Antonio salió a las 16:00 horas desde el '
   'casco urbano hacia su finca montado en su mulo de carga.'),
  ('d04_el_hallazgo', 'A las 07:00 horas del día siguiente (13 de abril), '
   'vecinos de la zona encuentran al mulo con la enjalma desprendida y '
   'húmeda'),
  ('d04_el_hallazgo', 'junto con el sombrero de Don Manuel atascado entre '
   'unas palizadas a 300 metros río abajo.'),
  ('d06_conocia_el_rio', 'la familia señala que Don Manuel conocía '
   'perfectamente el río y nunca lo cruzaba si estaba crecido.'),
  ('d07_los_linderos', 'dos meses atrás había tenido discrepancias de '
   'linderos con un habitante de la zona'),
  ('d07_los_linderos', 'vinculado al grupo armado Bloque Central Renacer.'),
  ('d09_el_funcionario', '«Eso fue un ahogamiento por imprudencia invernal. '
   'La Fiscalía investiga delitos, no accidentes climáticos.'),
  ('d09_el_funcionario', 'Vayan a la Defensa Civil o al Comité de Gestión '
   'del Riesgo para que manden buzos o rescate».'),
 ],
 'E': [
  ('e02_el_mirador', 'El 28 de abril de 2026, a las 17:30 horas, mientras '
   'Gustavo Adolfo caminaba cerca del antiguo estadero El Mirador'),
  ('e07_setenta_y_dos_horas', 'Transcurridas 72 horas, no se ha recibido '
   'comunicación de los perpetradores'),
  ('e07_setenta_y_dos_horas', 'ni se conoce el lugar donde fue depositado o '
   'inhumado el cuerpo de Gustavo Adolfo.'),
  ('e08_el_fiscal_de_turno', 'el fiscal de turno califica provisionalmente '
   'las diligencias de manera exclusiva como «Homicidio Agravado»'),
  ('e08_el_fiscal_de_turno', '«como hubo testigos de los disparos fatales, '
   'el hecho ya se consumó como homicidio y no corresponde a un caso de '
   'desaparición'),
  ('e08_el_fiscal_de_turno', 'por lo que no procede activar la búsqueda '
   'sino esperar la aparición fortuita del cadáver».'),
 ],
}


def renglones(t):
    from PIL import Image, ImageDraw
    import cartones_ta as C
    import apertura_verbatim_p3c5 as V
    f = C.fuente(C.F_BOLD, CUERPO)
    d = ImageDraw.Draw(Image.new('RGBA', (10, 10)))
    return len(V.partir(t, f, d))


def presentar(trozo, primero_del_bloque, empieza_oracion):
    """Los unicos arreglos: mayuscula inicial si el trozo abre el carton en
    medio de la oracion, y la comilla de una cita partida."""
    t = trozo
    if t.count('»') > t.count('«'):
        t = '«' + t
    if t.count('«') > t.count('»'):
        t = t.rstrip('.') + '»' + ('.' if trozo.endswith('.') else '')
    if primero_del_bloque and not empieza_oracion:
        for i, ch in enumerate(t):
            if ch.isalpha():
                t = t[:i] + ch.upper() + t[i + 1:]
                break
            if ch not in '«':
                break
    return t


def calcula(letra):
    rej = json.load(open(os.path.join(R.voces(letra), 'SIT_%s_rejilla.json'
                                      % letra), encoding='utf-8'))
    tr = {t['bloque']: t for t in rej['tramos']}
    tx = {b[0]: ' '.join(b[2].split()) for b in bloques(letra)}
    piezas = []
    for k, (bl, trozo) in enumerate(ELEGIDOS[letra]):
        texto = tx[bl]
        pos = texto.find(trozo)
        assert pos >= 0, '%s: el trozo no esta VERBATIM en %s:\n  %s' % (
            letra, bl, trozo)
        t = tr[bl]
        ini = CABEZA + int(round((t['entra'] + t['dur'] * pos / len(texto))
                                 * FPS))
        fin_bloque = CABEZA + int(round(t['sale'] * FPS))
        primero = k == 0 or ELEGIDOS[letra][k - 1][0] != bl
        empieza = pos == 0 or texto[:pos].rstrip().endswith(('.', ':'))
        frase = presentar(trozo, primero, empieza)
        ok, motivo = CP.comprobar_arreglo(trozo, frase)
        assert ok, (letra, motivo, frase)
        piezas.append({'situacion': letra, 'bloque': bl, 'ini': ini,
                       'fin_bloque': fin_bloque, 'frase': frase,
                       'frase_cruda': trozo, 'arreglado': frase != trozo,
                       'relevo': not primero})
    # Un relevo entra cuando la voz llega a su primera palabra; pero si el
    # trozo anterior no alcanza a leerse (menos de 14 car/s), el relevo se
    # corre unos cuadros: un carton puede ir un poco detras de la voz, nunca
    # tan rapido que no se lea. Sin pasar del punto en que el relevo mismo
    # dejaria de leerse a 16 car/s.
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
    # duraciones
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
        p['cuadros'] = fin - p['ini']
        p['densidad'] = round(len(p['frase']) / (p['cuadros'] / FPS), 1)
    for n, p in enumerate(piezas, 1):
        p['archivo'] = 'SIT_%s_p%02d_carton.mov' % (letra, n)
    return piezas


def quemar(d):
    from PIL import Image, ImageDraw
    import cartones_ta as C
    C.TINTE = (0, 72, 144)
    import apertura_verbatim_p3c5 as V
    dest = os.path.join(R.sub(d['situacion'], '02 CARTONES'), d['archivo'])
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
    letras = [x.upper() for x in sys.argv[1:] if not x.startswith('--')] \
        or VIDEOS
    for L in letras:
        o = calcula(L)
        pieza = json.load(open(os.path.join(R.voces(L), 'SIT_%s_ranuras.json'
                                            % L), encoding='utf-8'))['pieza']
        cuerpo = pieza - (182 + 119 + 48 + 119 + 182)
        cub = sum(d['cuadros'] for d in o)
        w('=== situacion %s: %d cartones, %d cuadros = %.0f%% del cuerpo'
          % (L, len(o), cub, 100.0 * cub / cuerpo))
        for d in o:
            d['renglones'] = renglones(d['frase'])
            if d['renglones'] > TOPE_RENGLONES:
                fallas.append((d['archivo'], d['renglones']))
            if d['cuadros'] < 60:
                fallas.append((d['archivo'], 'corto %d' % d['cuadros']))
            w('  %s %5d +%4d  %4.1f car/s  %d ren %s%s'
              % (d['archivo'][6:9], d['ini'], d['cuadros'], d['densidad'],
                 d['renglones'], ' relevo' if d['relevo'] else '',
                 ' ARREGLO' if d['arreglado'] else ''))
            w('      ' + d['frase'])
        todo += o
    if fallas:
        w('FALLAS: %s' % fallas)
    json.dump(todo, open(SALIDA, 'w', encoding='utf-8'), ensure_ascii=False,
              indent=1)
    if '--quemar' in sys.argv and not fallas:
        for d in todo:
            p = quemar(d)
            w('quemado %s  %d cuadros' % (os.path.basename(p), d['cuadros']))
    w('LISTO')
