'''Qual a diferença entre except e finally no tratamento de exceções?'''

"""
O bloco except é executado quando ocorre uma exceção, ou seja, algo não aconteceu como esperado.
Ele é responsável por tratar o erro e evitar que o programa pare inesperadamente.
Já o bloco finally é executado sempre, independentemente de ocorrer um erro ou não.
Ele é útil para ações que devem ser realizadas independentemente do sucesso ou falha,
como fechar arquivos ou liberar recursos.

try:
    x = int(input("Digite um número: "))
except ValueError:
    print("Erro: Você deve digitar um número válido!")
finally:
    print("Este bloco será executado sempre, independentemente de erro.")


"""