"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

lista_nome = []
lista_invertida = []
lista_maiusculas = []

tamanho_do_nome = len(nome)

def inverte_nome():
    for letras in nome:
        lista_nome.append(letras)
    while lista_nome:
        ultm_letra = lista_nome.pop()
        lista_invertida.append(ultm_letra)
        nome_invertido = ''.join(lista_invertida)
    print(lista_invertida)
    print(f"Seu nome invertido é: {nome_invertido}")
    
def contem_espacos():
    if " " in nome:
        print("contem espaço")
    else:
        print("Não contem espaços")
        
def primeira_ultima_letra():
    print(f"A primeira letra do seu nome é: {nome[0]}")
    print(f"A ultima letra do seu nome é: {nome[-1]}")
        
def tamanho_nome():
    print(f"O seu nome contem '{tamanho_do_nome}' caracteres")
    
def verifica_maiuscula():
    for letra in nome:
        if letra.isupper():
            maiuscula = True
            lista_maiusculas.append(letra)
            
    if maiuscula:
        num_maiusculas = len(lista_maiusculas)  
        print(f"Existem {num_maiusculas} letras maiúsculas no seu nome")
    else:
        print("Não existem letras maiusclulas no seu nome")

if nome and idade:
    print(f"Seu nome é {nome}")
    inverte_nome()
    contem_espacos()
    tamanho_nome()
    primeira_ultima_letra()
    verifica_maiuscula()
else:
    print("Repita o processo! Você deixou campos vazios. ")