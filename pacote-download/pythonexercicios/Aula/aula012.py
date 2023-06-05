# Condicoes aninhadas
nome = str(input('Qula o seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito.')
elif nome == 'Matheus' or nome == 'Lucas' or nome == 'Pedro':
    print('O seu nome é bem popular no Brasil.')
elif nome in 'Jessica Claudia Ana Juliana':
    print('Belo nome feminino')
else:
    print('O seu nome é bem comum.')
print('Tenha um bom dia, {}!' .format(nome))
