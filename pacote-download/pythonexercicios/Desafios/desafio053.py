x = str(input('Digite sua frase: ')).strip().lower()
print(x[::-1])
if x == x[::-1]:
    print('Essa palavra/frase é um palindromo!')
else:
    print('Essa frase nao é um palindromo.')
