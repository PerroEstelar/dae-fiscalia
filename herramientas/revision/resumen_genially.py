"""Resumen por diapositiva de un Genially (JSON de view.genially.com/api/view/<id>)."""
import json, re, sys
d = json.load(open(sys.argv[1]))
S = sorted(d['Slides'], key=lambda s: float(s['BigOrder']))
slide_name = {s['Id']: s['Name'] for s in S}
def px(v):
    try: return round(float(str(v).replace('px', '')))
    except: return v
def texto(t):
    c = t.get('Content') or {}
    out = []
    def rec(n, depth=0):
        if n.get('type') == 'text': out.append(n.get('text', ''))
        for ch in n.get('content', []) or []: rec(ch, depth+1)
        if n.get('type') in ('paragraph', 'heading', 'listItem'): out.append('\n')
    rec(c)
    s = ''.join(out).strip()
    if not s:
        s = re.sub('<[^>]+>', ' ', t.get('TextMessage', '')).strip()
    return re.sub(r'\n+', ' / ', s)
ia = d['interactivityActions']
def inter(el):
    r = []
    for ev, ref in (el.get('interactivities') or {}).items():
        a = ia.get(ref, {})
        tgt = a.get('target', {})
        if a.get('type') == 'goToSlide':
            t = tgt.get('smartLink') or slide_name.get(tgt.get('slideId'), tgt)
        else:
            t = json.dumps(tgt, ensure_ascii=False)[:120]
        r.append('%s:%s→%s' % (ev, a.get('type'), t))
    return ' '.join(r)
kinds = ['Texts', 'Images', 'Groups', 'RichContents', 'Svgs', 'Audios', 'Videos']
by = {}
for k in kinds:
    for e in d.get(k, []):
        by.setdefault(e['IdSlide'], []).append((k, e))
only = sys.argv[2] if len(sys.argv) > 2 else None
for s in S:
    if only and only not in s['Name']: continue
    print('=' * 100)
    print('SLIDE %s  %s  %s%s' % (s['BigOrder'], s['Name'], 'POPUP ' if s.get('Popup') else '', 'HIDDEN' if s.get('Hidden') else ''))
    els = sorted(by.get(s['Id'], []), key=lambda x: x[1].get('BigZIndex', x[1].get('ZIndex', 0)))
    for k, e in els:
        pos = e.get('Position', {}); sz = e.get('Size', {})
        g = ' g' if e.get('IdGroup') else ''
        hid = ' HIDDEN' if e.get('IsHidden') else ''
        base = '%-5s %-22s (%4s,%4s %4sx%-4s)%s%s %s' % (k[:5], (e.get('Name') or '')[:22], px(pos.get('PositionLeft')), px(pos.get('PositionTop')), px(sz.get('Width')), px(sz.get('Height')), g, hid, inter(e))
        if k == 'Texts':
            base += ' [%s %s] «%s»' % (e.get('FontSize'), e.get('FontFamily'), texto(e)[:400])
        elif k == 'RichContents':
            m = re.search(r'src="([^"]+)"', e.get('Source', ''))
            base += ' IFRAME ' + (m.group(1) if m else e.get('Source', '')[:200])
        elif k == 'Images':
            base += ' ' + e.get('Source', '')[-60:]
        elif k in ('Audios', 'Videos'):
            base += ' ' + json.dumps({kk: e.get(kk) for kk in ('Source', 'Url', 'url')}, ensure_ascii=False)[:200]
        print('   ' + base)
