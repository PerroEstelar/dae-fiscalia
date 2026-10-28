import sys; sys.path.insert(0,'.')
import v2audio as A, numpy as np, soundfile as sf
from scipy.signal import fftconvolve
SR=48000
mix=A.leer(A.U+'stems/CH_U1_C04_v1mix.flac').astype(np.float64)
nar=A.leer_mp3(A.U+'stems/CH_U1_C04_narracion_v1.mp3').astype(np.float64)[:,0]
def refina(t_mix, off, win=1.5):
    a=A.s(t_mix); w=mix[a:a+A.s(win)].mean(1)
    b=A.s(t_mix-off)  # nar index estimate (off = mix - nar)
    seg=nar[b-2400:b+A.s(win)+2400]
    c=fftconvolve(seg, w[::-1], mode='valid'); k=int(np.argmax(c))
    return (t_mix - (b-2400+k)/SR)
o1=np.median([refina(t,12.480) for t in (15,20,25,30)]); o2=np.median([refina(t,11.771) for t in (40,55,70,80)])
print('offsets', o1, o2)
# cut point: find where segment-2 fits better, between mix 30 and 34
def err(t, off):
    a=A.s(t); w=mix[a:a+A.s(0.05)].mean(1); b=A.s(t-off); n=nar[b:b+len(w)]
    g=(w*n).sum()/((n*n).sum()+1e-12); return ((w-g*n)**2).sum()/((w*w).sum()+1e-12)
for t in np.arange(31.0,34.0,0.1):
    print('%.1f e1 %.3f e2 %.3f'%(t,err(t,o1),err(t,o2)))
cut=33.85
voz=np.zeros_like(mix)
for (a,b,off) in ((12.0,cut,o1),(cut,len(mix)/SR,o2)):
    i,j=A.s(a),A.s(b)
    idx=np.arange(i,j)-int(round(off*SR))
    ok=(idx>=0)&(idx<len(nar))
    n=np.zeros(j-i); n[ok]=nar[idx[ok]]
    for ch in (0,1):
        y=mix[i:j,ch]; g=(y*n).sum()/((n*n).sum()+1e-12)
        voz[i:j,ch]=g*n
        print('seg %.2f-%.2f ch%d gain %.4f (%.2f dB)'%(a,b,ch,g,20*np.log10(abs(g))))
fondo=mix-voz
def lv(y,a,b): return 20*np.log10(np.sqrt((y[A.s(a):A.s(b)]**2).mean())+1e-12)
for a in range(0,99,3):
    print('%3d mix %.1f voz %.1f fondo %.1f'%(a,lv(mix,a,a+3),lv(voz,a,a+3),lv(fondo,a,a+3)))
sf.write('out/CH_U1_C04_voz_v1sep.flac',voz.astype(np.float32),SR,subtype='PCM_24')
sf.write('out/CH_U1_C04_fondo_v1sep.flac',fondo.astype(np.float32),SR,subtype='PCM_24')
