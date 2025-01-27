'''2. Fatorial
Crie uma função que calcule o fatorial de um número fornecido pelo usuário.
Exemplo:
Entrada: 5
Saída: 120 (pois 5! = 5 × 4 × 3 × 2 × 1)'''

def fatorial(num):
    multiplicador = num
    resposta = num
    while multiplicador > 1:
        resposta = resposta * (multiplicador-1)
        multiplicador -= 1
        
    print(resposta)
        
    
def main():
    num = int(input("Digite um numero para exibir seu fatorial: "))
    fatorial(num)
    
    
main()