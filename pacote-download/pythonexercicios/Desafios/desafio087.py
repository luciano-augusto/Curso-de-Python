matriz = list()
primeiro = list()
segundo = list()
terceiro = list()
pares = maior = 0
for c in range(0, 3):
    primeiro.append(int(input(f'Digite um valor para [0, {c}]: ')))
matriz.append(primeiro[:])
for n in primeiro:
    if n % 2 == 0:
        pares += n

for c in range(0, 3):
    segundo.append(int(input(f'Digite um valor para [1, {c}]: ')))
matriz.append(segundo[:])
for n in segundo:
    if n % 2 == 0:
        pares += n
    # if n >= segundo[0]:
    #     n = maior
maior = max(segundo)

for c in range(0, 3):
    terceiro.append(int(input(f'Digit um valor para [2, {c}]: ')))
matriz.append(terceiro[:])
for n in terceiro:
    if n % 2 == 0:
        pares += n

soma = matriz[0][2] + matriz[1][2] + matriz[2][2]
print('='*30)
print(f'[{matriz[0][0]}] [{matriz[0][1]}] [{matriz[0][2]}]')
print(f'[{matriz[1][0]}] [{matriz[1][1]}] [{matriz[1][2]}]')
print(f'[{matriz[2][0]}] [{matriz[2][1]}] [{matriz[2][2]}]')
print('='*30)
print(f'A soma dos números pares digitados é {pares}')
print(f'A soma dos valores da terceira coluna é {soma}')
print(f'O maior valor da segunda linha é {maior}')
