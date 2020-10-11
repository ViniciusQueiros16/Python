print("\033[34m{:=^60}".format('\033[32mSoma de Impares Múltiplos de 3\033[34m'))
s = 0
i = 0
for M in range(1, 501, 2):
    if M % 3 == 0:
        i += 1 # Conta tds os valores
        s += M # Soma tds os valores
print(f'\033[4;34mA soma de \033[32m{i} \033[34mvalores é \033[32m{s}')
