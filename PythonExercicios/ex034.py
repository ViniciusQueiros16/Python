print('='*12, 'Aumentos múltiplos', '='*12)
salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    print(f'Quem ganhava R${salario:.2f} passa a ganhar R${salario+salario*15/100:.2f} agora.')
else:
    print(f'Quem ganhava R${salario:.2f} passa a ganhar R${salario+salario*10/100:.2f} agora.')
