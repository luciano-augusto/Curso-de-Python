import random
from time import sleep
aposta = list()
jogo = list()
qntd = 0
y = 0
print('-'*30)
print('      JOGO DA MEGA SENA')
print('-'*30)
quant = int(input('Quantos jogos voce quer que eu sorteie? '))
print(f'≥≥≥ SORTEANDO {quant} JOGOS ≤≤≤')
while qntd < quant:
    cont = 0
    while True:
        num = random.randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont >= 6:
            break
    aposta.append(sorted(jogo[:]))
    jogo.clear()
    qntd += 1
quantidade = len(aposta)
while y < quantidade:
    print(f'Jogo {(y + 1)}: {aposta[y]}')
    y += 1
    sleep(1)
print('≥≥≥≥≥ BOA SORTE! ≤≤≤≤≤')
