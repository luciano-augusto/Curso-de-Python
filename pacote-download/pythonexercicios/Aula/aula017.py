Listas usamos []
Tuplas se usa ()
Para adicionar algo a lista usamos o comando .append e esse item vai para o final da lista
Para adicionar algo em um lugar pre definido .insert(0, item) 0 indica o lugar na lista
Para aoagar um item dell item[3], 3 sendo o luga dele na lista e seu nome no lugar de item
item.pop(3), seguindo a mesma logica do anterior mas usando o comando .pop e usando aspas
caso queira eliminar o ultimo elemento, lista.pop(), nao se indica o nome nem o numero do elemento, somente o nome da lista
item.remove(item) com o remove, o nome do item que fica entre parenteses
caso nao saiba se o item esta na lista, usar o comando "if"
if pizza in lanche:
    lanche.remove(pizza)

valores = list(range(4, 11)) cria lista com os valores de 4 a 10 em ordem crescente
valores = [8, 2, 5, 4, 9, 3, 0] cria lista na ordem em que foi escrita
para organiza-los, valores.sort()
reverso valores.sort(reverse=True)
len(valores) para saber o tamanho da lista

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.insert(2, 2)
num.sort(reverse=True)
# num.pop(2)
if 4 in num:
    num.remove(4)
else:
    print('nao achei o numero 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')


valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posicao {c} encontrei o valor {v}.')
print('Cheguei no final da lista')

a = [2, 3, 4, 7]
b = a ligacaoe entre listas, o que for alterado em uma, sera alterado na outra
b = a[:] copia da lista, o que for alterado na copia, nao se altera na original
b[2] = 8
print(f'Lista {a}')
print(f'Lista {b}')

