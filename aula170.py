'''
video aula 283
os.listdir para navegar em caminhos
Linux e Mac:
/users/luizotavio/desktop/exemplo
no Windows precisa usar duas barras:
C:\\Users\\mactr\\Documents\\Exemplo
'''
import os


caminho = os.path.join('C:\\', 'Users', 'mactr', 'Documents', 'Exemplo')
# caminho = 'C:\\Usuários\\mactr\\Documents\\Exemplo'
print(caminho)

print('------------------------')

for item in os.listdir(caminho):
    print(caminho, item)

print('------------------------')

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    if not os.path.isdir(caminho_completo_pasta):
        continue
    for arquivo in os.listdir(caminho_completo_pasta):
        print(caminho_completo_pasta, arquivo)
