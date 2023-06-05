d= float(input('Qual a distancia do seu destino? '))
if d <= 200:
    v1 = d* 0.50
    print('O valor da sua passagem é de R${:.2f}.' .format(v1))
else:
    v2 = d* 0.45
    print('O valor da sua passagem é de R${:.2f}.' .format(v2))