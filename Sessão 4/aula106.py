'''
Argumentos nomeados e não nomeados em funções python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
'''

def soma(x,y,z):
    #Definição
    print(f'{x=} y={y} z={z}', '|', 'x + y + z = ', x + y + z)
    
soma(1, 2, 3)
soma(x=1, y=2, z=3)
soma(1, 2, z=5) #todos os valores depois de um argumento nomeados (z=5) todos os proximos argumentos precisam ser nomeados
