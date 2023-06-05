s = float(input('Qual o valor do seu salario? '))
if s >= 1250:
    s1 = s * 1.10
    print('O seu novo salario dera de R${:.2f}.' .format(s1))
else:
    s2 = s * 1.15
    print('O seu novo salario sera de R${:.2f}.'.format(s2))
