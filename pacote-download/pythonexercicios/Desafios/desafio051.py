# an = a1+(n-1)*r
x = int(input('Digite o a primeiro termo: '))
r = int(input('Digite a razao: '))
decimo = x + (10 - 1) * r
for c in range(x, decimo + r, r):
    print(c)
