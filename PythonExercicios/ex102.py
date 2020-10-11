def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show == True:
            print(f'{c} ', end=' ')
            if c > 1:
                print('x ', end='')
            else:
                print('= ', end='')
        f *= c
    return f


num = int(input('Digite um número para ver o seu fatorial: '))
while True:
    resp = str(input('Quer ver o calculo? [S/N] ')).upper()[0]
    if resp in 'SN':
        break
    else:
        print('Erro! Responda apenas com S ou N.')
if resp == 'S':
    resp = True
else:
    resp = False
print(fatorial(num, resp))
help(fatorial)
