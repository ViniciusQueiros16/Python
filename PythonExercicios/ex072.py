print("\033[33m{:=^60}".format('\033[34m Números por Extenso \033[33m'))
numeros = ('zero', 'um', 'dois', 'tres', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
resp = ' '
while resp not in 'Nn':
    num = int(input('\033[34mDigite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'\033[33mVocê digitou o número {numeros[num]}')
    if num < 0 or num > 20:
        while True:
            num = int(input('\033[31mTente Novamente! Digite um número entre 0 e 20: '))
            if num >= 0 and num <= 20:
                print(f'\033[33mVocê digitou o número {numeros[num]}')
                break
    resp = str(input('\033[34mQuer continuar? [S/N] ')).strip()[0]