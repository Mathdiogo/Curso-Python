'''Parte 1: Perguntas Teóricas'''
'''Como você cria e acessa chaves e valores em um dicionário no Python?'''
'''dicionário = {'nome': 'Matheus', 'idade':23}

print(dicionário.get('nome'))
print(dicionário.get('idade'))''''''

Explique a diferença entre break e continue em um loop.
Lista = [1, 2, 3, 4, 5]         No uso do Break, se o numero for 3, sai do loop
                                No uso do continue, se o numero for 3, pula o 3 e n sai do loop
For num in Lista:
    if num == 3 
        Break/Continue
Qual é a diferença entre @staticmethod e @classmethod em uma classe no Python?'''
#Classmethod: Método precisa estar vinculado a uma class, acessa atributos da classe
#Statcmethod: Método não precisa estar vinculado nem a uma classe nem a uma instancia, não tem acesso a atributos
'''Como você verifica se um valor existe em uma lista?'''
# Lista = [1,2,3]
    # if 2 in Lista
        #print('Valor está na lista)


#código com bug
'''def verificar_paridade(lista_numeros):
    # Cria uma lista para armazenar os números pares
    numeros_pares = []
    
    for numero in lista_numeros:
        if numero % 2 == 0:
            numeros_pares.append(numero)
    
    return numeros_pares

def imprimir_pares(lista_pares):
    # Imprime todos os números pares formatados
    for numero in lista_pares:
        print(f"Número par: {numero}")

def main():
    numeros = input("Digite uma lista de números separados por vírgulas: ")
    lista_numeros = [int(numero) for numero in numeros.split(",")]  # Converte cada item para inteiro
    
    pares = verificar_paridade(lista_numeros)
    imprimir_pares(pares)

main()'''

#Código arrumado
def verificar_paridade(lista_numeros):
    # Cria uma lista para armazenar os números pares
    numeros_pares = []
    
    for numero in lista_numeros:
        if numero % 2 == 0:
            numeros_pares.append(numero)
    
    return numeros_pares

def imprimir_pares(lista_pares):
    # Imprime todos os números pares formatados
    for numero in lista_pares:
        print(f"Número par: {numero}")

def main():
    lista_numeros= []
    numeros = input("Digite uma lista de números separados por vírgulas: ")
    for numero in numeros.split(","):
        lista_numeros.append(int(numero))

    print(lista_numeros)
    
    pares = verificar_paridade(lista_numeros)
    imprimir_pares(pares)

main()
