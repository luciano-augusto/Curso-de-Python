# tempo = int(input('Quantos anos tem seu carro? '))
# if tempo <=3:
#     print('Carro novo!')
# else:
#     print('Carro velho.')
# print('--FIM--')


# tempo= int(input('Quantos anos tem seu carro? '))
# print('Carro novo.' if tempo <= 3 else 'Carro velho.')
# print('--Fim--')

# nome= str(input('Qual o seu nome? '))
# if nome== 'Gustavo':
#     print('Que nome lindo voce tem!')
# else:
#     print('Seu nome é tao normal.')
# print('Bom dia {}.' .format(nome))

n1= float(input('Digite sua primeira nota: '))
n2= float(input('Digite sua segunda nota: '))
m= (n1+n2)/2
print('Sua média foi de {:.1f}.' .format(m))
if m>= 6.0:
    print('Parabens, voce alcancou a media necessaria para ser aprovado!')
else:
    print('Infelizmente voce nao alcancou a media ncessaria.')
# print('Parabens' if m>= 6.0 else 'Estude mais.')