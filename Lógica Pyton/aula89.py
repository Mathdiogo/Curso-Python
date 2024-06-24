"""
enumerate - enumera iteráveis (Índices)
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Matheus')

# lista_enumerada = enumerate(lista)

# for item in lista_enumerada:     
#     print(item)

#lista_enumerada = list(enumerate(lista)) #precisa converter para lista ou tupla
#se n ele mostra apenas o endereço de memória
#print(lista_enumerada)

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)


# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')