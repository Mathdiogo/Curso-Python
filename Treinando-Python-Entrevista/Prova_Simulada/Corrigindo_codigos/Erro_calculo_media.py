def calcular_media(notas):
    soma = 0
    for nota in notas:
        soma += nota
    return soma / len(notas) 

notas = [8, 7, 9, 6]
print(calcular_media(notas))
