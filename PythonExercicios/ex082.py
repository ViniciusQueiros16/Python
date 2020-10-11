print('\033[32m{:=^60}'.format('\033[36m Dividindo valores em várias listas \033[32m'))
lista = []
par = []
impar = []
while True:
    lista.append(int(input('\033[36mDigite um número: ')))
    resp = str(input('\033[32mQuer continuar? [S/N] ')).strip()[0]
    if resp in 'Nn':
        break
for c in range(len(lista)):
    if lista[c] % 2 == 0:
        par.append(lista[c])
    else:
        impar.append(lista[c])
print('\033[36m-\033[32m='*40)
print(f'\033[34mA lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')
