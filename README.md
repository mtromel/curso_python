# Curso de Python
#### Professor Luiz Otávio

## Descrição
Python é uma linguagem de programação Dinâmica de tipagem forte.
    Isso quer dizer que ao chamar uma função ou criar uma variável não preciso especificar o tipo de argumento que estou usando.
    Posso simplesmente passar o argumento o interpretador Python já irá reconhecer qual o tipo de argumento que está sendo enviado.

## Conceitos
* Docstring   -   usada para documentar o código. É iniciada e terminada por um conjunto de três aspas simples ou duplas. Pode conter 
                várias linhas. O interpretador Python lê o conteúdo e guarda em memória, mas não tenta executar o conteúdo.

* Comentário  -   começa com um # e só pode conter uma linha apenas. O interpretador Python ignora o que está depois do #, não lê e
                nem armazena em memória. Pode ser usado antes de uma linha de código, ao lado do código (no final), ou abaixo.

* String      -   é um texto. Pode ser inserido entre aspas simples ou duplas. Ex.: "Texto" ou 'Texto'

* Aspas       -   Posso usar em uma string aspas simples dentro de aspas duplas ou o contrário também, aspas duplas dentro de 
                aspas simples. Dessa forma pode ser dispensado o uso de caractere de escape.

* Conversão de tipos / Coerção
              -   É o ato de converter um tipo em outro. O mesmo que "type conversion", 'typecasting" e "coercion"

* Tipos primitivos e imutáveis 
              - str, int, float e bool

* Variáveis   -   São usadas para salvar algo na memória do computador. Para tornar o código mais legível e evitar
                repetir código. Inicie sempre com letras minúsculas, depois pode usar números e underline.

* Constantes  -   Por convenção as constantes são escritas com todas as letras maiúsculas em Python. Porém a linguagem
                não impede que seja atribuido um novo valor a uma constante em outra parte do programa porque para
                Python é uma variável. A convenção serve para que os programadores entendam que aquele valor não deve
                ser alterado depois de ser declarado.

* Precedência de operadores:             
              1) Parenteses de dentro para fora; 2) Exponenciação; 3) Multiplicação, divisão, divisão inteira, módulo; 4) Soma e subtração;

* Objeto      -   Pode executar algumas ações. Essas ações são chamadas de métodos.

* Parâmetro   -   Dentro da função, quando estou me referindo ao nome da variável, isso é chamado de parâmetro.

* Argumento   -   Dentro da função, quando estou me referindo ao valor da variável, isso é chamado de argumento.

* Método      -   Quando uma função está dentro de um objeto é chamada de método.

* Iterável    -   É algo que pode ser navegado item por item utilizando índices, tanto positivos quanto negativos.

* Loop infinito
            -   Quando um código não tem fim. É um erro de programação.

* Iterador    -   Quem sabe entregar um valor por vez

* Lista       -   Suporta vários valores de qualquer tipo.

* Desempacotamento
            -   extrair os valores de uma lista ou tupla e armazenas em diversas variáveis (uma variável para cada índice
                da lista ou tupla). Pode ser usado o '*' nas chamadas de métodos e funções para desempacotar.

* Tupla       -   é uma 'lista' imutável. É um pouco mais eficiente que uma lista.

* Operação ternária
            -   Similar ao if, mas é escrito em uma única linha. Pode ter várias condições, pode usar os operadores and, or,
                not. Sintaxe: <valor_se_condição_for_verdadeira> if <condição> else <outro_valor_se_condição_for_falsa>

* Funções     -   São trechos de código usados para replicar determinada ação ao longo do código. Podem receber valores para
                parâmetros (argumentos) e retornar um valor específico. Por padrão as funções em Python retornam None.

* Argumento   -   É o valor informado a ser enviado para a função que o recebe como parâmetro. Argumentos podem ser nomeados
                ou não nomeados (ou posicionais). Argumento nomeado tem o nome do parâmetro seguido por sinal de igual junto
                com o nome (não pode ter espaços). Argumento não nomeado, ou posicional, recebe apenas o argumento (valor), mas 
                esse precisa ser enviado na posição correta. É possível usar argumentos posicionais junto com nomeados, mas a
                partir do nomeado todos que vierem depois dele precisam ser nomeados. Os argumentos nomeados podem estar em
                qualquer posição em relação aos parâmetros da função, não precisam estar na mesma ordem criada na função.

* Parâmetro   -   São os parâmetros que esperamos receber como argumentos na chamada da função. Os parâmetros podem ter um valor
                padrão. Caso o valor não seja enviado na chamada da função o valor padrão será usado. Caso seja enviado um
                valor na chamada da função o valor padrão é ignorado.

* Refatorar   -   editar ou reescrever o código.

* Escopo      -   Significa o local onde aquele código pode alcançar. Existe o escopo global e local:
                Escopo global - é o escopo onde todo código é alcançavel.
                Escopo local - é o escopo onde apenas nomes do mesmo local podem ser alcançados. Não temos acesso a nomes
                de escopos internos nos escopos externos, mas o contrário é possível.
                Em classes existe o escopo da classe e o escopo do método. Se um atributo for declarado no escopo da classe
                ela pode ser acessada por qualquer método da classe usando classe.atributo tanto dentro da classe, dos métodos da classe ou na linha decódigo do programa fora da classe. Um argumento de um método pode ser acessado em
                qualquer outro método usando self. Fora da classe precisa usar a instância da classe no lugar de self.

* Higher Order Functions
            -   Funções que podem receber ou retornar outras funções.

* First-Class Functions
            -   Funções que são tratadas como outros tipos de dados comuns (str, int, etc...)

* Closure     -   É quando uso uma variável para salvar uma execução parcial (um escopo) de uma função e a uso com uma função
                para concluir a execução da função principal.

* Dicionários -   São estruturas de dados do tipo 'Chave' e 'Valor'. Chaves podem ser consideradas como índices e podem ser de
                tipos imutáveis como str, int, float, bool, tuple, etc. O valor pode ser de qualquer tipo, incluindo outro 
                dicionário. Usa-se as {} ou a classe dict() para criar dicionários.

* Set       -   Tipo de dados set. São conjuntos. Tipo de dados mutável. Aceitam apenas tipos imutáveis como valor interno
                (não aceitam valores mutáveis como listas e dicionários). Não garante a ordem dos valores armazenados. São eficientes para remover valores duplicados de iteráveis Seus valores sempre serão únicos. Não tem indexes. São iteráveis.

* Comprehension -   Se aplica a listas, dicionários ou conjuntos. É uma forma de criar a lista, dicionário ou conjunto a partir
                    de iteráveis. Sintaxe: 
                        lista = [n for n in range(10)] 
                        ou com dois for também:
                        lista = [(x, y) for x in range(3) for y in range(3)]
                        pode ser usado if antes e depois do for:
                        dc = {chave: valor.upper() if isinstance(valor, str) else valor for chave, valor in dicionario.items() if chave = 'categoria'}

* Falsy / Truthy    -   objetos vazios ou com valor zero são considerados Falsy. Ex.: listas, dicionários, conjuntos, tuplas 
                        ou strings vazias, 0, 0.0, None, False, range(0). 
                        Diferente disso é considerado Truthy mesmo que seja com valores negativos no caso dos int e float.

* Diferença entre iterável e iterador
                    -   O iterável tem a responsabilidade de ter os valores sequencialmente. 
                    -   O iterator só tem a responsabilidade de entregar um valor por vez. Só sabe quem é o próximo valor.
                        Não sabe quem é o primeiro ou o último e nem quem é o anterior. Não sabe o tamanho do iterável.

* Generator -   São funções que sabem pausar em determinada ocasião. É também um iterator. Não sabe mais nada além do próximo
                valor. Um generator não cria todos os valores de um range na memória ao ser criado. Ele vai criar um por vez
                conforme formos pedindo com next()

* Importação de módulos
            -   import nome_do_modulo  ->  importa o módulo inteiro
            -   from nome_do_modulo import objeto1, objeto2  ->  importa partes do módulo apenas. Esses objetos importados
                    serão usados como se tivessem sido criados no módulo atual.
            -   import nome_do_modulo as alias
            -   from nome_do_modulo import objeto as alias  ->  faz a importação do módulo ou do objeto e atribui um alias
                    (apelido) para ele que poderá ser usado no módulo atual.
            -   from nome_do_modulo import *  ->  má prática de programação. Pode causar confusão com os nomes das variáveis
                    já que não é possível enxergar o que está sendo importado.

* --main__  -   É o módulo principal. O Python sempre vai considerar o módulo atual como --main__
                O Python conhece todos os módulos e pacotes (pastas) presentes nos caminhos do sys.path. Também todas as 
                pastas e módulos que estão abaixo do --main__

* import    -   Faz a importação de módulos em Python. Só carrega uma vez o módulo. Se precisar carregar novamente durante
                uma mesma execução do --main__ precisar umar importlib.reload.

* --init__  -   Se nomear um módulo com essa descrição a pasta onde esse módulo está inserido poderá ser usada como se fosse
                um modulo. Nesse caso poderia acessar um objeto que está dentro de um módulo dessa pasta assim:
                    pasta.modulo.objeto
                Ou então podemos importar os módulos dentro de --init__ e então os objetos podem ser acessados assim:
                    pasta.objeto

* variáveis livres
            -   São variáveis definidas fora do escopo de uma função interna

* Funções decoradoras
            -   São funções que decoram outras funções. São factory functions

* Decorar   -   Significa Adicionar, Remover, Restringir, Alterar

* Decoradores
            -   São usados para fazer o Python usar as funções decoradoras em outras funções. São 'Sintax Sugar'.
                A ordem de execução dos decoradores é de baixo para cima (a linha mais próxima da função decorada é
                executada primeiro, depois a de cima).
                Ex.: @função_decoradora acima da definição da função que quero decorar.

* Função zipper
            -   Função usada para unir duas listas. Esse é um nome de convenção, essa função pode ter qualquer nome.

* Ambientes Virtuais    -   Um ambiente virtual carrega toda a sua instalação do Python para uma pasta no caminho escolhido.
                        Ao instalar um ambiente virtual, a instalação do ambiente virtual será usada. Podemos dar qualquer
                        nome para o ambiente virtual mas os mais usados são: venv, env, .venv, .env
                        Para criar o ambiente virtual digite no powershell: python -m venv nome_do_ambiente_virtual

* Interpretador Python  -   Posso escolher qual o interpretador Python quero usar. Para isso, no VSCode posso selecionar
                        na barra inferior do lado direito qual a versão.

* Posicional-Only Parameters  -  Representado por /. Tudo antes da barra  deve ser APENAS posiciona. PEP 570.

* Keyword-Only Parameters  -  Representado pelo * sozinho. tudo que vem DEPOIS do * deve ser nomeado. PEP 3102.
                                Exemplos:   def funcao(param1, param2, *, param3, param4):
                                Pode ser usado em conjunto com Posicional-Only Parameters:
                                            def funcao(param1, param2, /, *, param3, param4):

* Classes       -   São moldes para criar novos objetos. Geram novos objetos (também chamados instâncias) que podem ter
                        seus próprios atributos (dados dentro da classe) e métodos (ações dentro da classe). Os objetos
                        gerados pela classe podem usar seus dados internos para realizar várias ações. def dentro da classe
                        não cria uma função, cria um método.

* Hard coded    -   é algo que foi escrito diretamente no código. Ex. nome = 'João'

* Estados de instância  -   um método pode mudar o estado de outro método sem afetar o estado de outra instância da classe.

* Atributos de classe   -   é como uma constante declarada no escopo da classe que pode ser usado por todas as instâncias
                            usando classe.atributo. Força o Python a usar o valor do atributo da classe. Pode ser declarado
                            um valor diferente em um método para uma instância usando self.atributo. Esse valor será buscado
                            antes do valor do atributo na classe. Posso mudar o valor do atributo da classe de qualquer
                            parte do programa usando classe.atributo

* Convenções de nomes   -   PascalCase  -   todas as palavras iniciam com letras maiúsculas e nada é usado para separá-las.
                                            Essa é a convenção utilizada para classes em Python. Ex.: MinhaClasse, Classe
                            camelCase   -   a primeira letra sempre será minúscula e o restante das palavras deverá iniciar
                                            com letra maiúscula. Essa convenção não é usada em Python. Ex.: minhaFuncao.
                            snake_case  -   todas as letras são minúsculas e separadas por um underline. Este é o padrão
                                            usado em Python para definir qualquer coisa que não for uma classe.
                                            Ex.: minha_variavel, soma, funcao_legal
                            Os padrões usado em Python são: snake_case para qualquer coisa e PascalCase para classes.

* Método de classe  -   é um método que usa cls ao invés  de self. Ele recebe a classe ao invés da instância. Criado com o 
                            decorarador @classmethod.

* Factories method  -   Igual ao método de classe, recebe cls, mas serve para chamar outro método ou a própria classe para 
                            executar uma ação. Criado com o decorador @classmethod.

* Modificadores de acesso   -   Python não tem modificadores de acesso como em outras linguagens (public, protected, private).
                                    Por convenção a comunidade definiu que:
                                        Public -> o nome do atributo ou método é criado sem underline no começo. Pode ser
                                            usado em qualquer lugar do programa.
                                        Protected -> o nome do atributo ou método começa com um underline. Não deve ser 
                                            usado fora da classe ou da subclasse.
                                        Private -> o nome do atributo ou método começa com dois underline. Só deve ser usado
                                            na classe em que foi declarado.
* Name mangling -   desfiguração do nome. O Python desfigura o nome do atributo ou método que comça com dois underline. O
                        nome desfigurado fica assim: _NameClass__NameAttributeOrMethod

* Modo Pythônico    -   modo do Python de fazer as coisas.

* Código cliente    -   é o código que usa o seu código.

* Getter    -   é um método para obter um atributo. Criado com o decorator @property

* Setter    -   é um método para setar o valor de um atributo. O método é criado usando @nome_do_getter.setter.
                    veja módulo aula132.py e video aula 213

* Relações entre classes:
            ** Associação   -   É um tipo de relação onde os objetos estão ligados dentro do sistema. Geralmente temos uma     asssociação quando um objeto tem um atributo que referencia outro objeto. Não especifica como um objeto controla o ciclo de vida de outro objeto.
            ** Agregação    -   É uma especialização de associação entre dois ou mais objetos. Cada objeto terá seu ciclo de    vida independente. Geralmente é uma relação de um para muitos. Os objetos podem viver separadamente, mas pode se tratar de uma relação onde um objeto precisa de outro para fazer determinada tarefa.
            ** Composição   -   É uma especialização de agregação. Nela quando o objeto "pai" for apagado, todas as referências  aos objetos filhos também serão apagadas.



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
| pass    | É o mesmo que Ellipsis.                                                                                      |
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
| len()   | Função que conta os caracteres de uma string ou de uma fatia de string, ou de registros em um dicionario     |
| try     | Tenta executar um bloco de códigos que estiver indentado nele. Se não conseguir usar vai procurar o except   |
|         | e precisa ter o except ou o finally para funcionar. Não pode ser usado sozinho.                              |
| except  | Se ocorrer um erro na execução de try, executa o código indentado nele. Podem ser especificadas ações        |
|         | diferentes para cada erro possível de try. Try pode ter quantos except forem necessários                     |
| else    | Condição que pode ser usada com Try. Se não der erro a execução de Try, else será executado também. Se der   |
|         | erro e o except for acionado, else não é executado.                                                          |
| finally | Pode ser usado com Try, com ou sem except. Sempre será executado.                                            |
| Exception| É uma classe superior de excessões. Qualquer erro que não esteja sendo explicitamente tratado cai aqui se   |
|         | for usada com uma except.                                                                                    |
| --class__ | Método de exceptions. Mostra a mensagem de erro padrão do Python para aquele erro.                         |
| --name__ | Método de exceptions. Mostra o nome da exception. Posso usar esses métodos com um alias para apresentar os  |
|         | dados do erro na tela ou em um aquivo de log de forma personalizada.                                         |
| raise   | Usado para lançar erros (fazer com que mesmo sendo tratados eles sejam exibidos). Também pode ser usado para |
|         | personalizar a mensagem de erro padrão daquele erro.                                                         |
| \       | Pode ser usado para quebra uma linha de código e continuar escrevendo na linha de baixo                      |
| id()    | Função que mostra a identidade do elemento na memória.                                                       |
| while() | Executa um bloco de códigos enquanto uma condições for verdadeira                                            |
| for()   | Laço de repetição usado quando se sabe exatamente quantas repetições devem ocorrer.                          |
| range() | Usado para criar um range. Sintaxe: range(star, stop, step)                                                  |
| next()  | Função que entrega o proximo valor de um iterável.                                                           |
| iter()  | Função que retorna o iterador de um iterável.                                                                |
| append()| Método de list. Adiciona um item no final da lista.                                                          |
| insert()| Método de list. Adiciona um item no índice escolhido.                                                        |
| pop()   | Método de list. Remove do final (se o índice for omitido) ou do índice escolhido.                            |
| del()   | Método de list. Apaga um índice.                                                                             |
| clear() | Método de list. Limpa a lista inteira.                                                                       |
| extend()| Método de list. Faz um cópia de uma lista para dentro de outra lista.                                        |
| +       | Concatena duas listas dentro de outra lista.                                                                 |
| copy()  | Método de list. Faz a cópia de uma lista para outra posição da memória, criando uma lista independente.      |
| enumerate() | Enumera iteráveis.                                                                                       |
| round() | Arredonda a casa decimal. Retorna um float, omite os zeros à direita depois da virgula.                      |
| split() | Divide uma string. Por padrão divide nos espaços. Posso informar qualquer outro caracter para dividir a      |
|         | string. O caracter escolhido não vai ser inserido na lista.                                                  |
| strip() | Corta os espaços no começo e no fim da string.                                                               |
| rstrip()| Corta os espaços da direita da string.                                                                       |
| lstrip()| Corta os espaços da esquerda da string.                                                                      |
| join()  | Une strings, listas, tuplas. Apenas iteráveis.                                                               |
| def     | Usado para definir uma nova função. Sintaxe: def nome_da_função(parâmetros)                                  |
| global  | Faz uma variável de escopo externo ser a mesma no escopo interno. Com isso é possível mudar o valor da       |
|         | variável do escopo externo no escopo interno.                                                                |
| return  | Faz o retorno de um valor de uma função ao objeto que chamou a função.                                       |
| args    | Termo que pode ser usado como parâmetro de uma função. Permite que a função receba vários argumentos como    |
|         | uma lista ou tupla.                                                                                          |
| *args   | Empacota ou desempacota os argumentos recebidos. O '*' também pode ser usado com variáveis para desempacotar |
| **kwargs| Similar a args, mas nesse caso os argumentos são nomeados. Sempre deve ser usado com ** antes                |
| keys()  | Método de dict. Iterável com as chaves                                                                       |
| values()| Método de dict. Iterável com os valores                                                                      |
| items() | Método de dict. Iterável com chaves e valores                                                                |
| setdefault() | Método de dict. Adiciona valores se a chave não existir. Se a chave existir retorna o valor dela        |
| copy()  | Médodo de dict. Retorna uma cópia rasa (shallow copy)                                                        |
| get()   | Método de dict. Obtém uma chave                                                                              |
| pop()   | Método de dict. Apaga um item com a chave especificada (del)                                                 |
| popitem() | Método de dict. Apaga o último item adicionado                                                             |
| update()| Método de dict. Atualiza um dicionário com outro                                                             |
| set()   | Tipo de dados mutáveis. Cria um conjunto. Se enviar uma string vai iterar sobre ela e armazenar as letras    |
|         | separadas                                                                                                    |
| add()   | Método de set. Adiciona um valor ao conjunto. Só pode adicionar um valor de cada vez. Se enviar como valor   |
|         | uma string, add vai armazenar no conjunto a string inteira.                                                  |
| update()| Método de set. O mesmo que add mas aceita enviar vários valores separados por vírgula de uma vez. Assim como |
|         | set, se enviar uma string sozinha ele vai iterar sobre ela. Se enviar a string junto com outros valores ele  |
|         | vai armazenar a string inteira, assim como add.                                                              |
| clear() | Método de set. Limpa o set                                                                                   |
| discard()| Método de set. Descarta o valor informado.                                                                  |
| "\|"    | Operador de set. Operador de união. Une dois sets descartando os valores duplicados.                         |
| "&"     | Operador de set. Operador de intersecção. Retorna apenas os números presentes em ambos os sets               |
| "-"     | Operador de set. Operador de diferença. Retorna apenas os itens únicos presentes apenas no set da esquerda   |
| "^"     | Operador de set. Operador de diferença simétrica. Retorna apenas os itens únicos dos dois sets.              |
| lambda  | Função anônima (que não tem nome) que contêm apenas uma linha. Sintaxe: lambda <parametro>: <retorno>        |
| isinstnce()| Retorna um Bool referente a se o objeto informado como 1º argumento é do tipo informado como 2º argumento |
| dir()   | Retorna todos os atributos disponíveis em Python para o objeto ou tipo de dados iformado como argumento      |
| hasattr()| Verifica se um objeto informado como 1º argumento tem um atributo informado como 2º argumento.              |
| getattr()| Pega o método informado como 2º argumento e aplica ao objeto informado como 1º argumento.                   |
| yield   | Gera uma pausa na execução da função generator, retornando o resultado informado após o comando.             |
| yield from| Permite chamar outro generator antes de executar o restante do código desse generator                      |
| reload  | Método da biblioteca padrão do Python importlib. Usado para recarregar um módulo importado.                  |
| --code__.co_freevars" | Mostra as variáveis livres desse escopo. Sintaxe: funcao.--code__.co_freevars                   |
| locals() | Mostra as variaveis locais desse escopo                                                                     |
| nonlocal | Comando que torna possível o Python manipular uma variável livre. Sintaxe: nonlocal variável                |
| zip()   | Função padrão do Python que faz a união de duas listas na ordem se baseando pela lista menor.                |
| zip_longest() | Função do módulo intertools do Python. Faz a união de duas listas na ordem se baseando pela lista      |
|         | maior. Os valores ausentes da lista menor são preenchidos com None. Posso usar fillvalue= para personalizar  |
|         | o texto no lugar de None.                                                                                    |
| min()   | Função que retorna o menor valor de um range. Se usado com len(lista) retorna o menor número de indice       |
|         | das duas listas (a menor lista).                                                                             |
| max()   | Função que retorna o maior valor de um range. Se usado com len(lista) retorna o maior número de indice       |
|         | das duas listas (a maior lista)                                                                              |
| gcm     | Não é comando do Python, é um comando do powershell. É útil para identificar o caminho do path de onde está  |
|         | o Python instalado. gcm python -Syntax                                                                       |
| activate | Usado para ativar o ambiente virtual. Sintax no powershell: <caminho>\activate.                             |
|         | obs.: no Windows o activate fica dentro da pasta Scripts. No linux e no mac fica dentro da pasta bin         |
| deactivate | Usado para desativar o ambiente virtual.                                                                  |
| pip     | Comando usado no powershell para manipulação de pacotes do Python:                                           |
|         | pip install <pacote> - instala pacotes                                                                       |
|         | pip install <pacote> --upgrade - instala a atualização disponível para o pacote, substituindo a versão atual |
|         | pip install <pacote> == <versão> - instala o pacote com uma versão específica (anterior).                    |
|         | pip install -r <caminho>\requirements.txt - instala todos os pacotes listado no txt de uma vez               |
|         | pip uninstall <pacote> - desinstala pacotes                                                                  |
|         | pip freeze - lista todos os pacotes instalados nesse ambiente                                                |
|         | pip freeze > requirements.txt - cria um arquivo txt (padrão é usar o nome 'requirements') na pasta atual com |
|         |     a lista de todos os pacotes e suas versões instaladas nesse ambiente. Com esse arquivo guardado posso    |
|         |     excluir o ambiente virtual (apaga também os módulos python e pastas criadas) e usar esse arquivo txt para|
|         |     recriar o ambiente virtual com os mesmos pacotes e versões usados naquele projeto. Isso economiza espaço |
|         |     porque não preciso guardar a instalação do python inteira para aquele ambiente.                          |
|         | pip index versions <pacote> - lista as versões disponíveis para aquele pacote.                               |
| json    | biblioteca do Python. Quando importada para o módulo permite a manipulação de arquivos JSON                  |
| dump()  | método de json. Faz o dump - "jogar para dentro" do arquivo, salva o arquivo, cria o arquivo se não existir  |
|         |     usado com with open. Ex.: json.dump(lista, arquivo, ensure_ascii=False, indent=2)                        |
| ensure_ascii= | parâmetro para ser usado com json.dump. ensure_ascii=False faz com que os caracteres especiais não     |
|         |     sejam substituídos por padrão ascii no arquivo json                                                      |
| indent= | parâmetro para ser usado com json.dump. indent=2 faz com que o arquivo json tenha a indentação padrão do     |
|         |     json, o que facilita a visualização do arquivo                                                           |
| load()  | método de json. Faz a leitura do arquivo json e salva na lista que for indicada. lista = json.load(arquivo)  |
| --init__ | Método de classe. É um dos primeiros a ser chamado para inicializar os atributos da classe                  |
|         |     def --init__(self, param1, param2):                                                                      |
| self    | convenção de variável de métodos de classe. Referencia à instância da classe. Precisa ser o primeiro         |
|         |     parâmetro de cada método.                                                                                |
| --dict__ | método de classes que pode ser usado para listar o conteúdo do dicionário da instância da classe            |
| vars()  | método de classes que faz o mesmo que --dict__                                                               |
| @classmethod | Decorator para criar método de classe e também factories method.                                        |
| @staticmethod | Decorador para criar método estático, sem self e sem cls. Não tem acesso nem à instância e nem à       |
|         | classe. É como uma função, mas fica protegida dentro do escopo da classe. Pode ser usada para indicar que    |
|         | aquela função é usada com aquela classe porque para chamar ele precisa usar também Class.method()            |
| @property | Decorador usado para criar uma propriedade do objeto. É um método que se comporta como um atributo. É usada|
|         | como getter, para evitar quebrar o código cliente, para habilitar o setter e para executar ações ao obter o  |
|         | atributo.                                                                                                    |
|




## Cuidados e alertas ao programar em Python

* Listas são mutáveis, por isso é preciso tomar cuidado. O operador de atribuição '=' não faz uma cópia dos dados da lista
    para outra posição de memória, assim como faz com variáveis de tipos imutáveis. Com as listas o '=' apenas aponta a
    lista nova para a posição de memória onde o conteúdo da lista original está armazenado. Isso quer dizer que qualquer 
    alteração nesse conteúdo em uma das listas vai afetar as duas listas. É possível evitar isso usando o método copy().

* No VsCode, ao digitar ponto depois de um objeto é exibida uma lista dos atributos disponíveis para aquele objeto. 
    Mas essa lista é do VsCode, pode ter divergências com os atributos disponíveis na linguagem, pois é parte da programação
    da IDE.

* Problema com parâmetros mutáveis em Python - Sempre que for criar parâmetros em funções tenho que verificar se o parâmetro
    é um dado mutável. Se for, não devo colocar valor padrão para esse parâmetro na função. Por exemplo, se um dos parâmetros
    for uma lista, não informar na definição da função uma lista vazia assim: def funcao(param1, lista=[]):
    Se fizer assim vai dar problema porque ao chamar a função a primeira vez sem informar a lista o Python cria uma lista no
    escopo da função. Ao chamar a função novamente para criar outra lista (sem informar a lista) o Python vai mesclar a
    lista já criada no escopo da função com a nova. Para resolver isso preciso definir o parâmetro como None na definição
    da função e usar um if para verificar se não foi passado nenhum parâmetro na chamada da função. Assim o Python só vai
    criar a lista uma vez . Veja arquivo aula118.py e video aula 191
