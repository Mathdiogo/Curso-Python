def conta_vogal():
    print("Este programa contará o número de vogais na palavra digitada.")
    palavra = input("Digite uma palavra: ")
    vogais = "aeiou"

    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador += 1

    print(f"A palavra '{palavra}' contém {contador} vogais.")

conta_vogal()
