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


def aumentar(n=0, m=False):
    resp = n + (10 / 100 * n)
    if m == True:
        return f'R${resp:.2f}'.replace('.', ',')
    return resp


def diminuir(n, m=False):
    resp = n - (13 / 100 * n)
    if m == True:
        return f'R${resp:.2f}'.replace('.', ',')
    return resp


def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')
