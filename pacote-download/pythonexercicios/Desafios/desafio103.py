def ficha(a='<desconhecido>', b=0):
    print(f'O jogador {a} marcou {b} gol(s) no campeonato.')


nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(b=gols)
else:
    ficha(nome, gols)
