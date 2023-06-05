def fatorial(num=1, show=False):
    """
    -> Calcula o Fatorial de um numero.
    :param num: o numero a ser calculado
    :param show: (opcional) Mostrar ou nao a conta.
    :return: O valor fatorial de um numero num.
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    print(f)


fatorial(5, show=True)
help(fatorial)
