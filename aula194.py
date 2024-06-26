'''
video aula 320 e 321
Usando subprocess para executar processos e comandos externos
subprocess é um módulo do Python para executar
processos e comandos externos no seu programa.
o método mais simples para atingir o objetivo é usando subprocess.run().
Argumentos principais de subprocess.run():
- stdout, stdin e stderr -> Redirecionam saída, entrada e erros
- capture_output -> captura a saída ou o erro para uso posterior
- text -> Se True, entradas e saídas serão tratadas como texto
e automaticamente codificadas ou decodificadas com os conjunto
de caracteres padrão  da plataforma (geralmente UTF-8).
- shell -> Se True, terá acesso ao shell do sistema. Ao usar
shell (True), recomendo enviar o comando e os argumentos juntos.
- executable -> pode ser usado para especificar o caminho
do executável que iniciará o subprocesso.
Retorno:
stdout, stderr, returncode e args
Importante: a codificação de caracteres do windows pode ser
diferente. Tente usar cp1252, cp852, cp850 (ou outros). Linux e
mac, use utf-8.
Comando de exemplo:
Windows: ping 127.0.0.1
Linux/Mac: ping 127.0.0.1 -c 4
'''
import subprocess
import sys

# sys.platform = linux, linux2, darwin, win32

cmd = ['ping', '127.0.0.1', '-c', '4']
encoding = 'utf_8'

if sys.platform == 'win32':
    cmd = ['ping', '127.0.0.1']
    encoding = 'cp850'


proc = subprocess.run(cmd, capture_output=True, encoding=encoding)

print()
print(proc.args)
print(proc.stderr)
# print(proc.stdout.decode('cp850'))
print(proc.stdout)
print(proc.returncode)
