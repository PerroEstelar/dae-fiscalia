import pdfplumber, re
pdf=pdfplumber.open('ta_di.pdf')
out=[]
for pn,p in enumerate(pdf.pages):
    f=p.filter(lambda o: o.get('object_type')!='char' or 11.5<=o['size']<=12.5)
    words=f.extract_words(keep_blank_chars=True, use_text_flow=True, extra_attrs=['fontname'])
    # agrupar por renglón
    lines={}
    for w in words:
        k=round(w['top']/3)
        lines.setdefault(k,[]).append(w)
    for k in sorted(lines):
        ws=sorted(lines[k], key=lambda w:w['x0'])
        t=' '.join(w['text'].strip() for w in ws).strip()
        if not t: continue
        bold=sum(len(w['text']) for w in ws if 'Bold' in w['fontname'])
        tot=sum(len(w['text']) for w in ws)
        ita=sum(len(w['text']) for w in ws if 'Italic' in w['fontname'])
        pre='## ' if bold>0.6*tot else ''
        out.append('%s%s\t[p%d]'%(pre,t,pn+1))
open('cuerpo.txt','w').write('\n'.join(out))
print(len(out))
