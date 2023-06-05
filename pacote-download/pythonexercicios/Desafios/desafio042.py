n1 = int(input('Digite o valor do primeiro lado: '))
n2 = int(input('Digite o valor do segundo lado: '))
n3 = int(input('digite o valor do terceiro lado: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Com esses valores, é possível se formar um triangulo ', end='')
    if n1 == n2 == n3:
        print('Equilatero')
    elif n1 != n2 != n3 != n1:
        print('Escaleno')
    else:
        print('Isosceles')
else:
    print('Com esse valores, nao é possível se formar um triangulo.')
