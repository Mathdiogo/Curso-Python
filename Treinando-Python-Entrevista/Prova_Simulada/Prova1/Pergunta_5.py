'''Pergunta 5: Manipulação de Arquivos
Pergunta:
Explique o que o seguinte trecho de código faz. Qual seria o resultado esperado se o arquivo dados.txt não existir?'''

'''
#Arquivo com bug

Explicação: Ao tentar abrir o arquivo em modo apenas leitura, onde não será possivel realizar alterações no arquivo
caso o usuário não tenha esse arquivo no computador, acontecerá um erro e o código irá quebrar, por isso, adicionei
um try except para que o código nao quebre
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.readlines()'''



try:
    with open("dados.txt", "r") as arquivo:
        conteudo = arquivo.readlines()
except FileNotFoundError:
    print('Arquivo não encontrado')