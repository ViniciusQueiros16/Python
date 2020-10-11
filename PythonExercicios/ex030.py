print('=' * 12, 'Par ou Impar', '=' * 12)
from termcolor import colored

n = int(input('Me diga um número qualquer: '))
result = n % 2
if result == 0:
    print(colored(f'O número {n} é Par', 'green'))
else:
    print(colored(f'O número {n} é Impar', 'blue'))
