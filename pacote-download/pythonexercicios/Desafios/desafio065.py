soma = 0
maior = 0
menor = 0
tentativas = 0
x = 0
y = 0

while y != 'n':
    x = int(input('Digite um novo numero: '))
    soma += x
    tentativas += 1
    if tentativas == 1:
        maior = menor = x
    else:
        if x > maior:
            maior = x
        if x < menor:
            menor = x
    y = str(input('Deseja continuar? [S/N]  '))
media = soma / tentativas
print('A media dos numeros é {}, o maior numero é {} e o menor é {}. '.format(media, maior, menor))
