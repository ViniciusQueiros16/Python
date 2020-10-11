from random import randint
while True:
    try:
        resp = str(input('Você deseja jogar um dado? ')).upper()[0]
        if resp not in 'SN':
            print('Erro! Digite novamente.')
        else:
            break
    except:
        print('ERRO! Por favor digite s ou n')
if resp == 'S':
    while True:
        dado = randint(0, 10)
        print(f'O valor do dado foi {dado}')
        while True:
            try:
                resp = str(input('Quer jogar o dado novamente? ')).upper()[0]
                if resp not in 'SN':
                    print('Erro! Digite novamente.')
                else:
                    break
            except:
                print('ERRO! Por favor digite s ou n')
        if resp == 'N':
            break
print('Até Logo!')
