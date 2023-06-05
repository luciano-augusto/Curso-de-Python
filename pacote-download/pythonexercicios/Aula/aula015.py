'''cont = 1
while True:
    print(cont, ' ->', end='')
    cont += 1
print('Acabou')'''

# Comando break interrompe um looping
# n = 0
# while n != 999:
#     n = int(input('Digite um numero '))

n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
# print('A soma dos numeros é {}. ' .format(s))
print(f'a soma vale {s}')

