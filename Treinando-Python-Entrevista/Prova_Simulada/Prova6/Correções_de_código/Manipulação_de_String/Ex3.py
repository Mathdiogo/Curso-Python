'''palavra = "Hello"
palavra[0] = "h"
print(palavra)  # O que acontece?'''


palavra = "Hello"
palavra = palavra.replace("H", "h")
print(palavra)  # O que acontece?

# Uma mensagem de erro, pois strings são do tipo imutaveis, para alterar o valor de uma string, 
# é necessário criar um nova string e atribuir a essa variável, e não modifica-la diretamente como
# no primeiro código