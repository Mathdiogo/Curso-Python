# operadores in e not in
#Strings são iteráveis
# 0 1 2 3 4 5
# o t á v i o
#-6-5-4-3-2-1

nome = 'otávio'
print(nome[2]) #acessando a letra á pelo seu indice

nome2 = 'Matheus'
print(nome2[3])
print(10 * '-')

print('á' in nome) # Se á esta contido dentro de nome (otávio)
print('á' in nome2)
print(10 * '-')


print('vio' in nome)
print('zero' in nome)
print(10 * '-')
print('vio' not in nome)
print('zero' not in nome)