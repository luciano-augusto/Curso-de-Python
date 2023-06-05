galera = list()
dados = list()
total = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    maior = menor = dados[1]
    nomemaior = nomemenor = dados[0]
    for p in galera:
        if p[1] > maior:
            maior = p[1]
            nomemaior = p[0]
        if p[1] == 0 or p[1] < menor:
            menor = p[1]
            nomemenor = p[0]

    total += 1
    galera.append(dados[:])
    dados.clear()
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if continuar == 'N':
        break
print(f'Ao todo voce cadastrou {total} pessoas.')
print(f'O maior peso registrado foi {maior}kg, de ', end='' )
for p in galera:
    if p[1] == maior:
        print(f'{p[0]}. ')
print(f'O menor peso registrado foi {menor}kg, de ', end='')
for p in galera:
    if p[1] ==  menor:
        print(f'{p[0]}. ')
