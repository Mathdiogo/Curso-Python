def somar_elementos(lista):
    """
    Função que recebe uma lista de números e retorna a soma de seus elementos.
    """
    soma = 0
    #Para cada numero dentro da lista passada pora rgumento,
    #somara o numero inicial 0 com o primeiro numero da lista [1 2 3 4] 0+1 = 1, agora soma = 1
    #Segundo item da lista seria o 2, entao soma = 1 + 2, soma agora é 3 e assim por diante, totalizando soma = 10
    for numero in lista:
        soma += numero
    return soma

def calcular_media(lista):
    """
    Função que calcula a média de uma lista de números.
    """
    #Total recebe o "valor de soma da cunção somar_elementos"
    total = somar_elementos(lista)
    #A média seria o valor total = soma / numero de elementos na lista
    media = total / len(lista)
    return media

def main():
    """
    Função principal que solicita ao usuário uma lista de números e calcula a média.
    """
    Lista = []
    entrada = input("Digite os números separados por espaço: ")
    #Para cada numero da entrada,(esta separado pelos proprios espaços digitados na entrada)
    # Cada numero é adicionaddo a lista Lista[] como int, assim será possivel realizar as contas com 2 valores int
    #Antes o bug esstava acontecendo pois estavamos tentando realizar uma operação com uma string e um int
    for numero in entrada.split():
        Lista.append(int(numero))
    
    print("A média dos números é:", calcular_media(Lista))

main()

''' 1 Qual é a diferença entre uma lista e um conjunto (set) no Python?
Lista: Permite elementos duplicados e mantém a ordem de inserção. Exemplo: [1, 2, 2, 3].
Set: Não permite elementos duplicados e não mantém a ordem. Exemplo: {1, 2, 3}.
 Se tentar adicionar 2 novamente, ele será ignorado.
Resumo: Use listas quando a ordem importa ou duplicados são necessários.
 Use sets para garantir que os elementos sejam únicos.'''

''' 2 O que significa desempacotamento de variáveis em Python e como utilizá-lo?
O desempacotamento permite atribuir valores de uma sequência (como lista ou tupla) diretamente a variáveis.
 Exemplo:

a, b, c = [1, 2, 3]
print(a, b, c)  # Saída: 1 2 3
Também pode ser usado com * para capturar múltiplos valores:

a, *b = [1, 2, 3, 4]
print(a)  # Saída: 1
print(b)  # Saída: [2, 3, 4]'''


'''Explique o conceito de herança em programação orientada a objetos e como implementá-la no Python.
Herança: Permite criar uma nova classe (filha) baseada em uma classe existente (pai), 
reutilizando seus métodos e atributos.

Exemplo:

class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def som(self):
        pass  # Método genérico

class Cachorro(Animal):
    def som(self):
        return "Latido!"

cachorro = Cachorro("Rex")
print(cachorro.nome)  # Saída: Rex
print(cachorro.som())  # Saída: Latido!'''