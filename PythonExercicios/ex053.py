print("\033[31m{:=^60}".format('\033[32mDetector de Palíndromo\033[31m'))
n = str(input('Digite uma frase: ')).upper().strip()
palavras = n.split() #SEPARA AS PALAVRAS
junto = ''.join(palavras) #E DPS JUNTA PARA REMOVERS ESPAÇOS ENTRE ELAS
inverso = ''
for ultimo in range(len(junto) - 1, -1, -1):
    inverso += junto[ultimo]
print(f'\033[32mO inverso de {n} é {inverso}')
if junto == inverso:
    print('\033[36mTemos um palíndromo!')
else:
    print('\033[31mA frase digitada NÃO É UM PALÍNDROMO!')
