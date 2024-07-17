""" Calculadora com while """

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Digite o operador para realizar uma conta (+-/*): ')
    
    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
    except:
        numeros_validos = None
        
    if numeros_validos is None:
        print('Um ou mais dos numeros digitados são inválidos.')
        continue #Se os numeros forem None vai levar pro começo do loop novamente para perguntar outros numeros
    
    operadores_permitidos = '+-/*'
    
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break
    