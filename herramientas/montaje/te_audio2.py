# Audio v2 de la entrevista: igual cadena, techo -3 dBTP (el export v1 midió +0,3 dBTP tras el AAC de Resolve).
import json, os, subprocess, sys
sys.path.insert(0, r'D:\DAE\_repo\cursos\medio-ambiente\entrevista_tecnicas')
sys.path.insert(0, r'D:\DAE\_repo\herramientas\montaje')
import plan_te as P
import srpa_composicion as K
import srpa_audio as A
META = 'I=-16:TP=-3:LRA=7'
base = '[0:a]aresample=48000,' + A.CADENA
r = subprocess.run([K.FB + '/ffmpeg.exe', '-hide_banner', '-nostats', '-i', P.ORIGINAL, '-filter_complex',
                    base + ',loudnorm=%s:print_format=json[a]' % META, '-map', '[a]', '-f', 'null', '-'],
                   capture_output=True, text=True, errors='replace').stderr
m = json.loads(r[r.rfind('{'):r.rfind('}') + 1])
ln = ('loudnorm=%s:measured_I=%s:measured_TP=%s:measured_LRA=%s:measured_thresh=%s:offset=%s:linear=true'
      % (META, m['input_i'], m['input_tp'], m['input_lra'], m['input_thresh'], m['target_offset']))
dst = P.COMPUESTO.replace('_v1.mp4', '_v2.mp4')
fin = K.duracion(P.COMPUESTO)
subprocess.run([K.FB + '/ffmpeg.exe', '-y', '-v', 'error', '-i', P.ORIGINAL, '-i', P.COMPUESTO, '-filter_complex',
                base + ',' + ln + ',aresample=48000[a]', '-map', '1:v', '-map', '[a]', '-c:v', 'copy', '-t', '%.3f' % fin,
                '-c:a', 'aac', '-b:a', '256k', '-movflags', '+faststart', dst], check=True)
r = subprocess.run([K.FB + '/ffmpeg.exe', '-hide_banner', '-nostats', '-i', dst, '-vn', '-af', 'ebur128=peak=true', '-f', 'null', '-'],
                   capture_output=True, text=True, errors='replace').stderr
print('v2', r[r.rfind('Summary'):][:500])
