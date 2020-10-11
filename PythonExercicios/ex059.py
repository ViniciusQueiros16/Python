print("\033[31m{:=^60}".format('\033[34m Criando Menu de Opções \033[31m'))
from time import sleep
n1 = int(input('\033[36mDigite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print('\033[34m-\033[31m*'*22)
print('\033[36mAperte um desses números abaixo para:')
oq = 1
while oq != 5:
    print('\033[34m-\033[31m*'*22)
    print('\033[1;31;44m[ 1 ]SOMAR\33[m\n\033[1;31;44m[ 2 ]MULTIPLICAR\033[m\n\033[1;31;44m[ 3 ]MAIOR\033[m\n\033[1;31;44m[ 4 ]NOVOS NÚMEROS\033[m\n\033[1;31;44m[ 5 ]SAIR DO PROGRAMA\033[m')
    print('\033[34m-\033[31m*'*22)
    oq = int(input('\033[36mOque deseja fazer: '))
    if oq == 1:
        print(f'\033[1;35mA soma entre {n1} e {n2} é igual a {n1 + n2}')
    elif oq == 2:
        print(f'\033[1;35mO resultado de {n1} * {n2} é {n1*n2}')
    elif oq == 3:
        if n1 > n2:
            print(f'\033[1;35m{n1} é maior que {n2}')
        else:
            print(f'\033[1;35m{n2} é maior que {n1}')
    elif oq == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif oq == 5:
        print('Finalizando...')
        sleep(2)
        print('Até Breve!')
    else:
        if oq != 5:
            print('\033[1;31mOpção invalida. Tente novamente!')
