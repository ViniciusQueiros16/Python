from ex112.utilidadescev import moeda
def leiaDinheiro(n=0):
    fv = False
    while not fv:
        valor = str(input(n)).strip().replace(',', '.')
        if valor.isalpha() or len(valor) == 0:
            print(f'\033[31mERRO! {valor} é um preço invalido!\033[m')
        else:
            fv = True
            return float(valor)
