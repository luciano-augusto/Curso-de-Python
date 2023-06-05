import random
jogador = str(input('Escolha pedra, papel ou tesoura!! '))
print('-=-'*20)
lista = ['pedra', 'papel', 'tesoura']
computador = random.choice(lista)
print('O computador escolheu {}.'.format(computador))
if jogador == computador:
    print('Empate, tente mais uma vez.')
elif jogador == 'pedra' and computador == 'tesoura':
    print('Voce ganhou.')
elif jogador == 'papel' and computador == 'pedra':
    print('Voce ganhou.')
elif jogador == 'tesoura' and computador == 'papel':
    print('Voce ganhou!!.')
else:
    print('Voce perdeu!')
