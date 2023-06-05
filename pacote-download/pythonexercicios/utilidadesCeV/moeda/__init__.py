def metade(n, show=False):
    r = n / 2
    if show:
        return moeda(r)
    else:
        return r


def dobro(n, show=False):
    r = n * 2
    if show:
        return moeda(r)
    else:
        return r


def aumentar(v, p, show=False):
    r = v + (v * p) / 100
    if show:
        return moeda(r)
    else:
        return r


def diminuir(v, p, show=False):
    r = v - (v * p) / 100
    if show:
        return moeda(r)
    else:
        return r


def moeda(msg):
    return f'R${msg:.2f}'.replace('.', ',')


def resumo(v, a, r):
    print('-'*30)
    print('       RESUMO DO VALOR')
    print('-'*30)
    print(f'Preço analisado: \t{moeda(v)}')
    print(f'Metade do preço: \t{metade(v, True)}')
    print(f'Dobro do preço: \t{dobro(v, True)}')
    print(f'{a}% de aumento: \t{aumentar(v, a, True)}')
    print(f'{r}% de redução: \t{diminuir(v, r, True)}')
    print('-'*30)
