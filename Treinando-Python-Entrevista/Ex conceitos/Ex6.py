"""
Iterando strings com while
"""
nome = 'Matheus Diogo'  # Iteráveis
lista_letras_nome = []

tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])

while tamanho_nome > 0:
    for letra in nome:
        lista_letras_nome.append(letra)
        tamanho_nome -= 1
    nome_final = "*".join(lista_letras_nome)
    print(nome_final)