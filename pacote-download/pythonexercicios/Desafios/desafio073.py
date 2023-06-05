times = ('Botafogo', 'Palmeiras', 'Fluminense', 'Cruzeiro', 'Athletico-PR', 'Atletico-MG', 'Santos', 'Fortaleza', 'Flamengo', 'Sao Paulo',
         'Gremio', 'Internacional', 'Braganthino', 'Bahia', 'Goais', 'Vasco da Gama', 'Corinthians', 'Cuiaba', 'Coritiba', 'America-MG')
print(f'Os 4 primeiro colocados sao: {times[:5]}')
print(f'Os ultimo 4 colocados sao:{times[-4:]}')
print(f'Essa é alista em ordem alfabetica: {sorted(times)}')
print('O gremio esta na {} posicao'.format(times.index('Gremio')))