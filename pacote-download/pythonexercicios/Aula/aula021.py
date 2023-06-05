
INTERACTIVE HELP -- Ajuda Interativa
help()

Para imprimir os parametros internos de um comando:
print(input.__doc__) ≥ do comando print
print(input.__doc__)
help(input)

DOCSTRING: cria um manual de como se utiliza um funcao ou comando.
"""
"""  apos o comando def, usar aspas dulpas tres vezes para abrir e para fechar


def contador(i, f, p):
    """
    --> Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada na aula do Curso em Video.
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('Fim')

contador(1, 20, 3)

help(contador)


PARAMETRO OPCIONAL

def somar(a, b, c = 0):  # O "c" recebe valor 0 para que no caso de nao ser denominado um outro valor a ele, nao haja no retorno da funçao
#def somar(a=0, b=0, c=0) # tambem é possivel
    s = a + b + c
    print(f'A soma é {s}')

somar(3, 2, 5)
somar(4, 4) #nesse caso o c = 0
somar() # tambem é possivel


ESCOPO DE VARIAVEIS

def teste(b): #variavel local, b vale 5
    global a # torna o comando dentro do local, o novo valor global
    a = 8 # essa variavel é local e nao ira mudar o valor no escopo GLOBAL
    b += 4   # neste momento b passa a valer 9
    c = 2
    print(f'A dentro vale {a}') # 5
    print(f'B dentro vale {b}') # 9
    print(f'C dentro vale {c}') # 2


a = 5
teste(a) #variavel global dando ao teste o valor de 5
print(f'A fora vale {a}') # 5
print(f'B fora vale {b}') # erro, B so existe na variavel local
print(f'C fora vale {c}') # erro, C so existe na variavel local


RETORNO DE VALORES

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus calculos deram {r1}, {r2}, {r3}.')

def fatorial(num = 1):
    f = 1
    for c in range(num, 0 , -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados sao {f1}, {f2} e {f3}.')

n = int(input('Digite um numero: '))
print(fatorial(n))
print(f'O fatorial de {n} é {fatorial(n)}.')

def par(n=0):
    if n % 2 == 0 :
        return True
    else:
        return False

num = int(input('Digite um numero: '))
# print(par(num))
if par(num):
    print('É par.')
else:
    print('É impar.')