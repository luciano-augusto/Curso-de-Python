maior = menor = 0
lista = []
for c in range(0, 5):
    v = int(input(f'Digite o valor para a posicao {c}: '))
    lista.append(v)
    # lista.append(int(input(f'Digite um valor para a posicao {c}: ')))
print(f'Voce digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} na posicao ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}...', end=' ')
print(f'O menor valor digitado foi {min(lista)} na posicao ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}...', end=' ')
