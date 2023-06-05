n = int(input('Digite um numero inteiro: '))
c = n
f = 1
print('Calculando {}!' .format(n))
while c > 0:
    print('{}' .format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

'''resultado = 1
n = int(input('Digite um numero: '))
for n in range(1, n +1):
    resultado *= n
print(resultado)'''

# from math import factorial
# n = int(input('Digite um numeor inteiro: '))
# print('o fatorial de {} é {}.' .format(n, factorial(n)))