'''def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Divisão por zero!"
    except:
        return "Erro desconhecido"

print(dividir(10, 0))
print(dividir("10", 2))  # O que acontece aqui?'''


def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Divisão por zero!"
    except TypeError:
        return "Tipo de dado inserido está incorreto!"
    except:
        return "Erro desconhecido"

print(dividir(10, 0))
print(dividir("10", 2))  # O que acontece aqui?

# O primeiro print se da por uma divisão com denomidador 0, o que gera o erro division by zero, fazendo com
# que a função retorne "Divisão por zero!"

# O segundo print gera o retorno Erro desconhecido, mas na realidade a função tenta realizar uma conta
# com uma string e um numero inteiro, o que da o erro de valor inválido. Para corrigir isso, devemos
# adicionar o ValueError para avisar diretamente o erro caso o usuário coloque uma string ao ives de um
# numero