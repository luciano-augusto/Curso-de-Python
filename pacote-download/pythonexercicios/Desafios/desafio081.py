continuar = 0
lista = []
while continuar != 'n':
    num = int(input('Digite um numero: '))
    continuar = str(input('Voce deseja continuar? [S/N] ')).lower().strip()
    lista.append(num)
print(f'Voce digitou {lista}')
print(f'A lista em ordem decrescente fica assim: {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O numero 5 foi adicionado na sua lista')
else:
    print('O numero 5 nao foi adicionado na sua lista')
