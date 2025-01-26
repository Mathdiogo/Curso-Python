def soma_lista(valores):
    resultado = 0
    for valor in valores: # Se o valor for negativo, faz algo errado aqui
            resultado += valor
    return resultado

# Teste
print(soma_lista([1, -2, 3, -4, 5]))  # Esperado: 3 (1 + -2 + 3 + -4 + 5)
