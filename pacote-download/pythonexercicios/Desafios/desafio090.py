boletim = {
    'Nome': '',
    'Nota': '',
    'Situação': ''
}
boletim['Nome'] = str(input('Nome do Aluno: '))
boletim['Nota'] = float(input(f'Média de {boletim["Nome"]}: '))
if boletim['Nota'] >= 7.0:
    boletim['Situação'] = 'APROVADO'
else:
    boletim['Situação'] = 'REPROVADO'
for k, v in boletim.items():
    print(f'{k} igual a {v}')


#print(f'O(a) aluno(a) {boletim["Nome"] } foi {boletim["Situação']}')
