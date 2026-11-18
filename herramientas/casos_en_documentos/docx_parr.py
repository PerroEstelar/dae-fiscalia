# Parrafos de un .docx en orden de documento (cuerpo y celdas de tabla), con la pagina
# segun la ultima paginacion que guardo Word (w:lastRenderedPageBreak) y saltos manuales.
import zipfile,re,sys
from lxml import etree
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
def parrafos(path):
    z=zipfile.ZipFile(path)
    root=etree.fromstring(z.read('word/document.xml'))
    styles={}
    try:
        st=etree.fromstring(z.read('word/styles.xml'))
        for s in st.iter(W+'style'):
            n=s.find(W+'name')
            styles[s.get(W+'styleId')]=n.get(W+'val') if n is not None else s.get(W+'styleId')
    except KeyError: pass
    body=root.find(W+'body')
    pag=1; out=[]; nlr=0
    for p in body.iter(W+'p'):
        # texto y saltos dentro del parrafo, en orden
        txt=[]; pag_ini=None
        for el in p.iter():
            if el.tag==W+'lastRenderedPageBreak':
                pag+=1; nlr+=1
            elif el.tag==W+'br' and el.get(W+'type')=='page':
                pass  # Word ya deja lastRenderedPageBreak despues de un salto manual
            elif el.tag==W+'t':
                if pag_ini is None and (el.text or '').strip(): pag_ini=pag
                txt.append(el.text or '')
            elif el.tag==W+'tab': txt.append(' ')
            elif el.tag==W+'br': txt.append(' ')
        t=re.sub(r'\s+',' ',''.join(txt)).strip()
        ps=p.find(W+'pPr/'+W+'pStyle')
        est=styles.get(ps.get(W+'val'),'') if ps is not None else ''
        en_tabla=any(a.tag==W+'tc' for a in p.iterancestors())
        neg=False
        rs=[r for r in p.iter(W+'r') if ''.join(x.text or '' for x in r.iter(W+'t')).strip()]
        if rs and all(r.find(W+'rPr/'+W+'b') is not None and r.find(W+'rPr/'+W+'b').get(W+'val') not in ('0','false') for r in rs): neg=True
        out.append({'t':t,'pag':pag_ini or pag,'estilo':est,'tabla':en_tabla,'negrita':neg})
    return out,nlr
if __name__=='__main__':
    ps,nlr=parrafos(sys.argv[1])
    print('parrafos',len(ps),'con texto',sum(1 for p in ps if p['t']),'saltos Word',nlr,'paginas Word',ps[-1]['pag'])
    pat=sys.argv[2] if len(sys.argv)>2 else None
    if pat:
        for i,p in enumerate(ps):
            if re.search(pat,p['t'],re.I): print(i,p['pag'],p['estilo'][:18],'T' if p['tabla'] else '-','B' if p['negrita'] else '-',p['t'][:150])
