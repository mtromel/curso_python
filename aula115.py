'''
video aula 181, 182, 183, 184
Ambientes virtuais em Python (venv)
Um ambiente virtual carrega toda a sua instalação do Python para uma pasta no caminho escolhido.
Ao ativar um ambiente virtual, a instalação do ambiente virtual será usada.
venv é o módulo que vamos usar para criar ambientes virtuais.
Você pode dar o nome que preferir para um ambiente virtual, mas os mais comuns são: venv env .venv .env
'''

# para criar um ambiente virtual digite no powershell:
# python -m venv nome_do_ambiente_virtual
# gcm python -Syntax      mostra o caminho do path de onde está o python instalado.

# para ativar o ambiente virtual criado:
# no powershell acessar o caminho onde está a pasta scripts do ambiente virtual:
# \venv\Scripts\activate
# no linux e mac: . venv/bin/activate ou também pode ser source venv/bin/activate


# na barra inferior do VSCode clicar sobre a versão do python que aparece e escolher qual o interpretador será usado

# pip install - instala pacotes do Python
# pip uninstall - desinstala pacotes do Python
# pip freeze - lista todos os pacotes instalados
# pip index versions 'pacote'  -  lista as versões disponíveis para aquele pacote
# pip install 'pacote'=='versão_desejada'  -  instala uma versão diferente da versão atual. não vai deixar as duas
                                                # versões instaladas. Vai instalar só a versão solicitada
# pip install 'pacote' --upgrade  -  instala a atualização disponível para o pacote informado, substituindo a versão atual.
# pip freeze > requirements.txt  -  cria um arquivo txt na pasta atual com a lista de todos os pacotes e versões que tenho.
# posso excluir o ambiente virtual e guardar só esse requirements.txt e se precisar voltar nesse projeto posso recriar o 
#   ambiente virtual e instalar todos os pacotes de uma vez só usando o requirements.txt
# pip install -r <caminho>\requirements.txt -  instala todos os pacotes listados dentro do arquivo txt no novo venv


