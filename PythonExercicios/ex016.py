print('\033[33m='*12, '\033[34mQuebrando Números\033[m', '\033[33m=\033[m'*12)
'''from math import trunc
num = float(input('Digite um número:'))
inteiro = trunc(num)
print('\033[34mO número {} tem a parte inteira {}'.format(num, inteiro))'''

import math
num = float(input('\033[33mDigite um número: '))
print('\033[35mO número \033[36m{} \033[35mtem a parte inteira \033[36m{}'.format(num, math.trunc(num)))
