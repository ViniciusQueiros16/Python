print("\033[35m{:=^60}".format(' \033[36mExtraindo dados de uma Lista\033[35m '))
valores = []
cont = 0
while True:
    valores.append(int(input('\033[36mDigite um valor: ')))
    cont += 1
    resp = str(input('\033[36mQuer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('\033[35m=\033[32m-'*40)
print(f'\033[36mVocê digitou {cont} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print(f'O valor 5 faz parte da lista! E ele está na posição {valores.index(5)}')
else:
    print('O valor 5 não faz parte da lista!')
