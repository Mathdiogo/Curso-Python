'''# Tratamento de exceções
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print("O resultado é:", resultado)
except:
    print("Ocorreu um erro!")'''
    
    # Tratamento de exceções
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print("O resultado é:", resultado)
except ZeroDivisionError:
    print("Ocorreu um erro, impossivel dividir um número por!")
except ValueError:
    print('É neccesário digitar um número inteiro')
except Exception as e:
    print("Ocorreu um erro:", e)