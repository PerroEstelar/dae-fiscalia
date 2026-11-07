import sys, os
H = r'D:\DAE\_repo\herramientas'
for sub in ('montaje', 'prompts', os.path.join('voz', 'textos')):
    sys.path.insert(0, os.path.join(H, sub))
import rutas_da as R
from PIL import Image
V = sys.argv[1]
E = __import__('escenas_da_' + V.lower())
sal = os.path.join(r'D:\DAE\_tmp\da\up\kling', V)
os.makedirs(sal, exist_ok=True)
g = os.path.join(R.sub(V, '01 PLANOS'), '_grade')
for n in sorted(E.KLING):
    nom = 'DA_%s_r%02d_%s' % (V, n, E.NOMBRE[n])
    p = os.path.join(g, nom + '.png')
    if not os.path.exists(p):
        print('FALTA', nom); continue
    im = Image.open(p).convert('RGB')
    if im.width > 2048:
        im = im.resize((2048, int(im.height * 2048 / im.width)), Image.LANCZOS)
    im.save(os.path.join(sal, nom + '.jpg'), 'JPEG', quality=93)
    print('ok', nom, os.path.getsize(os.path.join(sal, nom + '.jpg')))
