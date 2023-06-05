total = maior = barato = nome = 0
nomebarato = ''
print('         TEM DE TUDO         ')
while True:
    nome = str(input('Nome do produto: '))
    preco = int(input('Valor R$'))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]  ')).upper().strip()[0]
    print('-=-'*15)

    total += preco

    if preco >= 1000:
        maior += 1
    if barato == 0 or preco < barato:
        barato = preco
        nomebarato = nome

    if continuar == 'N':
        print('-=-=-= FIM DA COMPRA =-=-=-')
        print(f'O total da sua compra é de R${total},00.')
        print(f'Voce comprou {maior} produtos com valor a cima de R$1000.00.')
        print(f'O produto mais barato é o {nomebarato}.')
        break
