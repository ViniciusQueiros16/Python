print('\033[35m='*12, '\033[32mIndice de Massa Corporal', '\033[35m='*12)
altura = float(input('\033[36mDigite a sua altura(m): '))
peso = float(input('Digite o seu peso(Kg): '))
imc = peso/(altura**2)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc <= 18.5:
    print('\033[33m Esta Abaixo do Peso')
elif imc <= 25:
    print('\033[32mEsta no Peso Ideal, Parabéns!')
elif imc <= 30:
    print('\033[34mEsta em Sobrepeso!')
elif imc <= 40:
    print('\033[35mVocê esta em Obesidade, CUIDADO!')
else:
    print('\033[31mVocê esta em Obesidade Mórbida, MUITO CUIDADO!')
