print("\033[32m{:=^60}".format('\033[34m Analise de Grupo de Dados \033[32m'))
f = h = maisid = 0
while True:
    print('\033[34m-' * 40)
    print('\033[36mCADASTRE UMA PESSOA')
    print('\033[34m-' * 40)
    idade = int(input('Idade: '))
    sexo = ' '
    continua = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: ')).upper().strip()[0]
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if sexo == 'F' and idade <= 20:
        f += 1
    if sexo == 'M':
        h += 1
    if idade >= 18:
        maisid += 1
    if continua == 'N':
        print('acabou')
        break
print(f'\033[32mTotal de pessoas com mais de 18 anos: {maisid}')
print(f'Ao todo temos {h} homens cadastrados')
print(f'E temos {f} mulheres com menos de 20 anos.')
