print("{:=^60}".format('Trantando variaveis v1.0'))
num = s = i = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    i += 1
    s += num
    num = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {i} números e a soma entre eles foi {s}.')


