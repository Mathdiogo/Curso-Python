#As variáveis frutas, precos, kg e valores são respectivamente quais tipos de variáveis?

frutas = ['banana', 'uva', 'abacaxi'] #Lista string
precos = (2.5, 6, 4) #Tupla float
kg = [1,0.5,2] #Lista float
valores = [a*b for a,b in zip(precos, kg)]#Lista

print(type(frutas))
print(type(precos))
print(type(kg))
print(type(valores))