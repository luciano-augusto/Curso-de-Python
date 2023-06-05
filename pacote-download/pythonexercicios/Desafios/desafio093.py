aproveitamento = {'Nome': '', 'Gols': '', 'Total': ''}
partidas = list()
tot = 0

aproveitamento['Nome'] = str(input('Nome do jogador: '))
x = int(input(f'Quantas partidas {aproveitamento["Nome"]} jogou? '))
for c in range(1, x + 1):
    y = int(input(f'Quantos gols na {c}º partida: '))
    tot += y
    partidas.append(y)
aproveitamento['Gols'] = partidas.copy()
aproveitamento['Total'] = tot
print('-=-'*10)
print(aproveitamento)
print('-=-'*10)
for k, v in aproveitamento.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=-'*10)
print(f'O jogador {aproveitamento["Nome"]} jogou {len(aproveitamento["Gols"])} partidas.')
for a, b in enumerate(partidas):
    print(f' ==> Na partida {a + 1}, fez {b} gols.')
print(f'Foi um total de {aproveitamento["Total"]} gols.')
