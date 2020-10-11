print("\033[33m{:=^60}".format('\033[34mMaior e Menor valores\033[33m'))
s = i = maior = menor = 0
c = 'S'
while c in 'Ss':
    num = int(input('Digite um número: '))
    i += 1
    s += num
    c = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if i == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'\033[33mVocê digitou \033[34m{i} \033[33mnúmeors e a média foi \033[34m{s/i}.')
print(f'\033[33mO maior valor foi \033[34m{maior} \033[33me o menor foi \033[34m{menor}.')
