'''
Faça um programa que peça ao usuário para digitar um numero inteiro,
informe se este numero é par ou ímpar. Caso o usuario nao digite um numero inteiro,
informe que nao é um numero inteiro
'''
entrada = input('Digite um Número inteiro: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'
    
    if par_impar:
        par_impar_texto = 'par'
        
    print(f'O número {entrada_int} é {par_impar_texto}')
    
else:

    print('Você não digitou um número inteiro')
    
        








'''
Faça um programa que pergunte a hora do usuario e, baseando-se no horário
descrito, exiba a saudação apropriada Ex:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
'''











'''
Faça um programa que peça o primeiro nome do usuario. Se o nome tiver 4 letras ou
menos escreva "seu nome é curto; se tiver entre 5 e 6 letras, escreva 
"seu nome e normal", maior que 6 letras escreva "Seu nome é grande".
'''