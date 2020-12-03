print('Exercício Python #035 - Analisando Triângulo v1.0')
from time import sleep
print('=-=' * 20)
#Valor dos segmentos
a = float(input('Primeiro Segmento: '))
b = float(input('Segundo Segmento: '))
c = float(input('Terceiro Segmento: '))
print('PROCESSANDO...')
sleep(2)
print('=-=' * 20)
#Caso for um triangulo
if (b - c) < a < b + c and (a - c) < b < a + c and (a-b) < c < a + b:
    print('Os segmentos PODEM formar um TRÂNGULO')
#Caso não for
else: print('Os segmentos não podem formar um TRIÂNGULO')