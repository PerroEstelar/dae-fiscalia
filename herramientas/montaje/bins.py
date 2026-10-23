#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Donde vive cada cosa en el media pool, y como importarla ahi derecho.

POR QUE EXISTE ESTE MODULO
    Los montajes del C5U2 v2, C5U3 y C5U4 creaban su bin en la RAIZ del Master
    (`AddSubFolder(raiz, CARPETA)`) y volcaban los 45 medios sueltos ahi
    dentro. La estructura buena del proyecto es

        C5 BIENES EN EL PROCESO PENAL > U<n> > CASO <n> >
            RANURAS | CARTONES | VOCES | MUSICA | B-ROLL | COMUNES

    asi que las lineas de tiempo quedaban en un bin paralelo al final de la
    lista y no se encontraban. Ordenar 45 medios a mano despues cuesta mas que
    importarlos en su sitio de una vez. 19 oct 2026.

COMO SE USA DESDE UN montar_*.py

    import bins
    CASO = ['C5 BIENES EN EL PROCESO PENAL', 'U4', 'CASO 04 - los ilustres']

    def _carpeta(mp):
        return bins.carpeta(mp, CASO)          # la raiz del caso: ahi va la linea

    def _clips(mp):
        return bins.clips(mp, CASO)            # medios de todo el subarbol

    def medios(mp):
        bins.importar(mp, CASO, rutas)         # cada archivo a su subbin

LA REGLA DE CLASIFICACION ES EL NOMBRE DEL ARCHIVO
    Es la misma convencion que ya respetan los renders, asi que no hace falta
    una tabla aparte que se desincronice:

        FGN_intro* / MARCA_DE_AGUA*          COMUNES
        *_r00_* / *lecho* / *_respiro*       RANURAS
        *_carton_* / *_n0_* / *_n00_* / *_p0*  CARTONES
            (el C5U1 numeraba los cartones con un digito, _n5_; del C5U2
             en adelante van con dos, _n05_. Entran los dos.)
        *_ae00_* / *_prop0* / *_cita00_* /    CARTONES
        *_lt00_*
            (la nomenclatura de la PRIORIDAD 03: `_ae01_` una afirmacion
             establecida, `_prop1_` una propuesta, `_cita01_` un verbatim,
             `_lt01_` un rotulo. Los Casos 3 y 4 ya se llamaban asi y los
             23 archivos caian sin clasificar en la raiz del caso.)
        *NARRADOR* / *PREGUNTAS* / *DIALOGO* VOCES
        *MUSICA*                             MUSICA
        cualquier otra cosa                  la raiz del caso, y se avisa

    Lo que no clasifica NO se esconde: queda a la vista en la raiz del caso con
    un aviso por consola. Un archivo mal nombrado se nota ahi mismo.
"""
import os
import re

SUBBINS = ['RANURAS', 'CARTONES', 'VOCES', 'MUSICA', 'B-ROLL', 'COMUNES']

# Las versiones archivadas de un caso van a un subbin que empieza por "_"
# (p. ej. "_v1 ARCHIVO"). clips() no los lee, para que un nombre repetido de
# una version vieja no le gane al vigente en el diccionario.
PREFIJO_ARCHIVO = '_'
# El subbin donde `importar()` deja un medio cuyo nombre choca con el vigente.
ARCHIVO = '_v1 ARCHIVO'


def carpeta(mp, ruta, crear_subbins=True):
    """Devuelve la carpeta en `ruta` (lista de nombres bajo Master), creandola.

    `ruta` es relativa a Master y NO lo incluye:
        ['C5 BIENES EN EL PROCESO PENAL', 'U4', 'CASO 04 - los ilustres']
    """
    f = mp.GetRootFolder()
    for nombre in ruta:
        hijas = {s.GetName(): s for s in f.GetSubFolderList()}
        f = hijas.get(nombre) or mp.AddSubFolder(f, nombre)
        if f is None or f is False:
            raise RuntimeError('no se pudo crear el bin %r de %r' % (nombre, ruta))
    if crear_subbins:
        hijas = {s.GetName() for s in f.GetSubFolderList()}
        for s in SUBBINS:
            if s not in hijas:
                mp.AddSubFolder(f, s)
    return f


def clasificar(nombre):
    """El subbin que le toca a un archivo, o None si no se reconoce."""
    n = os.path.basename(nombre).upper()
    if n.startswith('FGN_INTRO') or n.startswith('MARCA_DE_AGUA'):
        return 'COMUNES'
    if re.search(r'_R\d\d_', n) or 'LECHO' in n or '_RESPIRO' in n:
        return 'RANURAS'
    if '_CARTON_' in n or re.search(r'_N\d{1,2}_', n) or re.search(r'_P\d[AB]?_', n):
        return 'CARTONES'
    # LA NOMENCLATURA DE LA PRIORIDAD 03
    #     Un carton de esta tanda se llama por lo que AFIRMA, no por su
    #     numero de orden: `_ae01_` lo que el documento da por establecido,
    #     `_prop1_` una propuesta o premisa que la pieza pone a examinar,
    #     `_cita01_` un verbatim, `_lt01_` un rotulo. Ninguno de los cuatro
    #     entraba por las reglas de arriba, asi que los 17 cartones, las dos
    #     citas y los cinco rotulos de cada caso caian en la raiz.
    if re.search(r'_(AE|CITA|LT)\d\d_', n) or re.search(r'_PROP\d', n):
        return 'CARTONES'
    if 'NARRADOR' in n or 'PREGUNTAS' in n or 'DIALOGO' in n:
        return 'VOCES'
    if 'MUSICA' in n:
        return 'MUSICA'
    return None


def importar(mp, ruta, rutas):
    """Importa `rutas` al caso en `ruta`, cada archivo a su subbin.

    Idempotente: lo que ya esta en el subarbol del caso no se vuelve a importar.
    Devuelve el diccionario de clips del caso, como clips().
    """
    raiz_caso = carpeta(mp, ruta)
    ya = clips(mp, ruta)

    # UN NOMBRE IGUAL QUE APUNTA A OTRO ARCHIVO NO ES "YA ESTA"
    #     23 oct 2026. El P3C5 v2 se monto entero y paso sus trece
    #     comprobaciones con DIECINUEVE de sus cuarenta y tres ranuras
    #     tomadas de la v1. La causa es esta funcion: `if base in ya:
    #     continue` miraba el NOMBRE. Las ranuras de la v2 se llaman igual
    #     que las de la v1 -el nombre sale del guion, que no cambio- y
    #     viven en `RANURAS v2` en vez de `RANURAS`. Asi que cada una de
    #     esas diecinueve se dio por importada, nunca entro al media pool,
    #     y `clips()` entrego la vieja. Ningun paso fallo: la linea tenia
    #     48 clips contiguos, el conteo exacto y las rimas en su sitio,
    #     porque la ranura vieja dura lo mismo que la nueva. El Caso 4 v2
    #     ya se habia exportado y entregado con dos ranuras de la v1.
    #
    #     El nombre no identifica un medio; la RUTA si. Cuando el nombre
    #     coincide y la ruta no, el clip viejo se archiva y el nuevo entra.
    viejos = []
    for r in rutas:
        c = ya.get(os.path.basename(r))
        if c is None:
            continue
        p = os.path.normcase(os.path.abspath(c.GetClipProperty('File Path') or ''))
        if p != os.path.normcase(os.path.abspath(r)):
            viejos.append((os.path.basename(r), c, p))
    if viejos:
        print('   %d medios con el nombre de otra version; se archivan en %r:'
              % (len(viejos), ARCHIVO))
        for base, _, p in viejos:
            print('      %-44s %s' % (base, p))
        archivar(mp, ruta, [c for _, c, _ in viejos], nombre=ARCHIVO)
        ya = clips(mp, ruta)

    grupos = {}
    for r in rutas:
        base = os.path.basename(r)
        if base in ya:
            continue
        grupos.setdefault(clasificar(base), []).append(r)

    subs = {s.GetName(): s for s in raiz_caso.GetSubFolderList()}
    for sub in sorted(grupos, key=lambda x: (x is None, x or '')):
        destino = raiz_caso if sub is None else subs[sub]
        mp.SetCurrentFolder(destino)
        mp.ImportMedia(grupos[sub])
        etiqueta = sub or 'LA RAIZ DEL CASO (sin clasificar)'
        print('   %-34s %2d archivos' % (etiqueta, len(grupos[sub])))
        if sub is None:
            for r in grupos[sub]:
                print('      AVISO nombre no reconocido:', os.path.basename(r))

    hay = clips(mp, ruta)
    faltan = [os.path.basename(r) for r in rutas if os.path.basename(r) not in hay]
    # Y DESPUES SE MIDE: cada nombre pedido tiene que apuntar al archivo
    # pedido. Es la comprobacion que no existia y por eso el error paso.
    torcidos = []
    for r in rutas:
        c = hay.get(os.path.basename(r))
        if c is None:
            continue
        p = c.GetClipProperty('File Path') or ''
        if os.path.normcase(os.path.abspath(p)) != os.path.normcase(os.path.abspath(r)):
            torcidos.append((os.path.basename(r), p, r))
    print('en el caso %d medios; faltan %s' % (len(hay), faltan or 'ninguno'))
    if faltan:
        raise RuntimeError('no entraron al media pool: %s' % faltan)
    if torcidos:
        raise RuntimeError('el media pool devuelve otro archivo con el mismo '
                           'nombre:\n  ' + '\n  '.join(
                               '%s\n    pool %s\n    pedido %s' % x for x in torcidos))
    return hay


def clips(mp, ruta):
    """Medios del subarbol del caso, por nombre. Sin lineas de tiempo y sin
    los subbins de archivo (los que empiezan por "_").

    Avisa si dos archivos distintos comparten nombre: eso significa que hay una
    version vieja sin archivar, y el diccionario se queda con una sola.
    """
    out = {}
    def rec(f):
        for c in f.GetClipList():
            try:
                if c.GetClipProperty('Type') == 'Timeline':
                    continue
            except Exception:
                pass
            n = c.GetName()
            if n in out and out[n] is not c:
                print('   AVISO nombre repetido en el media pool:', n)
            out.setdefault(n, c)
        for s in f.GetSubFolderList():
            if not s.GetName().startswith(PREFIJO_ARCHIVO):
                rec(s)
    rec(carpeta(mp, ruta, crear_subbins=False))
    return out


def archivar(mp, ruta, clips_viejos, nombre='_v1 ARCHIVO'):
    """Mueve una tanda de medios a un subbin de archivo dentro del caso.

    Para cuando se rehace un caso y conviven dos juegos de medios con los
    mismos nombres. Los que use la linea vigente se quedan donde estan.
    """
    raiz_caso = carpeta(mp, ruta, crear_subbins=False)
    subs = {s.GetName(): s for s in raiz_caso.GetSubFolderList()}
    destino = subs.get(nombre) or mp.AddSubFolder(raiz_caso, nombre)
    return mp.MoveClips(list(clips_viejos), destino)
