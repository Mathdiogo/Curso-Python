"""
Clousure e funções que retornam outras funções
"""

# def criar_saudacao(saudacao, nome):
#     return f'{saudacao}, {nome}!'

# saudacao1 = criar_saudacao('Bom dia', 'Matheus')
# saudacao2 = criar_saudacao('Boa noite', 'Matheus')
# print(saudacao1)
# print(saudacao2)

# def criar_saudacao(saudacao, nome):
#     def saudar():
#         return f'{saudacao}, {nome}!'
#     return saudar()

# saudacao1 = criar_saudacao('Bom dia', 'Matheus')
# saudacao2 = criar_saudacao('Boa noite', 'Matheus')




# print(saudacao1)
# print(saudacao2)

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')




for nome in ['Maria', 'Rayssa', 'Matheus', 'João']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))