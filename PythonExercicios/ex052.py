print('Números Primos')
num = int(input('Digite um número: '))
i = 0
for c in range(1, num+1):
    if num % c == 0:
        i += 1
        print('\033[34m', end=' ')
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[35mO número {num} foi divisível {i} vezes')
if i > 2:
    print('Por isso ele NÃO É PRIMO')
else:
    print('Por isso ele É PRIMO')