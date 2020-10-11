print("\033[33m{:=^60}".format('\033[32mMaior e menor da sequência\033[33m'))
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c} pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'\033[34mO maior peso lido é {maior}Kg')
print(f'E o menor peso lido é {menor}Kg')