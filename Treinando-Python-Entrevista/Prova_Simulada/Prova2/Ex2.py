# Explique o que o seguinte bloco de código faz e como ele pode ser melhorado:

'''try:
    x = int(input("Digite um número: "))
    print(10 / x)
except:
    print("Erro!")'''


try:
    x = int(input("Digite um número: "))
    print(10 / x)
    
except ZeroDivisionError:
    print("Erro ao tentar dividir por 0!")