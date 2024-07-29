""" Calculadora com while """

while True:
    sair = input('Quer sair? [s]im: ')
    sair = sair.lower() #sair.lowe retorna a mesma strig eviada em sair porem em letras minusculas
    sair = sair.startswith('s') #startswith pra ver se começa com alguma letra ou endswith se termina com alguma letra
    
    if sair is True:
        break
    
'''
while True:
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break
'''