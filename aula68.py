""" Calculadora com while """

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Digite o operador para realizar uma conta (+-/*): ')
    
    numeros_validos = None
    
    numero_1_float = 0
    numero_2_float = 0
    
    resultado_soma = 0
    resultado_sub = 0
    resultado_div = 0
    resultado_multi = 0
    
    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True
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
    
    if operador == '+':
       resultado_soma = numero_1_float + numero_2_float
       print(f'{numero_1_float} + {numero_2_float} =',resultado_soma)
    elif operador == '-':
       resultado_sub = numero_1_float - numero_2_float 
       print(f'{numero_1_float} - {numero_2_float} =',resultado_sub)
    elif operador == '/':
        resultado_div = numero_1_float / numero_2_float
        print(f'{numero_1_float} / {numero_2_float} =',resultado_div)
    elif operador == '*':
        resultado_multi = numero_1_float * numero_2_float
        print(f'{numero_1_float} * {numero_2_float} =',resultado_multi)
    else:
        print('Nunca deveria chegar aqui.')
        
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break
    