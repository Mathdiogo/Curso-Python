'''Pergunta 3: Tratamento de Exceções
Pergunta:
Explique o que acontece neste código e como ele poderia ser corrigido:'''

#Código com erro
'''t"ry:
    resultado = 10 / 0
except ValueError as e:
    print("Erro de valor:", e)'''

#Aqui uma divisão pór 0 esta tentando ser executada, como sabemos que isso é "impossível", e que
#o denomidador não pode ser 0, tentamos utilizar o try except para tentar capturar o erro sem que 
# o código quebre, porem eestávamos coletando o erro de valor e não de divisão por 0
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print("Erro de valor:", e)