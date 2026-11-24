import sys, glob
from PIL import Image, ImageDraw
pref = sys.argv[1]; out = sys.argv[2]
fs = sorted(glob.glob('/home/claude/ta/out/final/%s*_E*.png' % pref))
W, H = 556, 312
n = 12
for part in range(0, len(fs), n):
    sub = fs[part:part + n]
    c = Image.new('RGB', (W * 3, (H + 16) * ((len(sub) + 2) // 3)), 'white'); d = ImageDraw.Draw(c)
    for k, f in enumerate(sub):
        im = Image.open(f).resize((W, H)); x = (k % 3) * W; y = (k // 3) * (H + 16)
        c.paste(im, (x, y + 16)); d.text((x + 4, y + 2), f.split('/')[-1], fill='red')
    c.save('%s_%d.png' % (out, part // n))
    print('%s_%d.png' % (out, part // n))
