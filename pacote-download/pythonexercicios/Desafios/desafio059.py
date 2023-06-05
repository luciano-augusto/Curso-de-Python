z = 0
print('Bem vindo a nossa CALCULADORA')
x = int(input('Digite o primeiro valor: '))
y = int(input('Digite o segundo valor: '))
while True:
    z = int(input('''    [1] Somar
    [2] Multiplicar
    [3] Para saber qual é o maior valor
    [4] Reiniciar
    [5] SAIR  
    Digite qual tipo de operacao deseja realizar: '''))
    if z == 1:
        print('O valor da somar do valores é {} .' .format(x + y))
    elif z == 2:
        print('O valor da multiplicacao desses valores é {} .' .format(x * y))
    elif z == 3:
        maior = x
        if y > maior:
            maior = y
        print('O maior valor digitado foi {}.' .format(maior))
    elif z == 4:
        x = int(input('Digite o primeiro valor: '))
        y = int(input('Digite um segundo valor: '))
        continue
    elif z == 5:
        print('FIM')
        break
    else:
        print('Reiniciando')
    print('-=-'*15)
print('Obrigado!')
