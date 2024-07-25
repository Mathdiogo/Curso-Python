import random
cpf_criado = 0
for _ in range(10):
    cpf_criado += 1
    cpf_gerado = ''
    for i in range(9):
        cpf_gerado += str(random.randint(0, 9))
    print('CPF', cpf_criado)
    print(cpf_gerado)

    digitos = []
    for digito in cpf_gerado: #para cada digito do cpf pegando apenas os 9 primeiros digitos
        digitos.append(int(digito))# adicionar cada digito em uma lista
            
                
    multi = 10
    while multi > 1:
        operacao = []
        for numero in digitos:
            operacao.append(numero*multi)
            multi -= 1
                
    resultado = 0
    for numero in operacao:
        resultado += numero

    resto = (resultado * 10) % 11

    if resto > 9:
        resultado = 0
        primeiro_digito = resultado
    else:
        primeiro_digito = resto
        
    cpf_dez_digitos = str(cpf_gerado) + str(primeiro_digito)
    print('CPF com primeiro digito gerado: ', cpf_dez_digitos)
        
    cpf_primeiro_digito_verficado = []
    for digito in cpf_dez_digitos: #para cada digito do cpf pegando apenas os 10 primeiros digitos
        cpf_primeiro_digito_verficado.append(int(digito))# adicionar cada digito em uma lista       

    multi = 11
    while multi > 1:
        segunda_operacao = []
        for numero in cpf_primeiro_digito_verficado:
            segunda_operacao.append(numero*multi)
            multi -= 1   
            
    resultado2 = 0
    for numero in segunda_operacao:
        resultado2 += numero
        
    resto2 = (resultado2 * 10) % 11

    if resto2 > 9:
        segundo_digito = 0
    else:
        segundo_digito =  resto2
        
    cpf_onze_digitos = str(cpf_gerado) + str(segundo_digito)
    print('CPF com segundo digito gerado: ', cpf_onze_digitos)    
    cpf = f'{cpf_gerado}{primeiro_digito}{segundo_digito}'
    print('CPF completo: ', cpf)
    print('\n')
