'''try:
    lista = [1, 2, 3]
    print(lista[3])
except ValueError:
    print("Índice inválido!")'''
    
    
try:
    lista = [1, 2, 3]
    print(lista[2])
except ValueError:
    print("Índice inválido!")
    
    
    #Como o indice começa em 0, a tentativa de exibir o indice 3 em uma lista com 3 elementos dara um erro,
    # ja que o indice do terceiro elemento é o indice 2