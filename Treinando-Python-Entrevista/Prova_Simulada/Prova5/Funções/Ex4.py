'''Explique o que faz a compreensão de listas no código abaixo:'''

numeros = [x**2 for x in range(5)]
print(numeros)
'''Explicando com um for padrão'''
'''
Temos uma lista chamada numeros, para um tal valor x que pode ir de 0 a 5
eleve x ao quadrado e o resultado adicione na lista numeros
'''
numeros = [ ]
for x in range(5):
    x = x**2
    numeros.append(x)
print(numeros)