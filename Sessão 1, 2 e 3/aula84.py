"""
Cuidados com dados mutaveis
= - copiado o valor (imutaveis)
= - aponta para o mesmo valor na memória (mutável)
"""

# nome = 'Matheus'
# outra_variavel = nome
# nome = 'Rayssa'
# print(nome)
# print(outra_variavel)

# lista_a = ['Matheus', 'Rayssa']
# lista_b = lista_a

# lista_a[0] = 'qualquer coisa' #mesmo mudando a lista a, como lista b esta no mesmo 
# #endereço de memória, acaba gerando alterações tambem na lista b (por ser valor mutável)
# print(lista_b)

lista_a = ['Matheus', 'Rayssa']
lista_b = lista_a.copy()

lista_a[0] = 'qualquer coisa' #mesmo mudando a lista a, como lista b esta no mesmo 
#endereço de memória, acaba gerando alterações tambem na lista b (por ser valor mutável)
print(lista_a)
print(lista_b)