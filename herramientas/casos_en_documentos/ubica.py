# Ubica textos en los documentos de los cursos: pagina y parrafo.
#  - .docx: parrafos reales del documento (docx_parr) + pagina tomada de la conversion a PDF (LibreOffice).
#  - .pdf : bloques de texto de pdftotext -bbox-layout, con su pagina exacta.
import json,re,os,subprocess,unicodedata,sys,html
sys.path.insert(0,'/home/claude/casos')
from docx_parr import parrafos
SRC='/home/claude/casos/src'; LO='/home/claude/casos/lo'
IDX=json.load(open(SRC+'/index.json'))
def norm(s):
    s=unicodedata.normalize('NFD',s.lower())
    return ''.join(c for c in s if c.isalnum() and unicodedata.category(c)!='Mn')
def paginas_pdf(pdf):
    n=int(re.search(r'Pages:\s+(\d+)',subprocess.run(['pdfinfo',pdf],capture_output=True,text=True).stdout).group(1))
    t=subprocess.run(['pdftotext','-raw',pdf,'-'],capture_output=True,text=True).stdout
    pp=t.split('\f')
    return pp[:n]
_cache={}
def carga_docx(fid):
    if fid in _cache: return _cache[fid]
    ps,_=parrafos('%s/%s.docx'%(SRC,fid))
    pdf='%s/%s.pdf'%(LO,fid)
    pp=[norm(x) for x in paginas_pdf(pdf)]
    full=''.join(pp); ofs=[]; a=0
    for x in pp: ofs.append(a); a+=len(x)
    def pag_de(pos):
        k=0
        for i,o in enumerate(ofs):
            if o<=pos: k=i
        return k+1
    pos=0; pag=1; sin=0
    out=[]
    for p in ps:
        if not p['t']: continue
        n=norm(p['t'])
        hit=-1
        if len(n)>=12:
            k=n[:60]
            win=20000 if len(k)>=40 else 8000 if len(k)>=24 else 2500
            hit=full.find(k,pos,pos+win)
            if hit<0 and len(k)>24:
                hit=full.find(n[:24],pos,pos+8000)
        if hit<0 and 4<=len(n)<12:
            h2=full.find(n,pos,pos+900)   # rotulos cortos («Situación A:»): justo despues del parrafo anterior
            if h2>=0: hit=h2
        pf=None
        if hit>=0:
            pag=pag_de(hit); pos=hit+min(len(n),8)
            if len(n)>=40:
                h3=full.find(n[-24:],hit,hit+len(n)+2500)
                if h3>=0: pf=pag_de(h3+23)
        else: sin+=1 if len(n)>=12 else 0
        out.append({'t':p['t'],'pag':pag,'pagf':pf or pag,'estilo':p['estilo'],'neg':p['negrita'],'ok':hit>=0})
    # ordinal dentro de la pagina; el trozo de un parrafo que viene de la pagina anterior cuenta como el primero
    cnt={}
    for p in out:
        cnt[p['pag']]=cnt.get(p['pag'],0)+1; p['n']=cnt[p['pag']]
        for q in range(p['pag']+1,p['pagf']+1): cnt[q]=cnt.get(q,0)+1
    _cache[fid]=(out,len(pp),sin)
    return _cache[fid]
def carga_pdf(pdf):
    """Parrafos de un PDF: lineas de pdftotext -bbox-layout unidas por interlineado.
    No cuentan el encabezado y el pie repetidos, los numeros de pagina ni los comentarios al margen."""
    if pdf in _cache: return _cache[pdf]
    x=subprocess.run(['pdftotext','-bbox-layout',pdf,'-'],capture_output=True,text=True).stdout
    pags=[]
    for m in re.finditer(r'<page width="([\d.]+)" height="([\d.]+)">(.*?)</page>',x,re.S):
        W_,H_=float(m.group(1)),float(m.group(2)); ls=[]
        for l in re.finditer(r'<line xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</line>',m.group(3),re.S):
            ws=re.findall(r'<word [^>]*>(.*?)</word>',l.group(5),re.S)
            t=html.unescape(' '.join(ws)).strip()
            if t: ls.append([float(l.group(1)),float(l.group(2)),float(l.group(3)),float(l.group(4)),t])
        pags.append((W_,H_,ls))
    npag=len(pags)
    # texto repetido en muchas paginas = encabezado o pie
    from collections import Counter
    c=Counter()
    for W_,H_,ls in pags:
        for k in set(norm(l[4])[:50] for l in ls): c[k]+=1
    rep=set(k for k,v in c.items() if v>=max(4,npag*0.2) and len(k)>=6)
    # columna principal: borde derecho del texto
    xs=sorted(l[2] for W_,H_,ls in pags for l in ls)
    xmin=sorted(l[0] for W_,H_,ls in pags for l in ls)
    Wp=pags[0][0] if pags else 600
    from collections import Counter as C2
    hist=C2(int(v/4) for v in xs)
    R=(max(hist,key=hist.get)+1)*4+2   # moda del borde derecho (texto justificado)
    out=[]; coms=[]
    for np_,(W_,H_,ls) in enumerate(pags,1):
        cuerpo=[]
        for l in ls:
            k=norm(l[4])[:50]
            if k in rep or re.fullmatch(r'[\d\s]+|p[aá]gina \d+( de \d+)?',l[4].lower()): continue
            if l[0]>R+3: coms.append((np_,l[1],l[4])); continue
            cuerpo.append(l)
        cuerpo.sort(key=lambda l:(round(l[1]/3),l[0]))
        # une lineas del mismo renglon (celdas de una fila quedan seguidas)
        gaps=[b_[1]-a_[3] for a_,b_ in zip(cuerpo,cuerpo[1:]) if 0<=b_[1]-a_[3]<14]
        med=sorted(gaps)[len(gaps)//2] if gaps else 2.0
        par=[];n=0
        def cierra():
            nonlocal par,n
            if par:
                n+=1; out.append({'t':' '.join(p_[4] for p_ in par),'pag':np_,'n':n,'estilo':'','neg':False,'ok':True,'y':par[0][1]})
                par=[]
        for l in cuerpo:
            if par:
                ant=par[-1]; gap=l[1]-ant[3]; alto=ant[3]-ant[1]
                corta=ant[2]<R-0.10*(R-60)
                ini=l[4][:1]
                nuevo=(gap>med+2.6) or (gap<-alto*0.5) or (corta and (ini.isupper() or ini.isdigit() or ini in '¿¡«"“(•-–—*[') ) or re.match(r'^(\d+[.)]|[a-zA-Z][.)]|[•\-–—*]|Pregunta \d|Opci[oó]n [A-D])\s',l[4]) is not None
                if nuevo: cierra()
            par.append(l)
        cierra()
    _cache[pdf]=(out,npag,0); _cache[pdf+'#com']=coms
    return _cache[pdf]
ROT=re.compile(r'^(lecci[oó]n|unidad|actividad|tipo de estrategia|fase|caso|recurso|estudio|momento|tema|ejercicio|taller|video|gui[oó]n|situaci[oó]n|animaci[oó]n|expediente|experiencia|actividades|reto|an[aá]lisis|contexto|consigna|estrategia|nombre|objetivo|descripci[oó]n|foro|quiz|cuestionario|evaluaci[oó]n|veamos|ejemplo|introducci[oó]n|cierre|pregunta)',re.I)
def busca(pars,clave,desde=0):
    k=norm(clave); r=[]
    for i,p in enumerate(pars):
        if i<desde: continue
        if k in norm(p['t']): r.append(i)
    return r
def rotulos(pars,i,atras=120,cuantos=7,largo=110):
    r=[]
    for j in range(i-1,max(-1,i-atras),-1):
        p=pars[j]; t=p['t']
        if p['estilo'].lower().startswith(('heading','title','título','titulo')) or ROT.match(t) and len(t)<200 or (p['neg'] and len(t)<120):
            r.append('[%d p%d]%s %s'%(j,p['pag'],'H' if p['estilo'] else '',t[:largo]))
            if len(r)>=cuantos: break
    return r[::-1]
def ver(pars,i,antes=0,despues=0,largo=140):
    for j in range(max(0,i-antes),min(len(pars),i+despues+1)):
        p=pars[j]; print('  %s[%d] p%d n%d %s'%('>' if j==i else ' ',j,p['pag'],p['n'],p['t'][:largo]))
