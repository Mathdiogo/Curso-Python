'''contador = 0

def incrementar():
    contador += 1
    return contador

print(incrementar())  # O que acontece?'''

contador = 0

def incrementar():
    contador += 1
    return contador

print(incrementar())  # O que acontece?

'''
Acontecerá um erro, por conta que a variavel contador esta sendo criada fora do escopo da função
onde ela é utilizada, e a função em si está tentando alterar o valor de uma variavel global
'''