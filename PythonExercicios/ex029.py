import emoji
from termcolor import colored
print(emoji.emojize(':car: :car: :car: :car: Radar Eletrônico :car: :car: :car: :car:',use_aliases=True))
v = float(input('Qual a velocidade atual do carro? '))
multa = (v - 80) * 7
if v > 80:
    print(f'Multado! Você excedeu o limite permitido que é de 80Km/h \nVocê deve pagar uma multa de R${multa:.2f}!')
print(emoji.emojize('Tenha um bom dia!:sunny: Dirija com segurança!',use_aliases=True))