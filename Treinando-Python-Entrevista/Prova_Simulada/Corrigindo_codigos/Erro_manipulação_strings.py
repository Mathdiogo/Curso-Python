def contar_vogais(palavra):
    contador = 0
    for letra in palavra:
        if letra in ['a', 'e', 'i', 'o', 'u']:
            contador += 1
    return contador

# Teste
print(contar_vogais("python"))  # Esperado: 1
