'''Escreva uma função que retorne o maior valor entre dois números.'''

def retorna_maior_valor(v1, v2):
    try:
        if float(v1) > float(v2):
            return print(f"O maior valor é {v1}")
        else:
            return print(f"O maior valor é {v2}")

    except ValueError:
        print("É necessário que o valor inserido seja um numero e não uma string")


def main():
    valor1 = input("Digite o primeiro valor: ")
    valor2 = input("Digite o segundo valor: ")
    retorna_maior_valor(valor1, valor2)

main()