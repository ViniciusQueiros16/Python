print("{:=^40}".format('Soma dos Pares'))
s = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c} valor: '))
    if num % 2 == 0:
        s += num
print(f'A soma dos números pares é igual a {s}')
