v = int(input('Qual o valor a ser pago? '))
print('Escolha entre dinheiro, cartao, 2x ou 3x.')
c = str(input('Qual a condicao de pagamento? '))
if c == 'dinheiro':
    p = v * 0.9
    print('O valor a ser pago é de R${:.2f}.' .format(p))
elif c == 'cartao':
    p = v * 0.95
    print('O valor a ser pago é de R${:.2f}.' .format(p))
elif c == 'duas':
    p = v * 1
    print('O valor a ser pago é de R${:.2f}.' .format(p))
elif c == 'tres':
    p = v * 1.2
    print('O valor a ser pago é de R${:.2f}.' .format(p))
