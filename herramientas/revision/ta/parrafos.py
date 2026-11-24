import re,sys,json
L=[l.rsplit('\t',1) for l in open('cuerpo.txt',encoding='utf-8').read().split('\n')]
def parrafos(a,b):
    out=[];cur=[];ini=a
    for i in range(a-1,b):
        t,pg=L[i] if len(L[i])==2 else (L[i][0],'')
        h=t.startswith('## ')
        t=t[3:] if h else t
        nuevo = h or re.match(r'^([●·•\-]|[a-hA-H]\.\s|[a-l]\)\s|\d+(\.\d+)*\.?\s|Veamos|Respuesta|Afirmación|Opción|Pregunta|ACTIVIDAD|REFLEXI|Objetivo|Conclusión|¿)',t) or (cur and re.search(r'[.:?!”"]\s*$',cur[-1]) )
        if nuevo and cur:
            out.append((ini,' '.join(cur),hh)); cur=[]
        if not cur: ini=i+1; hh=h
        cur.append(t.strip())
        if h: out.append((ini,' '.join(cur),True)); cur=[]
    if cur: out.append((ini,' '.join(cur),hh))
    return out
if __name__=='__main__':
    a,b=int(sys.argv[1]),int(sys.argv[2]); n=int(sys.argv[3]) if len(sys.argv)>3 else 110
    for ini,t,h in parrafos(a,b):
        w=len(t.split())
        print('%5d %s%s%s'%(ini,'## ' if h else '   ',t[:n],' …(%d)'%w if len(t)>n else ''))
