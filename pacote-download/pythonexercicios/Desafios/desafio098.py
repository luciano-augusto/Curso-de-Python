from time import sleep


def contador():
    print('=-='*10)
    print('Contagem de 1 ate 10 de 1 em 1:')
    for x in range(1, 11, 1):
        print(x, end=' ')
        # sleep(0.25)
    print('FIM!')
    print('=-='*10)
    for x in range(10, 0, -2):
        print(x, end=' ')
        # sleep(0.25)
    print('FIM!')
    print('Agora é sua vez de personalizar a contagem!')
    i = int(input('Inicio: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))
    print('=-='*10)
    print(f'Contagem de {i} ate {f} de {p} em {p}.')
    if f < i and p != 0:
        for x in range(i, f-1, -p):
            print(x, end=' ')
            sleep(0.25)
    if p < 0:
        for x in range(i, f-1, p):
            print(x, end=' ')
            sleep(0.25)
    if f < i and p == 0:
        for x in range(i, f-1, p-1):
            print(x, end=' ')
    if i <= f:
        for x in range(i, f+1, p):
            print(x, end=' ')
    print('FIM!')


contador()
