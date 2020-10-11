print("\033[32m{:=^60}".format('\033[34mLista ordenada sem Repetições\033[32m'))
lista = []
for c in range(0, 5):
    valores = int(input('\033[34mDigite um valor: '))
    if c == 0 or valores > lista[-1]:
        lista.append(valores)
        print('\033[33mAdicionado ao final da lista...')
    else:
        dps = 0
        while dps < len(lista):
            if valores <= lista[dps]:
                lista.insert(dps, valores)
                print(f'\033[33mValor adicionado na posição {dps}')
                break
            dps += 1
print(f'\033[33mOs valores digitados foram {lista}')

