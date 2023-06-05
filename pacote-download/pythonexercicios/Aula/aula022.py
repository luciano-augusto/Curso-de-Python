'''
MODULARIZAÇÃO = construi modulos
- Sistemas ficando cada vez maior
- Foco: dividir um programa grande, aumentar a legibilidade, facilitar a manutenção, dividi um grande problema em
pequenos problemas.

VANTAGENS:

- Organização de código
- Facilidade na manutenção
- Ocultação de código detalhado
- Reutilização em outros projetos

PACOTES OU BIBLIOTECA

Varios pacotes separados por assunto, números, strings, datas, cores...
'''
def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f

num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatoria de {num} é {fat}')