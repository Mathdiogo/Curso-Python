'''Qual a diferença entre break e continue dentro de um laço?'''


'''
A diferença é que o continue ele ignora o processo atual que esta acontecendo,
porem no caso de um loop ele continuaria a proxima execução. Já um break ele interrompe completamente
a execução do processo atual, no caso de um loop, ele cancelaria o loop 
e pularia para a proxima estrutura

EXP:

Lista = [1,2,3,4,5]

for i in Lista          for i in Lista
    if i == 3               if i == 3
       continue                break
    
    pula a iteração         interrompe completamente o loop
    atual do 3, depois
    continua normalmente
'''