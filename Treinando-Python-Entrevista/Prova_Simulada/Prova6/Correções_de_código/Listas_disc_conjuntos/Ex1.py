'''# Manipulação de listas
numeros = [1, 2, 3, 4, 5]
dobro = [x * 2 for x in numeros if x % 2 == 0]
print("O dobro dos números pares é:", dobro)

# Manipulação de dicionários
pessoa = {"nome": "Ana", "idade": 25}
print("Nome:", pessoa.nome)'''

# Manipulação de listas
numeros = [1, 2, 3, 4, 5, 6]
dobro = [x * 2 for x in numeros if x % 2 == 0]
print(f"O dobro dos números pares é: {dobro}")

# Manipulação de dicionários
pessoa = {"nome": "Ana", "idade": 25}
print("Nome:", pessoa.get('nome'))