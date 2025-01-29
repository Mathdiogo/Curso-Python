'''# Função com parâmetro opcional
def saudacao(nome, mensagem="Olá"):
    print(mensagem, nome)

saudacao("João")
saudacao("Maria", "Bom dia")
saudacao("Pedro", "Boa noite", "!")'''

# Função com parâmetro opcional
def saudacao(nome, mensagem="Olá", opcional = None):
    print(mensagem, nome, opcional)

saudacao("João")
saudacao("Maria", "Bom dia")
saudacao("Pedro", "Boa noite", opcional="!")