# -*- coding: utf-8 -*-
r"""Cambia el MEDIO de una o varias ranuras en una linea que Sebastian ya
toco a mano, SIN remontar (P3C5 §3: «no se remonta una linea que el editor
toco»).

    python reemplazar_en_sitio_jr.py "<nombre de la linea>" nuevo1=>destino1 [nuevo2=>destino2 ...] [--motivo texto]
    python reemplazar_en_sitio_jr.py "<nombre de la linea>" ruta1 [ruta2 ...]
    python reemplazar_en_sitio_jr.py "<nombre de la linea>" nuevo=>>viejo

La tercera forma cambia el ARCHIVO al que apunta el clip (otro nombre, mismo
largo): el item del pool que apunta a `viejo` se relee con `ReplaceClip(nuevo)`
y `viejo` se queda donde esta. En el retrato solo puede cambiar ese nombre.

La segunda forma es para cuando la herramienta que hace el medio ya lo
escribio en su sitio (construir, mov_jr, detalle_jr apartan el viejo y
escriben el nuevo con el mismo nombre): solo se relee con `ReplaceClip`.

Para cada par: el archivo que la linea usa (destino) va a `_descartes` con el
motivo, el nuevo toma su lugar con el MISMO nombre y en la MISMA ruta, y el
item del media pool que apunta a esa ruta se relee con `ReplaceClip`. El
largo tiene que ser el mismo (se comprueba antes de tocar nada).

Antes y despues se toma un RETRATO de la linea: pista, nombre, entrada,
salida y desplazamiento de cada clip de video y audio. Si algo cambio que no
sea el medio, lo dice y para (el proyecto no se guarda).
"""
import os
import shutil
import sys

H = r'D:\DAE\_repo\herramientas'
for sub in ('montaje', 'prompts', 'cartones', os.path.join('voz', 'textos')):
    sys.path.insert(0, os.path.join(H, sub))

import jr_pieza as SP                                     # noqa: E402


def norm(p):
    return os.path.normcase(os.path.normpath((p or '').replace('/', os.sep)))


def retrato(tl):
    r = []
    for tipo in ('video', 'audio'):
        for i in range(1, tl.GetTrackCount(tipo) + 1):
            for it in tl.GetItemListInTrack(tipo, i) or []:
                mpi = it.GetMediaPoolItem()
                fp = mpi.GetClipProperty('File Path') if mpi else ''
                r.append((tipo, i, it.GetStart(), it.GetEnd(), it.GetLeftOffset(),
                          os.path.basename(fp or it.GetName())))
    return sorted(r)


def items_de(carpeta, quiero, out):
    for c in carpeta.GetClipList() or []:
        if norm(c.GetClipProperty('File Path')) in quiero:
            out.append(c)
    for s in carpeta.GetSubFolderList() or []:
        items_de(s, quiero, out)
    return out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    motivo = 'reemplazado_en_sitio'
    if '--motivo' in sys.argv:
        motivo = sys.argv[sys.argv.index('--motivo') + 1]
        args = [a for a in args if a != motivo]
    linea = args[0]
    pares, cambia = [], {}
    for a in args[1:]:
        if '=>>' in a:
            nuevo, viejo = a.split('=>>')
            cambia[norm(viejo)] = (nuevo, viejo)
            pares.append([None, viejo])
            assert SP.cuadros(nuevo) == SP.cuadros(viejo), (nuevo, viejo)
        elif '=>' in a:
            pares.append(a.split('=>'))
        else:
            pares.append([None, a])
    for nuevo, dest in pares:
        if nuevo is None:
            assert os.path.exists(dest), dest
            continue
        assert os.path.exists(nuevo), nuevo
        assert os.path.exists(dest), dest
        a, b = SP.cuadros(nuevo), SP.cuadros(dest)
        assert a == b, 'largo distinto: %s %d vs %s %d' % (nuevo, a, dest, b)
    resolve = SP._resolve()
    pm = resolve.GetProjectManager()
    pr = pm.GetCurrentProject()
    tl = None
    for i in range(1, int(pr.GetTimelineCount()) + 1):
        t = pr.GetTimelineByIndex(i)
        if t.GetName() == linea:
            tl = t
    assert tl is not None, 'no hay linea %s' % linea
    antes = retrato(tl)
    SP.w('linea %s: %d clips' % (linea, len(antes)))
    quiero = {norm(d) for _, d in pares}
    pool = items_de(pr.GetMediaPool().GetRootFolder(), quiero, [])
    SP.w('items del pool que apuntan a esas rutas: %d' % len(pool))
    for nuevo, dest in pares:
        if nuevo is None:
            SP.w('  %s  ya escrito en su sitio (%d cuadros)' % (os.path.basename(dest),
                                                              SP.cuadros(dest)))
            continue
        SP.aparta(dest, motivo)
        shutil.copyfile(nuevo, dest)
        SP.w('  %s  <- %s  (%d cuadros)' % (os.path.basename(dest), os.path.basename(nuevo),
                                            SP.cuadros(dest)))
    for c in pool:
        fp = c.GetClipProperty('File Path')
        destino = cambia.get(norm(fp), (fp, fp))[0]
        SP.w('  ReplaceClip %s -> %s: %s' % (os.path.basename(fp), os.path.basename(destino),
                                             c.ReplaceClip(destino)))
    despues = retrato(tl)
    # 30 oct: con normcase el nombre viejo salia en minusculas y la
    # comparacion fallaba aunque la linea no hubiera cambiado
    nombres = {os.path.basename(n): os.path.basename(v) for n, v in cambia.values()}
    despues_cmp = [x[:5] + (nombres.get(x[5], x[5]),) for x in despues]
    antes_cmp = [x[:5] + (os.path.basename(x[5]),) for x in antes]
    if sorted(antes_cmp) != sorted(despues_cmp):
        SP.w('LA LINEA CAMBIO: %s' % sorted(set(antes) ^ set(despues))[:10])
        sys.exit(1)
    SP.w('retrato identico antes y despues (%d clips)' % len(despues))
    pm.SaveProject()
    SP.w('LISTO')


if __name__ == '__main__':
    main()
