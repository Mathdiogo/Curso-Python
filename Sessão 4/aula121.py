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

pessoa = {
    'nome': 'Matheus',
    'sobrenome': 'Diogo Teixeira',
}

#print(len(pessoa))
#print(pessoa.keys())
#print(list(pessoa.keys()))
# #print(list(pessoa.values()))
# print(list(pessoa.items()))

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa.setdefault('idade', None)# pra n gerar erro eu seto um valor padrao
#caso n exista a chave no dicionário
print(pessoa['idade'])


