# -*- coding: utf-8 -*-
"""Sitio publicable de Terminaciones anticipadas (GitHub Pages) para embeber escena por escena en Genially.

python3 sitio.py  ->  publica las 13 lecciones con el motor, arma out/sitio/ (sin los .mp4: esos los pone el equipo)
y escribe out/sitio_videos.json (qué video va en qué unidad) y out/genially_plan.json (título y URL de cada diapositiva).
"""
import importlib, json, os, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import maqueta as M

BASE = 'https://zwaard88-source.github.io/prueba-terminaciones-anticipadas/'
LECC = ['1.1', '1.2', '1.3', '2.1', '2.2', '3.1', '3.2', '3.3', '3.4', '4.1', '4.2', '4.3', '4.4']
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out')


def main():
    videos, plan = {}, []
    for k in LECC:
        u, l = map(int, k.split('.'))
        mod = importlib.import_module('lecciones.l%d%d' % (u, l))
        M.publicar(u, l, mod.ESCENAS)
        url = BASE + 'unidad-%02d/leccion-%02d/' % (u, l)
        diap = []
        for n, e in enumerate(mod.ESCENAS, 1):
            if e.get('video'):
                videos.setdefault('unidad-%02d' % u, []).append(os.path.basename(e['video']['src'])[:-4])
            diap.append({'n': n, 'titulo': e['titulo_genially'], 'url': url + '?escena=%d' % n})
        plan.append({'leccion': k, 'heading': M.HEADINGS[k], 'unidad': u, 'nombre_unidad': M.UNIDADES[u], 'url': url, 'diapositivas': diap})
    dst = os.path.join(OUT, 'sitio')
    if os.path.isdir(dst):
        shutil.move(dst, os.path.join(OUT, '_descartes', 'sitio_%d' % len(os.listdir(os.path.join(OUT, '_descartes')))))
    shutil.copytree(M.TA, dst)
    # Portada del sitio: índice de lecciones (para revisar sin Genially)
    filas = ''.join('<li><a href="unidad-%02d/leccion-%02d/">%s</a> <small>(%d escenas)</small></li>' % (p['unidad'], int(p['leccion'][2]), p['heading'], len(p['diapositivas'])) for p in plan)
    open(os.path.join(dst, 'index.html'), 'w', encoding='utf-8').write(
        '<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>Terminaciones anticipadas · mediaciones</title><style>body{font:16px/1.5 Arial,sans-serif;max-width:760px;margin:40px auto;padding:0 16px;color:#002F46;background:#fff}'
        'h1{font-size:22px}a{color:#002F46}small{color:#666}</style><h1>%s</h1><p>Mediaciones del curso (una por lección). En Genially cada diapositiva embebe una escena con <code>?escena=N</code>.</p><ol>%s</ol></html>' % (M.CURSO, filas))
    open(os.path.join(dst, '.nojekyll'), 'w').write('')
    json.dump({u: sorted(set(v)) for u, v in videos.items()}, open(os.path.join(OUT, 'sitio_videos.json'), 'w'), indent=1)
    json.dump(plan, open(os.path.join(OUT, 'genially_plan.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(json.dumps({u: sorted(set(v)) for u, v in videos.items()}))
    print(sum(len(p['diapositivas']) for p in plan), 'diapositivas')


if __name__ == '__main__':
    main()
