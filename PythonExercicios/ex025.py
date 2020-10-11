print('\033[34m='*12, '\033[31mProcurando uma string dentro da outra','\033[34m='*12)
nome = str(input('\033[35mQual é o seu nome completo? ')).lower().split()
print('\033[34mSeu nome tem Silva?', 'silva' in nome)
