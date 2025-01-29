'''def multiplicar_por(fator):
    def multiplicar(numero):
        return numero * fator
    return multiplicar

dobro = multiplicar_por(2)
print(dobro(5))  # Output esperado: 10?'''

def multiplicar_por(fator):
    def multiplicar(numero):
        return numero * fator
    return multiplicar

dobro = multiplicar_por(2)
print(dobro(5))  # Output esperado: 10?

#Realmente a saida sera 10, 2 é passado como argumento para a função multiplicar_por
#Na primeira chama a função devolve numero * 2, quando no print passamos o numero 5 como parametro
#O numero 2 é lembrado pela função multiplicar_por, e o valor 5 é destinado a função multiplicar
# dessa forma 5 * 2 = 10