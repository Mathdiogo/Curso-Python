'''numeros = [10, 20, 30, 40, 50]
numeros[5] = 60  # Tentativa de alterar um índice que não existe

meu_set = {1, 2, 3, [4, 5]}  # Conjuntos não permitem elementos mutáveis como listas

dados = {"nome": "Maria", "idade": 25}
print(dados["profissao"])  # Tentativa de acessar uma chave inexistente'''


numeros = [10, 20, 30, 40, 50]
#éra impossivel acessar um valor edntro da lista que nao existe, para isso eu adicionei o valor a lista
numeros.append(60)
print(numeros)

meu_set = {1, 2, 3, 4, 5}  
print(meu_set)
#Os valores 4 e 5 n podiam estar dentro de uma lista que esta dentro de um set, set's podem ter apenas 1 tipo de dado, e sao imutaveis

dados = {"nome": "Maria", "idade": 25}
dados['profissao'] = 'Professora'
print(dados["profissao"])  
# Eu nao poderia acessar a profissao de maria sendo que eu n tinha adicionado o par chave valor da profissao dentro do dicionario
