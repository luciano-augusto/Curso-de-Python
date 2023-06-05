cont = soma = 0
while True:
    x = int(input('Digite 999 para interromper: '))
    if x != 999:
        cont += 1
        soma += x
    if x == 999:
        break
print(f'Programa interrompido, a soma dos  {cont} valores é igual a  {soma}.')
