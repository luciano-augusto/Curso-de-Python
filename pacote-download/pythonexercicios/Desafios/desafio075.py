numero = (int(input('Digite o primeiro numero: ')),
         int(input('Digite o segundo numero: ')),
         int(input('Digite o terceiro numero: ')),
         int(input('Digite o quarto valor: ')))
print(numero)
print(numero.count(9))
if 3 in numero:
    print(numero.index(3) + 1)
else:
    print('O valor 3 nao foi digitado em nenhuma posicao.')
for n in numero:
    if n % 2 == 0:
        print(n)
