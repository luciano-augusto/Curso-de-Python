#Tuplas sao imutaveis
#lanche[1] = regrigerante nao pode ser executado
lanche = ('hanbuerguer', 'suco', 'pizza', 'pudim', 'bataa frita' )
#print(:2)
for comida in lanche: # criei minha variavel lanche em cima e nao preciso usar o range
    print(f'Eu vou comer {comida}.')
print('Eu comi pra caramba') # maneira tradicional que nao precisa enumerar as posicoes

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

#caso seja necessario enumerar o is tens
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')
#ou

for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posicao {cont}.')

#para ordenar a forma que ele mostra a tupla
print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c) #ele nao adiciona, mas juntas seus integrantes e a ordem influencia no resultado
print(len(c)) #mostra quantos elementos ele tem no total
print(c.count(5)) #mostra quantas vezes o elemento 5 aparece no resultado
print(c.index(8)) #mostra em que posicao estao elemento 8 no resultado
print(c.index(5, 1)) #mostra em posicao o elemento 5 esta a partir da posicao 1

pessoa = ('Gustavo', 39, 'M', 99.88) #aceita quelquer tipo de dado
del(pessoa) #aceita o comando delete, mas nao aceita ser mudada 
print(pessoa)