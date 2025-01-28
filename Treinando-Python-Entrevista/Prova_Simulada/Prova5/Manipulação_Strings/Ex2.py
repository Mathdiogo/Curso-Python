'''Como você junta os elementos de uma lista em uma única string, separando-os por vírgulas?'''

lista = ['ola', 'bom', 'dia']

for palavra in lista:
    print(palavra.format(','))