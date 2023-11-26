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

Conversão de tipos / Coerção:
            -   É o ato de converter um tipo em outro. O mesmo que "type conversion", 'typecasting" e "coercion"

Tipos primitivos e imutáveis:
            -   str, int, float e bool

Variáveis   -   São usadas para salvar algo na memória do computador. Para tornar o código mais legível e evitar
                repetir código. Inicie sempre com letras minúsculas, depois pode usar números e underline.

Constantes  -   Por convenção as constantes são escritas com todas as letras maiúsculas em Python. Porém a linguagem
                não impede que seja atribuido um novo valor a uma constante em outra parte do programa porque para
                Python é uma variável. A convenção serve para que os programadores entendam que aquele valor não deve
                ser alterado depois de ser declarado.

Precedência de operadores:
            -   1° Parenteses de dentro para fora
                2° Exponenciação
                3° Multiplicação, divisão, divisão inteira, módulo
                4° Soma e subtração

Objeto      -   Pode executar algumas ações. Essas ações são chamadas de métodos.

Parâmetro   -   Dentro da função, quando estou me referindo ao nome da variável, isso é chamado de parâmetro.

Argumento   -   Dentro da função, quando estou me referindo ao valor da variável, isso é chamado de argumento.

Método      -   Quando uma função está dentro de um objeto é chamada de método.

Iterável    -   É algo que pode ser navegado item por item utilizando índices, tanto positivos quanto negativos.

## Comandos

| Comando | Descrição e exemplos                                                                                         |
|--------:|--------------------------------------------------------------------------------------------------------------|
| print() | Função usada para imprimir os argumentos na tela. Os argumentos são separados por vírgula dentro da função.  |
|         | O separador padrão dos argumentos é o espaço. Usando o argumento sep="caracter" pode ser alterado o caracter |
|         | do separador. No final da linha a função automaticamente insere uma quebra de linha. Usando o argumento      |
|         | end="caracter ou comando" pode ser alterado o comportamento da função no final da linha de argumentos.       |
| \r\n    | CRLF. É a quebra de linha nos Windows mais antigos                                                           |
| \n      | LF. É a quebra de linha no Linux, Unix e Windows 11                                                          |
| \       | É usado como caracter de ESCAPE em uma string. O Python vai ignorar a execução de um caractere depois do     |
|         | escape ou vai mostrar na tela se for no comando print. Ex.: print("Marcos \"Trömel\"") vai imprimir :        |
|         | Marcos "Trömel". Veja "Aspas" no grupo "Conceitos" acima.                                                    |
| r       | é utilizado para expressões regulares. Mas posso usar para imprimir o caracter \ se quiser em uma string     |
| int     | Tipo de dado composto por qualquer número positivo ou negativo. Sem sinal é considerado positivo.            |
| float   | Tipo de dado composto por qualquer número positivo ou negativo com ponto flutuante, ou casas decimais.       |
| type()  | Classe que mostra qual o tipo do objeto informado como argumento                                             |
| bool    | Tipo de dado composto por sim(True) ou não(False). Boolean. String vazia é considerada False                 |
| int()   | Classe que faz a coerção do tipo para inteiro, se for possível.                                              |
| float() | Classe que faz a coerção do tipo para float, se for possível.                                                |
| +       | Operador usado para soma de dois números inteiros ou de ponto flutuante e também para concatenação entre     |
|         | dois caracteres do tipo string. Não pode ser usado para concatenar string com números                        |
| *       | Operador usado para multiplicação de dois números inteiros ou de ponto flutuante, ou para repetição de uma   |
|         | string. Ex.: 3 * A = AAA.                                                                                    |
| ...     | Ellipsis. Pode ser usado como 'place holder' (um código que ainda não foi escrito)                           |
| pass    | É o mesmo que Ellipsis.
| input() | Função usada para coletar dados do usuário. Sempre retorna os dados coletados no tipo str                    |
| if      | Insere um bloco de códigos que serão executados SE uma condição for atendida.                                |
| and     | Operador lógico em que todas as condições precisam ser True para que a expressão seja avaliada como True     |
| or      | Operador lógico em que qualquer condição precisa ser True para que toda a expressão seja avaliada True       |
| not     | Operador lógico utilizado para inverter expressões. Ex. not True = False / not False = True                  |
| %s, %d  | Interpolação de strings. É feita da mesma forma que na linguagem "C", usando o símbolo de %s para string     |
|         | ou %d para números inteiros, ou %f para números de ponto flutuante ou %x para hexadecimal minúsculo ou %X    |
|         | para hexadecimal maiúsculo dentro da string. Depois usa-se o símbolo de % depois das aspas da string e       |
|         | informa as variáveis. Se for mais de uma variável precisam estar dentro de parenteses e separadas por        |
|         | virgula na mesma ordem que são chamadas dentro da string.                                                    |
| [i:f:p] | Fatiamento de strings. Usa-se para fazer o fatiamento de uma string onde i=início, f=fim e p=passo. Se i for |
|         | omitido o Python entende que deve pegar desde a posição 0 da string. Se f for omitido que deve pegar até o   |
|         | final da string e p se for omitido assume o padrão que é 1. Também pode-se usar indices ou passos negativos  |
| len()   | Função que conta os caracteres de uma string ou de uma fatia de string.                                      |
| try     | Tenta executar um bloco de códigos que estiver indentado nele. Se não conseguir usar vai procurar o except   |
| except  | Se ocorrer um erro na execução de try, executa o código indentado nele. Podem ser especificadas ações        |
|         | diferentes para cada erro possível de try.                                                                   |
| \       | Pode ser usado para quebra uma linha de código e continuar escrevendo na linha de baixo                      |
| id()    | Função que mostra a identidade do elemento na memória.                                                       |


