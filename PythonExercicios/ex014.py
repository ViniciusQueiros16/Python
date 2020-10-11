print('\033[33m=\033[m'*12, '\033[1;31mConversor de Temperaturas\033[m', '\033[33m=\033[m'*12)
c = float(input('\033[7;30mInforme a temperatura em °C:\033[m'))
f = (c*9/5) + 32
print('\033[4;33mA temperatura de \033[4;31m{}°C \033[4;33mcorresponde a \033[4;31m{}°F!'.format(c, f))
