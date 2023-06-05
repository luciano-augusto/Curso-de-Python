boletim = list()
aluno = list()
x = 0

while True:
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    boletim.append(aluno[:])
    aluno.clear()
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if continuar == 'N':
        break
qntd = len(boletim)
print('='*30)
print('No.  NOME          MÉDIA')
print('-'*30)
while x < qntd:
    media = (boletim[x][1] + boletim[x][2]) / 2
    print(f'{x}   {boletim[x][0]}          {media:.2f}')
    x += 1
print('='*30)
while True:
    num = int(input('Mostra nora de qual aluno? (999 interrompe): '))
    if num != 999:
        print(f'As notas de {boletim[num][0]} são {boletim[num][1]} e {boletim[num][2]}')
        print('-'*30)
    else:
        print('FINALIZANDO...')
        print('≤≤≤VOLTE SEMPRE≥≥≥')
