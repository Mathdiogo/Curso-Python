'''Código com bugs
class Calculadora:
    def __init__(self, valor_inicial):
        self.valor = valor_inicial
    
    def adicionar(self, x):
        self.valor += x
    
    def subtrair(self, x):
        self.valor -= x
    
    def multiplicar(self, x):
        self.valor *= x
    
    def dividir(self, x):
        self.valor /= x  # Possível bug aqui!
    
    def resultado(self):
        return self.resultado  # Bug!

calc = Calculadora(10)
calc.adicionar(5)
calc.dividir(0)  # Outro possível bug
print(calc.resultado())

'''


#código corrigido
class Calculadora:
    def __init__(self, valor_inicial):
        self.valor = valor_inicial
    
    def adicionar(self, x):
        self.valor += x
        print(f"Resultado da adição: {self.valor}")
    
    def subtrair(self, x):
        self.valor -= x
        print(f"Resultado da subtração: {self.valor}")
    
    def multiplicar(self, x):
        self.valor *= x
        print(f"Resultado da multiplicação: {self.valor}")
    
    def dividir(self, x):
        try:
            self.valor /= x
            print(f"Resultado da divisão: {self.valor}")
        except ZeroDivisionError:
            print('Impossível realizar uma divisão com denominador = 0')
    
    def resultado(self):
        print(f"Resultado final: {self.valor}")
        return self.valor  # Corrigido para retornar o valor atual

# Teste da classe
calc = Calculadora(10)
calc.adicionar(5)
calc.dividir(0)  # Vai gerar erro na divisão
calc.resultado()

