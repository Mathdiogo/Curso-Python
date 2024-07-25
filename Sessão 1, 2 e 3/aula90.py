"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os

lista = []

while True:
    print('Selecione uma opção')
    print("[I]nserir")
    print("[A]pagar")
    print("[L]istar")
    print("[S]air")
    opcao = input()
    
    if opcao.lower() == 'i':
        os.system('cls')
        valor = input('Digite o item a ser inserido: ')
        lista.append(valor)
    elif opcao.lower() == 'a':
        indice_str = input('Escolha o índice para apagar: ')
        
        try:
            indice = int(indice_str)
            del lista[indice]
        except:
            print('Não foi possível apagar esse índice')
    elif opcao.lower() == 'l':
        os.system('cls')
        
        if len(lista) == 0:
            print('Lista vazia')
            
        for i, valor in enumerate(lista):
            print(i, valor)
    elif opcao.lower() == 's':
        break
    else:
        print('Opção selecionada inválida')
        