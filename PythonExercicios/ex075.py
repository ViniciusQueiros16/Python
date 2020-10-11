print("\033[31m{:=^60}".format('\033[32m Análise de dados em uma Tupla \033[31m'))
valores = (int(input('\033[36mDigite um número: ')),
           int(input('\033[36mDigite outro número: ')),
           int(input('\033[36mDigite mais um  número: ')),
           int(input('\033[36mDigite o último número: ')))

print(f'\033[32mVocê digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nehuma posição')
print(f'Os valores pares digitados foram ', end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')
