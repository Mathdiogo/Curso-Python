"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal

numero_1 = decimal.Decimal('0.1') #Usar função Decimal para numeros de ponto flutuante
#com muitas casas decimais onde a cona precisa ser extremamente precisa
#para extrema precisão usar em formato de string, mas normalmente usar como float funciona
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')# Retornando uma string (formatando numero em string)
#OU
print(round(numero_3, 2))# Recebe o numero + as casas decimais, se os numeros
#forem 0 ele não exibe. (Retorna um numero de ponto flutuante)