print("\033[36m{:=^60}".format('\033[32m Calculo Fatorial \033[36m'))
from math import factorial
n = int(input('\033[32mDigite um número para calcular seu fatorial: \033[36m'))
i = 1
c = n
print(f'{n}! = ', end='')
while c > 1:
    print(c, end=' x ')
    c = c - 1
    i *= c+1
print(1, end='')
print(f' = {i}')

#calculo utilizando modulo factorial
'''f = factorial(n)
print(f'O fatorial de {n} é {f}')'''
#calculo utilizando FOR
'''for c in range(n, -1+2, -1):
    i *= c
    print(c, end=' x ')
print(1, end=' ')
print(f'= {i}')'''
