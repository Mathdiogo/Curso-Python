import math

def calcular_area(raio):
    # Calcula a área de um círculo dado o raio pi*r^2
    return math.pi * raio ** 2

def imprimir_resultado(area):
    # Imprime o resultado formatado com 2 casas decimais
    print(f"A área do círculo é: {area:.2f}")

def main():
    #Coletando input do usuário como numero inteiro 
    raio = int(input("Digite o raio do círculo: "))
    #como raio não pode ser negativo (para verificação funcionar, comparação entre mesmos tipos de dados [int])
    if raio < 0:
        print("O raio não pode ser negativo.")
        return
    
    #O valor da área do círculo é armazenada na variavel área depois da func calcular área ter calculado com base
    #no rio passado como parâmetro
    area = calcular_area(raio)
    #chamada da função que vai executar um print formatado com 2 casas decimais
    imprimir_resultado(area)

#chamada da função main
main()
