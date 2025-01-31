'''def contar_palavras(texto):
    palavras = texto.split(" ")
    contagem = {}
    
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] == 1  # Aqui está o possível bug
    
    return contagem

texto_teste = "python é incrível incrível python"
resultado = contar_palavras(texto_teste)
print(resultado)
'''


def contar_palavras(texto):
    palavras = texto.split(" ")
    print(palavras)
    contagem = {}
    
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1 
    
    return contagem

texto_teste = "python é incrível incrível python"
resultado = contar_palavras(texto_teste)
print(resultado)



