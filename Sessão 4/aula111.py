'''
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
'''

# Lembrete sobre desempacotamento
x, y, *resto = 1, 2, 3, 4 # apenas alguns valores me interessam, o resto eu empacoto em resto
print(x, y, resto)

#de soma(x, y):
#   return x + y

def soma(*args):
    #print(args, type(args))
    total = 0
    for numero in args:
        print('total', total, numero)
        total = total + numero
        print('total', total)
    print(total)
    
soma(1, 2, 3, 4, 5, 6)