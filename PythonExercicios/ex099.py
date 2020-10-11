from time import sleep
def maior(* vls):
    mvalor = i = 0
    print('-='*20)
    print('Analisando os valores passados...')
    for c in vls:
        print(c, end=' ')
        sleep(0.5)
        i += 1
        if i == 0:
            mvalor = c
        else:
            if c > mvalor:
                mvalor = c
    print(f'- Foram informados {i} valores ao todo.')
    print(f'O maior valor informado foi {mvalor}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
