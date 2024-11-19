<<<<<<< HEAD
# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" (índice) e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }

pessoa = {

    'nome': 'Matheus',
    'sobrenome': 'Diogo Teixeira',
    'idade': 23,
    'altura': 1.81,
    'endereços': [
        {'rua': 'Rua ana augusto', '289': 12},
        {'rua': 'Rua Antônio Carlos Comitre', '155': 0}
    ]
}
#pessoa2 = dict(nome='Rayssa', sobrenome='Lopes') # Outro modo de criar um dicionario 
# da mesma forma que a superior

print(pessoa['nome'])
print(pessoa['endereços'])
print(pessoa['idade'])

print()
print()

for chave in pessoa:
=======
# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" (índice) e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }

pessoa = {

    'nome': 'Matheus',
    'sobrenome': 'Diogo Teixeira',
    'idade': 23,
    'altura': 1.81,
    'endereços': [
        {'rua': 'Rua ana augusto', '289': 12},
        {'rua': 'Rua Antônio Carlos Comitre', '155': 0}
    ],
}
#pessoa2 = dict(nome='Rayssa', sobrenome='Lopes') # Outro modo de criar um dicionario 
# da mesma forma que a superior

print(pessoa['nome'])
print(pessoa['endereços'])
print(pessoa['idade'])

print()
print()

for chave in pessoa:
>>>>>>> 30259dc (Adiciona arquivos da Sessão 4)
    print(chave, pessoa[chave])