print('\033[34m{:=^60}'.format('\033[36m Progressão Aritimética \033[34m'))
termo = int(input('\033[36mPrimeiro termo: '))
razão = int(input('Razão: \033[34m'))
dec = termo + (10-1) * razão
for c in range(termo, dec+razão, razão):
    print(c, end='\033[31m -> \033[34m')
print('ACABOU')