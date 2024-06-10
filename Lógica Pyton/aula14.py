a = 'AAAAAAAA'
b = 'BBBBBBBB'
c = 1.1
#string = 'a={0} b={1} c={2:.2f}' #ordenando por indice
string = 'b={nome2} a={nome1} b={nome2} c={nome3:.2f}'#chamando por nome(string)

#formato = string.format(a, b, c)
formato = string.format(nome1=a, nome2=b, nome3=c)

print(formato)