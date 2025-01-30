'''texto = "Python é uma linguagem de programação"
partes = texto.split(" ")
nova_string = partes.join("-")
print(nova_string)  # Erro aqui?'''


texto = "Python é uma linguagem de programação"
partes = texto.split(" ")
nova_string = "-".join(partes)
print(nova_string)  # Erro aqui?
print(partes)