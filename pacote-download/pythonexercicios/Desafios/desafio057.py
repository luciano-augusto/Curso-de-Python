s = 0
while s != 'M' and s != 'F':
    s = str(input('Qual o seu sexo? [M/F] ')).upper()
    if s == 'M' or s == 'F':
        print('Voce é do sexo {}, obrigado por participar.' .format(s))
    else:
        print('Tente novamente.')
print('Fim')
