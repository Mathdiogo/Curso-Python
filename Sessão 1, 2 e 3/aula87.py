"""
Introdução ao desempacotamento 
"""

# nomes = ['maria', 'Helena', 'Luiz']

# nome1, nome2, nome3 = nomes

# print(nome2)

_, _, nome1, *resto = ['maria', 'Helena', 'Luiz'] #Uma convensão dos programadores python
#é que ao criar uma variavel que nao vai ser usada , coloca-se um _ underline (underscore) 
# variavel para sinalizar que ela nao vai ser utilizada

print(nome1)