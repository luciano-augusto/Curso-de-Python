soma = 0
cont = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        cont = cont + 1
        soma = soma + num
print('a soma de todos os valore é {}'.format(soma))
print(' quantidade de valores solicitados {}' .format(cont))
