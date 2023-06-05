import time
x  = int(input('Digite o primeiro valor: '))
r = int(input('Digite a razao: '))
c = 1
y = 10
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while c <= total:
        print(x)
        x += r
        c += 1
    print('PAUSA')
    mais = int(input('Mais quantos termos voce gostaria de mostrar? '))
print('progressa finalizada com {} termos mostrados. '.format(c))
