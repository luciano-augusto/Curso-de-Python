import datetime
ano = int(input('Bem vindo! Digite seu ano de nascimento: '))
idade = datetime.date.today().year - ano
print('Voce tem {} anos.' .format(idade))
if idade <= 9:
    print('Voce ira competir na categoria Mirim.')
elif 9 < idade <= 14:
    print('Voce ira competir na categoria Infantil.')
elif 14 < idade < 19:
    print('Voce ira competir na categoria Junior.')
elif 19 < idade < 21:
    print('Voce ira competir na categoria Senior.')
elif idade >= 21:
    print('Voce ira competir na categoria Master.')