soma = 0
for c in range(1, 7):
    n = int(input('Digite um numero inteiro: '))
    if n % 2 == 0:
        soma += n
print('A soma de todos os numero pares é de {}.' .format(soma))
