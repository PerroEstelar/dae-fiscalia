# -*- coding: utf-8 -*-
"""Pantallazos de cada diapositiva de los Genially que nos enviaron (vista pública, tal como están hoy).
Chrome sin ventana con DevTools (perfil aparte, sin la sesión de nadie): abre view.genially.com/<id>, captura, pasa con la
flecha derecha y captura otra vez. Junto a cada PNG deja un JSON con las cajas de texto e imágenes visibles (también las de
los iframes de las escenas), para ubicar después las marcas de revisión.

python pantallazos.py config.json            (lanzar suelto: escribe pantallazos.log)
python pantallazos.py config.json sonda      (una lección, dos diapositivas, vuelca el DOM para estudiar la vista)
config: {"salida": "D:\\...", "cursos": [{"curso": "DA", "lecciones": [["U1 L1", "<id>", <n visibles>], ...]}]}
"""
import base64, hashlib, json, os, socket, struct, subprocess, sys, time, urllib.request, glob

AQUI = os.path.dirname(os.path.abspath(__file__))
LOG = open(os.path.join(AQUI, 'pantallazos_%s.log' % os.path.splitext(os.path.basename(sys.argv[1]))[0]), 'a', encoding='utf-8')


def log(*a):
    LOG.write(time.strftime('%H:%M:%S ') + ' '.join(str(x) for x in a) + '\n')
    LOG.flush()


class WS:
    """Cliente WebSocket mínimo (solo texto) para el protocolo de DevTools; guarda los eventos de contextos."""

    def __init__(self, url):
        hp, _, path = url[5:].partition('/')
        host, _, port = hp.partition(':')
        self.s = socket.create_connection((host, int(port or 80)), timeout=90)
        key = base64.b64encode(os.urandom(16)).decode()
        req = ('GET /%s HTTP/1.1\r\nHost: %s\r\nUpgrade: websocket\r\nConnection: Upgrade\r\n'
               'Sec-WebSocket-Key: %s\r\nSec-WebSocket-Version: 13\r\n\r\n') % (path, hp, key)
        self.s.sendall(req.encode())
        resp = b''
        while b'\r\n\r\n' not in resp:
            resp += self.s.recv(4096)
        self.buf = resp.split(b'\r\n\r\n', 1)[1]
        self.n = 0
        self.ctx = {}          # frameId -> contextId (mundo por defecto)

    def _leer(self, k):
        while len(self.buf) < k:
            d = self.s.recv(1 << 20)
            if not d:
                raise IOError('conexión cerrada')
            self.buf += d
        out, self.buf = self.buf[:k], self.buf[k:]
        return out

    def enviar(self, texto):
        data = texto.encode('utf-8')
        cab = bytearray([0x81])
        n = len(data)
        if n < 126:
            cab.append(0x80 | n)
        elif n < 65536:
            cab.append(0x80 | 126); cab += struct.pack('>H', n)
        else:
            cab.append(0x80 | 127); cab += struct.pack('>Q', n)
        m = os.urandom(4)
        cab += m
        self.s.sendall(bytes(cab) + bytes(b ^ m[i % 4] for i, b in enumerate(data)))

    def recibir(self):
        partes = []
        while True:
            b1, b2 = self._leer(2)
            fin, op = b1 & 0x80, b1 & 0x0F
            n = b2 & 0x7F
            if n == 126:
                n = struct.unpack('>H', self._leer(2))[0]
            elif n == 127:
                n = struct.unpack('>Q', self._leer(8))[0]
            data = self._leer(n)
            if op == 9:
                continue
            partes.append(data)
            if fin:
                return b''.join(partes).decode('utf-8', 'replace')

    def evento(self, r):
        m = r.get('method')
        if m == 'Runtime.executionContextCreated':
            c = r['params']['context']
            a = c.get('auxData') or {}
            if a.get('isDefault') and a.get('frameId'):
                self.ctx[a['frameId']] = c['id']
        elif m == 'Runtime.executionContextDestroyed':
            i = r['params'].get('executionContextId')
            for k in [k for k, v in self.ctx.items() if v == i]:
                del self.ctx[k]
        elif m == 'Runtime.executionContextsCleared':
            self.ctx.clear()

    def cmd(self, metodo, **params):
        self.n += 1
        mid = self.n
        self.enviar(json.dumps({'id': mid, 'method': metodo, 'params': params}))
        while True:
            r = json.loads(self.recibir())
            if r.get('id') == mid:
                if 'error' in r:
                    raise RuntimeError(r['error'])
                return r.get('result', {})
            self.evento(r)

    def vaciar(self, seg=0.3):
        """Lee los eventos pendientes sin mandar nada."""
        self.s.settimeout(seg)
        try:
            while True:
                self.evento(json.loads(self.recibir()))
        except (socket.timeout, TimeoutError):
            pass
        finally:
            self.s.settimeout(90)


CAJAS = r'''(() => {
  const W = innerWidth, H = innerHeight, out = [], im = [];
  const vis = el => { for (let a = el; a && a.nodeType === 1; a = a.parentElement) { const s = getComputedStyle(a);
      if (s.visibility === 'hidden' || s.display === 'none' || +s.opacity < 0.05) return false; } return true; };
  const dentro = b => b.width > 1 && b.height > 1 && b.right > 0 && b.bottom > 0 && b.left < W && b.top < H;
  const raiz = document.body || document.documentElement;
  const tw = document.createTreeWalker(raiz, NodeFilter.SHOW_TEXT);
  let n; const vistos = new Set();
  while ((n = tw.nextNode())) {
    const t = n.textContent.replace(/\s+/g, ' ').trim(); if (t.length < 2) continue;
    const el = n.parentElement; if (!el || vistos.has(el) || /^(SCRIPT|STYLE|NOSCRIPT)$/.test(el.tagName)) continue; vistos.add(el);
    const rg = document.createRange(); rg.selectNodeContents(n); const b = rg.getBoundingClientRect();
    if (!dentro(b) || !vis(el)) continue;
    out.push({t: t.slice(0, 220), x: Math.round(b.left), y: Math.round(b.top), w: Math.round(b.width), h: Math.round(b.height),
              fs: Math.round(parseFloat(getComputedStyle(el).fontSize) * 10) / 10});
    if (out.length > 500) break;
  }
  document.querySelectorAll('img,svg,video,iframe,canvas,button,[role=button]').forEach(e => {
    const b = e.getBoundingClientRect();
    if (b.width > 24 && b.height > 18 && dentro(b) && vis(e) && !(e.tagName === 'svg' && e.closest('svg') !== e))
      im.push({k: e.tagName.toLowerCase(), x: Math.round(b.left), y: Math.round(b.top), w: Math.round(b.width), h: Math.round(b.height),
               src: (e.src || e.getAttribute('href') || '').toString().slice(0, 160)});
  });
  return JSON.stringify({w: W, h: H, url: location.href.slice(0, 240), t: out, im: im.slice(0, 120)});
})()'''

SONDA = r'''(() => {
  const r = [];
  document.querySelectorAll('*').forEach(e => {
    const at = [...e.attributes].map(a => a.name + '=' + a.value.slice(0, 60)).join(' ');
    if (/slide|page|scene/i.test(at)) r.push(e.tagName + ' ' + at.slice(0, 300));
  });
  return JSON.stringify({title: document.title, url: location.href, n: r.length, attrs: r.slice(0, 80),
                         iframes: [...document.querySelectorAll('iframe')].map(f => [f.src.slice(0, 150), JSON.stringify(f.getBoundingClientRect())]).slice(0, 30)});
})()'''


def chrome(puerto=9333):
    exe = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    perfil = os.path.join(AQUI, 'perfil_chrome_%d' % puerto)
    p = subprocess.Popen([exe, '--headless=new', '--remote-debugging-port=%d' % puerto, '--user-data-dir=' + perfil,
                          '--window-size=1280,720', '--hide-scrollbars', '--mute-audio', '--no-first-run',
                          '--disable-features=IsolateOrigins,site-per-process', '--disable-site-isolation-trials',
                          '--autoplay-policy=user-gesture-required', 'about:blank'])
    for _ in range(60):
        try:
            lst = json.load(urllib.request.urlopen('http://127.0.0.1:%d/json/list' % puerto, timeout=2))
            pg = [x for x in lst if x.get('type') == 'page']
            if pg:
                return p, pg[0]['webSocketDebuggerUrl']
        except Exception:
            pass
        time.sleep(0.5)
    raise RuntimeError('Chrome no respondió')


def evaluar(ws, expr, ctx=None):
    kw = dict(expression=expr, returnByValue=True)
    if ctx:
        kw['contextId'] = ctx
    r = ws.cmd('Runtime.evaluate', **kw)
    return (r.get('result') or {}).get('value')


def cajas(ws):
    """Cajas de texto e imágenes de la página y de cada iframe visible, en coordenadas de la página."""
    ws.vaciar(0.2)
    arbol = ws.cmd('Page.getFrameTree')['frameTree']
    frames = []

    def rec(nodo, padre):
        f = nodo['frame']
        frames.append((f['id'], padre, f.get('url', '')[:240]))
        for h in nodo.get('childFrames', []) or []:
            rec(h, f['id'])
    rec(arbol, None)
    out = []
    for fid, padre, url in frames:
        ctx = ws.ctx.get(fid)
        if not ctx:
            continue
        quad = None
        if padre:
            try:
                own = ws.cmd('DOM.getFrameOwner', frameId=fid)
                quad = ws.cmd('DOM.getBoxModel', backendNodeId=own['backendNodeId'])['model']['content']
            except Exception:
                continue
            xs, ys = quad[0::2], quad[1::2]
            if max(xs) < 0 or max(ys) < 0 or min(xs) > 1280 or min(ys) > 720 or max(xs) - min(xs) < 20:
                continue
        try:
            v = evaluar(ws, CAJAS, ctx)
        except Exception as e:
            v = json.dumps({'error': repr(e)[:200]})
        try:
            d = json.loads(v) if v else {}
        except Exception:
            d = {}
        d.update(frame=fid, padre=padre, quad=quad)
        out.append(d)
    return out


def captura(ws):
    return base64.b64decode(ws.cmd('Page.captureScreenshot', format='png')['data'])


def tecla(ws, k='ArrowRight', code=39):
    for t in ('keyDown', 'keyUp'):
        ws.cmd('Input.dispatchKeyEvent', type=t, key=k, code=k, windowsVirtualKeyCode=code, nativeVirtualKeyCode=code)


def abrir(ws, gid):
    ws.cmd('Page.navigate', url='https://view.genially.com/' + gid)
    time.sleep(10)
    ws.vaciar(0.5)
    # clic en el borde izquierdo (fuera de los botones) para que el lienzo tome el foco
    for t in ('mousePressed', 'mouseReleased'):
        ws.cmd('Input.dispatchMouseEvent', type=t, x=3, y=700, button='left', clickCount=1)
    time.sleep(1.5)


PAGINA = r'''(() => { for (const e of document.querySelectorAll('[aria-label], [aria-live], span, div')) {
    const t = (e.getAttribute('aria-label') || e.textContent || '').trim();
    const m = /^Page (\d+) of (\d+)(?:, (.*))?$/.exec(t); if (m) return JSON.stringify([+m[1], +m[2], m[3] || '']); }
  return null; })()'''


def pagina(ws):
    try:
        v = evaluar(ws, PAGINA)
        return json.loads(v) if v else None
    except Exception:
        return None


def guardar(ws, base, pg):
    open(base + '.png', 'wb').write(captura(ws))
    try:
        c = cajas(ws)
    except Exception as e:
        c = [{'error': repr(e)[:200]}]
    json.dump({'pagina': pg, 'frames': c}, open(base + '.json', 'w', encoding='utf-8'), ensure_ascii=False)


def leccion(ws, dst, nombre, gid, n_vis, espera=4.0):
    """Una captura por página: si la flecha revela elementos sin cambiar de página, se vuelve a capturar
    (queda el estado final de la página)."""
    os.makedirs(dst, exist_ok=True)
    abrir(ws, gid)
    pg = pagina(ws)
    if not pg:
        time.sleep(5); pg = pagina(ws)
    if not pg:
        log('  sin rótulo de página', nombre); return 0
    hechas, pasos = set(), 0
    while True:
        p, total, nom = pg
        guardar(ws, os.path.join(dst, '%s - %02d' % (nombre, p)), pg)
        hechas.add(p)
        if p >= total or pasos > total * 8:
            break
        tecla(ws); pasos += 1
        time.sleep(espera)
        nuevo = pagina(ws) or pg
        mismas = 0
        while nuevo[0] == p and mismas < 6:
            guardar(ws, os.path.join(dst, '%s - %02d' % (nombre, p)), nuevo)   # estado revelado
            tecla(ws); pasos += 1; mismas += 1
            time.sleep(espera)
            nuevo = pagina(ws) or nuevo
        if nuevo[0] == p:
            log('  no avanza de la página', p, nombre); break
        if nuevo[0] in hechas:
            log('  volvió a la página', nuevo[0], 'desde', p, nombre); break
        pg = nuevo
    log('OK', nombre, gid, len(hechas), 'de', pg[1], '(esperadas %d)' % n_vis)
    return len(hechas)


def main():
    cfg = json.load(open(sys.argv[1], encoding='utf-8'))
    modo = sys.argv[2] if len(sys.argv) > 2 else 'capturar'
    p, url = chrome(cfg.get('puerto', 9333))
    ws = WS(url)
    for d in ('Page.enable', 'Runtime.enable', 'DOM.enable'):
        ws.cmd(d)
    ws.cmd('Emulation.setDeviceMetricsOverride', width=1280, height=720, deviceScaleFactor=1, mobile=False)
    try:
        if modo == 'sonda':
            c = cfg['cursos'][0]
            nombre, gid, nv = c['lecciones'][0]
            dst = os.path.join(AQUI, 'sonda')
            os.makedirs(dst, exist_ok=True)
            abrir(ws, gid)
            for k in range(2):
                open(os.path.join(dst, 's%d.png' % k), 'wb').write(captura(ws))
                json.dump({'dom': json.loads(evaluar(ws, SONDA)), 'cajas': cajas(ws), 'ctx': ws.ctx},
                          open(os.path.join(dst, 's%d.json' % k), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
                tecla(ws)
                time.sleep(4)
            log('SONDA LISTA')
            return
        for c in cfg['cursos']:
            for nombre, gid, nv in c['lecciones']:
                dst = os.path.join(cfg['salida'], c['curso'], nombre)
                ya = glob.glob(os.path.join(dst, '*.png'))
                if len(ya) >= nv and not cfg.get('rehacer'):
                    log('ya estaba', c['curso'], nombre, len(ya))
                    continue
                try:
                    leccion(ws, dst, nombre, gid, nv)
                except Exception as e:
                    log('FALLA', c['curso'], nombre, gid, repr(e)[:300])
        log('LISTO')
    finally:
        try:
            ws.cmd('Browser.close')
        except Exception:
            p.kill()


if __name__ == '__main__':
    main()
