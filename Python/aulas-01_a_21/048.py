print('\033[36;40mExercício Python #048 - Soma ímpares múltiplos de três\033[m')
s = 0
cont = 0
from time import sleep
for c in range(1, 501, 2):
    if c % 3 == 0:
        s = s + c
        cont = cont + 1
print('A soma de todos os {} valores é {}'.format(cont, s))
