"""
faça um programa que peça ao usuário  para digitar  um numero inteiro, 
informe se esse numero é par ou impar. Caso  o usuário  nao digite  um núumero
inteiro, informe que  não  é um número inteiro
"""
try:
    numero_digitado = int(input('Digite um número inteiro: '))
    if numero_digitado % 2 == 0:
        print('Esse número é par')
    else:
        print('Esse número é ímpar')
except ValueError:
    print('Por favor, digite um número inteiro')


"""
faça um program que pergunta  a hora ao usuário, baseando-se no horário
descrito, exiba  a saudação apropriada EX:
Bom dia 0-11, boa tarde 12-17 e boa noite 18-23.
 """
horario = (input('Digite um horário (exemplo: 12, 16, 10 etc.): '))

if horario >= 0 and horario < 12:
    print("Bom dia")
elif horario >= 12 and horario < 18:
    print("Boa tarde")
elif horario >= 18 and horario < 24:
    print('Boa noite')
else:
    print('Não conheço esse horario')


"""
Faça um programa  que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva: "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva: Seu nome é normal;
maior que 6 escreva: Seu nome é grande
"""

nome = str(input('Digite seu nome: '))

if len(nome) <= 4:
    print('Seu nome é pequeno')
elif len(nome) > 4 and len(nome) <=6:
    print('Seu nome é normal')
else:
    print('Seu nome é grande')