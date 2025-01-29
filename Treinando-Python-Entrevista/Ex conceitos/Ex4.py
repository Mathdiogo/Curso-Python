def lista_ordenada():
    lista = []

    # Coletar 5 números do usuário
    for _ in range(5):
        numero = input("Digite um número: ")
        lista.append(int(numero))
        print(f"Lista atual: {lista}")
    
    # Criar uma lista ordenada
    lista_ordenada = []

    for numero in lista:
        if not lista_ordenada:
            lista_ordenada.append(numero)  # Adiciona o primeiro número diretamente
        else:
            # Inserir o número na posição correta
            for i, valor in enumerate(lista_ordenada):
                if numero < valor:
                    lista_ordenada.insert(i, numero)
                    break
            else:
                # Se não encontrar um valor maior, adiciona ao final
                lista_ordenada.append(numero)

    print(f"Lista ordenada: {lista_ordenada}")


lista_ordenada()
