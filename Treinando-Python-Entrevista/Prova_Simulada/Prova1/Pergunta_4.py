'''Pergunta 4: Classes e Objetos
Pergunta:
Crie uma classe chamada Retangulo que tenha os atributos largura e altura.
Adicione um método chamado area que retorna a área do retângulo.
Instancie um objeto dessa classe com largura 5 e altura 10, e imprima a área.'''


class Retangulo():
    def __init__(self, largura, altura) -> None:
      self.largura = largura
      self.altura = altura

    def area(self):
      area_do_triangulo = self.largura * self.altura
      return area_do_triangulo
   

retangulo = Retangulo(5,10)

print(retangulo.area())