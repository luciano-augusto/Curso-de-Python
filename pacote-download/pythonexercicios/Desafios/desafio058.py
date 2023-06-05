from random import randint
tentativa = 0
computador = randint(0, 10)
jogador = 0
print('Vou pensar em um numero de 0 a 10.')
while computador != jogador:
    jogador = int(input('Tente adivinhar o numero que eu pensei: '))
    if jogador != computador:
        tentativa += 1
        print('Voce errou, tente novamente')
    else:
        print('Parabens, voce pensou no numero {} e eu tambem pensei no numero {} !!.' .format(jogador, computador))
print('Voce acertou na {} tentativa.' .format(tentativa))

'''acertou = false
while not acertou:
    jogador = int(input('Qual o seu palpite? '))'''
