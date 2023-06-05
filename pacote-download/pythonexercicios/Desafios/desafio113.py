def leiaint(msg):
    while True:
        try:
            msg = int(input(msg))
        except (ValueError, KeyError):
            print('\033[31mErro de valor, digite um numero inteiro.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mProgram interrompido pelo usuario.\033[m')
            return 0
        else:
            break
    return msg


def leiareal(msg):
    while True:
        try:
            msg = float(input(msg))
        except (ValueError, KeyError):
            print('\033[31mErro de valor, digite um numero real.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mPrograma interrompido pelo usuario.\033[m')
            return 0
        else:
            break
    return msg



n = leiaint('Digite um numero Inteiro: ')
x = leiareal('Digite um numero Real: ')
print(f'O valor inteiro digitado é {n}, e o valor real é {x}.')
