print('\033[35m=\033[m'*12, '\033[34mCatetos e Hipotenusas\033[m', '\033[35m=\033[m'*12)
'''import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2)
raiz = math.sqrt(hi)
print('A hipotenusa vai medir: {:.2f}'.format(raiz))'''

import math
oposto = float(input('\033[7;30mComprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: \033[m'))
hipotenusa = math.hypot(oposto, adjacente)
print(f'\033[4;35mA hipotenusa vai medir \033[4;34m{hipotenusa:.2f}\033[m')
