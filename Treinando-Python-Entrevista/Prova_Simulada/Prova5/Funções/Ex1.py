'''Qual a saída do código abaixo?'''

def soma(a, b=5):
    return a + b

print(soma(3))


#Saida será 8, pois o valor 3, é passado como argumento de posição, enquanto b, é um argumento inserido
#Dentro do contexto da função ja, com o valor 5 atribuido ao b 5+3=8