print("\033[35m{:=^60}".format('\033[32mTabuada v3.0\033[35m'))
while True:
    v = int(input('\033[32mDigite um valor para ver a sua tabuada: '))
    if v < 0:
        break
    print('\033[35m-'*40)
    for c in range(1, 11):
        print(f'\033[36m{v} x {c} = {v * c}')
    print('\033[35m-'*40)
print('\033[34mPrograma encerrado. Até breve!')
