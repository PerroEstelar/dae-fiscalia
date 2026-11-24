# -*- coding: utf-8 -*-
"""Genially nativo de Derecho de petición revisado: el mismo armado de TA (herramientas/revision/ta/genially_ta.py),
con las escenas revisadas de cada lección.

python3 genially_dp.py  ->  en out/sitio/derecho-peticion/genially/: lUL.json (copyBuffer del editor) y carga.html
Nombres de los Geniallys: «DP · U1 L1 · …», sin el «… Y DAÑO ANTIJURÍDICO» que pedía corregir la revisión.
"""
import glob, json, os, random, re, sys
sys.path.insert(0, '/home/claude/dp2')
sys.path.insert(0, '/home/claude/ta')
from base import RE
from nucleo import OUT, BASE_URL
_cwd = os.getcwd(); os.chdir('/home/claude/ta')
import genially_ta as G
os.chdir(_cwd)

G.M.CURSO = 'Derecho de petición y acción de tutela'
G.M.UNIDADES = {1: 'Derecho de petición: fundamentos, modalidades y términos',
                2: 'Gestión y respuesta del derecho de petición',
                3: 'Acción de tutela: fundamentos y procedencia',
                4: 'Gestión, cumplimiento y seguimiento de la acción de tutela'}
_entradas_ta = G.entradas_indice


def entradas_indice(escenas):
    """Índice de hasta 11 filas: de los casos con dos pantallas («Caso N. …» + «Caso N. Actuaciones…») va la primera;
    si aún sobran, salen primero las de contexto («Problema jurídico…», «Implicaciones…»), no las de contenido."""
    tit = [e['titulo_genially'] for e in escenas]
    if len(tit) <= 11:
        return _entradas_ta(escenas)
    vistos, idx = set(), []
    for i, x in enumerate(tit):
        m = re.match(r'^(Caso \d+)\. ', x)
        if m and m.group(1) in vistos:
            continue
        if m:
            vistos.add(m.group(1))
        idx.append(i)
    for pat in (r'^Problema jurídico', r'^Implicaciones'):
        if len(idx) > 11:
            idx = [i for i in idx if not re.match(pat, tit[i])]
    if len(idx) > 11:
        return [(lab, idx[j]) for lab, j in _entradas_ta([escenas[i] for i in idx])]   # muestra pareja del resto
    return [(tit[i], i) for i in idx]


G.entradas_indice = entradas_indice
CARGA = G.CARGA.replace("tipo: 'ta-genially'", "tipo: 'dp-genially'")


def main():
    random.seed(20261124)
    dst = OUT + 'genially/'
    os.makedirs(dst, exist_ok=True)
    resumen = []
    for idx in sorted(glob.glob(OUT + 'unidad-0*/leccion-0*/index.html')):
        d = json.loads(RE.search(open(idx, encoding='utf-8').read()).group(2))
        u, l = d['unit'], d['lesson']
        k = '%d.%d' % (u, l)
        buf, meta, esc = G.leccion(k, esc=d['scenes'], heading=d['heading'], base=BASE_URL, sigla='DP')
        t = meta['titulo_genially']
        meta['titulo_genially'] = t if len(t) <= 70 else t[:69].rstrip(' ,;·') + '…'
        json.dump(buf, open(dst + 'l%d%d.json' % (u, l), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
        resumen.append(meta)
        print(k, meta['diapositivas'], 'diapositivas ·', meta['titulo_genially'], '·', ' | '.join(meta['indice']))
    open(dst + 'carga.html', 'w', encoding='utf-8').write(CARGA)
    json.dump(resumen, open(dst + 'lecciones.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
