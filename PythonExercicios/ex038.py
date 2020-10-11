print('\033[33m='*12, '\033[34mComparando Números', '\033[33m='*12)
n1 = int(input('\033[7;30mDigite o primeiro valor:\033[m '))
n2 = int(input('\033[7;30mDigite o segundo valor:\033[m '))
if n1 > n2:
    print('\033[36mO \033[1;33mPRIMEIRO \033[36mvalor é maior.')
elif n2 > n1:
    print('\033[36mO \033[1;33mSEGUNDO \033[36mvalor é o maior.')
elif n1 == n2:
    print('\033[36mNão existe valor maior ou menor, os dois são IGUAIS.')


