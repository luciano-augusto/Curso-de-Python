n1 = int(input('Digite o valor do primeiro lado: '))
n2 = int(input('Digite o valor do segundo lado: '))
n3 = int(input('digite o valor do terceiro lado: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Com esses valores, é possível se formar um triangulo')
else:
    print('Com esse valores, nao é possível se formar um triangulo.')

# maior = n1
# if (n2 > maior):
#     maior = n2
# if (n3 > maior):
#     maior = n3
# print('{} é o maior lado.' .format(maior))
#
# medio = n1
# if (medio > n2 > n3):
#     medio = n2
# if (medio > n3 > n2):
#     medio = n3
# print('{} é o medio.' .format(medio))
#
# menor =n1
# if (n2 < menor):
#     menor = n2
# if (n3 < menor):
#     menor = n3
# print('{} é o menor' .format(menor))
# if (maior < medio + menor):
