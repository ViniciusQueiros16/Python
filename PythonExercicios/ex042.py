print('\033[33m='*12, '\033[034m Analisando Triângulos v2.0', '\033[33m='*12)
a = float(input('\033[34mPrimeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and b+c > a and a+c > b:
    print('\033[32mOs segmentos acima \033[1;36mPODEM FORMAR \033[32mum triângulo \033[1;36m', end='')
    if a == b and a == c and b == c:
        print('EQUILÁTERO')
    elif a == b != c or a == c != b or b == c != a:
        print('ISÓSCELES')
    elif a and b != c and a and c != b and b and c != a:
        print('ESCALENO')
else:
    print('\033[31mOs segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO')
