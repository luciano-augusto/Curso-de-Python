while True:
    y = int(input('Quer ver a tabuada de qual valor ? '))
    print('-=-'*10)
    if y < 0:
        print('Programa encerrado.')
        break
    for x in range(1, 11):
        print(f' {y} x {x} = {y*x}')
    print('-=-'*10)

