continuar = 0
lista = []
while continuar != 'n':
    num = int(input('Digite um valor: '))
    if num in lista:
        print('Numero duplicado, nao vou adicionar.')
    else:
        print('Numero adicionado com sucesso.')
    continuar = str(input('Deseja continuar? [S/N] ')).lower()
    lista.append(num)
print('='*20)
print(f'Os numeros que voce digitou foram {sorted(lista)}')
