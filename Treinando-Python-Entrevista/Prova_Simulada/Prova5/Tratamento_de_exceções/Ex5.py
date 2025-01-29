'''Dado o código abaixo, o que será impresso?'''

try:
    print(10 / 0)
except ZeroDivisionError as e:
    print(f"Erro: {e}")

# Será Exibido Erro: division by zero