print('='*12, 'Analisador Triângulos', '='*12)
import math
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a+b > c and a+c > b and b+c > a:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')

