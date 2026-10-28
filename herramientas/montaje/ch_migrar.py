# -*- coding: utf-8 -*-
r"""Profe Carlos Humberto, Unidad 1: los seis casos de «casos para talleres»
pasan a DAE MASTER. Se COPIA (nunca se mueve): D:\FISCALIA y los proyectos
INTRO CRIPTO y DAE quedan intactos.

    python ch_migrar.py arbol copiar      (fuera de Resolve)
    python ch_migrar.py importar          (con Resolve abierto en DAE MASTER - CURSOS)

arbol     E:\DAE MASTER\PRIORIDAD 1\PROFE CARLOS HUMBERTO\CASO 0N - nombre\ con
          las subcarpetas de la casa, y 00 DOCUMENTOS FUENTE.
copiar    cada archivo que usa la linea del caso (inventario.json de
          ch_inventario.py) a su subcarpeta por tipo; el V1 entregado a
          05 EXPORTS como referencia. Manifiesto en _tmp\ch\copias.json.
importar  el .drt de cada linea a un bin PRIORIDAD 1 > PROFE CARLOS HUMBERTO >
          CASO 0N > 10 TIMELINE SEBASTIAN, renombrada «CH U1 CASO 0N - nombre»,
          relinkeada a la copia; el caso 4, que ya no tiene linea (la de
          INTRO CRIPTO se volvio el caso 5), se arma con su V1 ProRes como
          base. .drt de cada una a 10 TIMELINE SEBASTIAN.
"""
import json
import os
import shutil
import sys
import time

TMP = r'D:\DAE\_tmp\ch'
RAIZ = r'E:\DAE MASTER\PRIORIDAD 1\PROFE CARLOS HUMBERTO'
SUBS = ['01 PLANOS', '02 CARTONES', '03 VOCES', '04 B-ROLL', '05 EXPORTS',
        '06 GUION Y STORYBOARD', '07 MOVIMIENTO', '08 MUSICA', '09 A LA VOZ',
        '10 TIMELINE SEBASTIAN']
FUENTE_D = r'D:\FISCALIA\UNIDAD 1\profe carlos humberto'
CASOS = {
    1: ('Santiago y Valeria', 'prfe calors Unidad 1 Caso 1 copy', None),
    2: ('Rodman', 'prfe calors Unidad 1 Caso 2 copy',
        FUENTE_D + r'\caso 2\Unidad 1 Caso 2 v1.mov'),
    3: ('Disney', 'prfe calors Unidad 1 Caso 3',
        FUENTE_D + r'\caso 3\PROFE CALROS HUMBERTO U1 VID3 V1.mov'),
    4: ('Arley y Susana', None, FUENTE_D + r'\caso 4\prfe calors Unidad 1 Caso 4.mov'),
    5: ('Juan', 'prfe calors Unidad 1 Caso 5',
        FUENTE_D + r'\caso 5\prfe calors Unidad 1 Caso 5.mov'),
    6: ('Lenin', 'caso 6',
        r'D:\DAE\unidad 1\profe carlos humberto\caso 6\exportados\UNIDAD 1 PROFE CARLOS HUMBERTO CASO 6 V1.mov'),
}
# el 4 no tiene linea: lo suyo que hay en disco se lleva entero
EXTRA = {4: [FUENTE_D + r'\caso 4']}
DOCS = [FUENTE_D + r'\casos para talleres.docx',
        FUENTE_D + r'\CONTEXTO_Proyecto_DAE_Casos_SRPA.md']


def w(*a):
    print(*a, flush=True)


def carpeta(n):
    return os.path.join(RAIZ, 'CASO %02d - %s' % (n, CASOS[n][0]))


def nombre_linea(n):
    return 'CH U1 CASO %02d - %s' % (n, CASOS[n][0])


def tipo(p):
    b = os.path.basename(p).lower()
    e = os.path.splitext(b)[1]
    if e in ('.mp3', '.wav', '.m4a', '.aac'):
        if 'elevenlabs' in b or 'voz en off' in b or 'narracion' in b:
            return '03 VOCES'
        return '08 MUSICA'
    if 'rotulo' in b or 'title' in b or 'voz off.mp4' in b or 'logo' in b:
        return '02 CARTONES'
    if b.startswith('magnific_') and e in ('.png', '.jpg', '.jpeg'):
        return '01 PLANOS'
    if b.startswith('magnific_') or b.endswith('_hold.mov') or b.startswith('kf'):
        return '07 MOVIMIENTO'
    if e in ('.png', '.jpg', '.jpeg') and ('kf' in b or 'lenin' in b):
        return '01 PLANOS'
    return '04 B-ROLL'


def arbol():
    os.makedirs(os.path.join(RAIZ, '00 DOCUMENTOS FUENTE'), exist_ok=True)
    for n in CASOS:
        for s in SUBS:
            os.makedirs(os.path.join(carpeta(n), s), exist_ok=True)
    w('arbol', RAIZ, sorted(os.listdir(RAIZ)))


def copia(src, dst, man):
    if os.path.exists(dst) and os.path.getsize(dst) == os.path.getsize(src):
        man.append([src, dst, 'ya'])
        return 0
    if os.path.exists(dst):
        b, e = os.path.splitext(dst)
        k = 2
        while os.path.exists('%s__%d%s' % (b, k, e)):
            k += 1
        dst = '%s__%d%s' % (b, k, e)
    shutil.copy2(src, dst)
    man.append([src, dst, 'copiado'])
    return os.path.getsize(src)


def copiar():
    inv = json.load(open(os.path.join(TMP, 'inventario.json'), encoding='utf-8'))
    man, falta = [], []
    total = 0
    for d in DOCS:
        if os.path.exists(d):
            total += copia(d, os.path.join(RAIZ, '00 DOCUMENTOS FUENTE', os.path.basename(d)), man)
    for n, (nom, linea, v1) in sorted(CASOS.items()):
        cc = carpeta(n)
        usados = set()
        if linea:
            for pista in inv[linea]['pistas'].values():
                for it in pista['items']:
                    if it['archivo']:
                        usados.add(it['archivo'])
        for d in EXTRA.get(n, []):
            for f in os.listdir(d):
                p = os.path.join(d, f)
                if os.path.isfile(p) and p != v1:
                    usados.add(p)
        nombres = {}
        for p in sorted(usados):
            if not os.path.exists(p):
                falta.append([n, p])
                continue
            b = os.path.basename(p)
            if b in nombres and nombres[b] != p:
                w('  OJO nombre repetido en el caso %d: %s' % (n, b))
            nombres[b] = p
            total += copia(p, os.path.join(cc, tipo(p), b), man)
        if v1 and os.path.exists(v1):
            e = os.path.splitext(v1)[1]
            total += copia(v1, os.path.join(cc, '05 EXPORTS',
                                            'CH U1 CASO %02d - V1 entregado%s' % (n, e)), man)
        w('caso %d  %s  %d archivos  (%d MB copiados hasta aqui)' % (n, nom, len(usados), total >> 20))
    json.dump({'copias': man, 'faltan': falta}, open(os.path.join(TMP, 'copias.json'), 'w',
                                                     encoding='utf-8'), ensure_ascii=False, indent=1)
    w('faltan', len(falta), falta[:10])


def _resolve():
    import DaVinciResolveScript as dvr
    return dvr.scriptapp('Resolve')


def bin_de(mp, partes):
    f = mp.GetRootFolder()
    for p in partes:
        h = None
        for x in f.GetSubFolderList():
            if x.GetName().strip() == p:
                h = x
        f = h or mp.AddSubFolder(f, p)
    return f


def importar():
    resolve = _resolve()
    pm = resolve.GetProjectManager()
    pr = pm.GetCurrentProject()
    assert pr.GetName() == 'DAE MASTER - CURSOS', pr.GetName()
    mp = pr.GetMediaPool()
    inv = json.load(open(os.path.join(TMP, 'inventario.json'), encoding='utf-8'))
    existentes = {pr.GetTimelineByIndex(i).GetName()
                  for i in range(1, int(pr.GetTimelineCount()) + 1)}
    for n, (nom, linea, v1) in sorted(CASOS.items()):
        cc = carpeta(n)
        nl = nombre_linea(n)
        if nl in existentes:
            w('ya existe', nl)
            continue
        rel = os.path.relpath(cc, r'E:\DAE MASTER').split(os.sep)
        b_tl = bin_de(mp, rel + ['10 TIMELINE SEBASTIAN'])
        b_media = bin_de(mp, rel + ['MEDIA V1'])
        if linea:
            drt = inv[linea]['drt']
            mp.SetCurrentFolder(b_media)
            tl = mp.ImportTimelineFromFile(drt, {'timelineName': nl, 'importSourceClips': True,
                                                 'sourceClipsPath': cc})
            if not tl:
                w('NO IMPORTO', nl)
                continue
            # la linea importada queda en el bin actual: se pasa al de timeline
            for c in b_media.GetClipList():
                if c.GetClipProperty('Type') == 'Timeline' and c.GetName() == nl:
                    mp.MoveClips([c], b_tl)
            clips = [c for c in b_media.GetClipList() if c.GetClipProperty('Type') != 'Timeline']
            ok = mp.RelinkClips(clips, cc) if clips else True
            w(nl, 'importada', 'clips', len(clips), 'relink', ok)
        else:
            mp.SetCurrentFolder(b_media)
            base = os.path.join(cc, '05 EXPORTS', 'CH U1 CASO %02d - V1 entregado.mov' % n)
            it = mp.ImportMedia([base])
            mp.SetCurrentFolder(b_tl)
            tl = mp.CreateEmptyTimeline(nl)
            pr.SetCurrentTimeline(tl)
            mp.AppendToTimeline([{'mediaPoolItem': it[0], 'startFrame': 0,
                                  'endFrame': int(it[0].GetClipProperty('Frames')),
                                  'trackIndex': 1, 'recordFrame': tl.GetStartFrame()}])
            w(nl, 'armada sobre el V1', it[0].GetClipProperty('Frames'))
        # .drt de la linea centralizada
        pr.SetCurrentTimeline(tl)
        dst = os.path.join(cc, '10 TIMELINE SEBASTIAN', nl + '.drt')
        if os.path.exists(dst):
            os.replace(dst, dst + '.%s.bak' % time.strftime('%H%M%S'))
        tl.Export(dst, resolve.EXPORT_DRT)
        w('   .drt', os.path.exists(dst))
    pm.SaveProject()


def verificar():
    resolve = _resolve()
    pr = resolve.GetProjectManager().GetCurrentProject()
    out = {}
    for i in range(1, int(pr.GetTimelineCount()) + 1):
        tl = pr.GetTimelineByIndex(i)
        if not tl.GetName().startswith('CH U1 CASO'):
            continue
        fuera, offline, n = set(), set(), 0
        for kind in ('video', 'audio'):
            for k in range(1, int(tl.GetTrackCount(kind) or 0) + 1):
                for it in tl.GetItemListInTrack(kind, k) or []:
                    m = it.GetMediaPoolItem()
                    if not m:
                        continue
                    p = m.GetClipProperty('File Path')
                    if not p:
                        continue
                    n += 1
                    if not p.startswith(RAIZ):
                        fuera.add(p)
                    if not os.path.exists(p):
                        offline.add(p)
        st = tl.GetStartFrame()
        out[tl.GetName()] = {'items_con_archivo': n, 'fuera_de_dae_master': sorted(fuera),
                             'sin_archivo': sorted(offline), 'largo': tl.GetEndFrame() - st}
        w(tl.GetName(), 'items', n, 'fuera', len(fuera), 'offline', len(offline))
    json.dump(out, open(os.path.join(TMP, 'verificar.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)


ORIGEN = {'prfe calors Unidad 1 Caso 1 copy': 1, 'prfe calors Unidad 1 Caso 2 copy': 2,
          'prfe calors Unidad 1 Caso 3': 3, 'prfe calors Unidad 1 Caso 5': 5, 'caso 6': 6}


def arreglar():
    """Despues de importar: ImportTimelineFromFile deja el nombre del .drt, la
    linea en el bin de media y los clips apuntando a D:\\FISCALIA (RelinkClips
    sobre la raiz del caso devolvio False). Aqui: renombra, pasa la linea a
    10 TIMELINE SEBASTIAN y relinkea CLIP POR CLIP a su copia en DAE MASTER
    segun el manifiesto de copiar (ReplaceClip si la copia quedo renombrada)."""
    resolve = _resolve()
    pr = resolve.GetProjectManager().GetCurrentProject()
    mp = pr.GetMediaPool()
    man = {}
    for src, dst, _ in json.load(open(os.path.join(TMP, 'copias.json'), encoding='utf-8'))['copias']:
        man[os.path.normcase(src)] = dst
    tls = {pr.GetTimelineByIndex(i).GetName(): pr.GetTimelineByIndex(i)
           for i in range(1, int(pr.GetTimelineCount()) + 1)}
    for viejo, n in ORIGEN.items():
        nl = nombre_linea(n)
        tl = tls.get(viejo) or tls.get(nl)
        if tl is None:
            w('no encuentro', viejo)
            continue
        if tl.GetName() != nl:
            tl.SetName(nl)
        rel = os.path.relpath(carpeta(n), r'E:\DAE MASTER').split(os.sep)
        b_tl = bin_de(mp, rel + ['10 TIMELINE SEBASTIAN'])
        b_media = bin_de(mp, rel + ['MEDIA V1'])
        for c in b_media.GetClipList():
            if c.GetClipProperty('Type') == 'Timeline':
                mp.MoveClips([c], b_tl)
        hechos, ya, sin = 0, 0, set()
        vistos = set()
        for kind in ('video', 'audio'):
            for k in range(1, int(tl.GetTrackCount(kind) or 0) + 1):
                for it in tl.GetItemListInTrack(kind, k) or []:
                    m = it.GetMediaPoolItem()
                    if not m:
                        continue
                    p = m.GetClipProperty('File Path') or ''
                    if not p or m.GetUniqueId() in vistos:
                        continue
                    vistos.add(m.GetUniqueId())
                    if p.startswith(RAIZ):
                        ya += 1
                        continue
                    dst = man.get(os.path.normcase(p))
                    if not dst:
                        sin.add(p)
                        continue
                    if os.path.basename(dst) == os.path.basename(p):
                        ok = mp.RelinkClips([m], os.path.dirname(dst))
                    else:
                        ok = m.ReplaceClip(dst)
                    if not (m.GetClipProperty('File Path') or '').startswith(RAIZ):
                        ok = m.ReplaceClip(dst)
                    hechos += 1 if (m.GetClipProperty('File Path') or '').startswith(RAIZ) else 0
        w('%s  relinkeados %d  ya estaban %d  sin copia %d %s'
          % (nl, hechos, ya, len(sin), sorted(sin)[:4]))
        pr.SetCurrentTimeline(tl)
        dst = os.path.join(carpeta(n), '10 TIMELINE SEBASTIAN', nl + '.drt')
        if os.path.exists(dst):
            os.replace(dst, dst + '.%s.bak' % time.strftime('%H%M%S'))
        tl.Export(dst, resolve.EXPORT_DRT)
    resolve.GetProjectManager().SaveProject()


PASOS = {'arbol': arbol, 'copiar': copiar, 'importar': importar, 'verificar': verificar,
         'arreglar': arreglar}

if __name__ == '__main__':
    for p in sys.argv[1:]:
        w('===', p)
        t0 = time.time()
        PASOS[p]()
        w('--- %s %.0f s' % (p, time.time() - t0))
    w('LISTO')
