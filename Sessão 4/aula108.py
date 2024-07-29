"""
Retorno de valores das funções (retrun)
"""
x = 1


def escopo():
    #global x
    x = 10

    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)


print(x)
escopo()
print(x)