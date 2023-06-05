
Função é uma rotina que nao existe uma definição previa no Python, com objetivo de otimizar o programa

def mostralinha():
    print('---------------')


def mostralinha():
    print('-'*30)

mostralinha()
print('CURSO EM VIDEO')
mostralinha()


def mensagem(msg):
    print('-'*30)
    print(msg)
    print('-'*30)

mensagem('SISTEMA DE ALUNOS')
mensagem('CURSO EM VIDEO')
mensagem('APRENDA PYTHON')


def soma(a, b): #dois parametros
    print(f'A é {a} e B é {b}.')
    s = a + b
    print(f'A soma A + B é igual a {s}.')
    print('-=-'*10)

soma(4, 5)
soma(8, 9)
soma(2, 1)
# soma(4)  vai apresentar erro pois foi usado somente um parametro
soma(b=4, a=5) #posso identificar a ordem, e ele executará da mesma maneira


EMPACOTAMENTO

def contador(* num):
    for valor in num:
        print(f'{valor}', end=' ')
    print('Fim')

def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e sao ao todo {tam}')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

def dobro(lst):  #formula para dobrar os valores da lista
    pos = 0
    while pos < len(lst):
        lst[pos]*=2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobro(valores)
print(valores)


def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)