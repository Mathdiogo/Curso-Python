def impar_par():
    print("Digite um número para realizar a verificação ou uma letra para encerrar!")
    while True:
        try:
            numero = input("Digite um número para verificar se é par ou ímpar: ")
            if numero.isalpha():
                print("Programa encerrado, caractere digitado não é um número")
                break
            numero = int(numero)
            if numero % 2 == 0:
                print("Esse número é par")
            else:
                print("Esse número é ímpar")
        except ValueError:
            print("Programa encerrado, caractere digitado não é um número")
            break

impar_par()

        
        
        
