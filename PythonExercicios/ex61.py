print("{:=^60}".format('Progressão Aritimética v2.0'))
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
dec = termo + (10-1) * razao
print(termo, end=' - ')
while termo < dec:
    termo += razao-1
    termo += 1
    print(termo, end=' - ')
print('Fim')
