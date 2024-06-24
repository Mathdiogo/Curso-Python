"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = 'virtuoso'
letras_acertadas = ''
Num_Erros = 0

while True:
    print("Jogo da palavra secreta! ")
    letra_digitada = input('Digite uma letra: ')
    
    
    if len(letra_digitada) > 1: #verificando se o usuário digitou apenas uma letra
        print('Digite apenas uma letra')
        continue #se colocou mais de uma letra volta pro começo do loop
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada #concatena as letras que estao dentro da palavra na variavel letras acertadas
    else:
        Num_Erros += 1 
        
    palavra_formada = ''
    for letra_secreta in palavra_secreta: #para cada letra secreta da palavra secreta
        if letra_secreta in letras_acertadas: #se a letra secreta esta dentro das letras acertadas
            palavra_formada += letra_secreta #estou concatenando as letras secretas q foram acertadas em uma variavel pra guardar essas string
        else:
            palavra_formada += '*' #estou concatenando o * para as letras que ainda não foram acertadas
    
    print('PALAVRA FOMRADA:', palavra_formada) #exibindo a palavra ja concatenada para exibir a palavra em apenas uma linha
        
    if palavra_formada == palavra_secreta:
        os.system('cls')#limpa o terminal
        print('VOCÊ GANHOU! PARABÉNS')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', Num_Erros)
        letras_acertadas = ''
        Num_Erros = 0
    
    