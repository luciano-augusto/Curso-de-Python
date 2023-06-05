dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0]) #retorna 'Pedro"
print(dados[1]) #retorna '25

pessoas = list()
pessoas.append(dados[:]) #gera uma copia completa de dados na lista pessoas


teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) #gerar copia se nao ira alterar a lista 'teste'
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:]) # copia para nao alterar o original
print(galera)

galera = [['Joao', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]  #uma lista com varios itens dentro dela
print(galera[2][0])  #printa o primeiro iten da terceira lista
for p in galera:
    print(p[0])  # vai printar o primeiro item de cada iten dentro de galera
    print(f'O(a) {p[0]} tem {p[1]} anos de idade!') #  printa os dados de cada pessoa no formato desejado

galera = list() #lista principal
dado = list() # lista contendo os dados separados
maior = menor = 0
for c in range(0,3):
    dado.append(str(input('Digite o seu nome: ')))
    dado.append(int(input('Digite a sua idade: ')))
    galera.append(dado[:]) #gero uma copia de nome e idade dentro de 'galera'
    dado.clear() # caso nao gere uma copia, ele ira apagar a lista 'galera'
print(galera)

for p in galera:
    if p[1] >= 21:  #conferindo a idade das pessoas cadastradas
        print(f'{p[0]} é maior de idade')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade')
        menor += 1
print(f'Temos {maior} pessoas maior(es) de idade e {menor} menor(es) de idade.')