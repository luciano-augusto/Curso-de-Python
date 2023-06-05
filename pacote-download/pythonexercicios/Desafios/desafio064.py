tentativa = 0
soma = 0
x = 0
x = int(input('Digite 999 para parar: '))
while x != 999:
    soma += x
    tentativa += 1
    x = int(input('Digite 999 para parar: '))
print('Voce digitou o codigo correto. Voce tentou {} vezes, e soma deles é {}' .format(tentativa, soma))
