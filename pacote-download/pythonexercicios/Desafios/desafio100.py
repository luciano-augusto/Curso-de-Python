from random import randint

lista = []


def sorteio():
    cont = 0
    while True:
        num = randint(1, 10)
        lista.append(num)
        cont += 1
        if cont >= 5:
            break
    print(f'Sorteando 5 valores da lista: {lista}')


def somapar():
    num = 0
    for x in lista:
        if x % 2 == 0:
            num += x
    print(f'A soma dos numeros pares de {lista}, temos {num}.')


sorteio()
somapar()
