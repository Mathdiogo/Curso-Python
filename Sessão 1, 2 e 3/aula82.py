"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Matheus')
nome = lista.pop()
lista.append(1233)
del lista[-1] # -1 sempre vai ser o ultimo item da lista, mesmo quando voce 
#não sabe quantos itens e qual dele eé o ultimo da sua lista
#lista.clear()
lista.insert(0, 5) #Adicionou 5 no indice 0 (primeiro elemento da lista)
lista.insert(0, 'Matheus')
print(lista)
# lista = ['Matheus', 5, 10, 20, 30, 40] no momento