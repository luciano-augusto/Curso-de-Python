'''Valor da casa, do salario e das prestacoes
parcela nao pode ser maior que 30%
se for, negar financiamento'''


c = float(input('Qual o valor do imovel que pretende adquirir? '))
p = int(input('Em quantas parcelas pretende pagar? '))
s = int(input('Qual o valor do seu atual salário? '))
m = c//p
print('O valor da sua mensalidade é de R${:.2f}' .format(m))
if m <= s * 0.7:
    print('O seu financiamento foi aprovando!')
elif m > s * 0.7:
    print('Infelizmente seu financiamento nao foi aprovado.')
