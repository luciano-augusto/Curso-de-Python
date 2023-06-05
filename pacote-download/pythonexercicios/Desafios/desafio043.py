p = float(input('Qual o seu peso? '))
h = float(input('Qual a sua altura? '))
imc = p / (h ** 2)
print('O seu IMC é de {:.1f}.' .format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal.')
elif 25 <= imc < 30:
    print('Você está com sobrepeso.')
elif imc >= 30:
    print('Você está com obesidade.')