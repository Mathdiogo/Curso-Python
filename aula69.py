"""while/else"""

string = "valor qualquer"

i = 0
while i <len(string):
    letra = string[i]
    
    if letra == " ":
        break
    
    print(letra)
    i+= 1

else:
    print('O else foi executado.')
print('Fora do while')#fora do while

#toda vez que encontra o break sai pra fora d while e n executa o break