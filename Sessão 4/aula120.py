<<<<<<< HEAD
#Manipulando chaves e valores em dicionários (CRUD dicionário)

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

#criando mais um "argumento" dentro do meu dicionários quando ele ja esta pronto
pessoa['Trabalho'] = 'Desenvolvedor de software'
pessoa['Hobbie'] = 'Automobilismo'

print(pessoa)
print(pessoa['Trabalho'])

print()
print()

del pessoa['Hobbie']
print(pessoa)
print(pessoa['nome'])

print(pessoa['Hobbie'])

print('Isso não vai executar pq excluimos hobbie do dicionário, e vai dar um key error')

print(pessoa.get('Hobbie', 'Não existe chave ou None'))

if pessoa.get('Hobbie') is None:
    print('Chave não existe')
else:
=======
#Manipulando chaves e valores em dicionários (CRUD dicionário)

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

#criando mais um "argumento" dentro do meu dicionários quando ele ja esta pronto
pessoa['Trabalho'] = 'Desenvolvedor de software'
pessoa['Hobbie'] = 'Automobilismo'

print(pessoa)
print(pessoa['Trabalho'])

print()
print()

del pessoa['Hobbie']
print(pessoa)
print(pessoa['nome'])

print(pessoa['Hobbie'])

print('Isso não vai executar pq excluimos hobbie do dicionário, e vai dar um key error')

print(pessoa.get('Hobbie', 'Não existe chave ou None'))

if pessoa.get('Hobbie') is None:
    print('Chave não existe')
else:
>>>>>>> 30259dc (Adiciona arquivos da Sessão 4)
    print(pessoa['Hobbie'])