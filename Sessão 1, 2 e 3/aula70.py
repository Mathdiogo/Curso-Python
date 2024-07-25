frase = 'O Python é uma linguagem de programação '\
        'multiparadigma. '\
        'Python foi criado por Guido van Rossum.'
        
i = 0
qntd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i+= 1
        continue #se eu nao colocar  i+= 1 ele vai ficar em um looping infinito e nao vai incrementar o i
    
    quantas_vezes_letra_apareceu_atual = frase.count(letra_atual)
    
    if qntd_apareceu_mais_vezes < quantas_vezes_letra_apareceu_atual:
        qntd_apareceu_mais_vezes = quantas_vezes_letra_apareceu_atual
        letra_apareceu_mais_vezes = letra_atual
    
    i += 1
    
    
print('A letra que apareceu mais vezes foi '
      f'"{letra_apareceu_mais_vezes}" que apareceu '
      f'{qntd_apareceu_mais_vezes}X')