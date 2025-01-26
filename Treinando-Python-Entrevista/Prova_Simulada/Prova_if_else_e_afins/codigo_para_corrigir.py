def verificar_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    else:
        return True  # Possível erro aqui?

numero = int(input("Digite um número: "))
if verificar_primo(numero):
    print("O número é primo.")
else:
    print("O número não é primo.")
