v= int(input('Qual a velocidade do veiculo? '))
if v <= 80:
    print('Voce esta dentro do limite de velocidade!')
else:
    print('Voce excedeu o limite de de velocidade!')
    m= (v-80)*7
    print('O valor da sua multa é de R${},00.' .format(m))



# (v-80)*7