# Curso de Python
#### Professor Luiz Otávio

## Descrição
Python é uma linguagem de programação Dinâmica de tipagem forte.
    Isso quer dizer que ao chamar uma função ou criar uma variável não preciso especificar o tipo de argumento que estou usando.
    Posso simplesmente passar o argumento o interpretador Python já irá reconhecer qual o tipo de argumento que está sendo enviado.

## Conceitos
Docstring   -   usada para documentar o código. É iniciada e terminada por um conjunto de três aspas simples ou duplas. Pode conter 
                várias linhas. O interpretador Python lê o conteúdo e guarda em memória, mas não tenta executar o conteúdo.

Comentário  -   começa com um # e só pode conter uma linha apenas. O interpretador Python ignora o que está depois do #, não lê e
                nem armazena em memória. Pode ser usado antes de uma linha de código, ao lado do código (no final), ou abaixo.

String      -   é um texto. Pode ser inserido entre aspas simples ou duplas. Ex.: "Texto" ou 'Texto'

Aspas       -   Posso usar em uma string aspas simples dentro de aspas duplas ou o contrário também, aspas duplas dentro de 
                aspas simples. Dessa forma pode ser dispensado o uso de caractere de escape.

## Comandos
| Comando | Descrição e exemplos
| print() | Função usada para imprimir os argumentos na tela. Os argumentos são separados por vírgula dentro da função.
|         | O separador padrão dos argumentos é o espaço. Usando o argumento sep="caracter" pode ser alterado o caracter
|         | do separador. No final da linha a função automaticamente insere uma quebra de linha. Usando o argumento
|         | end="caracter ou comando" pode ser alterado o comportamento da função no final da linha de argumentos.
| \r\n    | CRLF. É a quebra de linha nos Windows mais antigos
| \n      | LF. É a quebra de linha no Linux, Unix e Windows 11
| \       | É usado como caracter de ESCAPE em uma string. O Python vai ignorar a execução de um caractere depois do 
|         | escape ou vai mostrar na tela se for no comando print. Ex.: print("Marcos \"Trömel\"") vai imprimir :
|         | Marcos "Trömel". Veja "Aspas" no grupo "Conceitos" acima.
| r       | é utilizado para expressões regulares. Mas posso usar para imprimir o caracter \ se quiser em uma string
