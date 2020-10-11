def leiaint(num):
    while True:
        try:
            valor = int(input(num))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse número.')
            return 0
        else:
            return int(valor)


def leiafloat(num):
    while True:
        try:
            valor = float(input(num))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return float(valor)


i = leiaint('Digite um numero inteiro: ')
r = leiafloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {i} e o Real foi {r}')
