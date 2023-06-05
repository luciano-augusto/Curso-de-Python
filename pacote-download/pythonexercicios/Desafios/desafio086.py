matriz = list()
primeiro = list()
segundo = list()
terceiro = list()
for c in range(0, 3):
    primeiro.append(int(input(f'Digite um valor para [0, {c}]: ')))
matriz.append(primeiro[:])

for c in range(0, 3):
    segundo.append(int(input(f'Digite um valor para [1, {c}]: ')))
matriz.append(segundo[:])

for c in range(0, 3):
    terceiro.append(int(input(f'Digit um valor para [2, {c}]: ')))
matriz.append(terceiro[:])

print('='*30)
print(f'[{matriz[0][0]}] [{matriz[0][1]}] [{matriz[0][2]}]  ')
print(f'[{matriz[1][0]}] [{matriz[1][1]}] [{matriz[1][2]}]')
print(f'[{matriz[2][0]}] [{matriz[2][1]}] [{matriz[2][2]}]')
