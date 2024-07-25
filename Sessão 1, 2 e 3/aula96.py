#Desempacotamento em chamadas
#de métodos e funções

string = 'ABCD'
lista = ['maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'python', 'é', 'legal'

#a, b, c, *_ = lista
#print(a, c)

#primeiro, b, *_,antepenultimo, ultimo = lista
#print(primeiro, ultimo, antepenultimo)
'''
for nome in lista:
    print(nome, end=' ')'''
    
print('maria', 'Helena', 1, 2, 3, 'Eduarda')
print(*lista) # passando cada item da lista separadamente
print(*string) # passando cada item da lista separadamente
print(*lista, sep='\n')
print(*lista, end='\n')