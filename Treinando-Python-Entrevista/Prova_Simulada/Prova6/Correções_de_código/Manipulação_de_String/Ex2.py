'''lista = [[1, 2], [3, 4]]
nova_lista = lista.copy()
nova_lista[0][0] = 100
print(lista)  # O que será impresso?'''

lista = [[1, 2], [3, 4]]
nova_lista = lista.copy()
nova_lista[0][0] = 100
print(lista)  # O que será impresso?

# Sera impresso [[100, 2], [3, 4]], pois foi realizada uma cópia rasa da lista na nova_lista
# Quando uma alteração é feita em nova_lista, essa alteração também se aplica para lista
# Portando, quando é colocado nova_lista[0][0] = 100, estamos acessando o primeiro item
# da lista que é a primeira lista [1,2] e alterando o primeir elemento dessa lista para 100
# totalizando a lista final [[100, 2], [3, 4]]