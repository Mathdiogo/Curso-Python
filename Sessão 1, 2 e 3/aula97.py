'''
Operação ternária (condicional de uma linha)
<valor> if <confição> else <outro valor>
'''
#print('valor' if True else 'outro valor')

# variavel = 'valor' if False else 'Outro valor'
# print(variavel)

# digito = 10 #se for < 9 fica o proprio valor, maior q 9 fica 0
#  novo_digito = digito if digito <=9 else 0
# novo_digito = 0 if digito > 9 else digito
# print(novo_digito)

print('valor' if False else 'outro valor' if False else 'Fim')
#Se a primeira condição for verdadeira mostra Valor
#Se a segunda condição for verdadeira mostra outro valor
#Se nao, mostra fim