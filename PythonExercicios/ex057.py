print("\033[36m{:=^60}".format('\033[35m Sexo Masculino e Feminino \033[36m'))
s = str(input('Qual é o seu sexo? [M/F]: ')).upper().strip().upper()[0]
while s not in 'MnFf':
    s = str(input('\033[31mDados invalidos! \033[36mPor favor digite novamente: ')).strip().upper()[0]
if s == 'F':
    sexo = 'FEMENINO'
elif s == 'M':
    sexo = 'MASCULINO'
print(f'\033[4;34mSEU SEXO É {sexo} E FOI REGISTRADO COM SUCESSO.')