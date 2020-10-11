def dobro(n):
    return n * 2


def metade(n):
    return n / 2


def aumentar(n):
    return n + (10 / 100 * n)


def diminuir(n):
    return n - (13 / 100 * n)


def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')
