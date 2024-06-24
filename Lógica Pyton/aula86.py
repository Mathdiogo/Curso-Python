'''
Exercício
Exiba os índices da lista
0 maria
1 Helena
2 Luiz
'''

lista = ['Maria', 'Helena', 'Luiz']
indice = 0

for nome in lista:
    print(indice, nome, type(nome))
    indice += 1
    
#OU

# lista = ['Maria', 'Helena', 'Luiz']
#lista.append('João')

# indices = range(len(lista))

# for nome in lista:
#     print(lista[indices], type(lista[indices]))
#     indice += 1
