import time
print('Nosso foguete sera lançado, prepare-se para a contagem regressiva!!!')
for c in range(10, -1, -1):
    time.sleep(1)
    print(c)
print('We have lift off!!!')
