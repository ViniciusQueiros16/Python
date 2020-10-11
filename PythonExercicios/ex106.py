from time import sleep


def escreva(txt, cor=0):
    tam = len(txt) + 4
    if cor == 1:
        print('\033[46m~' * tam)
        print(txt)
        print('~' * tam)
    elif cor == 2:
        print('\033[44m~' * tam)
        print(txt)
        print('~' * tam)
    elif cor == 3:
        print('\033[41m~' * tam)
        print(txt)
        print('~' * tam)


while True:
    escreva(f'{"SISTEMA DE AJUDA PyHELP":^30}', cor=1)
    doc = str(input('\033[mFunção ou Biblioteca > '))
    if doc != 'fim':
        sleep(2)
        escreva(f'{"Acessando o manual do comando":>32} {doc}', cor=2)
        sleep(1)
        print('\033[40m')
        help(doc)
    if doc == 'fim':
        sleep(0.5)
        escreva(f'{"ATÉ LOGO!":>12}', cor=3)
        break
