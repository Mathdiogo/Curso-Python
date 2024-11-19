<<<<<<< HEAD
# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import copy

pessoa = {
    
    'nome': 'Matheus',
    'sobrenome': 'Diogo Teixeira',
    
}

d1 = {
    
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

#d2 = d1 #D2 aponta pro mesmo dicionário que d1, n copia os dados
d2 = d1.copy() #cria uma cópia rasa (dados imutáveis) para a linha de baixo nao alterar os dados do dicionario d1
#Ele nao entra em subniveis (ele n entra dentro da lista pra ver ou pegar os valores, ele ve apenas a lista em si)
d2['c1'] = 1000
d2['l1'][1] = 9999 # altera nos 2 dicionários 

print(d1)
print(d2)

print()
print()

d2 = copy.deepcopy(d1) #agora ele cria uma cópia com os valores da lista tambem!

print(d2)
=======
# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import copy

pessoa = {
    
    'nome': 'Matheus',
    'sobrenome': 'Diogo Teixeira',
    
}

d1 = {
    
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

#d2 = d1 #D2 aponta pro mesmo dicionário que d1, n copia os dados
d2 = d1.copy() #cria uma cópia rasa (dados imutáveis) para a linha de baixo nao alterar os dados do dicionario d1
#Ele nao entra em subniveis (ele n entra dentro da lista pra ver ou pegar os valores, ele ve apenas a lista em si)
d2['c1'] = 1000
d2['l1'][1] = 9999 # altera nos 2 dicionários 

print(d1)
print(d2)

print()
print()

d2 = copy.deepcopy(d1) #agora ele cria uma cópia com os valores da lista tambem!

print(d2) 
>>>>>>> 30259dc (Adiciona arquivos da Sessão 4)
