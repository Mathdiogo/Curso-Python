'''try:
    arquivo = open("arquivo_inexistente.txt", "r")
    conteudo = arquivo.read()
    arquivo.close()
except FileNotFoundError:
    print("Arquivo não encontrado!")
except:
    print("Erro ao fechar o arquivo?")'''
    
    
try:
    arquivo = open("arquivo_inexistente.txt", "r")
    conteudo = arquivo.read()
    arquivo.close()
except FileNotFoundError:
    print("Arquivo não encontrado!")
except:
    print("Erro ao fechar o arquivo?")
    

