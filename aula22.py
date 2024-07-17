# operadores lógicos
# and (e) or not(não)
# and - Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vo já viu)
# 0 0.0 '' False
#Também existe o tipo None que é
# usado para representar um não valor
'''
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')


senha_permitida = '123456'
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
'''
'''
senha = 0 or False or  0 or 'abc' or True
print(senha)
'''

senha = input('Senha: ') or 'sem senha'
print(senha)
