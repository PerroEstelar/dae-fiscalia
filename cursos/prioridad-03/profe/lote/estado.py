import os,time,shutil,subprocess,glob
T='D:/DAE/_tmp/tr_p/'
R='D:/DAE MASTER/PRIORIDAD 03/VIDEOS PROFE/'
def ls(f):
    try: return open(T+f,encoding='utf-8',errors='replace').read().splitlines()
    except OSError: return []
print(time.strftime('%H:%M:%S'),'D %.1f C %.1f G %.2f'%tuple(shutil.disk_usage(x).free/1e9 for x in ('D:/','C:/','G:/')))
print('recortes:',' | '.join(' '.join(l.split()[1:8]) for l in ls('recorta_lote.log') if 'pedido' not in l))
for k in ('trci','tru1i','trcc','tru1r','tru2i','tru2r','tru3i','tru3r'):
    s=ls(k+'/recorta.out')
    if s and 'LISTO' not in s[-1]: print('  en curso',k,s[-1][:60])
print('cadena:',' | '.join(' '.join(l.split()[2:7]) for l in ls('lote_cadena.log') if 'en cola' not in l))
for l in ls('lote_entrega.log'):
    p=l.split()
    if len(p)>1 and p[1] in ('lt','linea','revision','calibra','entrega_gpu:'): print(' '.join(p[:7]))
    else: print(l[:300].encode('ascii','backslashreplace').decode())
print('pendientes:',ls('pendientes.txt'))
for o in ('lote_cadena.out','entrega_gpu.out','recorta_lote.out'):
    s=chr(10).join(ls(o))[-300:]
    if s.strip(): print('!!',o,s.encode('ascii','backslashreplace').decode())
r=subprocess.run(['nvidia-smi','--query-gpu=utilization.gpu,memory.used','--format=csv,noheader'],capture_output=True,text=True); print('gpu',r.stdout.strip())
print('subidas:',[(os.path.basename(x),os.path.getsize(x)) for x in glob.glob('G:/My Drive/_MA subidas/traficoytrata*')])
