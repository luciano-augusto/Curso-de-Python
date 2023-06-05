maior = homens = mulheres = 0
while True:
    print('---' * 20)
    print('                   CADASTRE UMA PESSOA     ')
    print('---' * 20)
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
    print('---'*20)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar: [S/N] ')).strip().upper()
    if idade > 18:
        maior += 1
    if idade < 20 and sexo == 'F':
        mulheres += 1
    if sexo == 'M':
        homens += 1
    if continuar == 'N':
        print('-' * 20)
        print('====== FIM DO PROGRAMA ======')
        print(f'Total de pessoas com mais de 18 anos é {maior}.')
        print(f'Ao todo foram cadastrados {homens} homens.')
        print(f'E temos {mulheres} mulher(es) com menos de 20 anos.')
        break
