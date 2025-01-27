'''3. Palíndromos
Crie um programa que determine se uma palavra ou frase é um palíndromo (lê-se da mesma forma de trás para frente).
Exemplo:
Entrada: "arara"
Saída: "É um palíndromo"
Entrada: "python"
Saída: "Não é um palíndromo"'''

def ehpalindromo(palavra):
    print(len(palavra))
    tamanho = len(palavra)
    Lista_letras_iguais = []
    while tamanho > 1:
        if palavra[0] == palavra[-1]:
            print(palavra[0])
            print(palavra[-1])
            tamanho -= 1 
            Lista_letras_iguais.append(palavra[0])
                
            

    
def main():
    palavra = str(input('Digite uma palavra para verificar se é palindromo: '))
    ehpalindromo(palavra)

main()