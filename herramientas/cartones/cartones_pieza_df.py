# -*- coding: utf-8 -*-
r"""Propone los cartones verbatim de una pieza SOBRE LA FRASE, no sobre la ranura.

POR QUE SE REHIZO
    27 de octubre, Sebastian: «what happened to cartones highlighting
    throughout the video whats being said?, with blu tinted opacity
    background?». Habia SEIS cartones en CINCUENTA Y SIETE ranuras.

    El calculo viejo ataba el carton a UNA ranura: duraba lo que durara el
    plano. Eso funcionaba con un carton por capitulo y se rompe en cuanto
    hay muchos, porque una oracion de 270 caracteres caia sobre un plano de
    108 cuadros -4,5 s- y era fisicamente ilegible.

    El carton no es del plano: es de la FRASE. Dura lo que la voz tarda en
    decirla y cruza los cortes que haga falta, que es justo lo que hacen los
    de las piezas que ya salieron -en el P3C5 los cartones promedian 213
    cuadros y los planos 179-.

LA MEDIDA DE LA CASA, SACADA DE LAS PIEZAS APROBADAS
    P3C5   20 cartones, 48 % de la pieza
    P3C4   16 cartones, 38 %
    C5U4   15 cartones, 35 %
    y el ritmo de lectura de esos veinte del P3C5 es de unos 18 caracteres
    por segundo. Por eso aqui el tope es 22: un poco mas denso, porque el
    espectador ademas lo esta oyendo, pero no mucho mas.

DOS FILTROS Y UN RESPIRO
    ILEGIBLE  Si la frase pide mas de 22 caracteres por segundo, no entra.
              Cortarla para que quepa seria reescribirla, y eso es
              exactamente lo que la regla del verbatim prohibe.
    CORTA     Menos de 60 cuadros -2,5 s- no alcanza a entrar, leerse y
              salir.
    RESPIRO   Entre un carton y el siguiente tiene que haber al menos 30
              cuadros de plano limpio. Sin eso el tinte azul no se levanta
              nunca y la pieza se vuelve una pared de texto.
"""
import json
import os
import re
import sys
import unicodedata

FPS = 23.976
CABEZA = 301            # intro 182 + entrada 119: la voz empieza aqui

DENSIDAD_MAX = 22.0     # caracteres por segundo
MINIMO = 60             # cuadros
RESPIRO = 24            # cuadros limpios entre carton y carton


def _palabras(t):
    t = unicodedata.normalize('NFD', t.lower())
    t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    return [w for w in re.split(r'[^0-9a-z]+', t) if w]


def comprobar_arreglo(crudo, arreglado):
    """El arreglo solo puede AGREGAR: todas las palabras del fragmento
    original tienen que seguir ahi, en el mismo orden y sin cambiar."""
    a, b = _palabras(crudo), _palabras(arreglado)
    i = 0
    for w in b:
        if i < len(a) and w == a[i]:
            i += 1
    if i != len(a):
        return False, 'el arreglo perdio o cambio palabras del original'
    agregadas = len(b) - len(a)
    if agregadas > 3:
        return False, 'el arreglo agrega %d palabras: ya no es minimo' % agregadas
    return True, 'agrega %d palabra(s)' % agregadas


def oraciones(t):
    """Parte en oraciones sin romper la comilla angular ni los decimales."""
    t = ' '.join(t.split())
    partes, cur = [], ''
    for i, ch in enumerate(t):
        cur += ch
        if ch in '.:' and i + 1 < len(t) and t[i + 1] == ' ':
            if re.match(r'\d', t[i + 1:i + 2] or ' '):
                continue
            if cur.strip().endswith('»') or cur.count('«') > cur.count('»'):
                continue
            partes.append(cur.strip())
            cur = ''
    if cur.strip():
        partes.append(cur.strip())
    return partes


def frases_de_la_pieza(rejilla, textos):
    """Cada oracion del capitulo con su ventana en cuadros de la PIEZA.

    El reparto es por caracteres sobre la duracion del bloque. La voz no va
    a ritmo constante, asi que esto PROPONE: la frase se mira contra el
    audio antes de quemarla.
    """
    tr = {t['bloque']: t for t in rejilla['tramos']}
    out = []
    for e in textos:
        # guion_df entrega (bloque, voz, texto escrito, texto fonetico, ...)
        # y el carton lleva el ESCRITO, que es lo que el profesor escribio.
        bloque, voz, texto = e[0], e[1], e[2]
        t = tr.get(bloque)
        if t is None:
            continue
        texto = ' '.join(texto.split())
        pos = 0
        for o in oraciones(texto):
            i = texto.index(o, pos)
            pos = i + len(o)
            a = t['entra'] + t['dur'] * i / float(len(texto))
            z = t['entra'] + t['dur'] * (i + len(o)) / float(len(texto))
            f0 = CABEZA + int(round(a * FPS))
            f1 = CABEZA + int(round(z * FPS))
            out.append({'bloque': bloque, 'voz': voz, 'frase': o,
                        'ini': f0, 'cuadros': f1 - f0})
    return out


def _cita(f):
    """Una frase entre comillas angulares es testimonio literal: la minuta
    del comandante, el panfleto, lo que alguien dijo. Es el material que mas
    justifica un carton -el espectador tiene que poder leer EXACTAMENTE que
    se escribio-, y casi siempre es corto, asi que maximizar tiempo en
    pantalla lo deja fuera. Pesa mas de lo que dura.

    27 de octubre: con peso 1,0 el capitulo 1 perdia «mujer con hijos de
    varios hombres, se fue con otro», que es la frase sobre la que se
    construye el capitulo entero.
    """
    return '«' in f or '»' in f


# ---------------------------------------------------------------- recorte
#  EL CARTON LLEVA UN FRAGMENTO, NO LA ORACION ENTERA
#      27 de octubre, Sebastian: «que sean verbatim pero legibles (...) que
#      aparezca solo cantidad de palabras suficientes y que sean comodas de
#      leer (...) son dos o tres lineas de texto a la vez (...) ahora me estas
#      entregando el verbatim de pedazos muy largos de texto».
#
#      Medido en el C5U4, que el aprobo: el texto de sus quince cartones va de
#      50 a 110 caracteres -dos renglones- y dura de 114 a 210 cuadros. O sea
#      entre 6 y 12 caracteres por segundo: tiempo de sobra para leerlo.
#      Los mios traian la oracion entera, 180 a 309 caracteres a 15-17 car/s.
#
#      Entonces el carton se queda con la duracion de la frase -que es cuando
#      la voz la dice- y el TEXTO se recorta a un fragmento de dos o tres
#      renglones. El fragmento es literal y contiguo: se corta SOLO en junta
#      de clausula, nunca a mitad de una.
TOPE_RENGLONES = 3
CUERPO = 52              # uno solo para todos, y no se cambia por carton

# Las juntas donde una oracion se puede partir sin romper la gramatica.
_JUNTAS = (u'; ', u': ', u', ')
_NEXOS = (u' y que ', u' y ', u' que ', u' para ', u' tras ', u' ante ',
          u' donde ', u' mientras ', u' porque ', u' con el ', u' con la ',
          u' en el ', u' en la ', u' al ')


def _clausulas(t):
    """Parte la oracion en trozos que se pueden leer solos."""
    trozos = [t]
    for sep in _JUNTAS:
        out = []
        for x in trozos:
            partes = x.split(sep)
            for i, q in enumerate(partes):
                out.append(q + (sep.strip() if i < len(partes) - 1 else ''))
        trozos = out
    out = []
    for x in trozos:
        resto = x
        while True:
            corte = None
            for nx in _NEXOS:
                k = resto.find(nx, 25)
                if k > 0 and (corte is None or k < corte[0]):
                    corte = (k, nx)
            if corte is None or len(resto) < 70:
                break
            out.append(resto[:corte[0]])
            resto = resto[corte[0] + 1:]
        out.append(resto)
    return [q.strip() for q in out if q.strip()]


def _peso(t):
    """Que tanto APORTA el fragmento. Un numero, una ley o un nombre propio
    es lo que el espectador necesita ver escrito; un conector no."""
    pal = t.split()
    n = sum(1 for w in pal if any(c.isdigit() for c in w)) * 3
    n += sum(1 for w in pal[1:] if w[:1].isupper()) * 2
    n += sum(1 for w in pal if len(w) > 8)
    return n + len(pal) * 0.12


#  Caracteres por segundo con los que se lee comodo. Los quince cartones
#  del C5U4 que Sebastian aprobo van entre 6 y 12.
DENSIDAD_COMODA = 13.0

#  Arranques de relleno que se pueden saltar sin romper la gramatica: son
#  adverbiales cortos que no llevan informacion -«Ademas,», «Finalmente,»,
#  «Tras varios dias de ausencia,»-. Saltarlos deja el carton empezando en
#  el sujeto, que es donde el lector quiere empezar.
RELLENO_MAX = 42

#  Un carton de seis caracteres no es un carton. Y uno que termina en
#  «comenzaron los macabros rumores de» deja la frase colgando: si el
#  ultimo trozo es una palabra de enlace, se quita.
MINIMO_CARACTERES = 35
_COLGANTES = set(u'de del a al y o e ni que con en para por tras sobre '
                 u'entre hacia desde como cuando donde la el los las un '
                 u'una unos unas su sus mi mis lo se'.split())


def _limpia(w):
    import unicodedata as U
    w = ''.join(c for c in U.normalize('NFD', w.lower())
                 if U.category(c) != 'Mn')
    return ''.join(c for c in w if c.isalpha())


def recorta(frase, mide_renglones, cuadros=None):
    """El ARRANQUE de la oracion, hasta donde quepa en dos o tres renglones.

    Es la regla simple, y es la de las piezas aprobadas: el carton no elige
    el trozo 'mas interesante' de la oracion -eso deja fragmentos huerfanos
    como «halladas con el vientre abierto» o «Etnico e Interseccional»-,
    sino que empieza donde empieza la oracion y corta en junta de clausula
    cuando ya no cabe. Asi siempre se lee como una frase.

    Lo unico que se permite saltar es un adverbial de relleno al principio.
    """
    seg = (cuadros / FPS) if cuadros else None

    def cabe(t):
        if mide_renglones(t) > TOPE_RENGLONES:
            return False
        return (len(t) / seg) <= DENSIDAD_COMODA if seg else True

    if cabe(frase):
        return frase
    cl = _clausulas(frase)
    if not cl:
        return frase
    arranques = [0]
    if (len(cl) > 1 and len(cl[0]) <= RELLENO_MAX
            and not frase.lstrip().startswith(u'\u00ab')):
        arranques.append(1)
    mejor = None
    for a in arranques:
        acum = None
        for b in range(a, len(cl)):
            trozo = ' '.join(cl[a:b + 1]).strip()
            if mide_renglones(trozo) > TOPE_RENGLONES:
                break
            if seg and (len(trozo) / seg) > DENSIDAD_COMODA and acum is not None:
                break
            acum = trozo
        if acum and (mejor is None or len(acum) > len(mejor)):
            mejor = acum
    if mejor is None or len(mejor) < MINIMO_CARACTERES:
        # Demasiado corto para ser un carton: se crece aunque apriete el
        # ritmo, que es menos malo que poner «Ademas» solo en pantalla.
        largo = None
        for a in arranques:
            acum = None
            for b in range(a, len(cl)):
                trozo = ' '.join(cl[a:b + 1]).strip()
                if mide_renglones(trozo) > TOPE_RENGLONES:
                    break
                acum = trozo
            if acum and (largo is None or len(acum) > len(largo)):
                largo = acum
        if largo is None or len(largo) < MINIMO_CARACTERES:
            # Ultimo recurso: ninguna clausula cabe entera -el capitulo 3
            # tiene una de 147 caracteres sin una sola coma-, asi que se
            # corta por palabra. Sigue siendo literal y contiguo; lo unico
            # que se pierde es que termine en junta de clausula.
            arranque = arranques[-1] if len(arranques) > 1 else 0
            pal = ' '.join(cl[arranque:]).split()
            acum = ''
            for w in pal:
                probe = (acum + ' ' + w).strip()
                if mide_renglones(probe) > TOPE_RENGLONES:
                    break
                acum = probe
            if len(acum) > len(largo or ''):
                largo = acum
        mejor = largo or cl[0]
    mejor = mejor.rstrip(' ,;:')
    # nada de frases que cuelgan de una preposicion
    pal = mejor.split()
    while len(pal) > 6 and _limpia(pal[-1]) in _COLGANTES:
        pal.pop()
    mejor = ' '.join(pal).rstrip(' ,;:')
    if frase.rstrip().endswith(mejor + '.'):
        mejor += '.'
    #  Una comilla que abre y no cierra se lee como un error de montaje.
    #  Cerrarla no toca una sola palabra, asi que comprobar_arreglo la pasa.
    if mejor.lstrip().startswith(u'\u00ab') and u'\u00bb' not in mejor:
        mejor = mejor.rstrip('.') + u'\u00bb'
    return mejor


def _entrada(f):
    """Una frase que termina en dos puntos es un ARRANQUE: lo que importa
    viene despues. Vale la mitad, asi que solo entra si no le quita el sitio
    a la frase que anuncia."""
    return f.rstrip().endswith(':')


def escoge(frases, arreglos=None):
    """Elige el MEJOR conjunto de frases, no el primero que quepa.

    POR QUE NO ES PRIMERO EL QUE LLEGA
        Tomar siempre la primera de cada par dejaba fuera justo las que mas
        importan: el Mecanismo de Busqueda Urgente perdia contra «En esta
        fase, el equipo misional debe actuar de inmediato:», y el Protocolo
        de Atencion Digna perdia contra la frase anterior.

        Y cambiar una por otra sobre la marcha tampoco sirve: el cambio
        corre el final hacia adelante y tumba la siguiente en cascada -el
        capitulo 3 paso de cuatro cartones a dos-.

        Entonces se elige el conjunto entero de una vez, con la programacion
        dinamica de toda la vida: se maximiza el tiempo con carton en
        pantalla respetando el respiro. Es exactamente lo que uno haria a
        mano, pero sin equivocarse.
    """
    arreglos = arreglos or {}
    cands, fuera = [], []
    for f in frases:
        crudo = f['frase']
        frase = arreglos.get(crudo, crudo)
        if frase is not crudo:
            ok, motivo = comprobar_arreglo(crudo, frase)
            assert ok, '%s\n  crudo:     %s\n  arreglado: %s' % (motivo, crudo, frase)
        n = f['cuadros']
        dens = len(frase) / (n / FPS) if n else 999
        if n < MINIMO:
            fuera.append((f['ini'], 'corta (%d cuadros)' % n, crudo[:48]))
            continue
        if dens > DENSIDAD_MAX:
            fuera.append((f['ini'], 'ilegible (%.1f car/s en %.1f s)'
                          % (dens, n / FPS), crudo[:48]))
            continue
        cands.append(dict(f, frase=frase, frase_cruda=crudo,
                          arreglado=frase != crudo, densidad=round(dens, 1)))

    cands.sort(key=lambda d: d['ini'])
    n = len(cands)
    valor = [c['cuadros'] * (0.5 if _entrada(c['frase'])
                              else 1.6 if _cita(c['frase']) else 1.0)
             for c in cands]
    # anterior[i]: la ultima que termina con respiro suficiente antes de i
    anterior = []
    for i, c in enumerate(cands):
        j = -1
        for k in range(i - 1, -1, -1):
            if cands[k]['ini'] + cands[k]['cuadros'] + RESPIRO <= c['ini']:
                j = k
                break
        anterior.append(j)
    mejor = [0.0] * (n + 1)
    toma = [False] * n
    for i in range(n):
        con = valor[i] + (mejor[anterior[i] + 1] if anterior[i] >= 0 else 0.0)
        sin = mejor[i]
        if con > sin:
            mejor[i + 1], toma[i] = con, True
        else:
            mejor[i + 1] = sin
    elegidas, i = [], n - 1
    while i >= 0:
        if toma[i]:
            elegidas.append(cands[i])
            i = anterior[i]
        else:
            i -= 1
    elegidas.reverse()
    puestas = {id(c) for c in elegidas}
    for c in cands:
        if id(c) not in puestas:
            fuera.append((c['ini'], 'no cabe con respiro', c['frase_cruda'][:48]))
    fuera.sort()
    return elegidas, fuera
