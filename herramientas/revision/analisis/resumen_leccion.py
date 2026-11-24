import json, sys
r = json.load(open('/tmp/claude-0/rev/escenas.json', encoding='utf-8'))
for ll in sys.argv[1:]:
    L = r[ll]
    print('##', ll, L['heading'] if isinstance(L['heading'], str) else '')
    for e in L['escenas']:
        sc = ['%d/%d' % (s[1], s[2]) for s in e['scroll']]
        its = '; '.join('%s(%d)' % ((it['label'] or '')[:38], it['palabras']) for it in e['items'])
        print(' E%02d %-9s %3dp %s | %s | scroll %s%s' % (e['n'], e['layout'], e['palabras'], (e['titulo'] or '')[:60],
              e['mediacion'][:70], sc or '-', ' | AUDIO' if e['audio'] else ''))
        if its: print('      items:', its[:300])
