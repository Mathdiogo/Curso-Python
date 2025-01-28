# Inverta a ordem da lista:

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#    0  1  2  3  4  5  6  7  8  9   10  11  12  13  14
# Fim aqui representa o ultimo numero da lista, pois len(x) é o tamanho total da lista (15)
# O numero 15 que queremos acessar é o indice 14 da lista
# portando len(x) = 15 - 1 = 14 (onde esta o numero 15 de fato)
fim = len(x) - 1

    # Se a gente vai pergocrer com i o começo da lista e com fim o final da lista, precisamos então
    # apenas percorrer metade da lista, ja que vamos trocar as posições de i com fim
    # x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    # x = [15, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1]
    #     [fim]                                           [i]
    # por conta disso utilizamos len(x)//2
    # 2 barras // é para a divisão ser inteira, o len n aceitaria dividir por um não inteiro
for i in range(len(x)//2):
    # Se eu apenas trocar as x[i] com x[fim] por exemplo, vamos supor que eu coloco o x[fim] no x[i]
    # o 15 ficará na primeira posição e quando for fazer ao contrario e guardar i no fim,
    # i agora é 15 tambem, eu perdi o valor de x[i], por isso criei uma variavel auxiliar para
    # guardar o valor de x[i]
    aux = x[i]
    x[i] = x[fim]
    x[fim] = aux
    fim -= 1
    
print(x)