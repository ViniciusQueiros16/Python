print('\033[32m{:=^60}'.format('\033[34m Menor e maior valores na Lista \033[32m'))
valor = list()
for v in range(0, 5):
    valor.append(int(input(f'\033[34mDigite um valor para ver a posição {v}: ')))# Ler os valores e joga tds eles em uma lista
print('\033[32m=\033[34m-'*40)
print(f'\033[34mVocê dogitou os valores \033[32m{valor}')
print(f'\033[34mO maior varlor digitado foi \033[32m{max(valor)}\033[34m nas posições ', end=' \033[32m')
for c, v in enumerate(valor):
    if v == max(valor):
        print(c, end='... ')
print(f'\n\033[34mO menor valor digitado foi \033[32m{min(valor)}\033[34m nas posições ', end=' \033[32m')
for c, v in enumerate(valor):
    if v == min(valor):
        print(c, end='... ')
