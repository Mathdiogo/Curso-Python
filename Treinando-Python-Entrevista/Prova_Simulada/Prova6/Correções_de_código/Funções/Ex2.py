'''def calcular_imc(peso, altura):
    return peso / (altura ** 2)

print(calcular_imc(70, 1.75))  # Funciona?
print(calcular_imc(1.75, 70))  # E aqui?'''

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

print(calcular_imc(70, 1.75))  # Funciona?
print(calcular_imc(1.75, 70))  # E aqui?

'''
Rodar o código rodaria nas duas chamadas da função calcular_imc, porém só vai calcular corretamente
o imc na primeira instancia da função. Por conta da ordem dos parâmetros. Ela deve ser respeitada
para que a conta seja realizada de maneira correta. Primeiro o peso e depois a altura!
'''