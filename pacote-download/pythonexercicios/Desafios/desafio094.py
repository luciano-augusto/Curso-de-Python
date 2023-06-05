dados = {}
grupo = []
media = 0
while True:
    dados['Nome'] = str(input('Nome: '))
    dados['Idade'] = int(input('Idade: '))
    media += dados['Idade']
    dados['Sexo'] = str(input('Sexo: [M/F] ')).upper().strip()
    grupo.append(dados.copy())
    dados.clear()
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if continuar == 'N':
        print('-=-'*10)
        break
print(f' - O grupo tem {len(grupo)} pessoas.')
print(f'A media de idade é de {media / len(grupo):.2f}.')
print('As mulheres cadastradas foram:', end=' ')
for p in grupo:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]},', end=' ')
print('.')
print('Lista das pessoas que estão a cima da media:')
for i in grupo:
    if i['Idade'] > media / len(grupo):
        print(f'Nome: {i["Nome"]}; Sexo: {i["Sexo"]}; Idade: {i["Idade"]}')
print('≥≥≥ ENCERRADO ≤≤≤')
