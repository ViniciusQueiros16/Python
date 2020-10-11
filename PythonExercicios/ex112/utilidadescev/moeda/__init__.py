def dobro(n=0, m=False):
    resp = n * 2
    if m == True:
        return f'R${resp:.2f}'.replace('.', ',')
    return resp


def metade(n=0, m=False):
    resp = n / 2
    if m == True:
        return f'R${resp:.2f}'.replace('.', ',')
    return resp


def aumentar(n=0, tx=0, m=False):
    resp = n + (tx / 100 * n)
    if m == True:
        return f'R${resp:.2f}'.replace('.', ',')
    return resp


def diminuir(n, tx=0, m=False):
    resp = n - (tx / 100 * n)
    if m == True:
        return f'R${resp:.2f}'.replace('.', ',')
    return resp


def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')


def resumo(n=0, ta=0, td=0):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço:  \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{ta}% de aumento:\t\t{aumentar(n, ta, True)}')
    print(f'{td}% de redução:\t\t{diminuir(n, td, True)}')
    print('-' * 30)
