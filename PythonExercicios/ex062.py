print("{:=^60}".format(' Super Progressão Aritmetíca v3.0 '))
termo = int(input('Primeiro Termo: '))
razão = int(input('Razão da PA: '))
#termo = primeiro
n = 1
mais = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while n <= total:
        print(termo, end=' - ')
        termo += razão
        n += 1
    print('PAUSA')
    mais = int(input('Quer que mostre mais quantos termos? '))
print(f'Progressão finalizada com {total} termos')