'''Prova de Estruturas de Controle de Fluxo
1. If, Else e Comparações
Crie um programa que solicite ao usuário sua idade e exiba:
"Menor de idade" se a idade for menor que 18.
"Maior de idade" se a idade estiver entre 18 e 60.
"Idoso" se a idade for maior ou igual a 60.'''
idade = int(input('Digite a sua idade: '))

if idade < 18:
    print('Menor de idade')
elif idade >= 18 and idade < 60:
    print('Maior de idade')
else:
    print('Idoso')
'''2. If e Verificações de Números
Escreva um código que solicite ao usuário um número inteiro e:
Verifique se o número é positivo, negativo ou zero.
Exiba a mensagem correspondente.'''
numero = int(input('Digite um número qualquer: '))

if numero > 0:
    print(f'O numero {numero} é positivo')
elif numero == 0:
    print(f'O numero é {numero}')
else:
     print(f'O numero {numero} é negativo')


'''3. Elif e Classificação
Crie um programa que solicite ao usuário uma nota (0 a 10) e exiba:
"Aprovado" para notas maiores ou iguais a 7.
"Em recuperação" para notas entre 5 e 6.9.
"Reprovado" para notas menores que 5.'''
nota = float(input('Digite a nota do aluno: '))

if nota >= 7:
    print('APROVADO')
elif nota > 5 and nota < 7:
    print('EM RECUPERAÇÃO')
else:
    print('REPROVADO')

'''4. For - Tabuada
Crie um programa que solicite ao usuário um número e exiba a tabuada desse número (de 1 a 10).'''

numero_tabuada = int(input('Digite um número para saber sua tabuada: '))

multiplicador = 1

for numero in range(10):
    resultado = numero_tabuada * multiplicador
    print(f'{numero_tabuada} * {multiplicador} =  {resultado}')
    multiplicador += 1


'''5. While - Contagem Regressiva
Implemente um programa que realize uma contagem regressiva de 10 até 0 e exiba "FIM!" ao final.'''

numero_contagem = 10
print('')
print('Iniciando contagem: ')
print('')
while numero_contagem != 0:
    print(numero_contagem)
    numero_contagem -= 1
    
print("FIM")
