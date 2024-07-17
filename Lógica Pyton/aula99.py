"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = input("Digite um cpf (apenas números) para verificação: ")#929.934.680-14
if len(cpf) != 11 or not cpf.isdigit():
    print("CPF inválido, por gentileza digite um cpf com 11 dígitos numéricos")
else:
    digitos = []
    for digito in cpf[:9]: #para cada digito do cpf pegando apenas os 9 primeiros digitos
        digitos.append(int(digito))# adicionar cada digito em uma lista
       
print('Digitos do cpf: ', digitos) #printando os digitos do cpf        
multi = 10
while multi > 1:
    operacao = []
    for numero in digitos:
        operacao.append(numero*multi)
        multi -= 1
        
print('Resultado da operação: ', operacao)        
resultado = 0
for numero in operacao:
    resultado += numero
    
print('Resultado da soma: ', resultado)

resultado *= 10 #Multiplicando resultado por 10
resto = resultado % 11
print('Resto: ', resto)

if resto > 9:
    resultado = 0
    primeiro_digito = resultado
    print('Primeiro dígito: ', primeiro_digito)
else:
    primeiro_digito = resto
    print('Primeiro dígito: ', primeiro_digito)
