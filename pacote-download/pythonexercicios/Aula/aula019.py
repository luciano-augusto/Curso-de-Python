Dicionarios = indices literais {}

dados = dict() ou {}
dados = {'nome':'Pedro', 'idade':25}
print(dados['nome']) Pedro
print(dados['idade']) 25
Para criar um novo dado = dados['sexo'] = 'M'
Comando .append nao funciona em dicionarios
Para remover um dado = del.dados['idade'] : apaga o dado e a estrutura

filme = { 'titulo': 'Star Wars',
            'ano': 1977,
            'diretor': 'Jorge Lucas'
        } importante sempre fechar as chaves

print(filme.values()) : retorna a informacao dentro do dicionarios ≥ sem os nomes dos dicionarios
≥≥≥ INFORMAÇÃO

print(filme.keys()) : retorna titulo, ano, diretor ≥ o nome dado as estruturas dentro do dicionario
≥≥≥ NOME DA ESTRUTURA

print(filmes.items()) : retorna todos os dados, nome do dicionarios e informacoes dentro deles
≥≥≥ ESTRUTURA : INFORMAÇÃO

for k, v in filme.itens():
    print(f'O (k) é (v)')
    O tittulo é Star Wars
    O ano é 1977... etc



pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') #quando ja estiver usando aspas simples, usar "aspas duplas depois

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)

pessoas['nome'] = 'Leandro' #para mudar um valor dentro do dicionario
pessoas['peso'] = 98.5 #para adicionar um item 
for k, v in pessoas.items():
    print(f' {k} = {v}')

estado = dict()
brasil = list()
for c in range(0,3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy()) #para criar uma copia dentro de dicionario
for e in brasil: #estado
    for k, v in e.items(): #key(estado)  V(sigla)
        print(f'O campo {k} tem valor {v}.')

    for v in e.values():
        print(v)
