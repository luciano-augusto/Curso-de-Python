pares = []
impares = []
lista = []
continuar = 0
while continuar != 'n':
    num = int(input('Digite um numero: '))
    continuar = str(input('Deseja continuar? [S/N] ')).lower().strip()
    if num % 2 == 0:
        pares.append(num)
        lista.append(num)
    else:
        impares.append(num)
        lista.append(num)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares {impares}')
