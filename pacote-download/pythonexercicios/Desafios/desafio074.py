import random
aleatorios = []
for _ in range(5):
    aleatorios.append(random.randint(0, 100))
print(f'Os numero sorteados foram {aleatorios}')
maior = max(aleatorios)
menor = min(aleatorios)
print(f'O maior numero sorteado foi {maior}')
print(f'O menor numero sorteado foi {menor}')


