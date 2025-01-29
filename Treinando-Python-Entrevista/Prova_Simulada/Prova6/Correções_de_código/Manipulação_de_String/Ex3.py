'''dados = {"nome": "Carlos", "idade": 30, "profissao": None}
if dados["profissao"]:
    print("Profissão definida")
else:
    print("Profissão não definida")  # O que é impresso?'''
    
dados = {"nome": "Carlos", "idade": 30, "profissao": None}
if dados["profissao"]:
    print("Profissão definida")
else:
    print("Profissão não definida")  # O que é impresso?
    
    # É impresso "Profissão não definida", pois por mais que a chave profissão exista
    # no dicionário, essa chave não contem valor (None), portando não entra no if dados["profissão"],
    # ja que None é considerado como false em um if