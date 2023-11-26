'''
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
'''
string = 'marcos cristiano'
# string[3] = 'ABC'  # isso não funciona porque o tipo int em python é imutável
outra_variavel = f'{string[:3]}ABC{string[4:]}'  # eu consigo alterar o conteudo da variavel string mas para isso preciso de outra variavel, 
                                                 # dessa forma

print(string)
print(outra_variavel)

# Métodos de string
print(string.capitalize())
print(string.zfill(20))