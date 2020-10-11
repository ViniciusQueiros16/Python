print('\033[31m='*12, '\033[33mAprovando Empréstimo', '\033[31m='*12)
casa = float(input('\033[36mQual é o valor da casa? R$'))
sal = float(input('Qual é o seu salário? R$'))
parcelas = int(input('Em quantos anos desja pagar? '))
prestação = casa / (parcelas * 12)
print(f'\033[33mO valor da prestação é de R${prestação}')
porcentagem = sal*30/100
if prestação > porcentagem:
    print('\033[31me vc não pode pegar o emprestimo.Sinto muito!')
else:
    print('\033[34me vc pode pegar o emprestimo!Parabéns')