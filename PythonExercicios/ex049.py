print("\033[34m{:=^40}".format('\033[31mTabuada v2.0\033[34m'))
num = int(input('\033[32mDigite um número para ver a sua tabuada: '))
print('\033[31m='*12)
for c in range(1, 11):
    print(f'\033[36m{num} x {c} = {num*c}')
print('\033[31m='*12)
