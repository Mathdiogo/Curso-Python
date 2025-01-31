'''Parte 1: Perguntas Teóricas (Ajustadas para Fundamentos Básicos)
1 - Qual a diferença entre lista (list) e tupla (tuple) em Python? Quando usar cada uma?

A diferença é que a lista possibilita dados repetidos e também possibilita a edição dos dados da lista pelo
indice que esse dado ocupa dentro de uma lista. Já a tupla, além de ser um tipo de dado imutável, impossibilita a
repetição de um mesmo dado, então dependendo da sua aplicação, deve-se utilizar um ou outro. Exemplo:

Uma lista de nomes pode conter nomes repetidos, além de talvez a ordem ou os nomes contidos nessa lista precisem
ser alterados, nesse caso deve-se usar lista

Já uma tupla, pode armazenar id de usuários, como seu id é único, seria ideal para impedir que tenham 2 id's por exemplo,
obviamente que para armazenar id's de uma forma segura envolve muito mais requisitos, mas deu pare exemplificar bem



2 - O que são dicionários em Python? Como acessar e modificar valores dentro de um dicionário?

Dicionários em python é um tipo de dado baseado em chave-valor, onde você tem uma chave, e por essa chave é
possivel acessar o valor da mesma., é um tipo de dato mutável.

dicionario = {'nome': 'matheus', 'idade': 23}

print(dicionario.get('nome')) # como acessar

dicionario['nome'] = 'Rayssa'

print(dicionario.get('nome')) #a Agora o valor da chave nome passa a ser Rayssa




3 - Explique o que são funções em Python e como definir uma função que recebe dois números e retorna a soma deles.

Funções em python é uma forma de você conseguir reutilizar um mesmo código sem ter que escrevelo várias vezes. Ao criar
uma função, é possivel chama-la e a chamada dessa função executa as linhas do código dentro dessa função.
É possivel passar parâmetros para essa fução, onde ela pode executar a função com valores pré definidos ou
valores inputados pelo usuário

a = input("Digite o primeiro número: ")
b = input("Digite o segundo número: ")

def soma(a,b):
    try:
        resposta = int(a) + int(b)
        print(f"A resposta da soma de {a} + {b} é igual a {resposta}")
    except TypeError:
        print("Tipo de dado inserido inválido")
    except ValueError:
        print("Valor inserido inválido")

soma(a, b)



Qual a diferença entre break e continue em um loop for?

Em um laço for, o continue ignora a iteração atual, porem continua com o próximo iterável,
enquanto o break interrompe completamente a iteração




O que acontece se tentarmos acessar um índice que não existe em uma lista? Como podemos evitar esse erro?

Retornará um erro dizendo que não é possivel acessar um indice na lista que não existe, uma maneira de resolver isso
seria usando um try except para absorver o erro e devolver essa informação ao usuário sem que quebre o código


Como abrir e ler um arquivo em Python? Qual a diferença entre os modos 'r', 'w' e 'a' na função open()?
Não sei, preciso dar uma atenção nisso. Na sua consepção, seria um fundamento que perguntariam?

Qual a finalidade do bloco try-except? Dê um exemplo de uso.

O try except é utilizado para capturar erros do código de uma maneira que o código não seja interrompido,
é um tratamente de erro, dando um destino dentro do código para um erro já esperado ou inesperado. É possivel
realizar processos caso algum erro aconteça, para poder contorna-lo, ou apenas avisar o usuário do erro em questão.

Um exemplo seria a própria função soma que eu escrevi em algumas questões anteriores
a = input("Digite o primeiro número: ")
b = input("Digite o segundo número: ")

def soma(a,b):
    try:
        resposta = int(a) + int(b)
        print(f"A resposta da soma de {a} + {b} é igual a {resposta}")
    except TypeError:
        print("Tipo de dado inserido inválido")
    except ValueError:
        print("Valor inserido inválido")

soma(a, b)




O que são listas por compreensão (list comprehension)? Como transformar uma lista de números em uma lista onde cada número é elevado ao quadrado usando essa técnica?


List comprehesion é uma lista em apenas uma linha, uma liste literalmente comprimida, onde alguma ação como um cálculo
é realizado internamente e o resultado já sai em formato de lista

Eu até agora aprendi apenas ler uma list comprehesion e transformar em um código normal, ainda nao aprendi de fato a criar essa lista
'''