'''Pergunta 2:
Explique o que faz o seguinte código e reescreva-o utilizando um loop tradicional:'''

# numeros = X^2 para quando x esta no rang de 0 a 5 e o resto da divisão de x por 2 = 0
# no caso x pode ser 0, 2 e 4 apenas
numeros = [x**2 for x in range(5) if x % 2 == 0]
print(numeros)

numeros = []
for x in range(5):
    if x % 2 == 0:
        numeros.append(x**2)
        
print(numeros)