print('\033[34m=' * 12, '\033[1;35mSeparando Digitos de Números', '\033[34m=' * 12)
'''n = str(input('Digite um número: '))
print(f'Analisando o número {n}')
com = ' '.join(n)
separado = com.split()
print(f'Unidade: {separado[3]}')
print(f'Dezena: {separado[2]}')
print(f'Centena: {separado[1]}')
print(f'Milhar: {separado[0]}')'''

n1 = int(input('Digite um número: '))
print(f'\033[1;35mAnalisando o número {n1}')
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print(f'\033[33mUnidade{u}: ')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
