print('\033[35m='*12, '\033[31mConversor de Bases Numéricas', '\033[35m='*12)
n = int(input('\033[34mDigite um número inteiro: '))
print('\033[32mEscolha uma das bases para conversão:\n\033[35m[ 1 ] converter para BINÁRIO \n[ 2 ] converter para OCTAL\n[ 3 ] converter para HEXADECIMAL')
opçao = int(input('\033[34mSua opção: '))
if opçao == 1:
    print(f'\033[36m{n} \033[34mconvertido para \033[1;35mBINÁRIO \033[34mé igual a \033[36m{bin(n)[2:]}')
elif opçao == 2:
    print(f'\033[36m{n} \033[34mconvertido para \033[1;35mOCTAL \033[34mé igual a \033[36m{oct(n)[2:]}')
elif opçao == 3:
    print(f'\033[36m{n} \033[34mconvertido para \033[1;35mHEXADECIAMAL \033[34mé igual a \033[36m{hex(n)[2:]}')
else:
    print('\033[31mValor invalido, digite novamente.')
