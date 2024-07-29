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

cpf = input("Digite um cpf (apenas números) para verificação: ")#74682489070
if len(cpf) != 11 or not cpf.isdigit():
    print("CPF inválido, por gentileza digite um cpf com 11 dígitos numéricos")
else:
    digitos = []
    for digito in cpf[:9]: #para cada digito do cpf pegando apenas os 9 primeiros digitos
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
    
cpf_primeiro_digito_verficado = []
for digito in cpf[:10]: #para cada digito do cpf pegando apenas os 10 primeiros digitos
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

decimo_digito = int(cpf[9])    
decimo_primeiro_digito = int(cpf[10])

if decimo_digito == primeiro_digito and decimo_primeiro_digito == segundo_digito:
    print("CPF Válido! ")
else:
    print("CPF Inválido. ")
