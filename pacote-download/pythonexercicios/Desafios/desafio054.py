import datetime
totmaior = 0
totmenor = 0
for c in range(1, 8):
    ano = int(input('Digite o {}º ano de nascimento: ' .format(c)))
    idade = datetime.date.today().year - ano
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('{} pessoas sao maiores.' .format(totmaior))
print('{} pessoas sao menores.' .format(totmenor))
