import datetime
cadastro = {}
while True:
    cadastro['Nome'] = str(input('Nome: '))
    nascimento = int(input('Ano de Nascimento: '))
    cadastro['Idade'] = datetime.datetime.now().year - nascimento
    cadastro['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
    if cadastro['CTPS'] == 0:
        print('-=-'* 15)
        for k, v in cadastro.items():
            print(f'{k} tem o valor {v}.')
        break
    cadastro['Contratação'] = int(input('Ano de Contratação: '))
    cadastro['Salário'] = int(input('Salário R$'))
    cadastro['Aposentadoria'] = (cadastro['Contratação'] + 35) - nascimento
    print('-=-'*15)
    for k, v in cadastro.items():
        print(f'{k} tem o valor {v}.')
    break
