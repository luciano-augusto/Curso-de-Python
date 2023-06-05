def area(l, c):
    t = l * c
    print(f'A area do seu terreno de {l} x {c} é de {t}m2.')


print('CONTROLE DE TERRENOS')
print('-=-'*10)
a = float(input('Largura (m): '))
b = float(input('Comprimento (m): '))
area(a, b)
