print("\033[33m{:=^60}".format('\033[35m Maior e menor valores em Tupla \033[33m'))
from random import randint
sorteio = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram: {sorteio}')
print(f'O maior valor sorteado foi {sorted(sorteio)[-1]}')
print(f'O menor valor sorteado foi {sorted(sorteio)[0]}')
#print(f'O maior valor é {max(sorteio)} e o menor é {min(sorteio)}.')
