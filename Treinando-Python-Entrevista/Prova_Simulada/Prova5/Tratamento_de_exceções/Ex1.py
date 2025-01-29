'''O que o código abaixo faz?'''

try:
    x = int("abc")
except ValueError:
    print("Erro de valor!")

# o código abaixo tenta converter uma string em um valor inteiro e atribuir a uma variavel, porem o valor "abc" não é
# um valor possivel de se converter para um inteiro, por essem motivo entra no except ValueError 
# e a mensagem "Erro de valor!"" é exibida