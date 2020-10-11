print("\033[32m{:=^60}".format('\033[36m Tabela do Brasileirão 2019 Serié A \033[32m'))
tabela = ('FLAMENGO', 'SANTOS', 'PALMEIRAS', 'GRÊMIO',
          'ATHLETICO-PR', 'SÃO PAULO', 'INTERNACIONAL',
          'CORINTHIANS', 'FORTALEZA', 'GOIÁS', 'BAHIA',
          'VASCO', 'ATLÉTICO-MG', 'FLUMINENSE',
          'BOTAFOGO', 'CEARÁ', 'CRUZEIRO', 'CSA', 'CHAPECOENSE', 'AVAÍ')
print('''Ver a Tabela de classific. [ 1 ]
Ver o G5                   [ 2 ]
Ver a zona de rebaixamento [ 3 ]
Ver em ordem alfabética    [ 4 ]
Ver a posição de um time   [ 5 ]
Finalizar o programa       [ 6 ]''')
opção = 0
i = 1
while opção != 6:
    print('\033[31m-=' * 20)
    opção = int(input('\033[34mO que vc deseja? '))
    print('\033[31m-=\033[36m' * 20)
    if opção == 1:
        for t in tabela:
            print(f'{i} {t}')
            i += 1
    if opção == 2:
        print(f'Os 5 primeiros colocados são: {tabela[0:5]}')
    if opção == 3:
        print(f'\033[31mOs times da zona de rebaixamento são: {tabela[-4:]}')
    if opção == 4:
        for o in sorted(tabela):
            print(o)
    if opção == 5:
        time = str(input('Quer ver a posição de qual time? ')).upper()
        print(f'O {time} está na {tabela.index(time) + 1}ª posição.')
print('Programa Finalisado! Volte Sempre.')
