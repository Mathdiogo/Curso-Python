'''Como você cria um loop infinito com while?'''

# Fazendo uma condição que sempre será atendida (que nunca falhe)
# Dessa maneira, nunca terá uma condição para que saia do loop

#EXP:

i=0

while i < 10:
    i -= 1
    print(i) #Cuidado ao tentar rodar o código! Loop infinito! :)