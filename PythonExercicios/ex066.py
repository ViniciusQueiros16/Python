d = '\033[34mDesconsiderando o fleg\033[31m'
print(f'\033[31m{d:=^60}\033[31m')
s = i = 0
while True:
    n = int(input('Digite um número [999 pra parar]: '))
    if n == 999:
        break
    i += 1
    s += n
print(f'\033[34mA soma dos {i} valores foi {s}!')
