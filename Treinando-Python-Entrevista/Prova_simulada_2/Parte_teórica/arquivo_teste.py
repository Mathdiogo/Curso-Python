a = input("Digite o primeiro número: ")
b = input("Digite o segundo número: ")

def soma(a,b):
    try:
        resposta = int(a) + int(b)
        print(f"A resposta da soma de {a} + {b} é igual a {resposta}")
        #Ou return resposta
    except TypeError:
        print("Tipo de dado inserido inválido")
    except ValueError:
        print("Valor inserido inválido")

soma(a, b)