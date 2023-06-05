p = float(input('Qual o seu peso? '))
h = float(input('Qual a sua altura? '))
imc = p / (h ** 2)
print('O se IMC é de {}.'.format(imc))
if imc < 18.5:
    print('Voce esta abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Voce esta no peso ideal.')
elif 25 <= imc < 30:
    print('Voce esta com sobrepeso.')
elif 30 <= imc < 40:
    print('Voce esta com obesidade.')
elif imc > 40:
    print('Voce esta com obesidade mórbida.')
