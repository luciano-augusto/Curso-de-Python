from random import randint
tentativa = 0
print('Bem vindo ao nosso jogo de PAR ou IMPAR!!')
while True:
    jogador = int(input('Escolha um numero: '))
    x = str(input('Par ou Impar? [P/I]  ')).lower()
    computador = randint(0, 10)
    soma = jogador + computador
    if x == 'p':
        if soma % 2 == 0:
            print(f'Parabens, voce GANHOU! Voce escolheu {jogador} e o computador escolheu {computador}.')
            tentativa += 1
        if soma % 2 == 1:
            print(f'Voce PERDEU, sua escolha foi {jogador} e a do computador foi {computador}.')
            tentativa += 1
            print(f'Voce perdeu apos {tentativa} vitorias consecutivas.')
            break
    if x == 'i':
        if soma % 2 == 1:
            print(f'Parabens, voce GANHOU! Voce escolheu {jogador} e o computador escolheu {computador}.')
            tentativa += 1
        if soma % 2 == 0:
            print(f'Voce PERDEU, sua escolha foi {jogador} e a do computador foi {computador}.')
            tentativa += 1
            print(f'Voce perdeu apos {tentativa} vitorias consecutivas.')
            break
print('FIM DO PROGRAMA')
