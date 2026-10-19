#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grade de luma del set de placas: curva monotona por cinco puntos.

POR QUE CINCO PUNTOS Y NO UN ESTIRON MAS GAMMA
    Hay que colocar TRES percentiles a la vez -p2, p50 y p98-. Un estiron
    lineal mas gamma no puede: el gamma que coloca la mediana arrastra el
    negro consigo. Medido en el C5U2: se pedia p2 en 32 y quedaba en 52 y en
    66 segun la placa.

    Con una curva que pasa por (0,0), (p2,T2), (p50,T50), (p98,T98) y (255,255)
    los tres caen donde se pide. La interpolacion es PCHIP de Fritsch-Carlson,
    que es monotona por construccion: no inventa inversiones de tono ni
    ondulaciones entre los puntos de control, que es lo que pasa con un spline
    cubico normal cuando los puntos estan muy juntos.

EL TOPE DE DUREZA
    Estirar el contraste endurece el borde. En vez de un tope absoluto -que
    esta confundido por el tema: un cielo liso baja la media y un interior de
    detalle la sube- se limita el AUMENTO: si la placa graduada endurece mas
    de TOPE_DUREZA, se mezcla con la original hasta bajar de ahi.

EL CROMA OBJETIVO ES DEL ENTORNO, NO DEL CUADRO ENTERO
    CROMA_OBJETIVO salio del ancla del C5U1, una placa sin acento: es el croma
    que debe tener el GRIS. Medirlo sobre el cuadro entero en una placa con
    acento mete la prenda en el promedio y obliga a una mezcla con gris que
    existe solo para compensar el acento. Medido el 19 oct 2026: la camisa
    azul de Victor ocupaba lo bastante como para subir el croma medio a 25,2 y
    la neutralizacion bajaba a 0,17, o sea 83 % de gris sobre TODA la placa.

    Por eso `croma(..., solo_fondo=True)` promedia unicamente los pixeles de
    croma <= 40 -el entorno- y deja el acento fuera de la cuenta. Si el entorno
    ya esta en objetivo, la mezcla queda en 1,00 y el acento llega intacto a
    `acentos.py`. El salvavidas: si el acento ocupara mas del 80 % del cuadro
    no quedarian pixeles de fondo que promediar y se vuelve a medir sobre todo.

LA CURVA SUBE EL CROMA, Y HAY QUE BAJARLO DESPUES
    Medido en el C5U4: el set entraba con croma medio 4,91 y salia de la curva
    en 7,50. No es un error de la curva: comprimir una placa clara y plana
    hacia un rango mas oscuro y contrastado separa los canales, porque la
    pendiente de la curva en la zona clara es mayor que 1 y multiplica la
    diferencia que ya habia entre R, G y B.

    Por eso la neutralizacion va DESPUES de la curva, nunca antes: si se
    neutraliza primero, la curva vuelve a abrir el croma y la placa termina
    fuera de objetivo igual. Se mezcla con la version en gris lo justo para
    aterrizar en CROMA_OBJETIVO, que es el del ancla. Es gratis y no toca ni
    el contenido ni la luma: mezclar con el gris conserva la luminancia.

UNA CURVA POR CANAL CUANDO LA PLACA TRAE DOMINANTE (`por_canal=True`)
    Con una sola curva compartida, el dominante del modelo sobrevive a la
    curva y la neutralizacion tiene que llevarselo mezclando con el gris. Esa
    mezcla es global y no distingue un dominante de un acento: medido el 19
    oct 2026 en el PRIORIDAD 03, la placa de la tienda entraba con croma 36,5
    y salia mezclada al 0,11 -es decir, 89 % de gris-, y la camisa azul de
    Victor al 0,16. El acento institucional moria con el dominante.

    Es el mismo hallazgo que ya estaba en `grade_clips.py` para los clips de
    Kling: tres curvas, una por canal, llevan cada canal a su percentil y el
    dominante desaparece por alineacion y no por desaturacion. La
    neutralizacion queda entonces casi en 1,00 y el acento sobrevive para que
    `acentos.py` lo clave despues en el hexadecimal del Manual.

    Se usa en toda placa con acento o con dominante visible. El modo de una
    sola curva se conserva porque es el que graduo los sets del CURSO 5 y
    cambiarlo retroactivamente desalinearia esas piezas.

NO ARREGLA TODO
    Lo tonal y lo cromatico son gradeables. El contenido, la textura y el
    modelo de luz no: una placa con haces de luz o con render fotografico
    sobrevive intacta a cualquier curva. Esas hay que volver a generarlas.
"""
import os
import sys

from PIL import Image, ImageFilter

Image.MAX_IMAGE_PIXELS = None

OBJETIVO = (23, 84, 205)      # p2, p50, p98 — el promedio del set del C5U1
TOPE_DUREZA = 1.15            # 15 % de aumento como maximo
CROMA_OBJETIVO = 4.2          # el del ancla: 4,17 con 0,0 % de pixeles sobre 40


def _pchip(xs, ys):
    """Fritsch-Carlson: derivadas que garantizan monotonia."""
    n = len(xs)
    h = [xs[i + 1] - xs[i] for i in range(n - 1)]
    d = [(ys[i + 1] - ys[i]) / h[i] for i in range(n - 1)]
    m = [0.0] * n
    m[0], m[-1] = d[0], d[-1]
    for i in range(1, n - 1):
        if d[i - 1] * d[i] <= 0:
            m[i] = 0.0
        else:
            w1, w2 = 2 * h[i] + h[i - 1], h[i] + 2 * h[i - 1]
            m[i] = (w1 + w2) / (w1 / d[i - 1] + w2 / d[i])
    return m


def curva(p2, p50, p98, objetivo=OBJETIVO):
    xs = [0.0, float(p2), float(p50), float(p98), 255.0]
    ys = [0.0, float(objetivo[0]), float(objetivo[1]), float(objetivo[2]), 255.0]
    # puntos de control pegados o fuera de orden: la curva no existiria
    for i in range(1, len(xs)):
        if xs[i] <= xs[i - 1]:
            xs[i] = xs[i - 1] + 1.0
    m = _pchip(xs, ys)
    lut = []
    for v in range(256):
        k = 0
        while k < len(xs) - 2 and v > xs[k + 1]:
            k += 1
        h = xs[k + 1] - xs[k]
        t = (v - xs[k]) / h
        t2, t3 = t * t, t * t * t
        y = (ys[k] * (2 * t3 - 3 * t2 + 1) + m[k] * h * (t3 - 2 * t2 + t)
             + ys[k + 1] * (-2 * t3 + 3 * t2) + m[k + 1] * h * (t3 - t2))
        lut.append(max(0, min(255, int(round(y)))))
    return lut


def perfiles(im):
    g = im.convert('L').resize((640, 360), Image.BOX)
    lum = sorted(g.getdata())
    n = len(lum)
    e = g.filter(ImageFilter.FIND_EDGES)
    dureza = sum(e.getdata()) / float(len(e.getdata()))
    return lum[int(n * 0.02)], lum[int(n * 0.50)], lum[int(n * 0.98)], dureza


def croma(im, solo_fondo=False):
    c = im.resize((400, 225), Image.BOX)
    v = [max(q) - min(q) for q in c.getdata()]
    alto = 100.0 * sum(1 for x in v if x > 40) / len(v)
    if solo_fondo:
        fondo = [x for x in v if x <= 40]
        if len(fondo) >= 0.2 * len(v):
            v = fondo
    return sum(v) / len(v), alto


def neutralizar(im, objetivo=CROMA_OBJETIVO):
    # Mezcla con la version en gris hasta aterrizar en el croma del ENTORNO.
    #
    # EL CONJUNTO DE PIXELES SE FIJA UNA SOLA VEZ, Y ES CRITICO
    #   Si en cada vuelta se vuelve a preguntar cuales pixeles son entorno, la
    #   propia mezcla mete pixeles de acento en el conjunto -uno de croma 45
    #   baja de 40 en cuanto se mezcla- y el promedio sube en vez de bajar. El
    #   bucle responde bajando mas la mezcla, y asi hasta destenir la placa
    #   entera. Medido el 19 oct 2026 en el PRIORIDAD 03: el entorno de la
    #   placa del telefono estaba en 5,81 contra un objetivo de 4,20 -un ajuste
    #   de nada- y el bucle terminaba en 0,35, o sea 65 % de gris sobre todo.
    #
    #   Por eso la mascara se toma del ORIGINAL y se mide siempre sobre esos
    #   mismos indices. Con el conjunto fijo el croma si es lineal en la mezcla
    #   y la correccion converge en una o dos vueltas.
    base = im.resize((400, 225), Image.BOX)
    v = [max(q) - min(q) for q in base.getdata()]
    idx = [i for i, x in enumerate(v) if x <= 40]
    if len(idx) < 0.2 * len(v):
        idx = list(range(len(v)))

    def _medir(img):
        d = list(img.resize((400, 225), Image.BOX).getdata())
        return sum(max(d[i]) - min(d[i]) for i in idx) / float(len(idx))

    cr = _medir(im)
    if cr <= objetivo:
        return im, 1.0
    gris = im.convert('L').convert('RGB')
    k = objetivo / cr
    out = Image.blend(gris, im, k)
    for _ in range(8):
        c2 = _medir(out)
        if abs(c2 - objetivo) <= 0.05 or k <= 0.02:
            break
        k = max(0.02, min(1.0, k * objetivo / max(c2, 0.01)))
        out = Image.blend(gris, im, k)
    return out, k

def graduar(origen, destino, forzar=None, por_canal=False):
    """`forzar` salta el tope de dureza y aplica esa mezcla tal cual.

    LA RAZON DE DUREZA ES LA QUE AVISA DEL GRANO, Y EL TOPE TIENE RAZON
        El 19 oct 2026 forcé 1,00 en las tres placas nuevas del C5U3
        argumentando que la dureza aterrizaba dentro del rango del set ya
        conformado (9,3 a 31,0) y que el tope protegia de nada. Era un
        argumento equivocado y se vio en pantalla: el cenital y el folio
        salieron oscuros y con grano visible en el concreto y en el papel.

        Lo que crea el grano no es DONDE aterriza la dureza sino CUANTO
        sube, porque el grano es textura fina de la placa multiplicada por
        la pendiente de la curva. Medido:

            kf11_deposito   19,1 -> 23,9   razon 1,26   bien
            kf03c_cenital   17,1 -> 27,5   razon 1,61   con grano
            kf10_folio       9,9 -> 25,7   razon 2,58   con grano

        Las dos de razon alta se rehicieron a 0,50 -el piso del tope- y
        quedaron limpias. Es decir: el tope relativo estaba haciendo
        exactamente su trabajo y el que se equivoco fui yo al anularlo.

        El caso del C5U4 (`kf05_escritura`) sigue siendo valido pero es otra
        cosa: alli el barrido mostro que la dureza NO se movia -18,71 a 0,90
        contra 18,98 a 1,00, razon 1,01- y el tope saltaba por la densidad
        del tema, no por un estiron real. Ese es el unico caso en que se
        fuerza: cuando el barrido demuestra que la razon es ~1.

        Regla: barrer SIEMPRE, mirar la razon, y forzar solo si es cercana a
        1. Si la razon pasa de ~1,3 hay grano, aunque los percentiles no
        lleguen al objetivo. Una placa que de verdad nace muy clara -un
        folio sobre un escritorio- no se arregla con curva: se vuelve a
        generar mas oscura, o se acepta mas clara que el set.
    """
    im = Image.open(origen).convert('RGB')
    p2, p50, p98, d0 = perfiles(im)
    if por_canal:
        # Los percentiles por canal salen SOLO de los grises.
        #
        #   Tomarlos del cuadro entero deja que una prenda de acento grande
        #   arrastre su canal: medido el 19 oct 2026, la camisa azul de Victor
        #   ocupaba el 19 % del cuadro, subia el percentil del canal B y la curva
        #   resultante rotaba el tono de TODO lo demas. La piel salio violeta y
        #   el pelo rojizo. El dominante que se quiere quitar vive en los grises,
        #   asi que es ahi donde hay que medirlo: alineando los tres canales
        #   sobre la poblacion neutra, el gris queda neutro y el acento conserva
        #   su posicion relativa.
        ch = im.resize((640, 360), Image.BOX)
        datos = list(ch.getdata())
        gris = [q for q in datos if max(q) - min(q) <= 40]
        if len(gris) < 0.2 * len(datos):
            gris = datos
        lut = []
        for c in range(3):
            dd = sorted(q[c] for q in gris)
            n = len(dd)
            lut += curva(dd[int(n * 0.02)], dd[int(n * 0.50)], dd[int(n * 0.98)])
        out = im.point(lut)
    else:
        lut = curva(p2, p50, p98)
        out = im.point(lut * 3)
    # tope de dureza: se mezcla con la original lo justo para bajar del tope
    mezcla = 1.0 if forzar is None else float(forzar)
    for _ in range(0 if forzar is not None else 12):
        prueba = Image.blend(im, out, mezcla) if mezcla < 1.0 else out
        _, _, _, d1 = perfiles(prueba)
        if d1 <= d0 * TOPE_DUREZA or mezcla <= 0.5:
            break
        mezcla -= 0.05
    final = Image.blend(im, out, mezcla) if mezcla < 1.0 else out
    cr0, _ = croma(final, solo_fondo=True)
    final, color = neutralizar(final)
    a2, a50, a98, d1 = perfiles(final)
    cr, alto = croma(final, solo_fondo=True)
    final.save(destino)
    return dict(placa=os.path.basename(origen), antes=(p2, p50, p98), despues=(a2, a50, a98),
                dureza=(d0, d1), mezcla=mezcla, croma=cr, croma0=cr0, color=color, alto=alto)


if __name__ == '__main__':
    ent, sal = sys.argv[1], sys.argv[2]
    forzar = float(sys.argv[3]) if len(sys.argv) > 3 else None
    os.makedirs(sal, exist_ok=True)
    print('%-26s %14s %14s %13s %6s %6s %13s' % (
        'placa', 'antes', 'despues', 'dureza', 'mezcl', 'color', 'croma'))
    filas = []
    for f in sorted(os.listdir(ent)):
        if not f.endswith('.png') or f.startswith('_v'):
            continue
        r = graduar(os.path.join(ent, f), os.path.join(sal, f[:-4] + '_grade.png'), forzar)
        filas.append(r)
        print('%-26s %14s %14s %5.1f->%5.1f %6.2f %6.2f %5.2f->%5.2f' % (
            r['placa'][5:-4], '%d/%d/%d' % r['antes'], '%d/%d/%d' % r['despues'],
            r['dureza'][0], r['dureza'][1], r['mezcla'], r['color'],
            r['croma0'], r['croma']))
    print('\nobjetivo %d/%d/%d · croma %.1f · tope de dureza +%d %%' % (
        OBJETIVO + (CROMA_OBJETIVO, int((TOPE_DUREZA - 1) * 100))))
    print('croma medio %.2f · peor %.2f' % (
        sum(r['croma'] for r in filas) / len(filas), max(r['croma'] for r in filas)))
    print('placas con pixeles sobre 40:',
          [r['placa'][5:-4] for r in filas if r['alto'] > 0.5] or 'ninguna')
