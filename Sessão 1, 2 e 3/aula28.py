'''
peça ao usuario para digitar seu nome
peça ao usuario para digitar sua idade
se nome e idade forem digitados:
    exiba:
        seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
'''
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    
    if ' ' in nome:
        print('Seu nome possui espaços')
    else:
        print('Seu nome não possui espaços')
        
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primera letra do seu nome é {nome[0]}')
    print(f'a ultima letar do seu nome é {nome[-1]}')
else:
    print(f'Desculpe, você deixou campos vazios')
        
    