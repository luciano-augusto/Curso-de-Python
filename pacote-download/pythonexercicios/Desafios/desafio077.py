palavras = ('aprender' ,'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
            'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavras {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou': # se fosse acentuado deveria incluir áãâ...
            print(letra, end=', ')
