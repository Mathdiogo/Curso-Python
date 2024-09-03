# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

numero_da_pergunta = 0
Acertos = 0
Erros = 0  
for dicionario in perguntas:
    numero_da_pergunta += 1
    print("Pergunta", numero_da_pergunta,":", dicionario.get('Pergunta'))
    for indice, opcao in enumerate(dicionario.get('Opções')):
        print(f"Opção {indice}: {opcao}")
        
    Resposta = input("Digite uma Opção: ")
    
    opcao_escolhida = dicionario['Opções'][int(Resposta)]

    if opcao_escolhida == dicionario.get('Resposta'):
        print('Você Acertou!')
        Acertos += 1
        print(Acertos)
    elif opcao_escolhida != dicionario.get('Resposta'):
        print('Você Errou!')
        Erros += 1
    else:
        print('Opção inválida')
        
        
    print("---")
    
print(f'Você Acertou {Acertos} Perguntas de {numero_da_pergunta} perguntas')
print('Você Errou', Erros, 'Perguntas')
# opcoes = ['A', 'B', 'C'] Ou usamos a função enumerate para iterar dentro de opções dentro do dicionario
# ou utilizamos um contador manual que ao iterar, aumenta e percorre entre as posições
# indice = 0
# for opcao in opcoes:
#     print(f"Opção {indice}: {opcao}")
#     indice += 1
