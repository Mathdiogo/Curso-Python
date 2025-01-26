#Questões Teóricas/Práticas
#Conceito: Explique o que são os tipos de dados primitivos em Python. Cite exemplos de cada um.

'''
Tipos de dados são diferentes dados para diferentes tios de uso e necessidades. Um tipo int é para trabalhar especificamente com inteiros,
float ja abre um leque para trabalhar com numeros decimais, tipo boolean é basicamente um True or false e string para trabalhar com textos
'''

#Conversão: Qual é a diferença entre int() e float()? Dê exemplos de como cada um funciona.

'''
Int trabalha com numeros itneiros Exp; 1,2,3,4
float trabalha com numeros com casas decimais, 1.1, 2.6, 3.8, 4.3 etc
'''

#Booleanos: O que acontece quando convertemos os seguintes valores para booleanos em Python?

0 #False
1 #True
"" #False, qualquer string vazia retorna falso
"Python" #True, qualquer string não vazia retorna verdadeiro
None # Ausencia de valor

#Operações com Strings: Qual é o resultado da seguinte operação?
"Python" + " é legal " * 2
'''
python é legal é legal,  o *2 repete a string multiplicada
'''

#Comparação: O que será exibido ao executar o seguinte código?
x = 10
y = 20
print(x > y or x + 10 == y)
'''
True
'''
#Floats: Por que o seguinte código não exibe True?
print(0.1 + 0.2 == 0.3)
'''
Numeros de ponto flutuante como 0.2, 0.1 não podem ser representados exatamente como binários, 
então como o python nentende exatamente o valalor da soma como provavelmente 0.300000000000000004, ele não considera True, diferente
se fosse com numeros inteiros
'''


#Manipulação de Strings: Complete o código para exibir a mensagem "Bem-vindo, João!", onde o nome deve vir de uma variável.
nome = "João"
print(f'Bem-vindo, {nome}!')
# Complete aqui


#Erros comuns: Qual é o erro neste código, e como corrigir?
numero = "10"
soma = numero + 5
#Devemos converter o tipo de dado numero que esta como string para int para poder somar com um int(5)
soma = int(numero)+ 5

#Booleanos em Condições: O que será exibido ao executar este código?
ativo = False
if not ativo:
    print("Inativo")
else:
    print("Ativo")
#vai ser exibido inativo, pois se nao esta ativo (not ativo) quer dizer que ativo esta não/false, entraria no print inativo


#Misto: Quais os valores finais de a e b após executar este código?

a = 5
b = "5"
a = int(b) + a
b = float(a) + 0.5

# a = 5 + 5 = 10
#a agora tem um novo valor
# b = 10.0 + 0.5 = 10.5