import datetime
ano = int(input('Qual o seu ano de nascimento? '))
idade = datetime.date.today().year - ano
n1 = idade - 18
print('Voce tem {} anos.' .format(idade))
if idade == 18:
    print('Voce deve se alistar esse ano!')
elif idade < 18:
    print('Voce ainda nao precisa se alistar, mas fique atento!')
elif idade > 18:
    print('Voce perdeu o prazo de alistamento. Voce devia ter se alistado a {} atras.' .format(n1))
