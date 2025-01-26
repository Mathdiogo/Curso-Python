def busca_binaria(lista, valor):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == valor:
            return meio
        elif lista[meio] > valor:
            fim = meio - 1
        else:
            inicio = meio + 1

    return -1

lista = [1, 3, 5, 7, 9, 11]
print(busca_binaria(lista, 7))
