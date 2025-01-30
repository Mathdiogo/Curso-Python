def impar_par():
    # O loop while tru é usado para quando o usuário deseja encerrar a verificação ele digita uma letra
    # Caso contrário o programa se repetirá diversas vezes enquanto o usuário decidir verificar numeros
    while True:
        #o Try está sendo utilizado para pegar o erro ValueError caso coloque um valor inválido em numero
        try:
            # Aqui recebemos a entrada do usuário
            numero = input("Digite um número para verificar se é par ou ímpar ou uma letra para encerrar: ")
            # Uma verificação se o valor de numero ém compativel com a conta a ser realizada
            numero = int(numero)
            # Se o numero for divisível por 2 com resto = 0, ele é par
            if numero % 2 == 0:
                print("Esse número é par")
            # Caso contrário o numero é impar
            else:
                print("Esse número é ímpar")
        # Aqui captamos o erro caso o valor de numero para realizar a conta numero % 2 foi invalido,
        # pois até conseguimos inserir uma string em int(numero), porem não será possivel realizar a conta
        except ValueError:
            print("Programa encerrado, caractere digitado não é um número")
            #Caso o erro seja captado, o programa é encerrado!
            break

impar_par()

        
        
        
