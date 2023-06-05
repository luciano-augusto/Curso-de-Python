import datetime
n= int(input('Digite um ano: '))
if n == 0:
    n = datetime.date.today().year
if n % 4 ==0 and n % 100 != 0 or n % 400 == 0:
    print('{} é um ano bissexto.'.format(n))
else:
    print('{} NAO é um ano bissexto.' .format(n))