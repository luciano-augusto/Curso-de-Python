from time import sleep
def linha(msg):
    tam = len(msg)
    print('~'*tam)
    print(f'  Acessando o manual do "{msg}"!')
    print('~'*tam)

def cabeçalho(msg):
    tam = len(msg)
    print('~'*tam)
    print(msg)
    print('~'*tam)

def sair():
    print('~'*13)
    print('ATÉ LOGO!')
    print('~'*13)


while True:
    cabeçalho('SISTEMA DE AJUDA PyHELP')
    comando = str(input('Função ou Comando > ')).lower()
    linha(comando)
    sleep(0.25)
    print(help(comando))
    if comando == 'fim':
        sair()
        break
