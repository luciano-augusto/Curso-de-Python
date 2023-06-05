n1 = int(input('Digite o valor da primeira nota: '))
n2 = int(input('Digite o valor da segunda nota: '))
m = (n1 + n2) / 2
print('A sua media é {:.2f}!' .format(m))
if m < 5:
    print('Reprovado!!')
elif m > 7:
    print('Aprovado!!')
elif 5 < m < 6.9:
    print('Recuperação!!')
