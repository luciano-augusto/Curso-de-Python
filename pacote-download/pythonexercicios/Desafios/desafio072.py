numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
          'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    x = int(input('Digite um numero de 0 a 20: '))
    print(numero[x])
    y = str(input('Voce deseja continuar: [S/N]'))
    if y in 'Nn':
        break

