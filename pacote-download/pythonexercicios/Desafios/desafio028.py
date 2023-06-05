from random import randint
import time
computador = randint(0, 5)  #faz o computador sortear o numero
print('-=-'*20)
print('Vou pensar em um numero entre 0 e 5. Tente advinhar...')
print('-=-'*20)
jogador = int(input('Tente advinhar em qual numero eu pensei: '))
print('PROCESSANDO...')
time.sleep(3)  #comando para fazer esperar em segundos
if computador == jogador:
    print('Que incrivel, voce advinhou o numero')
else:
    print('Voce errou, mais sorte da proxima vez.')
    print('eu pensei no numero {}' .format(computador))
