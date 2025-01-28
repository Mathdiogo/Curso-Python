'''Escreva um código que verifica se a chave "nome" está presente no dicionário:'''

dados = {"idade": 25, "cidade": "São Paulo"}

try:
   print(f"O nome é {dados['nome']} no dicionário dados")
except:KeyError
print("'nome' não esta incluso no dicionário")
