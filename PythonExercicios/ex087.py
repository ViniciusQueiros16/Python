print('{:=^60}'.format(' Mais sobre Matriz em Python '))
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
s = somatc = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para ver a posição {l}, {c}: '))
        if matriz[l][c] % 2 == 0:
            s += matriz[l][c]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {s}.')
for p in matriz:
    somatc += p[2]
print(f'A soma dos valores da terceira coluna é {somatc}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')
