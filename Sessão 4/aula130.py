# Exemplo de uso dos sets

letras = set()
numero_tentativas = 0

while True:
    letra = input('Digite uma letra até encontrar a letra correta: ')
    letras.add(letra.lower())
    
    if 'l' in letras:
        print('parabens, vc encontrou a letra')
        print('Você tentou', numero_tentativas, 'vezes até acertar')
        break
    else:
        numero_tentativas += 1
        
    print(letras)