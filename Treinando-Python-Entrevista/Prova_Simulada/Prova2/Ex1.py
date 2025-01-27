def soma_numeros(Lista):
    soma = 0
    for numero in Lista:
        if numero % 2 == 0:
            soma += numero
    print(soma)
            
    
def main():

    Lista = []
    numero = None
    while numero != 0:
        numero = int(input('Digite numero para adicionar a lista, para terminar digite uma letra: '))
        Lista.append(numero)
        print(Lista)
    
    soma_numeros(Lista)
    
    
main()