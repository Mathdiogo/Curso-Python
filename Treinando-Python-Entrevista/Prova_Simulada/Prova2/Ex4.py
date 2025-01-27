'''try:
    with open("arquivo_inexistente.txt") as arquivo:
        conteudo = arquivo.read()
    print(conteudo)
except FileNotFoundError:
    print("Arquivo não encontrado!")
else:
    print("Leitura concluída com sucesso!")
finally:
    print("Operação finalizada.")
'''

try:
    with open("arquivo_inexistente.txt ") as arquivo:
        conteudo = arquivo.read()
    print(conteudo)
except FileNotFoundError:
    print("Arquivo não encontrado!")
else:
    print("Leitura concluída com sucesso!")
finally:
    print("Operação finalizada.")
