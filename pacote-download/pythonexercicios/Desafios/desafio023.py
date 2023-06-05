n= int(input('Digite um numero de ate 4 casa decimais: '))
u= n // 1 % 10
d= n // 10 % 10
c= n // 100 % 10
m= n // 1000 % 10
print('Voce escolheu o numero: {}' .format(n))
print('Unidade: {}'.format(u))
print('Dezena: {}' .format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))