maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite um peso {}: ' .format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maio peso é {} e o menor peso é {}.' .format(maior, menor))
