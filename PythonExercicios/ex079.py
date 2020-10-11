print('\033[33m{:=^60}'.format('\033[35m Valores únicos em uma Lista \033[33m'))
valores = []
resp = ''
while resp in 'Ss':
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = str(input('Quer continuar? [S/N] ')).strip()[0]
print('\033[35m=\033[33m-'*40)
print(f'\033[33mVocê digitou os valores {sorted(valores)}')
