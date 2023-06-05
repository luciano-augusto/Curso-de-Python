def maior(*num):
    tam = len(num)
    print('Analisando os valores passados...')
    print(f'{num} Foram informados {tam} valores ao todo.')
    if len(num) > 0:
        print(f'O maior valor informado foi {max(num)}.')
    else:
        print('O maior numero informado foi 0')
    print('-=-'*20)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()