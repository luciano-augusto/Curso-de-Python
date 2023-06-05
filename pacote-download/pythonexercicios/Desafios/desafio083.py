contabre = 0
contfecha = 0
exp = str(input('Digite a expressão: '))
for caractere in exp:
    if caractere == '(':
        contabre += 1
    if caractere == ')':
        contfecha += 1
if contabre == contfecha:
    print('Sua expressao esta correte!')
else:
    print('Sua expressao esta errada...')
