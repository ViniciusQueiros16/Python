print('{:=^60}'.format(' Matriz em Python '))
n0 = list()
n1 = list()
n2 = list()
matriz = [[], [], []]
for c in range(0, 9):
    valor = int(input('Digite um valor para ver a matriz: '))
    if c < 3:
        n0.append(valor)
    if 2 < c < 6:
        n1.append(valor)
    if c > 5:
        n2.append(valor)
matriz[0].append(n0)
matriz[1].append(n1)
matriz[2].append(n2)
print('-='*30)
for c in matriz:
    print(f'[ {c[0][0]:^5} ] [ {c[0][1]:^5} ] [ {c[0][2]:^5} ]')
