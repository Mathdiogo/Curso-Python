def soma_lista():
    lista = []
    
    for _ in range(5):
        numero = input("digite 5 valores para adicionar a lista: ")
        if numero.isdigit():
            lista.append(int(numero))
      
        else:
            print("Caracter digitado não é um numero")
        
    soma = sum(lista)
    print(soma)
    
soma_lista()