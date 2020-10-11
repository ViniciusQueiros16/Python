def leiaint(num):
    while True:
        valor = str(input(num))
        if valor.isnumeric():
            return int(valor)
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        if valor.isnumeric():
            break


n = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o número {n}')
