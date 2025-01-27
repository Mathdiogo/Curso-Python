'''1. Operações Simples
Crie um programa que:

Solicite ao usuário dois números.
Pergunte qual operação matemática ele deseja realizar (+, -, *, /).
Retorne o resultado da operação.'''

def calcular(numero1, numero2):
    operador = input("Digite o caracter de qual operação deseja realizar? + - * / ")
    try:
        if operador == '+':
            resultado = numero1 + numero2
            print(resultado)

        if operador == '-':
            resultado = numero1 - numero2
            print(resultado)
        
        if operador == '*':
            resultado = numero1 * numero2
            print(resultado)
            
        if operador == '/':
            resultado = numero1 / numero2
            print(resultado)
    except ZeroDivisionError:
        print("O denominador da divisão não pode ser zero")
    
            
            
        
def main():
    
    num1 = float(input("Digite o primeiro numero para realizar uma operação matemática: "))
    num2 = float(input("Digite o segundo numero para realizar uma operação matemática: "))
    
    print(num1, num2)

    calcular(num1, num2)
        


main()