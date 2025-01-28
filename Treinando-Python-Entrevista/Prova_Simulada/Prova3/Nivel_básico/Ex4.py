def eh_primo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            return False
        else:
            return True

print(eh_primo(7))  # Deve retornar True
