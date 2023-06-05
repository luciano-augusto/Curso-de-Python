while not apple:
    if ground:
        walk
    if blank:
        jump
    if coin:
        grab
grab

for c in range(1, 10):
    print(c)

c = 1
while c < 11:
    print(c)
    c += 1

n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar? [S/N]')).upper()
print('Fim')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um numero: '))
    if n != 0:
        if n % 2 ==0:
            par += 1
        else:
            impar += 1
print('Voce digitou {} numero pares e {} numeros impares. ' .format(par, impar))