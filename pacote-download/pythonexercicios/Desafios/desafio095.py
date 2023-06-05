aproveitamento = {'Nome': '', 'Gols': '', 'Total': ''}
partidas = list()
time = []
tot = 0
while True:
    aproveitamento['Nome'] = str(input('Nome do jogador: '))
    x = int(input(f'Quantas partidas {aproveitamento["Nome"]} jogou? '))
    for c in range(1, x + 1):
        y = int(input(f'Quantos gols na {c}º partida: '))
        tot += y
        partidas.append(y)
    aproveitamento['Gols'] = partidas.copy()
    aproveitamento['Total'] = tot
    partidas.clear()
    time.append(aproveitamento.copy())
    tot = 0
    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()
    print('-'*47)
    if continuar == 'N':
        break
print('-=-'*15)
print('Cod   Nome          Gols               Total')
print('-'*47)
for p, d in enumerate(time):
    print(f'{p}     {d["Nome"]}        {d["Gols"]}          {d["Total"]} ')
print('-'*47)
while True:
    num = int(input('Mostrar dados de qual jogador? '))
    if num == 999:
        break
    else:
        print(f'-- Levantamento do jogador: {time[num]["Nome"]}')
        for k, v in enumerate(time[num]['Gols']):
            print(f' No jogo {k} fez {v} gols.')
        print('-'*47)

print('≥≥≥ FIM DO PROGRAMA ≤≤≤')
