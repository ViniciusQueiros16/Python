print("\033[34m{:=^60}".format('\033[32m Simulador de caixa eletronico \033[34m'))
valor = int(input('Que valor vc quer sacar? R$'))
total = valor
dinheiro = 50
tdsdinheiro = 0
while True:
    if total >= dinheiro:
        total -= dinheiro
        tdsdinheiro += 1
    else:
        if tdsdinheiro > 0:
            print(f'Total de {tdsdinheiro} cedulas de R${dinheiro}')
        if dinheiro == 50:
            dinheiro = 20
        elif dinheiro == 20:
            dinheiro = 10
        elif dinheiro == 10:
            dinheiro = 1
        tdsdinheiro = 0
        if total == 0:
            break
