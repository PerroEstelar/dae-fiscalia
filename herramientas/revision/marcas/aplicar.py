# -*- coding: utf-8 -*-
"""Aplica las marcas de specs/<curso>_u*.py a los pantallazos de cap/<CURSO>/ y deja los marcados en marcados/<CURSO>/.
python3 aplicar.py DA [lección]"""
import glob, importlib.util, json, os, sys, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import marcas

AQUI = os.path.dirname(os.path.abspath(__file__))


def specs(cur):
    S = {}
    for f in sorted(glob.glob(os.path.join(AQUI, 'specs', '%s_u*.py' % cur.lower()))):
        sp = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
        m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
        S.update(m.S)
    return S


def main():
    cur = sys.argv[1]
    solo = sys.argv[2] if len(sys.argv) > 2 else None
    S = specs(cur)
    problemas = []
    for lec in sorted(S):
        if solo and lec != solo:
            continue
        dst = os.path.join(AQUI, 'marcados', cur, lec)
        os.makedirs(dst, exist_ok=True)
        pngs = sorted(glob.glob(os.path.join(AQUI, 'cap', cur, lec, '*.png')))
        if len(pngs) != len(S[lec]):
            problemas.append('%s: %d pantallazos y %d en specs' % (lec, len(pngs), len(S[lec])))
        for png in pngs:
            n = int(png[-6:-4])
            com, mk = S[lec].get(n, (None, []))
            if com is None:
                problemas.append('%s %02d sin comentario' % (lec, n))
            js = json.load(open(png[:-4] + '.json', encoding='utf-8'))
            out = os.path.join(dst, os.path.basename(png))
            if mk:
                falta = marcas.marcar(png, js, mk, out, semilla=n * 7 + len(lec))
                for f in falta:
                    problemas.append('%s %02d: no encontré %r' % (lec, n, f))
            else:
                shutil.copy(png, out)
    print('\n'.join(problemas) or 'sin problemas')


if __name__ == '__main__':
    main()
