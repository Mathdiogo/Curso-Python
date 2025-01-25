'''Pergunta 3: Tratamento de Exceções
Pergunta:
Explique o que acontece neste código e como ele poderia ser corrigido:'''


try:
    resultado = 10 / 0
except ValueError as e:
    print("Erro de valor:", e)