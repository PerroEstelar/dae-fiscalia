import sys,json,os
sys.path.insert(0,'/home/claude/casos')
import ubica
A=json.load(open('/home/claude/casos/anclas.json'))
def carga(fid):
    f=ubica.IDX[fid]['files']
    if '.docx' in f: return ubica.carga_docx(fid)[0]
    return ubica.carga_pdf(f['.pdf'])[0]
def corrido(pars):
    # texto normalizado corrido con el indice de parrafo de cada caracter
    s=[];own=[]
    for i,p in enumerate(pars):
        n=ubica.norm(p['t']); s.append(n); own.extend([i]*len(n))
    return ''.join(s),own
_c={}
def halla_txt(fid,texto,desde_fin=False,minimo=18):
    if fid not in _c:
        pars=carga(fid); _c[fid]=(pars,)+corrido(pars)
    pars,full,own=_c[fid]
    n=ubica.norm(texto)
    for L in (60,45,32,24,minimo):
        k=n[-L:] if desde_fin else n[:L]
        if len(k)<minimo: continue
        hits=[];a=0
        while True:
            h=full.find(k,a)
            if h<0: break
            hits.append(own[h+len(k)-1] if desde_fin else own[h]); a=h+1
        if hits: return hits,L
    return [],0
def informe(clave,fids,rot=5,ver=True):
    a=A[clave]; out=[]
    for fid in fids:
        hi,L=halla_txt(fid,a['ini'])
        if not hi: continue
        pars=_c[fid][0]
        hf,Lf=halla_txt(fid,a['fin'],True)
        for i in hi:
            fin=[j for j in hf if j>=i]
            j=fin[0] if fin else None
            out.append((fid,i,j,L,Lf))
            if ver:
                p=pars[i]
                print('== %s  doc %s  ini[%d] p%d n%d (L%d) | fin %s'%(clave,ubica.IDX[fid]['title'][:28],i,p['pag'],p['n'],L,('[%d] p%d (L%d)'%(j,pars[j]['pag'],Lf)) if j is not None else 'NO'))
                for r in ubica.rotulos(pars,i,cuantos=rot): print('     ',r)
                print('      >',p['t'][:150])
    if not out and ver: print('== %s  NO HALLADO en %d docs'%(clave,len(fids)))
    return out

import re
def ficha(pars,i):
    d={}
    def atras(rx,maxlen=200,lim=400,cond=None):
        for j in range(i-1,max(-1,i-lim),-1):
            t=pars[j]['t']
            if len(t)<=maxlen and rx.search(t) and (cond is None or cond(pars[j])): return j
        return None
    j=atras(re.compile(r'^\d+(\.\d+)+\.?\s+\S'),160,2000); d['num']=(j,pars[j]['t']) if j is not None else None
    j=atras(re.compile(r'^Lecci[oó]n\s+\d+',re.I),220,2000); d['leccion']=(j,pars[j]['t']) if j is not None else None
    j=atras(re.compile(r'^(Primer|Segundo|Tercer|Cuarto|Quinto|Sexto|S[eé]ptimo|Octavo)\s+tema|^Tema\s+\d',re.I),220,1500); d['tema']=(j,pars[j]['t']) if j is not None else None
    j=atras(re.compile(r'^Actividad(es)?\b',re.I),220,400); d['actividad']=(j,pars[j]['t']) if j is not None else None
    j=atras(re.compile(r'^Tipo de estrategia',re.I),600,400)
    if j is not None:
        t=pars[j]['t']
        if len(t)<28 and j+1<len(pars): t=t+': '+pars[j+1]['t']
        d['estrategia']=(j,t[:260])
    j=atras(re.compile(r'^(Fase|Momento|Prop[oó]sito pedag[oó]gico|Tipo de actividad)\b|experiencia concreta',re.I),160,120); d['fase']=(j,pars[j]['t']) if j is not None else None
    j=atras(re.compile(r'video|animad|imagen|infograf|interactiv|h5p|ilustraci',re.I),260,60); d['recurso']=(j,pars[j]['t']) if j is not None else None
    rot=[]
    for j in range(i-1,max(-1,i-7),-1):
        t=pars[j]['t']
        if len(t)<130 and not t.startswith('___'): rot.append((j,t))
        else: break
    d['rot']=rot[::-1]
    return d
def linea(clave,fids):
    r=informe(clave,fids,ver=False)
    if not r: return '%-9s NO'%clave
    s=[]
    for fid,i,j,L,Lf in r:
        pars=_c[fid][0]
        s.append('%s [%d]p%d n%d L%d fin %s'%(ubica.IDX[fid]['title'][:10].strip(),i,pars[i]['pag'],pars[i]['n'],L,('[%d]p%d'%(j,pars[j]['pag'])) if j is not None else 'NO'))
    return '%-9s %s'%(clave,' || '.join(s))

def detalle(clave,fids,minL=45,largo=100):
    r=[x for x in informe(clave,fids,ver=False) if x[3]>=minL]
    if not r: print('## %s SIN COINCIDENCIA FIRME'%clave); return
    for fid,i,j,L,Lf in r:
        pars=_c[fid][0]; f=ficha(pars,i)
        print('## %s | %s | ini[%d] p%d n%d | fin %s'%(clave,ubica.IDX[fid]['title'][:22],i,pars[i]['pag'],pars[i]['n'],('[%d] p%d n%d'%(j,pars[j]['pag'],pars[j]['n'])) if j is not None else 'NO'))
        for k in ('num','leccion','tema','actividad','estrategia','fase','recurso'):
            v=f.get(k)
            if v: print('   %-10s [%d] %s'%(k,v[0],v[1][:largo]))
        print('   rot        '+' ¦ '.join('[%d] %s'%(a,b[:70]) for a,b in f['rot']))
        print('   ini> '+pars[i]['t'][:90])

def claves(fids,patron,maxn=8,largo=120,ctx=0):
    rx=re.compile(patron,re.I)
    for fid in fids:
        pars=carga(fid); n=0
        for i,p in enumerate(pars):
            if rx.search(p['t']):
                n+=1
                if n<=maxn:
                    print('%s [%d] p%d n%d %s'%(ubica.IDX[fid]['title'][:9].strip(),i,p['pag'],p['n'],p['t'][:largo]))
                    for j in range(i+1,min(len(pars),i+1+ctx)): print('        +[%d] %s'%(j,pars[j]['t'][:largo]))
        if n>maxn: print('   … %d más en %s'%(n-maxn,ubica.IDX[fid]['title'][:9]))
