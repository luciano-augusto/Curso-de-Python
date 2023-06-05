num = int(input('Digite um numero inteiro: '))
print('''Escolha umas das bases para conversao:
[1] para converter para BINARIO
[2] para converter para OCTAL
[3] para converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para Binario é {}' .format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para Ocatl é {}.' .format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para Hexadecimal é {}.'.format(num, hex(num)[2:]))
