print("\033[35m{:=^60}".format('\033[36mAnalisador completo\033[35m'))
s = 0
maior = 0
menor = 0
menorid = 0
for c in range(1, 5):
    print('{:-^25}'.format(' {}ª PESSOA '.format(c)))
    nome = str(input('\033[36mNome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: \033[35m')).upper().strip()
    s += idade
    if sexo == 'M' and c == 1:
        maior = idade
        mv = nome
        menor = idade
    else:
        if idade > maior:
            maior = idade
            mv = nome
            if idade < menor:
                menor = idade
    if sexo == 'F' and idade < 20:
        menorid += 1
print(f'\033[33mA média de idade do grupo é de {s/4} anos')
print(f'O homen mais velho tem {maior} e ele se chama {mv}.')
print(f'Ao todo são {menorid} mulheres com menos de 20 anos.')
