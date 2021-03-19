print('Exercício Python #042 - Analisando Triângulos v2.0')
from time import sleep
print('=-=' * 20)
#Valor dos segmentos
a = float(input('Primeiro Segmento: '))
b = float(input('Segundo Segmento: '))
c = float(input('Terceiro Segmento: '))
print('')
print('PROCESSANDO...')
sleep(2)
print('=-=' * 20)
#Caso for um triangulo
if (b - c) < a < b + c and (a - c) < b < a + c and (a-b) < c < a + b:
    # Equilatero
    if b == a and b == c and c == a:
        print('Os segmentos PODEM formar um TRÂNGULO EQUILÁTERO!')
        print('')
    # Isósceles
    elif a == b or b == c or c == a:
        print('Os segmentos PODEM formar um TRÂNGULO ISÓSCELES')
    # Escaleno
    else:
        print('Os segmentos PODEM formar um TRÂNGULO ESCALENO')
#Caso não for
else:
    print('Os segmentos não podem formar um TRIÂNGULO')
sleep(10)
