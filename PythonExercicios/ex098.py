from time import sleep
def contador(i, f, p):
    print('-='*20)
    if p == 0:
        p = 1
    if p < 0:
        p = p * -1
    if i > f:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        for c in range(i, f-p, -p):
            print(c, end=' ')
            sleep(0.5)
        print('FIM!')
    else:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        for c in range(i, f+p, p):
            print(c, end=' ')
            sleep(0.5)
        print('FIM!')


contador(1, 10, 1)
contador(10, 1, 2)
print('-='*20)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)
