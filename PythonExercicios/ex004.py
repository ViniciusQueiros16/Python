print('\033[34m=\033[m'*12, '\033[32mDissecando uma variável\033[m', '\033[34m=\033[m'*12)
n = input('\033[7;30mDigite algo: \033[m')
tipo = ('O tipo primitivo desse valor é')
print('\033[31m{} {}\033[m'.format(tipo, type(n)))
print('\033[34mSó tem espaço?', n.isspace())
print('É um numero ?', n.isnumeric())
print('É um alfabeto?', n.isalpha())
print('É alfanumerico?', n.isalnum())
print('Está em maiusculo?', n.isupper())
print('Ésta em minusculo?', n.islower())
print('Ésta capitalizada?', n.istitle())