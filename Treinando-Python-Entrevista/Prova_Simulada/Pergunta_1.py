'''Pergunta:
Escreva uma função chamada contar_palavras que recebe uma string e retorna a contagem de palavras.
Considere que as palavras são separadas por espaços.'''


def contar_palavras(frase):
    # Divide a frase em uma lista de palavras usando os espaços como separador
    palavras = frase.split(" ")
    # Retorna o número de palavras na lista
    return len(palavras)

def main():
    # Solicita uma frase ao usuário
    frase = input("Digite uma frase separada por espaços: ")
    # Chama a função contar_palavras e armazena o resultado
    num_palavras = contar_palavras(frase)
    # Exibe o número de palavras na frase
    print(f"O número de palavras na frase é: {num_palavras}")

main()
