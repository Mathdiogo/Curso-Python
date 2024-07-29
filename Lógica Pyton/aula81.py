"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40, 50, 60]
#numero = lista[2] #acessando o valor do indice 2 da minha lista por meio de uma variável
#print(numero)
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])

lista.append(70) #Adicionando um item a minha lista
lista.append(80)
#lista.pop() Removendo ultimo item da lista
ultimo_valor = lista.pop()
lista.append(90)
Remover_valor_escolhido = lista.pop(2) #Removendo 30
print(lista, 'Removido, ', ultimo_valor, 'Valor escolhido', Remover_valor_escolhido)