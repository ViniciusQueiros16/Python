print('\033[36m='*12, '\033[32mLendo notas', '\033[36m='*12)
n1 = float(input('\033[35mDigite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1+n2)/2
print(f'\033[36mA sua média é {media:.1f} e vc está:')
if media < 5:
    print('\033[31mReprovado!')
elif media >= 7:
    print('\033[32mAprovado!')
else:
    print('\033[33mEm Recuparaçao!')
