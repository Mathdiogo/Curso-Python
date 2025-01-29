'''Escreva um código que trate o erro de divisão por zero.'''

num = int(input("Digite o valor do numerador para realizar uma divisão: "))
denom = int(input("Digite o valor do denominador para realizar uma divisão: "))

try:
    resultado = num / denom
    print(resultado)
except ZeroDivisionError:
    print("Impossível realizar uma divisão com o denominador = 0 ")