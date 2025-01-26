'''1. Listas - Básico
Crie uma lista com os números de 1 a 10. Em seguida:

Exiba o terceiro elemento da lista.
Adicione o número 11 à lista.
Remova o número 5.'''
Lista = [1,2,3,4,5,6,7,8,9,10]
print(Lista[2])
Lista.append(11)
print(Lista)
Lista.remove(5)
print(Lista)

'''2. Tuplas - Imutabilidade
Considere a seguinte tupla:'''

minha_tupla = (10, 20, 30, 40, 50)
'''Como acessar o valor 30?
É possível alterar o valor 40 para 60? Explique.'''
print(minha_tupla[2])
#Não é possível modificar valroes da tupla, pois são um tipo de dado iutável


#3. Sets - Duplicatas
'''Crie um conjunto com os valores [1, 2, 2, 3, 4, 4, 5].
Qual será o tamanho do conjunto?
Adicione o número 6 ao conjunto.'''
meu_set = {1, 2, 2 ,3, 4, 4, 5}
print(meu_set)
# O tamanho do conjunto será de 5 numeros
meu_set.add(6)
print(meu_set)


'''4. Dicionários - Acessando dados
Dado o dicionário:'''
aluno = {"nome": "João", "idade": 22, "curso": "Engenharia"}
'''Como acessar o nome do aluno?
Como adicionar a chave "matricula" com o valor 12345?'''
aluno.get('nome')
aluno['matrícula'] = '12345'
print(aluno)


'''5. Listas e Loops
Dada a lista:'''

frutas = ["maçã", "banana", "laranja", "uva"]
#Use um for para imprimir cada fruta em letras maiúsculas.'''

for fruta in frutas:
    print(fruta.upper())
    

'''6. Operações com Tuplas
Dada a tupla:'''
coordenadas = (10, 20)
#Crie uma nova tupla chamada nova_coordenada que some 5 ao valor de cada coordenada.

nova_cordenada = (coordenadas[0] + 5, coordenadas[1] + 5)
print(nova_cordenada)


'''7. Conjuntos - Operações
Dado os conjuntos:'''
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
#Encontre a união dos dois conjuntos.
print(set1|set2)
#Encontre a interseção dos dois conjuntos.
print(set1 & set2)
#Encontre os elementos que estão em set1 mas não em set2.
print(set1 - set2)


'''8. Dicionários e Loops
Dado o dicionário:'''
notas = {"João": 8.5, "Maria": 9.0, "Pedro": 7.5}
#Itere sobre o dicionário e exiba:
"João tirou 8.5"
"Maria tirou 9.0"
"Pedro tirou 7.5"

for aluno in notas:
    print(f'{aluno} tirou {notas[aluno]}')
  


'''9. Listas dentro de Dicionários
Crie um dicionário onde as chaves são os nomes de três alunos e os valores são listas com suas três últimas notas.'''

#Calcule a média de cada aluno e exiba o nome e a média.

notas = {"João": [8.5, 9.0, 7.0], "Maria": [8.0, 6.0, 7.3], "Pedro": [10.0, 9.2, 5.0]}

for aluno in notas:
    soma = 0
    for nota in notas[aluno]:  # Itera pelas notas do aluno
        soma += nota
    media = soma / len(notas[aluno])  # Calcula a média
    print(f"{aluno} tem média {media:.2f}")


#10. Misturando todos
#Crie um programa que:

#Leia do usuário o nome de 3 frutas e armazene em uma lista.
#Crie um dicionário com a chave "frutas" que aponta para essa lista.
#Converta a lista em um conjunto para remover duplicatas, caso existam.

num_frutas = 0

Lista_frutas = []
while num_frutas < 3:
    fruta = input('Digite um nome de uma fruta: ')
    Lista_frutas.append(fruta)
    num_frutas += 1

print(Lista_frutas)

frutas = {"Frutas": Lista_frutas}

print(frutas)

conjunto_frutas = set(Lista_frutas)

print(conjunto_frutas)