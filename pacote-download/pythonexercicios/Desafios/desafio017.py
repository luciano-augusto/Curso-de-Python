import math
#c2=a2+b2
#a= float(input('Digite o valor do cateto 1: '))
#b= float(input('Digite o valor cateto 2: '))
#h= math.sqrt(a*a + b*b)
#print('O valor da hipotenusa é {:.2f}'. format(h))

co= float(input('Digite o valor do cateto oposto: '))
ca= float(input('Digite o valor do cateto adjascente: '))
hi= math.hypot(co,ca)
print('O valor da hipotenusa é: {:.2f}' .format(hi))