print("\033[32m{:=^60}".format('\033[34mGrupo da Maioridade\033[32m'))
from datetime import date
maior = 0
menor = 0
for c in range(1, 7+1):
    ano = int(input(f'\033[35mDigite o ano em que a {c}ª nasceu: '))
    atual = date.today().year
    if atual - ano >= 18:
        maior += 1
    else:
        menor += 1
print(f'\033[34mSão {maior} pessoas maiores de idade \nE também temos {menor} pessoas menores de idade')
