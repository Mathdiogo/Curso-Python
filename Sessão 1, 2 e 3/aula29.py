'''
Introdução try/except
try -> tentar executar 
except -> ocorreu algum erro ao tentar executar
'''
#numero = input('Vou dobrar o numero que voce digitar: ')

'''numero_float = float(numero)
numero_float = float(numero)
print(f'O dobro de {numero} é {numero_float * 2:.2f}')
'''

numero_str = input('Vou dobrar o numero que voce digitar')

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
    
except:
    print('isso não é um número')
    