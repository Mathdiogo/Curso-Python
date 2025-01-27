'''numeros = [1, 2, 3, 4, 5]
pares = [num % 2 == 0 for num in numeros]
print(pares)
'''
#Aqui ele não está imprimindo os numeros pares de fato, e sim a resposta se o valor de um indice é par ou não
numeros = [1, 2, 3, 4, 5]
pares = []
for num in numeros:
    if num %2 == 0:
        pares.append(num)
print(pares)
