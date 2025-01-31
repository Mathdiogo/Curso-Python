'''Prova Simulada – Analista de Desenvolvimento Júnior (Python)
Parte 1: Perguntas Teóricas
1 - O que são variáveis em Python e como podemos definir uma variável? Dê um exemplo.
Váriavel em python é um tipo de dado onde pode-se atribuir conteudo a ela, pode-se passar como
parametro em uma função, reatribuir valores/conteudo a ela.

x = 5 # Nesse caso a variavel x recebe o valor 5
y = 2 
Podemos realizar operações matemáticas no caso do tipo de dado numérico atribuido a ela, 
ou atribuir outro qualquer tipo de dado como string, lista, tuplas, set's entre outros



2 - Qual a diferença entre o operador == e o operador is em Python? Dê exemplos de quando cada um deve ser usado.

    O operador == é utilizado exclusivamente para comparações de objetos,
 enquanto o is verifica se 2 variaveis apontam pro mesmo endereço de memória

Exemplos: 

x = 5
y = 5

# Comparando valores
if x == y:
    print("Os valores são iguais.")  # Isso verifica se os valores são iguais

# Comparando identidade (mesmo objeto na memória)
if x is y:
    print("As variáveis x e y referenciam o mesmo objeto.")  # Isso verifica se x e y apontam para o mesmo objeto na memória


3 - Como fazer uma verificação condicional para saber se um número é positivo, negativo ou zero?
valor = int(input("Digite um valor para verificação: "))

def verifica_numero(valor):
    if valor > 0:
        print("O Valor positivo")
    elif valor == 0:
        print("O valor é zero")
    else:
        print("O valor é negativo")


verifica_numero(valor)


4 - Explique o que é uma lista em Python. Como adicionar, remover e acessar elementos de uma lista?
Lista em python é um tipo de dado que possibilita armazenar outros difetentes tipos de dado dentro dela
desde int, float, outras listas, tuplas e assim por diante. É possivel, adicionar, alterar, excluir itens
a esta lista.
EXP: Lista = [1,2,3]

Lista.append(4)
Lista.remove(3)
x = Lista[0]
print(Lista)
print(x)


5 - O que são loops for e while? Quando é mais vantajoso usar cada um deles?
Um loop for é um loop realizado em um itarável, quando temos aproximadamente o numero de iterações, 
onde por exemplo voce itera sobre uma lista, percorrendo
seus elementos, com possibilidade de adicionar alguma condição específica
Já o loop while é um loop baseado em uma condição, que norlamente repete um pedaço de código até essa
condição deixar de ser verdadeira ou deixar de ser falsa


6 - Como podemos contar o número de ocorrências de um valor em uma lista? Dê um exemplo de código.
Lista = [1, 2, 2, 3, 4, 4, 4, 5]
lista_aux = []
dicionario = {}

for numero in Lista:
    lista_aux.append(str(numero))
    if numero in dicionario:
        dicionario[numero] += 1
    else:
        dicionario[numero] = 1

print(f"Numero: qntd de repetições:  {dicionario}")


7 - O que são funções lambda em Python? Dê um exemplo simples de como usá-las.

Funções lambida em python são funções amônimas executadas em uma só linha, normalmente utilizadas para pequenos
trexos de código simples

soma = lambda x, y: x + y
print(soma(2, 3))  # Saída: 5


8 - O que são strings em Python e como podemos manipular strings, como por exemplo, obter uma substring?

Strings no python é um tipo de dado imutável, não é possivel alterar uma string diretamente, a não ser com
uma substrig

nome = 'Matheus'
nome[0] = 'J' #Não podemos realizar esse tipo de modificação do indice 0 da string por mais que string seja iteraveis
# A ideia seria deixar Jatheus, para isso ocorrer temos que criar uma substring dessa maneira:

nome = 'Matheus'

nome = nome.replace("M", "J")
print (nome)

'''

